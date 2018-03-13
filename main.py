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


def algo_menu(choice,algo_choice):
	if choice is 1:
		imageIn_loc = input('Enter the source image location : ')
		imageIn_name = input('Enter the image file name WITH extention : ')
		imageOut_loc = input('Enter the output image location : ')
		imageOut_name = input('Enter the image file name WITH extention : ')	
		textIn_loc = input('Enter the location of file : ')
		textIn_name = input('Enter the name of the file WITHOUT extention : ')

		imageIn = imageIn_loc + imageIn_name
		imageIn = '%r' % imageIn

		imageOut = imageOut_loc + imageOut_name
		imageOut = '%r' % imageOut

		textIn = textIn_loc + textIn_name
		textIn = '%r' % textIn

		print(imageIn,imageOut,textIn)



def menu():
	print("Choose a method or press 0 to exit\n1.Embed\n2.Retrieve")
	choice = int(input("Enter your choice : "))
	print('')
	if choice is 0:
		exit()
	elif choice in [1,2]:
		print('Choose an algorithm\n1.Least Significant Bit(LSB)\n2.Least Significant Bit alpha only(LSB_alpha)')
		print('Note: To retrieve the data select the algorithm that was used to embed')
		isvalid = False
		while not isvalid:
			algo_choice = int(input('Enter your choice : '))

			if algo_choice in [1,2]:
				isvalid = True
				algo_menu(choice,algo_choice)
			else:
				print('Invalid choice enter again')
	else:
		print('Invalid option')


print("Image Stegagraphy Lab")
print('\n'*2)

while True:
	menu()
	print('\n'*2)


