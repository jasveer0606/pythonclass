# Written in shorthand python
# Helpful links : www.pythonforbeginners.com/basics/list-comprehensions-in-python
#                 https://www.python.org/dev/peps/pep-0274/
#                 howto.lintel.in/writing-shorthand-statements-in-python

from random import *
names=list("ABCDEFGHIJ")
L=[{n:randint(1,5) for n in [i for i in names if i!=name]} for name in names]
S=[sum([i[name] for i in L if name in i]) for name in names]
print "Score={} and highest scorer={}".format(max(S),names[S.index(max(S))])
