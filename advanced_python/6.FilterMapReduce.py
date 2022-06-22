nums = [4,2,6,6,1,3,5,4,6,7,8,9,98,65,66]

#Filter function filters the list according to function condition
is_even = lambda x:x%2==0
evenlist = list(filter(lambda x:x%2==0,nums))
print(evenlist)

#map function maps the fuctions to all elements in iterable
squre = list(map(lambda x:x*x,nums))
print(squre)

#reduce: to reduce the all list into a number such as sum or avg
# below reduces the evenlist into average
from functools import  reduce
sum = reduce(lambda x,y:x+y/len(evenlist),evenlist)
print(sum)

#adding the curresping elemetnt in 2 lists
# custom zip
deg = list(map(lambda m,x,y:m+x+y,evenlist,squre,nums))
print(deg)

#to take all palindromes from a list

dromes = ("demigod", "rewire", "madam", "freer", "anutforajaroftuna", "kiosk","malayalam")

palindromes = list(filter(lambda word: word == word[::-1], dromes))
string = "english"
print(string[::-1])

print(palindromes)