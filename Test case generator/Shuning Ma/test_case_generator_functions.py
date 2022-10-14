
# this is a list of functions to be used

def separate_words_in_name_2(name):
	last_name = name[:name.find(',')]
	first_name = name[name.find(', ')+2:]
	
	separated_words = [first_name, last_name]
	
	return separated_words

def separate_words_in_name_3(name):
	first_name = name[name.find(', ')+2:name.find(' ',name.find(', ')+2)]
	middle_name = name[name.find(' ',name.find(', ')+2)+1:]
	last_name = name[:name.find(',')]
    
	separated_words = [first_name, middle_name, last_name]
	
	return separated_words

def alphabet():
	alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M',
							'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
							
	return alphabet
	
def rand_letter():
	import random
	alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M',
							'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	rand_letter = alphabet[random.randrange(1,26)]
	
	return rand_letter
	
def similar_letter(letter):
	import random
	similar_letter_dict = {
		'M' : 'N',
		'K' : ['C','G','Q'],
		'J' : ['G','D'],
		'F' : ['P']	
	}
	new_letter = similar_letter_dict[letter][random.randrange(0,len(similar_letter_dict[letter]))]
	
	return new_letter
	
def vowels():
	vowels = ['A','E','I','O','U']
	
	return vowels
	
def switch_vowel(letter):
	import random
	vowels = ['A','E','I','O','U']
	new_letter = vowels[random.randrange(0,5)]
	
	finished=False
	while not finished:
		new_letter = vowels[random.randrange(0,5)]
		if new_letter != letter:
			finished = True
			
	return new_letter
	
def number_to_word():
	numbers_to_words_dict = {
		'1' : 'ONE', '2' : 'TWO', '3' : 'THREE', '4' : 'FOUR', 
		'5' : 'FIVE', '6' : 'SIX', '7' : 'SEVEN', '8' : 'EIGHT',
		'9' : 'NINE', '10' : 'TEN', '11' : 'ELEVEN', '12' : 'TWELVE',
		'13' : 'THIRTEEN', '14' : 'FOURTEEN', '15' : 'FIFTEEN',
		'16' : 'SIXTEEN', '17' : 'SEVENTEEN', '18' : 'EIGHTEEN', 
		'19' : 'NINETEEN', '20' : 'TWENTY'
	}

	return numbers_to_words_dict
	
def punctuation():
	punctuation = [',', '.', ';', ':', '\'', '"', '!']
	
	return punctuation
	
def special_characters():
	special_characters = ['@','#','$','%','^', '&','*','(',')','()']
	
	return special_characters

def phonetic(x):
	import numpy as np
	similar_phonetic_dict = [['A', 'E', 'H', 'I', 'O', 'U', 'W', 'Y'],
	['B', 'P'],
	['C', 'G', 'J', 'K', 'Q'],
	['D', 'T'],
	['M', 'N'],
	['F', 'V'],
	['S', 'X']]

	for i in range(len(similar_phonetic_dict)):
		if x in similar_phonetic_dict[i]:
			similar_phonetic_dict[i].remove(x)
			return np.random.choice(similar_phonetic_dict[i])
		else:
			pass
	
	return x

def num_of_phonetic(word):
	cnt = 0
	for letter in word:
		new_letter = phonetic(letter)
		if new_letter != letter:
			cnt += 1
	
	return cnt

def num_of_alphabet(word):
	cnt = 0
	for letter in word:
		if letter in alphabet():
			cnt += 1
	
	return cnt