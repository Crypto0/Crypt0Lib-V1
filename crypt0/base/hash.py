import hashlib,time,sys
def hash(hashType,userHash,wordlist):
        if hashType == "md5" or hashType == "MD5":
            h = hashlib.md5
        elif hashType == "sha1" or hashType == "SHA1":
            h = hashlib.sha1
        elif hashType == "sha224" or hashType == "SHA224":
            h = hashlib.sha224
        elif hashType == "sha256" or hashType == "SHA256":
            h = hashlib.sha256
        elif hashType == "sha384" or hashType == "SHA384":
            h = hashlib.sha384
        elif hashType == "sha512" or hashType == "SHA512":
            h = hashlib.sha512
        else:
            return "Sorry!, We cant BruteForce %s , Please make sure you entered HashType correctly." % hashType
            exit()
        verbose = True
        start = time.time()
        with open(wordlist, "rU") as infile:
            for line in infile:
                line = line.strip()
                lineHash = h(line).hexdigest()
                if (verbose == True):
                    sys.stdout.write('\r' + str(line) + ' ' * 20)
                    sys.stdout.flush()
                if (str(lineHash) == str(userHash.lower())):
                    end = time.time()
                    return "\n\n[+] HASH IS CRACKED SUCCESSFUL : [ %s ]" % line
                    return "[*] Time Taken: %s seconds" % round((end - start), 2)
                    exit()
        end = time.time()
        return "\n\n[-]Cracking Failed"
        return "[*]Reached end of wordlist"
        return "[*] Time Taken: %s seconds" % round((end - start), 2)
        exit()
