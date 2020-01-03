[![Run on Repl.it](https://repl.it/badge/github/kgashok/huffman-coding)](https://repl.it/github/kgashok/huffman-coding)  
_(for additional configuration instructions, see [below](https://github.com/kgashok/huffman-coding#repo-to-repl))_

#### The Visual that _really_ works! 

A Glitch Project - https://shining-baroness.glitch.me/

### Python Implementation of Huffman Coding

Explanation at http://bhrigu.me/blog/2017/01/17/huffman-coding-python-implementation/ or http://j.mp/huffmanPy

Consists **compress** and **decompress** function.


#### Testing / Running the program

1. Save / Clone the above repository
2. The repository consists of a sample text file of size 715kB
3. Run the python code `useHuffman.py` to compress & decompress the given sample file


To run the code for compression of any other text file, edit the `path` variable in the `useHuffman.py` file.


For now, the *decompress()* function is to be called from the same object from which the *compress()* function was called, for compressing-decompressing a file (as the encoding information is stored in the data members of the object only) 

## Repo to Repl 
1. Click on the gray **repl.it badge** above. 
2. Wait for the repo to get loaded into repl.it
3. Look for the green "Run" button at the top of the screen. Click on it and existing tests cases should run

![run](/img/runButton.png)

4. If you get an error **"No module named pytest"**, then run the following commands on the right hand side in the bash prompt. 

    ```bash
    chmod 755 install.sh
    ```
    followed by
    ```bash
    . install.sh  # period and space and 'install.sh'
    # wait for 'pytest' and 'autopep8' install to complete
    ```

5. Now, try clicking the green "Run" button again. IT should work.


### The Genius of David Huffman

- Read https://www.maa.org/press/periodicals/convergence/discovery-of-huffman-codes
- Analysis as greedy algorithm https://www.codesdope.com/course/algorithms-huffman-codes/
- Read http://www.skypape.com/huffman.htm 

![huffman](/img/huffmanDr.jpg)