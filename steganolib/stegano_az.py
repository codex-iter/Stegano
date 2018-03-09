import cv2
import numpy as np 
from steganolib	import bitgen as bg
from PIL import Image

def lsb_embed(filename,imagename,mode):
	"""Embed the message in the image"""
	# NOTE: cv2 uses BGR instead of RGB 

	if mode == 1:
		bits = bg.bitGen_text(filename)

	file_len = next(bits)

	img = cv2.imread(imagename,-1)

	width,height,size = img.shape[1],img.shape[0],img.size

	if file_len*7 + 7 > size: # if length of file with the delimeter is more than what image can hold return
		print('File size exceeds the range')
		return
	end = 0
	for j in range(height):
		for i in range(width):
			pix = img[j,i].copy() 
			for k in range(3):                      # shorthand to modify BGR in one go
				if end == file_len*7 + 7:           # check where the stream would end
					cv2.imwrite('eimage.png',img)	# if stream ends write to the image
					return 							# return from the function
				end += 1
				bit = next(bits)                    # iterate over each bit from the file 
				pix[k] = bg.setBit(pix[k],bit)  
			img[j,i] = pix                          # data is written in reverse order

	
	

def lsb_retv(filename,imagename,mode):
	"""Retrieve data from the injested image"""
	img = cv2.imread(imagename,-1)

	if mode == 1:
		file = open(filename,'w')

	height,width = img.shape[:2]

	bin_data = ''                                  # gather the binary data of right most bit of each pixel
	length = 0                                     # check if the length is 7 or not 

	for j in range(0,height):
		for i in range(0,width):
			pix = img[j,i].copy() 				   # get pixel from location j,i
			for k in range(0,3):  				   # short-hand to scan data from BGR bands
				bit_data = pix[k] & 0b00000001     # use bitwise and with 0000001 as a result only right most bit is preserved others are set to zero
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


def lsb_alpha_embed(filename,imagename,mode):

	if mode == 1:
		bits = bg.bitGen_text(filename)

	file_len = next(bits)

	img = Image.open(imagename)
	img = img.convert("RGBA")
	width,height = img.size[0],img.size[1]


	if file_len*7 + 7 > width*height :
		print('File size exceeds the range')
		return

	end = 0
	for j in range(height):
		for i in range(width):
			r,g,b,a = img.getpixel((i,j))
			if end == file_len*7+7:
				img.save('eimagealpha.png')
				return
			bit = next(bits)
			a = bg.setBit(a,bit)
			img.putpixel((i,j),(r,g,b,a))
			end+=1



def lsb_alpha_retv(filename,imagename,mode):

	img = Image.open(imagename)
	width,height = img.size[0],img.size[1]

	if mode == 1:
		file = open(filename,'w')

	bin_data = ''
	length = 0

	for j in range(height):
		for i in range(width):
			a = img.getpixel((i,j))[3]
			bit_data = a & 0b00000001
			bin_data = str(bit_data) + bin_data
			length+=1

			if length == 7:
				length = 0
				data = chr(int(bin_data,2))
				bin_data = ''
				if data == '\x00':
					file.close()
					return
				else:
					print(data)
					file.write(data)

if __name__ == '__main__':

	lsb_embed('text.txt','image.jpg',1)           # call lsb embed function
	lsb_retv('output.txt','eimage.png',1)		  # call lsb the retrieval function

	lsb_alpha_embed('text.txt','image.jpg',1)     # call lsb alpha embed function


