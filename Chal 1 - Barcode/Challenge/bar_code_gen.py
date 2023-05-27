from PIL import Image, ImageDraw

with open('creds.txt') as f:
    text_to_encrypt = f.read()

binary = ""
for char in text_to_encrypt:
    binary += (bin(ord(char))[2:]).zfill(8)


HEIGHT: int = len(binary) // 4
PADDING_X: int = len(binary) // 16
PADDING_Y: int = HEIGHT // 4


image = Image.new('RGB', (len(binary) + 2 * PADDING_X,
                          HEIGHT + 2 * PADDING_Y), (255, 255, 255))

draw = ImageDraw.Draw(image)


for i in range(PADDING_X, len(binary) + PADDING_X):
    if binary[i - PADDING_X] == "1":
        draw.line((i, PADDING_Y, i, HEIGHT + PADDING_Y), (0, 0, 0))

image.save("example.png")
