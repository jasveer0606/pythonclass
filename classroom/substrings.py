# Classroom question to generate all contiguous substrings of a given string

# Regular iterative solution : 

def get_all_substrings(string):
  length = len(string)
  alist = []
  for i in xrange(length):
    for j in xrange(i,length):
      alist.append(string[i:j + 1]) 
  return alist

# Concise Pythonic solution :

def get_all_substrings_1(input_string):
  length = len(input_string)
  return [input_string[i:j + 1] for i in xrange(length) for j in xrange(i,length)]


from timeit import timeit

print timeit("get_all_substrings('abcde')", "from __main__ import get_all_substrings")
# ~3.3

print timeit("get_all_substrings_1('abcde')", "from __main__ import get_all_substrings_1")
# ~2.6

# Footnote : The iterative solution is timing worse here due to the xrange call on a small string.
# As a rule, inline loops are faster than comprehensions.
