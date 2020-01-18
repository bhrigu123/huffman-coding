# heapq is used as min heap
import heapq
import os
from functools import total_ordering
from collections import defaultdict, Counter
from pprint import pprint
#from bidict import bidict
from bitarray.util import huffman_code
from bitarray import bitarray

"""
Code for Huffman Coding, compression and decompression.
Explanation at http://j.mp/huffmanPy
"""


class HuffmanCoding:
  def __init__(self, path=None):
    self.path: str = path
    self.hc: dict = None

  # functions for compression:
  make_frequency_dict = Counter

  def get_encoded_text(self, text):
    b = bitarray()
    b.encode(self.hc, text)
    return b

  def pad_encoded_text(self, btext: str) -> str:
    pad_info = format(btext.fill(), 'b').zfill(8)
    return pad_info + btext.to01()

  def get_byte_array(self, padded_encoded_text):
    if(len(padded_encoded_text) % 8 != 0):
      print("Encoded text not padded properly")
      exit(0)

    return bitarray(padded_encoded_text).tobytes()

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

      # build a dictionary
      frequency = self.make_frequency_dict(text)
      self.hc = huffman_code(frequency)

      # actual conversion from text to stringified
      # padded binary stream
      encoded_text = self.get_encoded_text(text)
      padded_encoded_text = self.pad_encoded_text(encoded_text)
      # convert to actual bytes and write to file
      bytes = self.get_byte_array(padded_encoded_text)
      output.write(bytes)

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
    depad = slice(8, -extra_padding)
    encoded_text = padded_encoded_text[depad]

    return encoded_text

  # takes a stringified binary bit stream and refers
  # to the reverse_mapping to convert it into human
  # readable characters
  def decode_text(self, encoded_text: str) -> str:
    d = bitarray(encoded_text)
    return "".join(d.decode(self.hc))

  # returns a path to the text file
  # containing the decompressed text
  def decompress(self, input_path: str) -> str:
    filename, file_extension = os.path.splitext(self.path)
    output_path = filename + "_decompressed" + ".txt"

    # bytes to string of bits
    with open(input_path, 'rb') as file, open(output_path, 'w') as output:
      bytes = bitarray()
      bytes.fromfile(file)
      bit_string = bytes.to01()
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
