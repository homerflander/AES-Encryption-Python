from AESencryptfunc import * #import AESencryptfunc module to use functions created for this program
import math #import math module to use function such as ceiling

#check that script is running with the two text files as the two parameters or else quit
if len(sys.argv) is not 3:#takes in two arguments for the plaintext.txt file name and cipherhex.txt file name
    sys.exit("Error, script needs two command-line arguments. (Plaintext.txt File and cipherhex.txt File)")

# set passphrase to be a 16 characters, 16 characters * 8 bits = 128 bits strength
PassPhrase=""
while(len(PassPhrase)!=16):
    print("Enter in the 16 character passphrase to encrypt your text file %s" %sys.argv[1])
    PassPhrase=input()#takes in user input of char, eg. "Iwanttolearnkung"
    print(len(PassPhrase))
    if(len(PassPhrase)<16):#check if less than 16 characters, if so add one space character until 16 chars
        while(len(PassPhrase)!=16):
            PassPhrase=PassPhrase+" "
    if(len(PassPhrase)>16):#check if bigger than 16 characters, if so then truncate it to be only 16 chars from [0:16]
        print("Your passphrase was larger than 16, truncating passphrase.")
        PassPhrase=PassPhrase[0:16]

#open plaintext.txt file to read and encrypt
file=open(sys.argv[1], "r")
message=(file.read())
print("Inside your plaintext message is: %s" % message)

#set up some parameters
start=0#set starting pointer for the part to encrypt of the plaintext
end=0#set ending pointer for the part to encrypt of the plaintex
length=len(message)#check the entire size of the message
loopmsg=0.00#create a decimal value
loopmsg=math.ceil(length/16)+1#use formula to figure how long the message is and how many 16 character segmentss must be encrypted
outputhex=""#setup output message in hex

# set up the segement message loop parameters
for y in range(1, loopmsg): # loop to encrypt all segments of the message
    if(end+16<length): #if the end pointer is less than the size of the message, then set the segment to be 16 characters
        plaintextseg = message[start:end + 16]
    else: #or else if the end pointer is equal to or greator than the size of the message
        plaintextseg = message[start:length]
        for z in range(0,((end+16)-length),2): #run a while loop to pad the message segement to become 16 characters, if it is 16 already the loop will not run
            plaintextseg=BitVector(textstring=plaintextseg)
            plaintextseg=plaintextseg.get_bitvector_in_hex()+"00"
            plaintextseg=BitVector(hexstring=plaintextseg).get_bitvector_in_ascii()
    #add round key zero/ find round key one
    print("The round key string is : %s" % PassPhrase)
    print("The part of the message to be encrypted is : %s" % plaintextseg)
    bv1 = BitVector(textstring=plaintextseg)
    print("The plaintext message in hex is : %s" % bv1.get_bitvector_in_hex())
    bv2 = BitVector(textstring=PassPhrase)
    print("The password in hex/ roundkey zero is : %s" % bv2.get_bitvector_in_hex())
    resultbv=bv1^bv2
    roundkey=findroundkey(bv2.get_bitvector_in_hex(),1)
    print("The round key one is : %s" % roundkey)
    myhexstring = resultbv.get_bitvector_in_hex()
    print("The initial adding round key output is : %s" % myhexstring)

    for x in range(1, 10):  # loop through 9 rounds
        # sub byte
        print("Round: %i" % x)
        myhexstring = resultbv.get_bitvector_in_hex()
        temp1=subbyte(myhexstring)
        print("The subbyte output is: %s" % temp1)

        # shift rows
        temp2=shiftrow(temp1)
        print("The shiftrow output is: %s" % temp2)

        # mix column
        bv3 = BitVector(hexstring=temp2)
        newbvashex=mixcolumn(bv3)
        newbv=BitVector(hexstring=newbvashex)
        print("The Mixcolumn Output is: %s" % newbvashex)

        #add roundkey for current round
        bv1 = BitVector(bitlist=newbv)
        bv2 = BitVector(hexstring=roundkey)
        resultbv = bv1 ^ bv2
        myhexresult = resultbv.get_bitvector_in_hex()
        print("The output after adding the round key: %s" % myhexresult)

        #create new roundkey for next round
        roundkey=findroundkey(roundkey,x+1)
        print("The round key %i is " %(x+1) + roundkey)


    #start round 10
    # sub byte round 10
    print("Round 10:")
    myhexstring = resultbv.get_bitvector_in_hex()
    temp1=subbyte(myhexstring)
    print("The subbyte output of round 10 is: %s" % temp1)

    # shift rows round 10
    temp2=shiftrow(temp1)
    print("The output after shiftrow is: %s" % temp2)

    # addround key round 10
    newbv = BitVector(hexstring=temp2)
    bv1 = BitVector(bitlist=newbv)
    bv2 = BitVector(hexstring=roundkey)
    resultbv = bv1 ^ bv2
    myhexstring = resultbv.get_bitvector_in_hex()
    print("The output after adding the roundkey is: %s" % myhexstring)

    #set encrypted hex segement of message to output string
    outputhextemp = resultbv.get_hex_string_from_bitvector()
    print("The outputhex value for this part of the message is: %s" % outputhextemp)
    outputhex = outputhex + outputhextemp
    start = start + 16 #increment start pointer
    end = end + 16 #increment end pointer

#  encrypted output hex string to specified cipherhex file
print("The outputhex value for the entire message is: %s" % outputhex)
FILEOUT = open(sys.argv[2], 'w')
FILEOUT.write(outputhex)
FILEOUT.close()
