a = -100
print(abs(a))

a = [123, 45,0, 0.0, None, []]

print(any(a))

print(ascii('abcйцу'))

print(bin(8))
print(hex(16))

def sum_list(a):
    sum=[]
    for i in a: 
        sum.append(i)
    return sum

print(bool(sum_list(['', '', None])))

print(bytes(10))
print(bytes('ABCАПР', 'utf8'))


str = 'ABC'
print(callable(print))

print(chr(17))


s = compile('print(1000)', 'test', 'eval')
exec(s)

class Person:
    a = 10
    b = 120
    sum = a+b
    
p = Person()
p1 = Person()
print(p.sum)
delattr(Person, 'sum')
print(p1.a)

print(dir(p))

z = divmod(13, 3)
print(z[0])


def filter_f(x):
    if x > 10:
        if x <= 70:
            return 'Positive'
    else:
        return None
    
res = [12, 4, 5, 7, 89]
print(list(filter(filter_f, res)))



def map_f(x):
    return x**2

print(list(map(map_f, res)))

a = ["John", "Charles", "Mike"]
b = ["Jenny", "Christy"]
c = ['12', '454', '123']

x = zip(a, b, c)

#use the tuple() function to display a readable version of the result:

# print(dict(x))

import datetime 
fhand = open('test.txt', 'w')
fhand.write('this Message was written by Python\n')
fhand.write('Test 2\n')
fhand.write('Test 3\n')
fhand.writelines(['Test 4\n', 'Test5\n',])
fhand.close()
s = compile('print(150+130)', 'test', 'eval')
exec(s)

fhand2 = open('test.txt')
# for i in fhand2:
#     i = i.rstrip() 
#     print(i)



str = fhand2.read()
print(str[:35])

import os

# fname = input('Provide file name: ')
# fhand = open(fname, 'x')
# fhand.write('Subject: PP2')
# fhand.close()

test = os.path.abspath('.')
print(test)


fhand3 = open(test+'\\test.txt', 'a')
fhand3.writelines(['new', 'strings'])
fhand.close()
os.remove(test+'\\test2.txt')
