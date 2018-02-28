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

	if len(reader)*7 + 7 > size: # if length of file with the delimeter is more than what image can hold return
		print('File size exceeds the range')
		return


	end = 0
	for j in range(height):
		for i in range(width):
			if end == len(reader)*7 + 7: # check where the stream would end
				break
			end += 3
			pix = img[j,i].copy() 
			for k in range(3):  # shorthand to modify BGR in one go
				bit = next(bits) # iterate over each bit from the file 
				if bit == 1:
					pix[k] = pix[k] | bit # make the right most bit by using bitwise or with 
				else:
					pix[k] = pix[k] & 0b1111110  # make the right most bit zero by using bitwise and with 1111110
			img[j,i] = pix
	
	cv2.imwrite('eimage.png',img)

def az_lsb_retv(imagename):
	img = cv2.imread(imagename,-1)

	file = open('output.txt','w')

	height,width = img.shape[:2]

	bin_data = ''
	length = 0
	for j in range(0,height):
		for i in range(0,width):
			pix = img[j,i].copy()
			for k in range(0,3):
				bit_data = pix[k] & 0b0000001
				bin_data = str(bit_data)+bin_data 
				length+=1
				if length % 7 == 0:
					length = 0
					data = chr(int(bin_data,2))
					bin_data = ''
					if data == '\x00':
						file.close()
						return
					else:
						file.write(data)


if __name__ == '__main__':
	az_lsb_embed('text.txt','image.jpg')
	az_lsb_retv('eimage.png')