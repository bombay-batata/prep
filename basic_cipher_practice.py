


def caesar (text,offset):
    encrypted_text = ""
    for char in text:
        index = ord(char) + offset
        if index > ord("z"):
            index-=26
        elif index < ord("a"):
            index+=26
    encrypted_text+=chr(index)
    return encrypted_text



def main ():
    text = input("Enter the text to be encrypted here")
    offset = int (input("enter the offset number here"))
    encrypted_text = caesar(text, offset)
    print ("encrypted text with caesar cipher" + encrypted_text)

if __name__== "__main__":
    main()
    
    