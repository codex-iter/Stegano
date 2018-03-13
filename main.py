from steganolib import stegano_az as stg_az


def algo_menu(choice,algo_choice,typef):
	if choice is 1:
		imageIn_loc = input('Enter the source image location : ')
		imageIn_name = input('Enter the image file name WITH extention : ')
		imageOut_loc = input('Enter the output image location : ')
		imageOut_name = input('Enter the image file name WITHOUT extention : ')	
		fileIn_loc = input('Enter the location of file : ')
		fileIn_name = input('Enter the name of the file WITH extention : ')

		imageIn = imageIn_loc + '\\' + imageIn_name

		imageOut = imageOut_loc + '\\' + imageOut_name + '.png'

		fileIn = fileIn_loc + '\\' + fileIn_name

		if algo_choice is 1:
			stg_az.lsb_embed(fileIn,imageIn,imageOut,typef)
		elif algo_choice is 2:
			stg_az.lsb_alpha_embed(fileIn,imageIn,imageOut,typef)

		print('Successfully embeded')

	elif choice is 2:
		imageOut_loc = input('Enter the output image location : ')
		imageOut_name = input('Enter the image file name WITHOUT extention : ')

		fileOut_loc = input('Enter the location of file : ')
		fileOut_name = input('Enter the name of the file WITH extention : ')

		imageOut = imageOut_loc + '\\' + imageOut_name + '.png'

		fileOut = fileOut_loc + '\\' + fileOut_name

		if algo_choice is 1:
			stg_az.lsb_retv(fileOut,imageOut,typef)
		elif algo_choice is 2:
			stg_az.lsb_alpha_retv(fileOut,imageOut,typef)

		print('Successfully retrieved')


def menu():
	print('Choose a method or press 0 to exit\n1.Embed\n2.Retrieve')
	choice = int(input('Enter your choice : '))
	print('\n')

	if choice is 0:
		exit()
	elif choice in [1,2]:

		print('Choose a file type\n1.Text')
		isvalid = False
		while not isvalid:
			typef = int(input('Enter your choice : '))
			if typef in [1]:
				isvalid = True
			else:
				print('Invalid choice enter again')
		print('\n')
	
		print('Choose an algorithm\n1.Least Significant Bit(LSB)\n2.Least Significant Bit alpha only(LSB_alpha)')
		print('Note: To retrieve the data select the algorithm that was used to embed')
		isvalid = False
		while not isvalid:
			algo_choice = int(input('Enter your choice : '))

			if algo_choice in [1,2]:
				isvalid = True
				algo_menu(choice,algo_choice,typef)
			else:
				print('Invalid choice enter again')
	else:
		print('Invalid option')


print("Image Stegagraphy Lab")
print('\n'*2)

while True:
	menu()
	print('\n'*2)


