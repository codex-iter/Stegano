
def bitGen_text(filename):
	""" Return the character bit by bit"""

	file = open(filename,'r')
	reader = file.read()
	file.close()

	yield len(reader)   # first yield the file name 

	for r in reader:
		asc = ord(r)
		i = 0
		while i < 7:       # 7 bits in each character
			yield asc & 1  # returns the right most bit of the character by doing bitwise and with 1
			asc = asc >> 1 # once the bit has been returned it is shifted to right and removed
			i+=1           # increment the counter after each yield
	for i in range(7):     # using null as delemeter to mark the end of the file
		yield 0

def setBit(pix_val,bit):
	if bit == 1:
		return pix_val | bit        # make the right most bit by using bitwise or with 
	else:
		return pix_val & 0b11111110 # make the right most bit zero by using bitwise and with 11111110 for 8 bit