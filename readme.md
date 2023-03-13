<h1 align="center">
  <br>
  <a href=""><img src="https://github.com/ajmewal/Password-Cracker/blob/master/Pass_cracker.png" width="200px" alt="Pass_Cracker"></a>
</h1>



Basic password cracker. These tools can be used to crack various types of password hashes, the program applies the technique to recover the original password from the hash.

---

# Requirements

You need to have python3 to install this script.

# Installation

```bash
git clone https://github.com/ajmewal/Password-Cracker.git
cd Password-Cracker
python3 pass_cracker.py
```

# Usage
```bash 
Python3 pass_cracker.py -h
```
Please find below the instructions to access the tool's help function, along with a list of all available switches:
```bash
██╗░░██╗░█████╗░░██████╗██╗░░██╗░█████╗░██████╗░░█████╗░░█████╗░██╗░░██╗███████╗██████╗░
██║░░██║██╔══██╗██╔════╝██║░░██║██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║░██╔╝██╔════╝██╔══██╗
███████║███████║╚█████╗░███████║██║░░╚═╝██████╔╝███████║██║░░╚═╝█████═╝░█████╗░░██████╔╝
██╔══██║██╔══██║░╚═══██╗██╔══██║██║░░██╗██╔══██╗██╔══██║██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
██║░░██║██║░░██║██████╔╝██║░░██║╚█████╔╝██║░░██║██║░░██║╚█████╔╝██║░╚██╗███████╗██║░░██║
╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
                                                                    v1.0


usage: crack.py [-h] [-H HASH] [-w WORDLIST] [-f FORMAT] [-l]

options:
  -h, --help            show this help message and exit
  -H HASH, --hash HASH  Enter Your hash
  -w WORDLIST, --wordlist WORDLIST
                        Give the wordlist path
  -f FORMAT, --format FORMAT
                        Specify the hash format
  -l, --list-format     list the avilable format
```
## Authors

<a href="https://github.com/ajmewal"><img src="https://avatars.githubusercontent.com/u/82837448?v=4"></a>
