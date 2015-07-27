class List(object):
# a List holds one or more sets of words and maps each set to a string
	def __init__(self):
		# create an empty dictionary
		self.map = {}

	def insert(self, words, string):
		# inserts a set of words and maps it to a string
		for word in words:
			if word not in self.map:
				self.map[word] = string

	def member(self, word, string):
		# returns True if word is mapped to string, else False
		return self.map.get(word) == string

	def remove(self, word):
		# removes the word from the dicitionary if it exists, else ignores
		try:
			del self.map[word]
		except:
			pass

	def getMap(self):
		# Returns a dictionary representation of List
		return self.map

class taggedSentence(object):
	''' a Tagged Sentence able to return the original sentence, the words that were tagged, the 
	words not tagged and the sentence with the words replaced with strings from the List Object'''
	def __init__(self, string, dictionary):
		# initialization of the 4 strings and the dictionary from the List Object
		self.string = string
		self.tagged = ''
		self.untagged = ''
		self.classTagged = ''
		self.dictionary = dictionary

	def buildTag(self):
		# build 4 strings from the dictionary and input
		split = self.string.split()
		for s in split:
			lower = s.lower()
			if lower in self.dictionary:
				self.tagged += lower + ' '
				self.classTagged += self.dictionary[lower] + ' '
			else:
				self.untagged += lower + ' '
				self.classTagged += lower + ' '

	def getOriginal(self):
		return self.string

	def getTagged(self):
		# return tagged words
		return self.tagged[:-1]

	def getUntagged(self):
		# return untagged words
		return self.untagged[:-1]

	def getClassTagged(self):
		# return sentence with words replaced with strings
		return self.classTagged[:-1]


l = List()
print l.getMap()
l.insert({'jack', 'jill'}, 'NAME')
l.insert({'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'}, 'NUM')
l.insert({'Erli'}, 'NAME')
print l.getMap()
print l.member('one', 'NAME')
print l.member('Erli', 'NAME')
l.remove('Mike')
l.remove('Erli')
print l.member('Erli', 'NAME')

t = taggedSentence('I\'m Jack and I\'m three years old', l.getMap())
t.buildTag()
print t.getOriginal()
print t.getUntagged()
print t.getTagged()
print t.getClassTagged()