from PIL import Image

image = Image.open('Assets/1_Gammar.PNG')

# flip / rotate
image_transpose = image.transpose(Image.Transpose.ROTATE_90)

# # rotate
image_rotate = image.rotate(45)

# # crop
image_crop = image.crop((00, 00, 500, 500))

# # resize
image_resize = image.resize((1000, 600))

# combined
combined_image = image.transpose(Image.Transpose.ROTATE_90)\
    .resize((2000, 1500))\
    .rotate(10)

# combined_image.show()
combined_image.show()