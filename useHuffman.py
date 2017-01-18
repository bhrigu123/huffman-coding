from huffman import HuffmanCoding
import sys

if(len(sys.argv) == 1):
	print("Give complete file path as argument")
	exit(0)

path = sys.argv[1]

h = HuffmanCoding(path)

output_path = h.compress()
print("Compressed file path: " + output_path)

decom_path = h.decompress(output)
print("Decompressed file path: " + decom_path)