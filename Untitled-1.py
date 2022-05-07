# import stuff up here

import random
import string

# take user input, e.g. num of chars



passLen = input('Hi there, welcome to my password generator. Please input your desired password length: ')



# def functions for different user input lengths



def makePassword(length):
	avChars = string.digits + string.ascii_letters + string.digits + string.punctuation
	password = []
	for i in list(range(length)):
		password.append(random.choice(avChars))
	#return print(avChars)
	return ''.join(password)	



def passwordRelease(PL):
	print('Your password with {passwordlength} characters is:\n{password})'.format(passwordlength = PL, password = makePassword(int(PL))))




# print out generated passwords

passwordRelease(passLen)
newPass()

