import hashlib,argparse,os
def md5(hash,wordlist,format):
    file = open(wordlist,'r')
    for item in file.readlines():
        pas = hashlib.md5(item.strip().encode()).hexdigest()
        # pas.update(item.encode())
        # final = pas.hexdigest()
        print("[+] Hash type:",format)
        if pas == hash:
            print(f"\n[+] cracked\n[+] Hash: {hash}\n[+] Password:",item,'\n')
            exit()
    print("[!] Hash not cracked\n")

def sha1(hash,wordlist,format):
    file = open(wordlist,'r')
    for item in file.readlines():
        pas = hashlib.sha1(item.strip().encode()).hexdigest()
        # pas.update(item.encode())
        # final = pas.hexdigest()
        print("[+] Hash type:",format)
        if pas == hash:
            print(f"\n[+] cracked\n[+] Hash: {hash}\n[+] Password:",item,'\n')
            exit()
    print("[!] Hash not cracked\n")

def sha256(hash,wordlist,format):
    file = open(wordlist,'r')
    for item in file.readlines():
        pas = hashlib.sha256(item.strip().encode()).hexdigest()
        # pas.update(item.encode())
        # final = pas.hexdigest()
        print("[+] Hash type:",format)
        if pas == hash:
            print(f"\n[+] cracked\n[+] Hash: {hash}\n[+] Password:",item,'\n')
            exit()
    print("[!] Hash not cracked\n")

def sha384(hash,wordlist,format):
    file = open(wordlist,'r')
    for item in file.readlines():
        pas = hashlib.sha384(item.strip().encode()).hexdigest()
        # pas.update(item.encode())
        # final = pas.hexdigest()
        print("[+] Hash type:",format)
        if pas == hash:
            print(f"\n[+] cracked\n[+] Hash: {hash}\n[+] Password:",item,'\n')
            exit()
    print("[!] Hash not cracked\n")

def sha512(hash,wordlist,format):
    file = open(wordlist,'r')
    for item in file.readlines():
        pas = hashlib.sha512(item.strip().encode()).hexdigest()
        # pas.update(item.encode())
        # final = pas.hexdigest()
        print("[+] Hash type:",format)
        if pas == hash:
            print(f"\n[+] cracked\n[+] Hash: {hash}\n[+] Password:",item,'\n')
            exit()
    print("[!] Hash not cracked\n")

if __name__=='__main__':
    print('''

██╗░░██╗░█████╗░░██████╗██╗░░██╗░█████╗░██████╗░░█████╗░░█████╗░██╗░░██╗███████╗██████╗░
██║░░██║██╔══██╗██╔════╝██║░░██║██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║░██╔╝██╔════╝██╔══██╗
███████║███████║╚█████╗░███████║██║░░╚═╝██████╔╝███████║██║░░╚═╝█████═╝░█████╗░░██████╔╝
██╔══██║██╔══██║░╚═══██╗██╔══██║██║░░██╗██╔══██╗██╔══██║██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
██║░░██║██║░░██║██████╔╝██║░░██║╚█████╔╝██║░░██║██║░░██║╚█████╔╝██║░╚██╗███████╗██║░░██║
╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
                                                                    v1.0 @ajmewal
    \n''')
    parse = argparse.ArgumentParser()
    parse.add_argument('-H','--hash',help="Enter Your hash")
    parse.add_argument('-w','--wordlist',help="Give the wordlist path")
    parse.add_argument('-f','--format',help="Specify the hash format")
    parse.add_argument('-l','--list-format',action='store_true',help="list the avilable hash format")
    args = parse.parse_args()
    support_format=['md5','sha1','sha256','sha384','sha512']
    if args.list_format:
        for i in support_format:
            print('[+]',i)
        exit()
    hash = args.hash
    if hash==None:
        print("[?] please give a hash")
        exit()
    if args.wordlist==None:
        print('[?] Give a wordlist')
        exit()
    elif os.path.isfile(args.wordlist):
        wordlist=args.wordlist
    else:
        print("[?] wordlist is not avilable")
        exit()
    format=args.format
    if format==None:
        print('[?] Please specify a format for better result\n')
        exit()
    elif format not in support_format:
        print("[!] Format is not supported please use -l for list formats\n")
        exit()
    if format=='md5':
        md5(hash,wordlist,format)
    elif format=='sha1':
        sha1(hash,wordlist,format)
    elif format=='sha256':
        sha256(hash,wordlist,format)
    elif format=='sha384':
        sha384(hash,wordlist,format)
    elif format=='sha512':
        sha512(hash,wordlist,format)
