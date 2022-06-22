"""Counters
OrderedDict
DefaultDict
ChainMap
NamedTuple
DeQue
UserDict
UserList
UserString"""

#counter: which counts the frequency

from collections import Counter
items = ['B','B','A','B','C','A','B',
               'B','A','C']

print(Counter(items))
print(Counter(A=3, B=5, C=2))


#OrderedDict
from collections import OrderedDict
dic = OrderedDict({'a':'Arabic','b':'bank','c':'car'})
dic1 = {'a':'Arabic','b':'bank','c':'car'}
print(dic)
dic.pop('a')
dic['a']='Anar'

print(dic)
print(dic1)

from collections import ChainMap
c = ChainMap(dic,dic1)
print(c)

from collections import namedtuple

tup = namedtuple(typename='Student',field_names=['fname','lname','place'])
t=tup('Muhammed','Kutty','Kannur')
print(t.fname)

#deque: doubly ended queue
from collections import deque

l=deque([1,2,5,4,7,8,5,6,4])
l.append(4)
l.appendleft(100)
print(l)
l.popleft()
print(l)

#user defined list
from collections import UserList

class MyOwnList(UserList):
    def pop(self,s=None):
        raise RuntimeError("Pop not allowed")
L=MyOwnList([2,5,4])
L.pop(2)
print(L)