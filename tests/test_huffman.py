import filecmp
import huffman


def test_creation_of_huffman():
  hc = huffman.HuffmanCoding("sample.text")


def test_input_equals_output():

  hc = huffman.HuffmanCoding("sample.txt")
  compressed_file = hc.compress()
  decompressed_file = hc.decompress(compressed_file)

  actual = filecmp.cmp("sample.txt", decompressed_file)

  assert actual


def test_with_no_newline_at_end():

  # no new line at the end
  hc = huffman.HuffmanCoding("sample2_with_newline.txt")
  compressed_file = hc.compress()
  decompressed_file = hc.decompress(compressed_file)

  actual = filecmp.cmp("sample2_with_newline.txt", decompressed_file)


def test_with_multiple_lines():

  # no new line at the end
  hc = huffman.HuffmanCoding("sample3_with_twolines.txt")
  compressed_file = hc.compress()
  decompressed_file = hc.decompress(compressed_file)

  actual = filecmp.cmp("sample3_with_twolines.txt", decompressed_file)


def test_with_multiple_lines_with_newline():

  # no new line at the end
  hc = huffman.HuffmanCoding("sample4.txt")
  compressed_file = hc.compress()
  decompressed_file = hc.decompress(compressed_file)

  actual = filecmp.cmp("sample4.txt", decompressed_file)
