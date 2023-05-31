# Challenge 2 - Binary Exploitation

In this challenge we were given a executable binary, no other information was provided.

## Solution

### Running the binary

We run the binary and it shows the following output:

```
➜ ./epass
Welcome to EPass Password Manager!
=================
(0)  locker
(1)  lvlC
(2)  phone
(3)  pc
(4)  bank
(5)  mail
=================
choice:
```

I looks like a simple CLI password manager. We see an entry named "lvlC" which might give us the flag but it requires a master password.

```
Welcome to EPass Password Manager!
=================
(0)  locker
(1)  lvlC
(2)  phone
(3)  pc
(4)  bank
(5)  mail
=================
choice: 1
Enter Master password: xyz
Invalid password!
```

We try running `strings epass` to see if we find anything interesting.

```
➜ strings epass
/lib64/ld-linux-x86-64.so.2
libc.so.6
strncmp
__isoc99_scanf
printf
__libc_start_main
GLIBC_2.7
GLIBC_2.2.5
__gmon_start__
H=`A@
[]A\A]A^A_
locker
lvlC
phone
bank
mail
Welcome to EPass Password Manager!
=================
(%d)  %s
choice: 
Invalid choice!
Enter Master password: 
Password for [%s] => 
Invalid password!
;*3$"
libc.so.6
GCC: (Ubuntu 9.4.0-1ubuntu1~20.04.1) 9.4.0
clang version 10.0.0-4ubuntu1 
crtstuff.c
deregister_tm_clones
__do_global_dtors_aux
completed.8061
__do_global_dtors_aux_fini_array_entry
frame_dummy
__frame_dummy_init_array_entry
epass.c
__FRAME_END__
__init_array_end
_DYNAMIC
__init_array_start
__GNU_EH_FRAME_HDR
_GLOBAL_OFFSET_TABLE_
__libc_csu_fini
strncmp@@GLIBC_2.2.5
_edata
masterpass
printf@@GLIBC_2.2.5
passwords
__libc_start_main@@GLIBC_2.2.5
__data_start
__gmon_start__
__dso_handle
```

Here we can see the entry names "locker", "lvlC", "phone", etc. and some output strings.
There are some strings like "passwords" and "masterpass" but these are invalid. It means that the passwords are not stored as strings in this binary.

We also see that `strncmp` is used somewhere in this program, this is probably for checking the master password.
If we run ltrace on this program we can see what our input would be compared to for authentication.

```
➜ ltrace ./epass
printf("Welcome to EPass Password Manage"...Welcome to EPass Password Manager!
)                                                                              
printf("=================\n"=================
)                                                                              
printf("(%d)  %s\n", 0, "locker"(0)  locker
)                                                                              
printf("(%d)  %s\n", 1, "lvlC"(1)  lvlC
)                                                                              
printf("(%d)  %s\n", 2, "phone"(2)  phone
)                                                                              
printf("(%d)  %s\n", 3, "pc"(3)  pc
)                                                                              
printf("(%d)  %s\n", 4, "bank"(4)  bank
)                                                                              
printf("(%d)  %s\n", 5, "mail"(5)  mail
)                                                                              
printf("=================\n"=================
)                                                                              
printf("choice: ")                                                             
__isoc99_scanf(0x40206d, 0x7fff3cf15388, 0, 0choice: 1
)                                                                              
printf("Enter Master password: ")                                              
__isoc99_scanf(0x402099, 0x7fff3cf15360, 0, 0Enter Master password: testpass123
)                                                                              
strncmp("libc.so.6", "testpass123", 32)                                        
printf("Invalid password!\n"Invalid password!
)                                                                              
+++ exited (status 255) +++
```

And here we see that `strncmp` compares our input with "libc.so.6". This is for C library package, this is why it wasn't suspicious when we ran `strings` earlier.
So, we have our master password and get the flag for "lvlC".

```
➜  lvlB ./epass 
Welcome to EPass Password Manager!
=================
(0)  locker
(1)  lvlC
(2)  phone
(3)  pc
(4)  bank
(5)  mail
=================
choice: 1
Enter Master password: libc.so.6
Password for [lvlC] => d4rk{s1mpl3_strcmp}c0de
```
