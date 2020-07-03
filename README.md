### Python Implementaion of Huffman Coding

Explanation on YouTube video https://youtu.be/JCOph23TQTY.
Was originally posted in blog article at https://bhrigu.me/blog/2017/01/17/huffman-coding-python-implementation/

Consists **compress** and **decompress** function.


#### Testing / Running the program

1. Save / Clone the above repository
2. The repository consists of a sample text file of size 715kB
3. Run the python code `useHuffman.py` to compress & decompress the given sample file. For eg. open terminal and run `python3 useHuffman.py`
4. The above command will perform compression and decompression on the sample.txt file present here. Both the compressed and decompressed file will be present at the same location.


To run the code for compression of any other text file, edit the `path` variable in the `useHuffman.py` file.


For now, the *decompress()* function is to be called from the same object from which the *compress()* function was called. (as the encoding information is stored in the data members of the object only) 
