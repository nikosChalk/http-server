

import string

sz = 1024 * 1024 * 200 #200 megabytes
char_chunk_sz = int(sz/len(string.ascii_uppercase))
FILENAME_GARBAGE = './public/garbage.blob'
FILENAME_TESTPATH = './public/testpath.blob'

if __name__ == "__main__":
    garbage = ""
    for ch in string.ascii_uppercase:
        garbage += ch * char_chunk_sz
    garbage += '\n'

    with open(FILENAME_GARBAGE, 'w') as f:
        f.write("{}\n".format(garbage))

    with open(FILENAME_TESTPATH, 'w') as f:
        f.write("Hello World!\n")

