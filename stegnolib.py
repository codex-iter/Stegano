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



def az_lsb_embed(filename,imagename):
	"""Embed the message in the image"""
	# NOTE: cv2 uses BGR instead of RGB 

	file = open(filename) 
	reader = file.read()
	file.close()

	bits = bitGen(reader)

	img = cv2.imread(imagename,-1)

	width,height,size = img.shape[1],img.shape[0],img.size

	if len(reader)*7 + 7 > size:
		print('File size exceeds the range')
		return


	end = 0
	for j in range(height):
		for i in range(width):
			if end == len(reader)*7 + 7:
				break
			end += 3
			print(i,j)
			pix = img[j,i].copy()
			for k in range(3):
				bit = next(bits)
				if bit == 1:
					pix[k] = pix[k] | bit
				else:
					pix[k] = pix[k] & 0b1111110 
			img[j,i] = pix

	
	cv2.imwrite('eimage.png',img)


if __name__ == '__main__':
	az_lsb_embed('text.txt','image.jpg')