import cv2
import numpy as np 
import random 

def bitGen(reader):
	""" Return the character bit by bit"""
	for r in reader:
		asc = ord(r)
		i = 0
		while i < 7: # 7 bits in each character
			yield asc & 1 # returns the right most bit of the character by doing bitwise and with 1
			asc = asc >> 1 # once the bit has been returned it is shifted to right and removed
			i+=1           # increment the counter after each yield
	for i in range(7):     # using null as delemeter to mark the end of the file
		yield 0

	while True:
		yield random.randint(0,1) # return random 0s and 1s to populate the image


def az_lsb_embed(filename,imagename):
	file = open(filename)
	reader = file.read()
	file.close()

	bit = bitGen(reader)

	for i in range(100):
		print(next(bit))


if __name__ == '__main__':
	az_lsb_embed('text.txt','image.jpg')