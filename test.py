from steganolib import stegano_az as stg
from steganolib import bitgen as bg

imgin1 = '/home/loopaz/Desktop/image.jpg'
imgin2 = '/home/loopaz/Desktop/image2.jpg'
imgout1 = '/home/loopaz/Desktop/i.png'
imgout2 = '/home/loopaz/Desktop/i2.png'
fileout = '/home/loopaz/Desktop/out2.txt'
filename = '/home/loopaz/Desktop/text.txt'
file = open(filename)
reader = file.read()
reader += '\x00'
# stg_az.lsb_embed(reader,imgin1,imgout1,1)
# stg_az.retv('/home/loopaz/Desktop/out.txt',imgout1,1)

# stg_az.lsb_alpha_embed(reader,imgin2,imgout2,1)
# stg_az.retv('/home/loopaz/Desktop/out2.txt',imgout2,1)

data_base = {}

# meta = 'lsb' + '|' + '1' + ':'
# stg.lsb_embed(reader,imgin1,imgout1,1,meta)
# data_base.update(stg.retv(imgout1,1))

# file = open(fileout,'w')
# file.write(data_base[1])
# file.close()

# meta = 'lsa' + '|' + '2' + ':'
# stg.lsb_alpha_embed(reader,imgin2,imgout2,1,meta)
# data_base.update(stg.retv(imgout2,1))

# file = open(fileout,'w')
# file.write(data_base[2])
# file.close()

# mark = 'azm'
# bits = bg.water_mark(mark)

# binD = ''
# ver_mark = ''

# for k in range(21) :
# 	binD = str(next(bits)) + binD

# for i in range(len(mark)):
# 	raw = binD[i*7:(i+1)*7].reverse()
# 	raw = chr(int(raw,2))
# 	if raw.isalpha():
# 		ver_mark += raw
# 		if mark in ver_mark:
# 			break
# print(ver_mark,mark)

water_in = '/home/loopaz/Desktop/wat.jpg'
water_out = '/home/loopaz/Desktop/wat_out.png'
mark = 'azm'
stg.water(water_in,water_out,mark)

if stg.validate(water_out,mark) is True:
	print('water mark found')
else:
	print('water mark not found')