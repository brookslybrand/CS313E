def check_password(username, password):
  in_file = open("./passwords.txt", "r")
  passwords_dict = {}
  for line in in_file:
  	line = line.strip()
  	line = line.split(":")
  	passwords_dict[line[0]] = line[1]
  in_file.close()
  if username in passwords_dict:
  	return passwords_dict[username] == password
  else:
  	return False

def main():
  username = str(input("username: "))
  password = str(input("password: "))
  print(check_password(username, password))

main()