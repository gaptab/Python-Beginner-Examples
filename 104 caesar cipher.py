def main():
    print("Ceasar Cipher")
    print("1. Encrypt \n2. Decrypt:")
    try:
        func=int(input("Choose one of the above"))
    except:
        print("Invalid input")
        
    if func==2:
        decode()
    else:
        if func==1:
            encode()
        else:
            print("Invalid input")
        

def encode():
    text=input("Enter the text to encode:")
    key=input("Enter number of characters you want to shift:")
    encoded_cipher=""
    try:
        key=int(key)
    except:
        print("Only integers between 0 to 25 are allowed. Try again!")
        exit()
    if key>25:
        print("only integers between 0 to 25 are allowed")
        exit()
    else:
        key=key
    text=text.upper()
    for char in text:
        ascii=ord(char)
        if ascii >90:
            new_ascii=ascii
        else:
            new_ascii=ascii+key
            if new_ascii>90:
                new_ascii=new_ascii-26
            else:
                new_ascii=new_ascii
        encoded=chr(new_ascii)
        encoded_cipher=encoded_cipher+ encoded
    print("Encoded text:",encoded_cipher) 

def decode():
    cipher=input("enter your cipher text")
    print("Posibilities of cipher text are:\n")
    cipher=cipher.lower()
    for i in range(1,26):
        decoded=''
        decoded_cipher=''
        for char in cipher:
            ascii=ord(char)
            if ascii<97:
                new_ascii=ascii
            else:
                if ascii>122:
                    new_ascii=ascii
                else:
                    new_ascii=ascii-int(i)
                    if new_ascii<97:
                        new_ascii=new_ascii +26
                    else:
                        new_ascii=new_ascii
        decoded=chr(new_ascii)
        decoded_cipher=decoded_cipher + decoded
    print(decoded_cipher)
        
if __name__=='__main__':
    main()
