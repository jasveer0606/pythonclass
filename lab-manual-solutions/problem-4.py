f=raw_input("Enter filename:")
i=raw_input("Enter modified filename:")

try:
    with open(f,'r') as op:
        l=op.readlines()
        with open(i,'w') as tr:
            tr.write('\n'.join(filter(lambda x: not x[0]=='#',l)))
except:
    print "Error in opening file."
else:
    print "Write complete."
    raw_input()
