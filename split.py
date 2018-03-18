from steganolib import stegano_az as steg_az 
from steganolib import bitgen as bg

imageloc = ['/home/loopaz/Desktop/image.jpg','/home/loopaz/Desktop/image2.jpg','/home/loopaz/Desktop/image3.jpeg']
fileloc = '/home/loopaz/Desktop/text.txt'
outloc = '/home/loopaz/Desktop/out.txt'
outimloc = ['/home/loopaz/Desktop/i1.png','/home/loopaz/Desktop/i2.png','/home/loopaz/Desktop/i3.png']

file = open(fileloc)
reader = file.read()
file.close()

chunk_size = len(reader)//len(imageloc)

print(chunk_size,'\n\n\n')

db = bg.chunk(reader,chunk_size)

for df in db:
	print(df)
	print('\n'*2)

