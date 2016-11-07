def occurrences(str, target_str):
  wdn = len(str)
  count = 0
  while(wdn > 1):
  	start = 0
  	while(start + wdn <= len(str)):
  	  if (str[start:start + wdn] == target_str):
  	    count += 1
  	  start += 1
  	wdn -= 1
  return count

def occurrencesInFile(file_str, target_str):
  infile = open(file_str, "r")
  for line in infile:
  	line = line.strip()
  	line = line.upper()
  	print(occurrences(line, target_str.upper()))

  infile.close()

def forbiddenWords(file_str, f_words):
  infile = open(file_str, "r")

  for line in infile:
  	line = line.strip()
  	no_f = True
  	i = 0
  	while(no_f and i < len(f_words)):
  	  if(line.find(f_words[i]) != -1):
  	  	no_f = False
  	  i += 1
  	print(no_f)

  infile.close()

def odd_lines(in_file, out_file):
  infile = open(in_file, "r")
  outfile = open(out_file, "w")

  counter = 1
  for line in infile:
  	if(counter % 2 == 1):
  	  outfile.write(line)
  	counter += 1

  infile.close()
  outfile.close()


def main():
  #occurrencesInFile("test.txt", "this")
  #forbiddenWords("test.txt", ["thiss"])
  odd_lines("test.txt", "testOut.txt")

main()