from steganolib import stegano_az as stg_az


# textIn=r"C:\Users\HP\Desktop\test\text.txt"
# textOut=r"C:\Users\HP\Desktop\test2\output.txt"

# imageIn=r"C:\Users\HP\Desktop\test\image.jpg"
# imageOut=r"C:\Users\HP\Desktop\test2\eimage.png"

# stg_az.lsb_embed(textIn,imageIn,imageOut,1)
# stg_az.lsb_retv(textOut,imageOut,1)

# textOut=r"C:\Users\HP\Desktop\test2\outalpha.txt"
# imageOut=r"C:\Users\HP\Desktop\test2\eimagealpha.png"

# stg_az.lsb_alpha_embed(textIn,imageIn,imageOut,1)
# stg_az.lsb_alpha_retv(textOut,imageOut,1)


def algo_menu(choice):
	pass


def menu():
	print("Choose a method or press 0 to exit\n1.Least Significant Bit(LSB)\n2.Least Significant Bit alpha only(LSB_alpha)")
	choice = int(input("Enter your choice : "))
	print('')
	if choice is 0:
		exit()
	elif choice in [1,2]:
		algo_menu(choice)
	else:
		print('Invalid option')


print("Image Stegagraphy Lab")
print('\n'*2)

while True:
	menu()
	print('\n'*2)


