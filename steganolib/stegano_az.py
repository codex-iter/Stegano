import cv2
import numpy as np 
from steganolib	import bitgen as bg
from PIL import Image

def lsb_embed(fileobj,imagename,outimgae,typef,meta):
	"""Embed the message in the image"""
	# NOTE: cv2 uses BGR instead of RGB 
	if typef == 1:                           # typef = 1 stands for the file to be embeded is a text file
		bits = bg.bitGen_text(fileobj,meta)

	file_len = next(bits)                   # get the length of the file

	img = cv2.imread(imagename,-1)          # open the image

	width,height,size = img.shape[1],img.shape[0],img.size

	if file_len*7 + 7 > size:                      # if length of file with the delimeter is more than what image can hold return
		print('File size exceeds the range')
		return
	end = 0
	for j in range(height):
		for i in range(width):
			pix = img[j,i].copy() 
			for k in range(3):                      # shorthand to modify BGR in one go
				if end == file_len*7 + 7:           # check where the stream would end
					cv2.imwrite(outimgae,img)	    # if stream ends write to the image
					return 							# return from the function
				end += 1
				bit = next(bits)                    # iterate over each bit from the file 
				pix[k] = bg.setBit(pix[k],bit)  
			img[j,i] = pix                          # data is written in reverse order

	
	

def lsb_retv(imagename,typef,start):
	"""Retrieve data from the injested image"""
	img = cv2.imread(imagename,-1)                 # open the image  

	# if typef == 1:							   # type = 1 stands for the file to be embeded is a text file
	# 	file = open(filename,'w')

	height,width = img.shape[:2]                   # grab width and height of the image

	bin_data = ''                                  # gather the binary data of right most bit of each pixel
	length = 0                                     # check if the length is 7 or not 
	main_data = ''
	for j in range(0,height):
		for i in range(0,width):
			pix = img[j,i].copy() 				   # get pixel from location j,i
			for k in range(0,3):  				   # short-hand to scan data from BGR bands
				bit_data = pix[k] & 0b00000001     # use bitwise and with 0000001 as a result only right most bit is preserved others are set to zero
				bin_data = str(bit_data)+bin_data  # concatenating bits in reverse order to get original data
				length+=1				           # increment length after merging bits
				if length == 7: 			       # if length is 7 i.e., we have 7 bits of data 
					length = 0					   # reset length
					data = chr(int(bin_data,2))    # convert bits to character 
					bin_data = '' 				   # reset the bits to empty 
					if data == '\x00':             # if the coverted char is null then delimeter found hence close the file and return
						main_data = main_data[start:]
						return main_data
					else:
						main_data+=data           # else write data to file


def lsb_alpha_embed(fileobj,imagename,outimage,typef,meta):
	"""Method to embed data to apha channel of the image"""
	if len(meta) % 3 != 0:
		meta = meta + (3 - len(meta)%3)*' '
	if typef == 1:                                  # 1 means text file
		bits = bg.bitGen_text(fileobj,meta)            # send the filename to bit generator

	file_len = next(bits)                          # grab the file length 

	img = Image.open(imagename)                    
	img = img.convert("RGBA")					   # converting image to RGBA so it can hold alpha values
	width,height = img.size[0],img.size[1]         # grab the width and height of the image


	if file_len*7 + 7 > width*height :			   # if file length exceeds the range then return
		print('File size exceeds the range')
		return

	end = 0
	meta_em = 0                                   # to check the end of the file
	for j in range(height):                     
		for i in range(width):                    # loops to traverse each pixel 
			r,g,b,a = img.getpixel((i,j)) 		        # grab rgba values 
			if end == file_len*7+7:               # if the end of file is reached save the file and return
				img.save(outimage)
				return
			if meta_em < len(meta) * 7:
				pix = [b,g,r]
				for k in range(3):
					bit = next(bits)			
					pix[k] = bg.setBit(pix[k],bit)
					end+=1
					meta_em+=1
					img.putpixel((i,j),(pix[2],pix[1],pix[0],a))

			else:
				bit = next(bits)
				a = bg.setBit(a,bit)        		  # set alpha value as the bit data
				img.putpixel((i,j),(r,g,b,a))         # put the modified rgba back to the image
				end+=1                                # after each successful put operation increment end



def lsb_alpha_retv(imagename,typef,start):
	"""Retrieve the data from the resultant image of alpha embed""" 
	img = Image.open(imagename)                   # open the image
	width,height = img.size[0],img.size[1]        # grab its width and height

	# if typef == 1:                                 # type = 1 stands that the file was a text file
	# 	file = open(filename,'w')                 # open the output text file as write mode

	bin_data = ''                                 # bin_data to hold the binary data result
	length = 0                                    # used to check the length of binary data
	main_data = ''
	for j in range(0,height):
		for i in range(0,width):                    # traverse through each pixel
			a = img.getpixel((i,j))[3]            # grab the alpha channel only
			bit_data = a & 0b00000001			  # get the right most bit
			bin_data = str(bit_data) + bin_data   # concatenate to bin_data in reverse order
			length+=1                             # increment length

			if length == 7:                       # if length is 7 it means we have an ascii character/symbol/digit
				length = 0                        # reset length 
				data = chr(int(bin_data,2))       # convert the binary data to character
				bin_data = ''                     # reset binary data
				if data == '\x00':                # if the converted data is null it means we have reached end of file
					main_data = main_data[start // 3:]
					return main_data
				else: 
					main_data+=data		      # until the end of file is reached write the data to the file

def water(imagename,outimage,cred):
	img = cv2.imread(imagename,-1)

	width,height = img.shape[1],img.shape[0]

	bits = bg.water_mark(cred)

	for j in range(height):
		for i in range(width):
			pix = img[j,i].copy()
			for k in range(3):
				bit = next(bits)                   
				pix[k] = bg.setBit(pix[k],bit)
			img[j,i] = pix

	cv2.imwrite(outimage,img)


def validate(imagename,cred):
	img = cv2.imread(imagename,-1)

	width,height = img.shape[1],img.shape[0]

	bin_data = ''
	length = 0
	val_str = ''
	for j in range(height):
		for i in range(width):
			pix = img[j,i].copy()
			for k in range(3):
				bit = pix[k] & 0b00000001
				bin_data = str(bit) + bin_data
				length += 1
				if length%7 == 0:
					char =  chr(int(bin_data,2))
					bin_data = ''
					val_str += char

			if cred in val_str:
				return True
	return False




			
def retv(imagename,typef):
	"""Do decide which retrieval algorithm to use"""
	img = cv2.imread(imagename,-1)
	width,height = img.shape[1],img.shape[0]
	meta = ''
	bin_data = ''
	length = 0
	for j in range(height):
		for i in range(width):
			pix = img[j,i].copy() 				  
			for k in range(0,3):  				   
				bit_data = pix[k] & 0b00000001     
				bin_data = str(bit_data)+bin_data  
				length+=1				           
				if length == 7: 			        
					length = 0					   
					data = chr(int(bin_data,2))     
					bin_data = '' 
					if data == ':':
						start = len(meta)

						meta = meta.split('|')
						
						data_dict = {meta[1]:''}

						index = int(meta[1])
						if meta[0] == 'lsb':

							data_dict[index] = lsb_retv(imagename,typef,start+1)
						else:
							data_dict[index] = lsb_alpha_retv(imagename,typef,start+1)
						return data_dict
					meta += data





if __name__ == '__main__':

	lsb_embed('text.txt','image.jpg',1)           # call lsb embed function
	lsb_retv('output.txt','eimage.png',1)		  # call lsb the retrieval function

	lsb_alpha_embed('text.txt','image.jpg',1)     # call lsb alpha embed function


