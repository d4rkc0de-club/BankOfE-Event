# importing necessary libraries
from Crypto.Cipher import AES

# we first read the encrypted file
with open("file.enc","rb") as f:
    file = bytearray(f.read())

# from the source code we get the key
key = bytearray(b'=======anime_n_gaming.exe=======')

# Now we extract the IV and length of file from the rest file
IV = file[:16]
print("IV",IV)
lenfile = int(file[16:32].decode("utf-8"))
file = file[32:]

# Making the AES Decryptor
decryptor = AES.new(key, AES.MODE_CBC, IV)

# since its XOR, hence we simply xor it with itself as xor is interchangeable
newfile = decryptor.decrypt(file)

# removing padding from decrypted file
newfile = bytearray(newfile)
newfile = newfile[:lenfile]

# cutting the xorred content into 2 and doing some reversing and joining them back again and reversing
file1 = newfile[:len(newfile)//2]
file2 = newfile[len(newfile)//2:]
file1.reverse()
file2.reverse()
file = file1+file2
file.reverse()

# and we dump the file
with open("file.dec","wb") as f:
    f.write(file)
