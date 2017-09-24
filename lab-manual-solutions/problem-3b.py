class Polygon(object):
    def __init__(self,s):
        self.s = s
        self.side=[]
    def inputsides(self):
        self.side=[input("Input side {} :".format(i+1)) for i in range(self.s)]

class Triangle(Polygon):
    def __init__(self):
        super(Triangle,self).__init__(3)
    def findarea(self):
        return sum(self.side)/2.0

A = Triangle()
A.inputsides()
print "The area is :",A.findarea()
