from steganolib import stegano_az as stg_az
from steganolib import bitgen as bg

imgin1 = '/home/loopaz/Desktop/image.jpg'
imgin2 = '/home/loopaz/Desktop/image2.jpg'
imgout1 = '/home/loopaz/Desktop/i.png'
imgout2 = '/home/loopaz/Desktop/i2.png'
file = open('/home/loopaz/Desktop/text.txt')
reader = file.read()

stg_az.lsb_embed(reader,imgin1,imgout1,1)
stg_az.retv('/home/loopaz/Desktop/out.txt',imgout1,1)

# stg_az.lsb_alpha_embed(reader,imgin2,imgout2,1)
# stg_az.retv('/home/loopaz/Desktop/out2.txt',imgout2,1)