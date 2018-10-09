def caesar_cipher(text):
    def caeser(text,rot):
        result = ""
        for i in range(len(text)):
            char = text[i]
            if (char.isupper()):
                result += chr((ord(char) + rot - 65) % 26 + 65)
            elif char == ' ':
                result += ' '
            else:
                result += chr((ord(char) + rot - 97) % 26 + 97)
        return result
    for rot in range(26):
        return "ROT{} : {}".format(rot, caeser(text, rot))
