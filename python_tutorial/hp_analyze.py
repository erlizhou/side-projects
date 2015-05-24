import string
import operator
#http://www.glozman.com/textpages.html

hp_4 = open("hp_4.txt", "r")
oxford = open("words.txt", "r")
stop_words = set(["i", "you", "she", "but", "you", "it", "they","the", "and", "to", "of", "a", "he", "was", "his", "said", "in"])
# Your code here
dictionary = set()
for word in oxford:
	word = word.strip()
	dictionary.add(word)

wordcount = {}
for line in hp_4:
	if line != '\n':
		line = line.strip()
		split_line = line.split()
		split_line = filter(None, split_line)
		split_line = [x for x in split_line if x[0].isupper()]
		for word in split_line:
			newword = ''
			for ch in word:
				if ch.isalpha():
					newword += ch
			newword = newword[0].upper() + newword[1:].lower()
			if newword != '' and newword != 'Mr' and newword != 'Mrs' and newword.lower() not in stop_words and newword in dictionary:
				if newword in wordcount:
					wordcount[newword] += 1
				else:
					wordcount[newword] = 1

sorted_wordcount = sorted(wordcount.items(), key = operator.itemgetter(1), reverse = True)[:10]
for key, value in sorted_wordcount:
	print key, value

hp_4.close()
oxford.close()
