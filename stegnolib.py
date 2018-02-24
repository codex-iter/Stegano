import cv2
import numpy as np 

def embed(filename,imgname):
	img = cv2.imread(imgname,1)

	shape = img.shape
	# print('height : ',shape[0])
	# print('width : ',shape[1])
	# print('size : ',img.size)

	file = open(filename,'r')
	read = file.read()
	file.close()

	read = list(read)

	j = 0
	for i in range(0,len(read)):
		if(i % shape[1] == 0):
			j+=1
		pixel = img[j,i]
		img[j,i] = [ord(read[i]),pixel[1],pixel[2]]
	
	for k in range(1,4):
		if((k+i) % shape[1] == 0):
			j+=1
		pixel = img[j,k+i]
		img[j,i] = [ord('/'),pixel[1],pixel[2]]

	cv2.imwrite('eimage.jpg',img)
	


if __name__ == '__main__':
	embed('text.txt','image.jpg')