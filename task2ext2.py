#!python3
"""
Compound Interest Calculator
Create a class object that accepts paramters for Principal, Annual Interest Rate, 
Number of compounding periods.  
Create a class method that calculates the amount of compound interest for a given length of time.

Extension: accept time given in different measurements, 
but convert them to years for use in your class template.
"""


class Calc:
    principal = 0
    rate = 0
    nPeriods = 0
    time = 0
    def __init__(self, p=0, r=0, n=0):
        if p>0 and r>0 and n>0:
            self.principal = p
            self.rate = r
            self.nPeriods = n
            self.convert(self.rate)
    def convert(self, r):
        self.rate = (r/100)
    def interest(self,t):
        #A=P(1+r/n)^nt
        self.time = t
        return round(((self.principal*((1+(self.rate/self.nPeriods)) ** (self.nPeriods * self.time))) - self.principal), 2)
    
    def amount(self,t):
        return round((self.principal*((1+(self.rate/self.nPeriods)) ** (self.nPeriods * t))), 2)

a = Calc(p=1000,r=4,n=2)
assert a.interest(3) == 126.16
assert a.amount(5) == 1218.99

b = Calc(p=5000,r=5.25,n=12)
assert b.interest(10) == 3442.62
