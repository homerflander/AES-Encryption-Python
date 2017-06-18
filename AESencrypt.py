from AESfunc import *
import math

if len(sys.argv) is not 3:  # takes in two arguments for plaintext.txt and ciphertext.txt
    sys.exit("Error, script needs two command-line arguments. (Plaintext.txt File and Ciphertext.txt File)")

#PassPhrase = "Thats my Kung Fu"#set static pass for now 16 char * 8 bits = 128 bits strength

PassPhrase = ""
while(len(PassPhrase)!=16):
    print("Enter in the 16 character passphrase to encrypt your text file %s" %sys.argv[1])
    PassPhrase=input()
    print(len(PassPhrase))
    if(len(PassPhrase)<16):
        while(len(PassPhrase)!=16):
            PassPhrase=PassPhrase+" "
    if(len(PassPhrase)>16):
        print("Your passphrase was larger than 16, truncating passphrase.")
        PassPhrase=PassPhrase[0:16]



# open message to encrypt
file = open(sys.argv[1], "r")
message = (file.read())
print("Inside your plaintext message is: %s" % message)
start = 0
end = 0
length = len(message)
loopmsg = 0.00
loopmsg = len(message)/16
outputhex = ""
# add round key
for y in range(1, math.ceil(loopmsg)+1):  # loop to encrypt all parts of the message
    if(end+16<length):
        eightbit = message[start:end + 16]
    else:
        eightbit = message[start:length]
        for z in range(0,((end+16)-length)):
            eightbit=BitVector(textstring=eightbit)
            eightbit=eightbit.get_bitvector_in_hex()+"00"
            eightbit=BitVector(hexstring=eightbit).get_bitvector_in_ascii()
            z=z+1
    print("The round key string is : %s" % PassPhrase)
    print("The part of the message to be encrypted is : %s" % eightbit)
    bv1 = BitVector(textstring=eightbit)
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

        temp2=subbyte(myhexstring)
        print("The subbyte output is: %s" % temp2)
        # shift rows

        temp3=shiftrow(temp2)


        print("The shiftrow output is: %s" % temp3)

        # mix column
        bv3 = BitVector(hexstring=temp3)
        newbvashex=mixcolumn(bv3)
        newbv=BitVector(hexstring=newbvashex)
        print("The Mixcolumn Output is: %s" % newbvashex)

        #add roundkey
        bv1 = BitVector(bitlist=newbv)
        bv2 = BitVector(hexstring=roundkey)
        resultbv = bv1 ^ bv2
        myhexresult = resultbv.get_bitvector_in_hex()
        print("The output after adding the round key: %s" % myhexresult)
        roundkey=findroundkey(roundkey,x+1)
        print("The round key %i is " %(x+1) + roundkey)


        # sub byte round 10
    print("Round 10:")
    myhexstring = resultbv.get_bitvector_in_hex()
    temp2=subbyte(myhexstring)
    print("The subbyte output of round 10 is: %s" % temp2)

    # shift rows
    temp3=shiftrow(temp2)

    print("The output after shiftrow is: %s" % temp3)
    # addround key
    newbv = BitVector(hexstring=temp3)
    bv1 = BitVector(bitlist=newbv)
    bv2 = BitVector(hexstring=roundkey)
    resultbv = bv1 ^ bv2
    myhexstring = resultbv.get_bitvector_in_hex()
    print("The output after adding the roundkey is: %s" % myhexstring)

    outputhextemp = resultbv.get_hex_string_from_bitvector()
    print("The outputhex value for this part of the message is: %s" % outputhextemp)
    outputhex = outputhex + outputhextemp
    start = start + 16
    end = end + 16

# output encrypted to file
print("The outputhex value for the entire message is: %s" % outputhex)
FILEOUT = open(sys.argv[2], 'w')
FILEOUT.write(outputhex)
FILEOUT.close()
