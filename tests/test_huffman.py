import filecmp
import huffman
import pytest
import time 
from collections import Counter

def test_creation_of_huffman():
  
  hc = huffman.HuffmanCoding("sample.text")

def test_input_equals_output():
  
  hc = huffman.HuffmanCoding("sample.txt")
  compressed_file = hc.compress()
  decompressed_file = hc.decompress(compressed_file)

  assert filecmp.cmp("sample.txt", decompressed_file)

#@pytest.mark.skip
def test_with_no_newline_at_end():
  
  # no new line at the end
  hc = huffman.HuffmanCoding("sample2_with_newline.txt")
  compressed_file = hc.compress()
  decompressed_file = hc.decompress(compressed_file)

  assert filecmp.cmp("sample2_with_newline.txt", decompressed_file)

#@pytest.mark.skip
def test_with_multiple_lines():

  # no new line at the end
  hc = huffman.HuffmanCoding("sample3_with_twolines.txt")
  compressed_file = hc.compress()
  decompressed_file = hc.decompress(compressed_file)

  assert filecmp.cmp("sample3_with_twolines.txt", decompressed_file)

#@pytest.mark.skip
def test_with_multiple_lines_with_newline():

  # no new line at the end
  hc = huffman.HuffmanCoding("sample4.txt")
  compressed_file = hc.compress()
  decompressed_file = hc.decompress(compressed_file)

  assert filecmp.cmp("sample4.txt", decompressed_file)

def test_with_text_returning_encoded_text():
  tokens = "abaca"
  hc = huffman.HuffmanCoding()
  encoded_text = hc.compress_text(tokens)
  assert encoded_text != tokens

#@pytest.mark.skip
def test_defaultdict_vs_counter_for_compress():
  hc = huffman.HuffmanCoding("../sample.txt")

  start = time.time()
  hc.compress()
  defaultdict_time = time.time() - start
  print("Time taken (defaultdict):", defaultdict_time)

  hc.make_frequency_dict = Counter
  start = time.time()
  hc.compress()
  counter_time = time.time() - start
  print("Time taken (Counter):", counter_time)

  assert counter_time < defaultdict_time
  


  