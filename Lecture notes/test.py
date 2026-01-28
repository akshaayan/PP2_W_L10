t = [1, 2, 4, 'Name', [123, 222, 'New'], 'Surname']
print(t[4])
x = 2
# print(list(range(1, 10, (x**2))))
# print(type(range(4)))
for i in range(len(t[4])): 
    print(t[4][i])
    
# f = [1, 2, 5, 7, 'name', 'surname' ]
# f.sort()
# print(f)

c = '....hdgvajsb. isihk   hbkn ///////'
c = c.strip("/hbkn .")
print(c)


students = {'25BD010000': {'name': 'Daulet', 'email': 'test@example.com', 'phone' : '+777777', 'grades': {'math': [5, 5, 4, 5], 'PP2': [100]}}}
print(sum(students['25BD010000']['grades']['math'])/len(students['25BD010000']['grades']['math']))

for i in students: 
    print(i)
    for j in students[i]:
        print(students[i][j])
        

        

