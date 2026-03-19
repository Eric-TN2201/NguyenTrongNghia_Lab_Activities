from PIL import Image

# open image
image = Image.open('Assets/2_Gammar.PNG')

# show image
image.show()

# print info
print("Size:", image.size)
print("Filename:", image.filename)
print("Format:", image.format)

# rotate 30 degrees
img_rotated = image.rotate(30)

# save new image
img_rotated.save('img_rotated.png', 'PNG')
