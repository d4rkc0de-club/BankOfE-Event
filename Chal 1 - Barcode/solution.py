from PIL import Image, ImageDraw


image = Image.open("Challenge/3nc0ded.png")
binary = ""

width, height = image.size
bin_length = width * 8 // 9

PADDING_X = bin_length // 16
PADDING_Y = bin_length // 16

for i in range(PADDING_X, image.size[0] - PADDING_X):
    binary += '0' if (image.getpixel((i, PADDING_Y)))[0] == 255 else '1'

chars = [binary[i:i+8] for i in range(0, len(binary), 8)]
text = ""

for char in chars:
    text += chr(int(char, 2))

print(text)
