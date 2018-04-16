import os, re
from xml.etree import ElementTree as ET

def look_up(word):
	# print(word.capitalize())
	source = 'xml_files'
	file_template = 'gcide_%s.xml'

	f = open(os.path.join(source,file_template)%word[0].lower(), 'r')
	data = f.read()
	data = data.split('</p>')

	for line in data:		
		if (re.findall('<ent>{}</ent>'.format(word.capitalize()), line)) != []:
			if (re.findall('<pos>.*</pos>', line)) != []:
				x = re.search('<pos>.*</pos>', line).group(0)
				x = re.search('<pos>.*</pos>', x).group(0).split('</pos>')[0]
				# print(x+'</pos>')
				return ET.fromstring(x+'</pos>').text
	if word.endswith('s'):
		word = word[:-1]
		for line in data:		
			if (re.findall('<ent>{}</ent>'.format(word.capitalize()), line)) != []:
				if (re.findall('<pos>.*</pos>', line)) != []:
					x = re.search('<pos>.*</pos>', line).group(0)
					x = re.search('<pos>.*</pos>', x).group(0).split('</pos>')[0]
					# print(x+'</pos>')
					return ET.fromstring(x.replace('&amp;','')+'</pos>').text
	else:
		for line in data:		
			if (re.findall('<ent>{}</ent>'.format(word.lower()), line)) != []:
				if (re.findall('<pos>.*</pos>', line)) != []:
					x = re.search('<pos>.*</pos>', line).group(0)
					x = re.search('<pos>.*</pos>', x).group(0).split('</pos>')[0]
					# print(x+'</pos>')
					return ET.fromstring(x.replace('&amp;','')+'</pos>').text
	my_dicttt = {'PRONOUN':'pron.',
			'NOUN':'n.',
			'ADJECTIVE': 'a.',
			'CONJUNCTION': 'conj.',
			'VERB': 'v. i.',
			'ADVERB': 'adv.',
			'PREPOSITION': 'prep.'

	}
	user_choice = input('"{}" was not found in dictionary, please provide a tag [e.g. NOUN, ADJECTIVE, etc.]: '.format(word.upper()))
	for i in my_dicttt.keys():
		if i == user_choice.upper():

			return my_dicttt[i]

def part_of_speech(abr):
	# print(abr)
	abr = abr.split()[0]
	# print(abr)
	f = open('xml_files/gcide_abbreviations.xml', 'r')
	
	data = f.readlines()
	for line in data:
		if (re.findall('<ab.entry><ab>*{}*</ab> '.format(abr), line)) != []:
			# print(re.findall('<ab.entry><ab>*{}*</ab> '.format(abr), line))
			if (re.findall('<ab.full.*</ab.full>', line)) != []:
				x = re.search('<ab.full.*</ab.full>', line).group(0)
				# print((ET.fromstring(x).text).upper())
				return (ET.fromstring(x).text).upper()


def main():
	part_of_speech(look_up('plays'))

if __name__ == '__main__':
	main()