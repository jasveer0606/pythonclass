class OrderSet:
    iset = []
    def __init__(self, iset=[]):
        self.iset = iset
    def add(self, e):
        if e not in iset:
            iset.append(e)
    def del(self,e):
        if e in iset:
            iset.remove(e) 
    def __str__(self):
        return ' '.join(iset)
    def __get__(self):
        return self.iset

def substring(string):
    return [[s[i:i+j] for i in range(len(string)-j+1)] for j in range(len(string),0,-1)]

def costbuild(string, a, b):
    built = ''
    subs = OrderSet()
    cost = 0
    position = 0
    
    while built != string:

        # start case
        if not built:
            built += string[0]
            cost += a
            subs.add(string[0])
            position += 1
            
        # normal case
        else:
            if b>a:
                pass
            else:
                subs.add(substring(string))
            
if __name__ == '__main__':
    t=input()
    for _ in range(t):
        n,p,q = map(int,raw_input().split())
        string = raw_input()
        print costbuild(string, p, q)
