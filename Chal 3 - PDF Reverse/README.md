## Decompiling the pyc
Since its a .pyc file we first try to use online tools to decompile it

![image](https://github.com/d4rkc0de-club/BankOfE-Event/assets/64488123/d7d5d999-b04b-40da-b3ba-280d9e9e4c11)

As we can see that it cant decompile the work function which is where most of the encrpytion is happening but it identifies it as python 3.8

So, now we install Decompyle6 library and then try to decompyle it ourselves on a machine having python 3.8

![image](https://github.com/d4rkc0de-club/BankOfE-Event/assets/64488123/6b676b1a-52d4-4874-88e5-5c245d98dbb5)


![image](https://github.com/d4rkc0de-club/BankOfE-Event/assets/64488123/99d567c1-b061-491b-9b84-7f3c7acff3c6)


In here we see that it successfully decompiles the work function

Now with the encryptor with ourselves lets try to decrypt it

PS:- Self explanatory dec.py
