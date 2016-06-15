# Day 14 - IO

If you can't access a file, your program is isolated from the outside world. Try accessing a file by first, open it

    fRead = open('hello.txt', 'r')

where `hello.txt` is the (absolute/relative) path to the file, `r` means open for read.

You can later read the entire file by 'fRead.read()' or line-by-line by `fRead.readline()`

Open another file for writing using

    fWrite = open('world.txt', 'w')

and then `fWrite.write('Many thanks')` to write to it.

Don't forget to close the files once you're done with it.

    fRead.close()
    fWrite.close()

Find out more on ![doc](https://docs.python.org/2.7/tutorial/inputoutput.html)
