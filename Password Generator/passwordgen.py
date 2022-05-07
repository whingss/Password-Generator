# import stuff up here

import random
import string

# take user input, e.g. num of chars

userPassLen = input('Hi there, welcome to my password generator. Please input your desired password length: ')

# def functions for different user input lengths



def makePassword(length):
	avChars = string.digits + string.ascii_letters + string.digits + string.punctuation
	password = []
	for num in list(range(length)):
		password.append(random.choice(avChars))
	#return print(avChars)
	return ''.join(password)	



def passwordRelease(PL):
	print('Your password with {passwordlength} characters is:\n{password})'.format(passwordlength = PL, password = makePassword(int(PL))))



def newPass():
	userBool = input('Would you like to generate another password? (Yes/No): ')
	if userBool == 'Yes' or userBool == 'yes' or userBool == 'y' or userBool == 'Y':
		newPasswordLength = input('Please input your desired new password length: ')
		passwordRelease(newPasswordLength)
		newPass()


	elif userBool == 'No' or userBool == 'no' or userBool == 'n' or userBool == 'N':
		print('Have a nice day!')

	else:
		print('You did not answer with yes or no. Please do so:')
		newPass()



# print out generated passwords

passwordRelease(userPassLen)
newPass()

