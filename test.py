from steganolib import stegano_az as stg_az
from steganolib import bitgen as bg

imgin = '/home/loopaz/Desktop/image.jpg'
imgout1 = '/home/loopaz/Desktop/i.png'
imgout2 = '/home/loopaz/Desktop/i2.png'
file = open('/home/loopaz/Desktop/text.txt')
reader = file.read()

stg_az.lsb_embed(reader,imgin,imgout1,1)
stg_az.retv(imgout1)

