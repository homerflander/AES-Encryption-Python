# AES-Encryption-Python (Completed/Working)

Created by Van. June 2017 </br>

Resource(s) Used: </br>
-BitVector class created by Avinash Kak (kak@purdue.edu) at https://engineering.purdue.edu/kak/dist/BitVector-3.4.4.html </br>
-Nist Announcement Publication of AES in 2001 at http://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.197.pdf </br>
-Used Kavaliro Slides at https://kavaliro.com/wp-content/uploads/2014/03/AES.pdf to check work </br>
-Used Online AES Encryption Tools at http://aes.online-domain-tools.com/ and http://extranet.cryptomathic.com/aescalc/index to check work 

Summary:</br>
Two scripts in Python to encrypt/decrypt using the 128 bits AES algorithm, ECB mode with hex "00" as padding for each character. For the encryption, an ascii plaintext file is taken as the input, then an encrypted hex file is outputted. For the decryption, a ciphertext hex file is taken as the input, then a decrypted ascii file is outputted.</br>

Notes: </br> 
-ECB is not considered secure since it has vulnerabilities in encrypting the same plaintext block. Encrypting the same plaintext block will create the same block of ciphertext. Possible future improvement is to use a more psuedo random mode other than ECB.</br>
<br />
--------------------Demonstration--------------------<br />
General Overview Process: <br />
![general](/Demo/1.png)
<br /><br /><br />
AES Encryption and Decryption Process: <br />
![aesprocess](/Demo/2.png)
<br /><br /><br />
plaintext1.txt File Contents: <br />
![plaintext1](/Demo/3.png)
<br /><br /><br />
AESencryption Folder Contents: <br />
![aesfolder](/Demo/4.png)
<br /><br /><br />
Running AESencrypt.py Script: <br />
![encrypt.py](/Demo/5.png)
<br /><br /><br />
Checking ciphertext.txt File Contents: <br />
![ciphertext](/Demo/6.png)
<br /><br /><br />
Running AESdecrypt.py Script with Wrong Passphrase: <br />
![wrong](/Demo/7.png)
<br /><br /><br />
Running AESdecrypt.py Scipt with Correct Passphrase: <br />
![right](/Demo/8.png)
<br /><br /><br />
Checking plaintext1.txt File with plaintext2.txt File: <br />
![lastcheck](/Demo/9.png)
<br /><br /><br />
Checking AESencrypt.py Script with Online AES Encrypt Tool: <br />
![lastcheck](/Demo/10.png)
<br /><br /><br />
