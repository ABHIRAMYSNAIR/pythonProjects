class Time:
    def __init__(self,hour,minute,seconds):
        self.hour=hour
        self.minute=minute
        self.seconds=seconds
    def __add__(self, other):
        return self.hour+other.hour,self.minute+other.minute,self.seconds+other.seconds
o1=Time(5,20,18)
o2=Time(4,7,5)
print(o1+o2)