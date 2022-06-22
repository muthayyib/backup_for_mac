nums = [2,4,5,6,2,76]
#create and iterator from the list
itr = iter(nums)
print(itr.__next__())
print(itr.__next__())
print(itr.__next__())

#alternate method
print(next(itr))

#custom iterator
class Select:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self
    def __next__(self):
        if self.num<21:

            val = self.num
            self.num +=1
            a=[2,2,3,0,2]
            return a
        else:
            raise StopIteration

values = Select()
print("custom iteratior")
print(next(values))
print(values.__next__())
print(values.__iter__())
print(next(values))
for i in values:
    print(i)