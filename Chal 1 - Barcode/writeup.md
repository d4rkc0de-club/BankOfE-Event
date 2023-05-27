# Challenge 1 - Bar Code Reversing

In this challenge, we were given a barcode image and asked to reverse it. The barcode image is shown below:

![barcode](https://github.com/d4rkc0de-club/BankOfE/blob/main/Chal%201%20-%20Barcode/Challenge/3nc0d3d.png?raw=true)

# Solution
## Understand the generation
We first try to understand what is happening in `bar_code_generator.py`
    
```python
with open('creds.txt') as f:
    text_to_encrypt = f.read()

binary = ""
for char in text_to_encrypt:
    binary += (bin(ord(char))[2:]).zfill(8)
```

This tells us that we are taking `text_to_encrypt`, converting each character into it's 8 bit form, and concatenating them together to form a long strig

```python
HEIGHT: int = len(binary) // 4
PADDING_X: int = len(binary) // 16
PADDING_Y: int = HEIGHT // 4
```
There are also some constants here which are less important now, but their will be used later when decrypting.
```python
image = Image.new('RGB', (len(binary) + 2 * PADDING_X,
                  HEIGHT + 2 * PADDING_Y), (255, 255, 255))

draw = ImageDraw.Draw(image)
```
Here we make an empty white image with some padding involved, and it's atleast as long as the length of the binary string we made earlier
```python
for i in range(PADDING_X, len(binary) + PADDING_X):
    if binary[i-PADDING_X] == "1":
        draw.line((i, PADDING_Y, i, HEIGHT + PADDING_Y), (0, 0, 0))

image.save("example.png")
```

Now we are drawing a black line (indictated by `(0,0,0)`) whenever we see a `1` in the binary string. This is the barcode image we see above.

Now that we understand how the image is generated, we can start to reverse it.
## Beginning the decryption

Now we attempt to reverse it. First, we try to get back the original binary string by reading the barcode bits and converting them to `1` and `0` based on their color(0 for white, 1 for black), but we also need to calculate the padding of the image, so we do that first.

```python
from PIL import Image, ImageDraw

image = Image.open("flag.png")
binary = ""

width, height = image.size
bin_length = width * 8 // 9

PADDING_X = bin_length // 16
PADDING_Y = bin_length // 16
```

the exact calculations for `bin_length` and `PADDING_X` and `PADDING_Y` is left as an exercise for the user. Now we convert the image to binary

```python
image = Image.open("flag.png")
binary = ""

for i in range(20, image.size[0] - 20):
    binary += '0' if (image.getpixel((i, 20)))[0] == 255 else '1'
```

We have the binary string. Now we just need to convert it back to the original text. We do this by taking every 8 bits and converting them back to their original character.

```python
chars = [binary[i:i+8] for i in range(0, len(binary), 8)]
text = ""

for char in chars:
    text += chr(int(char, 2))

print(text)
```

And so, we get the text as  

```
uname: lvlA
passwd: d4rk{b4r_c0d3_c1ph3r}c0de 
```
