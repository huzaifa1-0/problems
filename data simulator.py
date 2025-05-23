import random

class dataset:
    def __init__(self,data):
        if not all(isinstance(x,(int,float)) for x in data):
            raise ValueError('all values must be numeric')
        self.data = data

    def mean(self):
        if not self.data:
            return None
        total = sum(self.data)
        return total/len(self.data)


