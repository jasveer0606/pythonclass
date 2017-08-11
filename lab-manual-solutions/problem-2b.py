str1, subs = raw_input("Enter String: "), raw_input("Enter Substring: ")
print "Number of occurences = {}".format(str1.count(subs))
L=[str1.find(subs,start) for start in range(0,len(str1),len(subs))]
print "Indices of occurences = ", list(set([i for i in L if i!=-1]))
