import filecmp
import huffman
import pytest
import time
from collections import Counter, defaultdict
from pprint import pprint


def test_input_equals_output():

  hc = huffman.HuffmanCoding("sample.txt")
  compressed_file = hc.compress()
  decompressed_file = hc.decompress(compressed_file)

  assert filecmp.cmp("sample.txt", decompressed_file)

# @pytest.mark.skip
def test_with_no_newline_at_end():

  # no new line at the end
  hc = huffman.HuffmanCoding("sample2_with_newline.txt")
  compressed_file = hc.compress()
  decompressed_file = hc.decompress(compressed_file)

  assert filecmp.cmp("sample2_with_newline.txt", decompressed_file)

# @pytest.mark.skip
def test_with_ABRACADABRA():

  # no new line at the end
  hc = huffman.HuffmanCoding("sample3_with_twolines.txt")
  compressed_file = hc.compress()
  decompressed_file = hc.decompress(compressed_file)

  assert filecmp.cmp("sample3_with_twolines.txt", decompressed_file)

# @pytest.mark.skip
def test_with_ABACA():

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

@pytest.mark.skip
def test_performance_compress(capsys):
  hc = huffman.HuffmanCoding("../sample.txt")

  timing = defaultdict(int)
  freq_options = [
      (hc.make_frequency_dict_default, "default"),
      (hc.make_frequency_dict_deprecated, "deprecated"),
      (Counter, "counter")
  ]
  
  with capsys.disabled():
    for tuple in freq_options:
      start = time.time()
      hc.make_frequency_dict = tuple[0]
      hc.compress()
      difference = time.time() - start
      print("(" + tuple[1] + ")", "time taken:", difference)
      timing[tuple[1]] = difference

  pprint(timing)

  improvement = (timing['deprecated'] - timing['counter']
                 ) / timing['deprecated'] * 100
  print("Performance improvement", f'{improvement:.2f}%')

  assert timing['counter'] < timing['default'] < timing['deprecated']
