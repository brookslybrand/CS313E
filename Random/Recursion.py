def towers(n, source, spare, dest):
  if(n == 1):
  	print("Move disk from", source, "to", dest)
  else:
  	towers(n-1, source, dest, spare)
  	print("Move disk from", source, "to", dest)
  	towers(n-1, spare, source, dest)

def main():
  towers(64, 'A', 'B', 'C')

if __name__ == "__main__":
  main()