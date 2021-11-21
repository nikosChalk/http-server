

import string

sz = 1024 * 1024 * 200 #200 megabytes
char_chunk_sz = int(sz/len(string.ascii_uppercase))
FILENAME = './public/garbage.html'

if __name__ == "__main__":
    garbage = ""
    for ch in string.ascii_uppercase:
        garbage += ch * char_chunk_sz
    garbage += '\n'

    with open(FILENAME, 'w') as f:
        f.write("<html><head><title>Garbage</title></head>\n")
        f.write("<body>\n")
        f.write("<p>{}</p>\n".format(garbage))
        f.write("</body></html>\n")
        f.write("\n")

