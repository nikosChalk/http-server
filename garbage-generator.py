

import string
import random

sz = 1024 * 1024 * 200 #200 megabytes
alphabet = string.ascii_lowercase + string.ascii_uppercase
char_chunk_sz = int(sz/len(alphabet))
FILENAME_GARBAGE = './public/garbage.blob'
FILENAME_TESTPATH = './public/testpath.blob'

if __name__ == "__main__":

    # Way 1:
    # garbage = [ alphabet[random.randrange(0, len(alphabet))] for _ in range(sz) ]
    # garbage = ''.join(garbage) + '\n'

    # Way 2: (better performance)
    garbage = []
    for ch in alphabet:
        garbage += list(ch * char_chunk_sz)
    random.shuffle(garbage)
    garbage = ''.join(garbage) + '\n'

    # Old way with no randomness:
    # garbage = ""
    # for ch in alphabet:
    #     garbage += ch * char_chunk_sz
    # garbage += '\n'

    with open(FILENAME_GARBAGE, 'w') as f:
        f.write("{}\n".format(garbage))

    with open(FILENAME_TESTPATH, 'w') as f:
        f.write("Hello World!\n")

