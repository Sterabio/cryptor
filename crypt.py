from cryptography.fernet import Fernet
import argparse
def main():
    parser = argparse.ArgumentParser(description ="cryptor")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-d",'--d',action='store', dest='decrypt',help="file")
    group.add_argument("-e",'--e',action='store', dest='encrypt',help="file")
    parser.add_argument("-k",'--key',action='store', dest='key',help="file")
    group.add_argument("-nk",'--nk',action='store_true',help="file")
    args = parser.parse_args()
    if args.nk:
        create_key()
    else:
        if args.key:
            key = args.key
        else:
            with open("key.key", 'rb') as f:
                key = f.read() 
        if args.decrypt:
            dec(args.decrypt,key)
        if args.encrypt:
            enc(args.encrypt,key)
    

def create_key():
    key = Fernet.generate_key()
    file = open('key.key', 'wb') 
    file.write(key)
    file.close()

def enc(file,key):
    with open(file, 'rb') as f:
        data = f.read() 

    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)

    with open(file, 'wb') as f:
        f.write(encrypted) 



def dec(file,key):
    with open(file, 'rb') as f:
        data = f.read() 

    fernet = Fernet(key)
    try:
        decrypted = fernet.decrypt(data)

        with open(file, 'wb') as f:
            f.write(decrypted)
    except:
        print("Invalid Key - Unsuccessfully decrypted")


#dec("test.txt",key)
if __name__ == '__main__':
    main()

