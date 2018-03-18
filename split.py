from steganolib import stegano_az as steg_az 
from steganolib import bitgen as bg

imageloc = ['/home/loopaz/Desktop/image.jpg','/home/loopaz/Desktop/image2.jpg'] #,'/home/loopaz/Desktop/image3.jpeg']
fileloc = '/home/loopaz/Desktop/text.txt'
outloc = '/home/loopaz/Desktop/out.txt'
outimloc = ['/home/loopaz/Desktop/i1.png','/home/loopaz/Desktop/i2.png'] # ,'/home/loopaz/Desktop/i3.png']

file = open(fileloc)
reader = file.read()
file.close()

print(len(reader))
print(len(imageloc))

chunk_size = len(reader) // len(imageloc) + 1

print(chunk_size,'\n\n\n')

db = bg.chunk(reader,chunk_size)

print(len(db))
print(db)


# for i in range(len(db)):
# 	steg_az.lsb_embed(db[i],imageloc[i],outimloc[i],1)
# 	print(db[i],imageloc[i],outimloc[i])
# 	print('successfully embeded')

# for i in range(len(outimloc)):
# 	steg_az.lsb_retv(outloc,outimloc[i],1)
# 	print('retrieved')

steg_az.lsb_retv(outloc,'/home/loopaz/Desktop/i2.png',1)