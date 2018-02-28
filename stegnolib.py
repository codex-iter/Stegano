import cv2
import numpy as np 
import random 

def bitGen(reader):
	for r in reader:
		asc = ord(r)
		i = 0
		while i < 7:
			yield asc & 1
			asc = asc >> 1
			i+=1
	for i in range(7):
		yield 0

	while True:
		yield random.randint(0,1)


def az_lsb_embed(filename,imagename):
	file = open(filename)
	reader = file.read()
	file.close()

	bit = bitGen(reader)

	for i in range(100):
		print(next(bit))


if __name__ == '__main__':
	az_lsb_embed('text.txt','image.jpg')