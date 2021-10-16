"""Problem 59: XOR decryption

Each character on a computer is assigned a unique code and the preferred
standard is ASCII (American Standard Code for Information Interchange). For
example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII,
then XOR each byte with a given value, taken from a secret key. The advantage
with the XOR function is that using the same encryption key on the cipher text,
restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text
message, and the key is made up of random bytes. The user would keep the
encrypted message and the encryption key in different locations, and without
both "halves", it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified
method is to use a password as a key. If the password is shorter than the
message, which is likely, the key is repeated cyclically throughout the
message. The balance for this method is using a sufficiently long password
key for security, but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower
case characters. Using cipher1.txt, a file containing the encrypted ASCII codes,
and the knowledge that the plain text must contain common English words, decrypt
the message and find the sum of the ASCII values in the original text.

byte1   a   b   c   d   e   f   g   h
byte2   i   j   k   l   m   n   o   p
xor    -------------------------------
output a^i b^j c^k d^l e^m f^n g^o h^p
x^y = x xor y

xor| 1 | 0 |
---+--------
 1 | 0   1 |
 0 | 1   0 |
"""
       
with open('cipher1.problem59.txt') as file:
    oldtext=(file.readlines()[0].replace('\n','')).split(',')
for i,j in enumerate(oldtext):
    oldtext[i]=int(j)


for a in range(97,123):
    for b in range(97,123):
        for c in range(97,123):
            key=(a,b,c)
            msg=''
            for i in range(60):
                msg+=chr(oldtext[i]^key[i%3])
            if ' ' not in msg: continue
            if (' the ' or ' The ' or ' you ' or ' You ' or ' we ' or ' We ' or
                ' he ' or ' He ' or ' She ' or ' she ' or ' it ' or ' It ' or
                ' they ' or ' They ' or ' of ' or ' from ' or ' in ') in msg:
                print(msg,'... ',key,end='\n\n',sep='')
                
#We found out that the key is 103 111 100=>'god'.
#Sample text: "(The Gospel of John, chapter 1) 1 In the beginning the Word..."
key=(103, 111, 100)

newtext=[]
length=len(oldtext)
file=open('cracked.cipher1.problem59.txt','w')

for i in range(length):
    newtext.append(oldtext[i]^key[i%3])
    file.write(chr(newtext[i]))
file.close()

print("Solution:", sum(newtext))
