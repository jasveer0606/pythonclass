class Time:
    def __init__(self, h, m, s):
        self.hours = h
        self.mins = m
        self.secs = s

    def gettime(self):
        self.hours = input("Enter hours:")
        self.mins = input("Enter minutes:")
        self.secs = input("Enter seconds:")

    def __str__(self):
        return "{}:{}:{}".format(self.hours,self.mins,self.secs)

    def __add__(self,other):
        nh = self.hours+other.hours
        nm = self.mins+other.mins
        ns = self.secs+other.secs
        while ns>60:
            ns -= 60
            nm += 1
        while nm>60:
            nm -= 60
            nh += 1
        return Time(nh,nm,ns)

    def __sub__(self,other):
        return Time(self.hours-other.hours,self.mins-other.mins,self.secs-other.secs)

    
t1 = Time(12,10,50)
t2 = Time(10,7,32)
print t1+t2
