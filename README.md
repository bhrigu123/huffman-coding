[![Run on Repl.it](https://repl.it/badge/github/kgashok/huffman-coding)](https://repl.it/github/kgashok/huffman-coding)


### Python Implementation of Huffman Coding

Explanation at http://bhrigu.me/blog/2017/01/17/huffman-coding-python-implementation/

Consists **compress** and **decompress** function.

#### Repo to Repl 
1. Click on the repl.it badge above. 
2. Look for the green "Run" button at the top of the screen. Click on it and existing tests cases should run

![run](/img/runButton.png)

3. If you get an error **"No module named pytest"**, then run the following commands on the right hand side in the bash prompt. 

    ```bash
    chmod 755 install.sh
    ./install.sh # (pytest and autopep8 install triggered)
    ```

4. Now, try clicking the green "Run" button again. IT should work.

#### Testing / Running the program

1. Save / Clone the above repository
2. The repository consists of a sample text file of size 715kB
3. Run the python code `useHuffman.py` to compress & decompress the given sample file


To run the code for compression of any other text file, edit the `path` variable in the `useHuffman.py` file.


For now, the *decompress()* function is to be called from the same object from which the *compress()* function was called, for compressing-decompressing a file (as the encoding information is stored in the data members of the object only) 

