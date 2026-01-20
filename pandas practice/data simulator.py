import random

from h5py.h5i import DATASET


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

    def median(self):
        if not self.data:
            return None
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        mid = n//2
        if n%2 == 0:
            return (sorted_data[mid-1]+ sorted_data[mid])/2
        else:
            return sorted_data[mid]
    def standard_deviation(self):
        if not self.data:
            return None
        mean_value = self.mean()
        variance = sum([(x-mean_value)**2 for x in self.data])/len(self.data)
        return variance**0.5

    def add_noise(self,magnitude):
        self.data = [x + random.uniform(-magnitude, magnitude) for x in self.data]

    def __str__(self):
        return f"dataset({self.data})"


dataset = dataset([3,5,7,8,9,0])

print('mean:', dataset.mean())
print('median', dataset.median())
print('standard Deviation:', dataset.standard_deviation())

dataset.add_noise(0.5)
print('noisy data:', dataset)

