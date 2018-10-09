import os
def zipcrack(filename,wordlist):
    return os.system("fcrackzip -u -D -p " + wordlist + " " + filename)
