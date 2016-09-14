# Find if the squirrels are going to have a cigar party

def cigar_party(cigars, is_weekend):
  ''' 
  There is a cigar party if there are over 40 cigars 
  and if it's either the weekend or there are less than 60 
  cigars 
  '''
  return ( (cigars >= 40) and (is_weekend or cigars <= 60) )