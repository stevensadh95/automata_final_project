from dictionary import part_of_speech, look_up 


def word_type(word):
	res = part_of_speech(look_up(word))
	
	if res != None:
		return res

	return 'Not Found'


def main():
	print(word_type('journey'))


if __name__ == '__main__':
	main()