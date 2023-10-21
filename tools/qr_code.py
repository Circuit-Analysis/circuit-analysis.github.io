import qrcode

qr = qrcode.QRCode(
    version = 1,
    error_correction=qrcode.ERROR_CORRECT_H,
    box_size=10,
    border=10,
)
qr.add_data('https://circuit-analysis.github.io')
qr.make(fit=True)

img = qr.make_image(fill_color=(254,204,0), back_color=(32,89,153))

img.save("../logo.png")

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


# from matplotlib import font_manager 
# print(font_manager.findSystemFonts(fontpaths=None, fontext='ttf'))

# Open an Image
img = Image.open('../logo.png')
 
# Call draw Method to add 2D graphics in an image
I1 = ImageDraw.Draw(img)
 
myFont = ImageFont.truetype('/System/Library/Fonts/Supplemental/Tahoma Bold.ttf', 55)
mySmallerFont = ImageFont.truetype('/System/Library/Fonts/Supplemental/Tahoma Bold.ttf', 35)

# Add Text to an image
I1.text((48, 16), "Circuit Analysis", fill=(254,204,0), font=myFont)
I1.text((58, 470), "Broderick & Kootsookos", fill=(254,204,0), font=mySmallerFont)
 
# Display edited image
img.show()
 
# Save the edited image
img.save("../logo.png")




