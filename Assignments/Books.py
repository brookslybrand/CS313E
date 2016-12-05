#  File: Books.py

#  Description: Compare the vocabularies of two different authors' works

#  Student Name: Charles Lybrand

#  Student UT EID: cbl652

#  Course Name: CS 303E

#  Unique Number: 51200

#  Date Created: 11/20/2016

#  Date Last Modified: 12/02/2016

# Create word dictionary from the comprehensive word list

word_dict = {}
def create_word_dict ():
  '''
  Populates the global word dictionary with a text file of English words
  '''
  # open the words.txt file
  words = open("words.txt", "r")

  # read file and populate in word_dict
  for word in words:
  	word = word.strip()
  	word_dict[word] = 1

  #close the file
  words.close()

# Removes punctuation marks from a string
def parseString (line):
  '''
  removes punctuations, except for certain apostrophes
  '''

  new_line = ""
  # go throug the line and replace all punctuation with " ", except for apostrophes
  i = 0
  while(i < len(line)):
  	# handle cases for apostrophes
  	if(line[i] == "\'"):
  	  # if at the end of the line, don't add the apostrophe
  	  if(i == (len(line) - 1) ):
  	  	i += 1
  	  elif(line[i+1] == "s" or line[i+1] == " "):
  	  	# if apostrophe is at the end of the word, or followed by an 's'
  	  	# don't add the apostrophe (and 's')
  	  	new_line = new_line + " "
  	  	i += 2
  	  else:
  	  	new_line = new_line + line[i]
  	# if value is numeric, keep it
  	elif(line[i].isalpha() or line[i].isspace()):
  	  new_line = new_line + line[i]
    # otherwise replace with space
  	else:
  	  new_line = new_line + " "

  	i += 1

  return new_line 

# Returns a dictionary of words and their frequencies
def getWordFreq (file):
  '''
  Calculate the word frequency for a single file (removing proper nouns and non-words)
  '''
  # open the file
  in_file = open(file, "r")

  file_word_dict = {}

  # read file line by line
  for line in in_file:
  	# strip the end of line character
  	line = line.strip()
  	# parse the string
  	line = parseString(line)

  	# get all of the words
  	words = line.split()

  	# count the appearances of every word
  	for word in words:
  	  if(word in file_word_dict):
  	  	file_word_dict[word] += 1
  	  else:
  	  	file_word_dict[word] = 1

  # close the file
  in_file.close()

  # get all the words that start with a capital letter
  capital_words = set()
  words = file_word_dict.keys()
  for word in words:
  	if(word[0].isupper()):
  	  capital_words.add(word)

  # go through and find if word exists already, or is a words, the add to file_word_dict
  for word in capital_words:
  	# if lowercase version exits, increase count
    if (word.lower() in file_word_dict):
      file_word_dict[word.lower()] += file_word_dict[word]
    else:
      # if it is a word, create an entry
      if(word.lower() in word_dict):
      	file_word_dict[word.lower()] = file_word_dict[word]
  
  # remove the capital words
  for word in capital_words:
  	del file_word_dict[word]

  return file_word_dict
  
# Compares the distinct words in two dictionaries
def wordComparison (author1, freq1, author2, freq2):
  '''
  Run some simple analysis on the two authors then compare between the two of them
  '''
  
  # stats on author 1
  author1_uniq = set(freq1.keys())
  author1_uniq_num = len(author1_uniq)
  author1_total_words = sum(freq1.values())
  author1_perc = (author1_uniq_num/author1_total_words)*100
  print(author1)
  print("Total distinct words =", author1_uniq_num)
  print("Total words (including duplicates) =", author1_total_words)
  print("Ratio (% of total distinct words to total words) =", author1_perc)

  print()

  # stats on author 2
  author2_uniq = set(freq2.keys())
  author2_uniq_num = len(author2_uniq)
  author2_total_words = sum(freq2.values())
  author2_perc = (author2_uniq_num/author2_total_words)*100
  print(author2)
  print("Total distinct words =", author2_uniq_num)
  print("Total words (including duplicates) =", author2_total_words)
  print("Ratio (% of total distinct words to total words) =", author2_perc)

  print()

  # author comparisons
  # unique word differences
  author12_dif = author1_uniq - author2_uniq
  author21_dif = author2_uniq - author1_uniq

  # get the frequency for words unique to each author
  author1_dif_total = 0
  for word in author12_dif:
    author1_dif_total += freq1[word]
  author1_dif_freq = (author1_dif_total/author1_total_words)*100
  author2_dif_total = 0
  for word in author21_dif:
    author2_dif_total += freq2[word]
  author2_dif_freq = (author2_dif_total/author2_total_words)*100
  
  print( "%s used %s words that %s did not use." % (author1, len(author12_dif), author2) )
  print( "Relative frequency of words used by %s not in common with %s = %s" % (author1, author2, author1_dif_freq) )
  print()
  print("%s used %s words that %s did not use." % (author2, len(author21_dif), author1))
  print( "Relative frequency of words used by %s not in common with %s = %s" % (author2, author1, author2_dif_freq) )

  print()

def main():
  # Create word dictionary from comprehensive word list
  create_word_dict()

  print()

  # Enter names of the two books in electronic form
  book1 = input ("Enter name of first book: ")
  book2 = input ("Enter name of second book: ")
  print()

  # Enter names of the two authors
  author1 = input ("Enter last name of first author: ")
  author2 = input ("Enter last name of second author: ")
  print() 
  
  # Get the frequency of words used by the two authors
  wordFreq1 = getWordFreq (book1)
  wordFreq2 = getWordFreq (book2)

  # Compare the relative frequency of uncommon words used
  # by the two authors
  wordComparison (author1, wordFreq1, author2, wordFreq2)

if __name__ == "__main__":
  main()