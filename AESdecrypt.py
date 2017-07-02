from AESdecryptfunc import * #import AESdecryptfunc module to use functions created for this program
import math #import math module to use function such as ceiling

#check that script is running with the two text files as the two parameters or else quit
if len(sys.argv) is not 3:#takes in two arguments for the ciphertext.txt file name and plainhex.txt file name
    sys.exit("Error, script needs two command-line arguments. (Ciphertext.txt File and plainhex.txt File)")
PassPhrase=""

while(len(PassPhrase)!=16):
    print("Enter in the 16 character passphrase to decrypt your text file %s" %sys.argv[1])
    PassPhrase=input()#takes in user input of char, eg. "Iwanttolearnkung"
    print(len(PassPhrase))
    if(len(PassPhrase)<16):#check if less than 16 characters, if so add one space character until 16 chars
        while(len(PassPhrase)!=16):
            PassPhrase=PassPhrase+" "
    if(len(PassPhrase)>16):#check if bigger than 16 characters, if so then truncate it to be only 16 chars from [0:16]
        print("Your passphrase was larger than 16, truncating passphrase.")
        PassPhrase=PassPhrase[0:16]

#open ciphertext.txt file to read and decrypt
file=open(sys.argv[1], "r")
message=(file.read())
print("Inside your ciphertext message is: %s" % message)

#set up some parameters
start=len(message)-32#set starting pointer for the part to decrypt of the ciphertext
end=len(message)#set ending pointer for the part to decrypt of the plaintex
length=len(message)#check the entire size of the message
loopmsg=0.00#create a decimal value
loopmsg=math.ceil(length/32)+1#use formula to figure how long the message is and how many 16 character segmentss must be decrypted
outputhex=""#setup output message in hex

#need to setup roundkeys here
PassPhrase=BitVector(textstring=PassPhrase)
roundkey1=findroundkey(PassPhrase.get_bitvector_in_hex(),1)
roundkey2=findroundkey(roundkey1,2)
roundkey3=findroundkey(roundkey2,3)
roundkey4=findroundkey(roundkey3,4)
roundkey5=findroundkey(roundkey4,5)
roundkey6=findroundkey(roundkey5,6)
roundkey7=findroundkey(roundkey6,7)
roundkey8=findroundkey(roundkey7,8)
roundkey9=findroundkey(roundkey8,9)
roundkey10=findroundkey(roundkey9,10)
roundkeys=[roundkey1,roundkey2,roundkey3,roundkey4,roundkey5,roundkey6,roundkey7,roundkey8,roundkey9,roundkey10]
print(roundkeys[9])
# set up the segement message loop parameters
for y in range(1, loopmsg): # loop to encrypt all segments of the message
    plaintextseg = message[start:end]
    print(plaintextseg)
    # add round key ten
    bv1 = BitVector(hexstring=plaintextseg)
    bv2 = BitVector(hexstring=roundkeys[9])
    resultbv = bv1 ^ bv2
    myhexstring = resultbv.get_bitvector_in_hex()
    print("The output after adding the roundkey 10 is: %s" % myhexstring)

