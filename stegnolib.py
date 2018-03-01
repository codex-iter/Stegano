import cv2
import numpy as np 

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
			pix = img[j,i].copy() 
			for k in range(3):                      # shorthand to modify BGR in one go
				if end == len(reader)*7 + 7:        # check where the stream would end
					cv2.imwrite('eimage.png',img)	# if stream ends write to the image
					return 							# return from the function
				end += 1
				bit = next(bits)                    # iterate over each bit from the file 
				if bit == 1:
					pix[k] = pix[k] | bit           # make the right most bit by using bitwise or with 
				else:
					pix[k] = pix[k] & 0b1111110     # make the right most bit zero by using bitwise and with 1111110
			img[j,i] = pix                          # data is written in reverse order
	
	

def az_lsb_retv(imagename):
	"""Retrieve data from the injested image"""
	img = cv2.imread(imagename,-1)

	file = open('output.txt','w')

	height,width = img.shape[:2]

	bin_data = ''                                  # gather the binary data of right most bit of each pixel
	length = 0                                     # check if the length is 7 or not 

	for j in range(0,height):
		for i in range(0,width):
			pix = img[j,i].copy() 				   # get pixel from location j,i
			for k in range(0,3):  				   # short-hand to scan data from BGR bands
				bit_data = pix[k] & 0b0000001      # use bitwise and with 0000001 as a result only right most bit is preserved others are set to zero
				bin_data = str(bit_data)+bin_data  # concatenating bits in reverse order to get original data
				length+=1				           # increment length after merging bits
				if length % 7 == 0: 			   # if length is 7 i.e., we have 7 bits of data 
					length = 0					   # reset length
					data = chr(int(bin_data,2))    # convert bits to character 
					bin_data = '' 				   # reset the bits to empty 
					if data == '\x00':             # if the coverted char is null then delimeter found hence close the file and return
						file.close()
						return
					else:
						file.write(data)           # else write data to file


if __name__ == '__main__':

	az_lsb_embed('text.txt','image.jpg')           # call embed function
	az_lsb_retv('eimage.png')					   # call the retrieval function

