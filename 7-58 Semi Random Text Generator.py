import string
import random

allLetters = 'abcdefghijklmnopqrstuvwxyz'#string.lowercase
vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxyz'

def getLetter(option='l'):
	letter = ''
	if option == 'l':
		letter = random.choice(allLetters)
	elif option == 'c':
		letter = random.choice(consonants)
	else:
		letter = random.choice(vowels)
	return letter

def generateText(letterOptions, lastLetter=''):
	text = ''
	for x in letterOptions:
		if x in ('c','v','l'):
			text += getLetter(x)
		else:
			lastLetter = x
	text += lastLetter
	return text

def main():
	text = ''
	lastLetter = ''
	letterOptions = ['l','l','l']
	for x in range(len(letterOptions)):
		letterOptions[x] = input("enter 'c' to get consontant 'v' for vowel and 'l' for any letter: ")

	for x in range(7):
		print(generateText(letterOptions))


main()