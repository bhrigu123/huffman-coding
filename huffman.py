# heapq is used as min heap
import heapq
import os
from functools import total_ordering
from collections import defaultdict, Counter
from pprint import pprint
from bidict import bidict
from bitarray.util import huffman_code

"""
Code for Huffman Coding, compression and decompression.
Explanation at http://j.mp/huffmanPy
"""


# Take a look at http://bit.ly/totalOrderExample
@total_ordering
class HeapNode:
  def __init__(self, char: str, freq: dict):
    self.char = char
    self.freq = freq
    self.left = None
    self.right = None

  # defining comparators less_than and equals
  def __lt__(self, other):
    return self.freq < other.freq

  def __eq__(self, other):
    if(other is None):
      return False
    if(not isinstance(other, HeapNode)):
      return False
    return self.freq == other.freq


class HuffmanCoding:
  def __init__(self, path=None):
    self.path: str = path
    # min heap implemented as an array (list)
    self.heap: list = []
    # bidirectional char to code to char
    self.mapping: bidict = bidict()

  # functions for compression:
  make_frequency_dict = Counter

  def make_heap(self, frequency):
    # pprint(frequency)
    for key in frequency:
      node = HeapNode(key, frequency[key])
      heapq.heappush(self.heap, node)

  def merge_nodes(self):
    while(len(self.heap) > 1):
      node1 = heapq.heappop(self.heap)
      node2 = heapq.heappop(self.heap)

      # through the merging process we can
      # the most frequeny raises to the top
      merged = HeapNode(None, node1.freq + node2.freq)
      merged.left = node1
      merged.right = node2

      heapq.heappush(self.heap, merged)

  # recursive function which is at the heart
  # of it all - need to make sense of this!
  def make_codes_helper(self, root, current_code):
    if(root is None):
      return

    # if it a leaf node
    if(root.char is not None):
      # place the code for the character
      self.mapping[root.char] = current_code
      return

    self.make_codes_helper(root.left, current_code + "0")
    self.make_codes_helper(root.right, current_code + "1")

  def make_codes(self):
    # Use the heap, a binary tree which was
    # build using the frequency dictionary
    # Eventually, a map is obtained between code and
    # character
    # print("heap size", len(self.heap))
    root = heapq.heappop(self.heap)
    current_code = ""
    self.make_codes_helper(root, current_code)
    # pprint(sorted(self.mapping.inv.items()))
    heapq.heappush(self.heap, root)

  def get_encoded_text(self, text):
    encoded_text = ""
    for character in text:
      encoded_text += self.mapping[character]
    return encoded_text

  def pad_encoded_text(self, encoded_text: str) -> str:
    # Extra bits at the end of the bit stream
    # so that the bit stream is a multiple of 8
    extra_padding = 8 - len(encoded_text) % 8
    for i in range(extra_padding):
      encoded_text += "0"

    # The above pads needs to be removed during decompress
    # That is also formatted as a byte and stored
    # ahead of the bit stream
    padded_info = "{0:08b}".format(extra_padding)
    encoded_text = padded_info + encoded_text
    return encoded_text

  def get_byte_array(self, padded_encoded_text):
    if(len(padded_encoded_text) % 8 != 0):
      print("Encoded text not padded properly")
      exit(0)

    b = bytearray()
    for i in range(0, len(padded_encoded_text), 8):
      byte = padded_encoded_text[i:i + 8]
      b.append(int(byte, 2))
    return b

  # takes a text string and returns back
  # a stringified version of the binary bit stream
  # that represents the compressed output
  def compress_text(self, text: str) -> str:
    return str(bin(len(text)))

  # returns a path to the compressed binary file
  def compress(self, text: str = None) -> str:
    filename, file_extension = os.path.splitext(self.path)
    output_path = filename + ".bin"

    if text or not self.path:
      compress_text(self, text)

    with open(self.path, 'r+') as file, open(output_path, 'wb') as output:
      text = file.read()
      # text = text.rstrip()

      # build a dictionary
      frequency = self.make_frequency_dict(text)
      # build a heapthat capture info in the dict
      self.make_heap(frequency)
      # merge nodes so automatically the most
      # frequency raises to the top
      self.merge_nodes()
      # capture this information in a mapping
      # instead of actually traversing the tree?
      self.make_codes()

      hc = [(c, bits.to01()) for c, bits in huffman_code(frequency).items()]
      self.mapping.update(hc)

      # actual conversion from text to stringified
      # padded binary stream
      encoded_text = self.get_encoded_text(text)
      padded_encoded_text = self.pad_encoded_text(encoded_text)
      # convert to actual bytes and write to file
      b = self.get_byte_array(padded_encoded_text)
      output.write(bytes(b))

    print("Compressed")
    return output_path

  """ functions for decompression: """

  def remove_padding(self, padded_encoded_text: str) -> str:
    padded_info = padded_encoded_text[:8]
    extra_padding = int(padded_info, 2)
    '''
    We have {pad_count in 8 bits} +
            bit_stream +
            {pads}
    '''
    bits_only = slice(8, -extra_padding)
    encoded_text = padded_encoded_text[bits_only]

    return encoded_text

  # takes a stringified binary bit stream and refers
  # to the reverse_mapping to convert it into human
  # readable characters
  def decode_text(self, encoded_text: str) -> str:
    current_code = ""
    decoded_text = ""
    # print(encoded_text)
    # print(self.reverse_mapping)

    for bit in encoded_text:
      current_code += bit
      if(current_code in self.mapping.inv):
        character = self.mapping.inv[current_code]
        decoded_text += character
        current_code = ""

    return decoded_text

  def is_leafnode(self, n):
    return not n.left and not n.right
    # return n and n.char is None

  def decode_text2(self, etext: str) -> str:
    #print("heap size", len(self.heap))
    root = heapq.heappop(self.heap)
    node = root
    print("etext", etext)
    decoded = ""
    for bit in etext:
      if bit == '1':
        node = node.right
        if self.is_leafnode(node):
          decoded += node.char
          node = root
      elif bit == '0':
        node = node.left
        if self.is_leafnode(node):
          decoded += node.char
          node = root
      print(decoded)
    return decoded

  # returns a path to the text file
  # containing the decompressed text

  def decompress(self, input_path: str) -> str:
    filename, file_extension = os.path.splitext(self.path)
    output_path = filename + "_decompressed" + ".txt"

    # bytes to string of bits
    with open(input_path, 'rb') as file, open(output_path, 'w') as output:
      bit_string = ""

      byte = file.read(1)
      while(len(byte) > 0):
        byte = ord(byte)
        bits = bin(byte)[2:].rjust(8, '0')
        bit_string += bits
        byte = file.read(1)

      # remove the pads, and decompress bits to
      # text by using reverse_mapping
      encoded_text = self.remove_padding(bit_string)
      decompressed_text = self.decode_text(encoded_text)
      output.write(decompressed_text)

    print("Decompressed")
    return output_path

  '''
  these methods are available for timing tests
  '''

  def make_frequency_dict_default(self, text):
    frequency = defaultdict(int)
    for character in text:
      frequency[character] += 1
    return frequency

  def make_frequency_dict_deprecated(self, text):
    frequency = {}
    for character in text:
      if character not in frequency:
        frequency[character] = 0
      frequency[character] += 1
    return frequency
