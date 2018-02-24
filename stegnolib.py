import cv2
import numpy as np 

def embed(filename,imgname):
	img = cv2.imread(imgname,1)

	shape = img.shape
	print('height : ',shape[0])
	print('width : ',shape[1])
	print('size : ',img.size)

	file = open(filename,'r')
	read = file.read()
	print(read)

	for r in read:
		dt = ord(r)
		


if __name__ == '__main__':
	embed('text.txt','image.jpg')