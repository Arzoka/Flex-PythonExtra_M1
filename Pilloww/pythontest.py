from PIL import Image, ImageFont, ImageDraw

BackgroundImage = Image.open("megamind.jpg")
TextType = ImageFont.truetype("impact", 40)
DrawArea = ImageDraw.Draw(BackgroundImage)
Text = "No bitches?"
DrawArea.multiline_text((BackgroundImage.width / 3,60), Text, font=TextType, fill=(0,0,0))

BackgroundImage.show()