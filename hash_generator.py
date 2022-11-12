# Python program to find hexadecimal hash string of a file
import hashlib
from os.path import exists

# Make an pause function because os.system("pause") seems to only work on windows
def pause():
    input("Press the <ENTER> key to continue...")
    
# Because there is no goto function just do a while loop which will run as long as there is not the "correct" answer
continueProgram = False
while (not continueProgram):
    #Ask for a filename, check if if exits. If yes continue else go back to asking
    filename = input("Enter the input file name: ")
    if (exists(filename)):
        continueProgram = True
    else:
        print("There is no file named " + filename)
        pause()

#Start same "loop" as above but this time ask which hash method he wants to use
print("""Please select the hash method.
It can be one of the following:
0: sha1
1: sha224
2: sha256
3: sha384
4: sha512
5: blake2b
6: blake2s
7: md5
8: sha3_224
9: sha3_256
10: sha3_384
11: sha3_512
12: shake_128
13: shake_256""")
continueProgram = False
while (not continueProgram):
    hashmethod = input("Hash method to use: ")
    #If we use shake we have to get a lenght else just continue
    if (hashmethod in ["12","13"]):
        #Get lenght and check if its a number and above 0
        hashmethod_lenght = input("What lenght should be used?: ")
        if (hashmethod_lenght.isnumeric()):
            hashmethod_lenght = int(hashmethod_lenght)
            continueProgram = True
        else:
            print("The provided input is not a valid")
            pause()
    else:
        if (hashmethod in ["0","1","2","3","4","5","6","7","8","9","10","11"]): 
            continueProgram = True
        else:
            print (hashmethod + " is not a number from the list!")
            pause()

#aks if theres a Value thats expected and
expected_hash = input("Enter expected Hash (optional): ")

# Open files in "readbytes" mode and generate the hash
with open(filename,"rb") as f:
    bytes = f.read() # read entire file as bytes

    if hashmethod == "0": #sha1
        readable_hash = hashlib.sha1(bytes).hexdigest()
    elif hashmethod == "1": #sha224
        readable_hash = hashlib.sha224(bytes).hexdigest()
    elif hashmethod == "2": #sha256
        readable_hash = hashlib.sha256(bytes).hexdigest()
    elif hashmethod == "3": #sha384
        readable_hash = hashlib.sha384(bytes).hexdigest()
    elif hashmethod == "4": #sha512
        readable_hash = hashlib.sha512(bytes).hexdigest()
    elif hashmethod == "5": #blake2b
        readable_hash = hashlib.blake2b(bytes).hexdigest()
    elif hashmethod == "6": #blake2s
        readable_hash = hashlib.blake2s(bytes).hexdigest()
    elif hashmethod == "7": #md5
        readable_hash = hashlib.md5(bytes).hexdigest()
    elif hashmethod == "8": #sha3_224
        readable_hash = hashlib.sha3_224(bytes).hexdigest()
    elif hashmethod == "9": #sha3_256
        readable_hash = hashlib.sha3_256(bytes).hexdigest()
    elif hashmethod == "10": #sha3_384
        readable_hash = hashlib.sha3_384(bytes).hexdigest()
    elif hashmethod == "11": #sha3_512
        readable_hash = hashlib.sha3_512(bytes).hexdigest()
    elif hashmethod == "12": #shake_128
        readable_hash = hashlib.shake_128(bytes).hexdigest(hashmethod_lenght)
    elif hashmethod == "13": #shake_256
        readable_hash = hashlib.shake_256(bytes).hexdigest(hashmethod_lenght)

#i think this is self explanatory
print("The hash is: " + readable_hash)
if not (expected_hash == ""):
    if (expected_hash == readable_hash):
        print("The hash matches the expected Hash")
    else:
        print("The hash does NOT matches the expected Hash")
pause()
quit()