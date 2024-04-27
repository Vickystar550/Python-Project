from PIL import Image, ImageDraw, ImageFont

# create an image
out = Image.new("RGB", (150, 100), (128, 128, 128, 0))

print(out.mode)
print(out.getcolors())

# get a font
fnt = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", 40)
# get a drawing context
d = ImageDraw.Draw(out)

# draw multiline text
d.multiline_text((10, 10), "Hello\nWorld", font=fnt, fill='yellow')

out.show()
out.save('new_image.png')

def count_text_character(text: str):
    if len(text) > 20:
        str1 = text[:21]
        str2 = text[21:]

        print(str1)
        print(str2)

count_text_character('Enter watermark here')