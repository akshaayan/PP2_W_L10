test = [100, 9 , 69, 45, 20, 'zet', 'beta']
# def sort_list(list):


def sort_list(list):
    num_list = []
    str_list= []
    for i in list:
        if isinstance(i, int):
            num_list.append(i)
        else: 
            str_list.append(i)
    print(num_list)
    print(str_list)
    
    for i in range(len(num_list)):    
        for j in range(i, len(num_list)):
            if num_list[i] > num_list[j]:
                num_list[i], num_list[j] = num_list[j] , num_list [i]
    
    for i in range(len(str_list)):    
        for j in range(i, len(str_list)):
            if str_list[i] > str_list[j]:
                str_list[i], str_list[j] = str_list[j] , str_list [i]
    return num_list, str_list

res, res1 = sort_list(test)
print(res1)

def computepay(h, r):
    n_h = 40
    if h > n_h:
        o_h = h - n_h
        return o_h*r*2+n_h*r
    else:
        return h*r
    
print(computepay(35, 20000))

def new_func(*args, **kwargs):
    for i in args: 
        print(i)
        
    print(args)
    print(kwargs)
    
new_func(1, 2, 4, 6, 9, g=100, y = 1000)

class Student:
    def __init__(self, id, name, major, gpa):
        self.id = id
        self.name = name
        self.major = major
        self.gpa = gpa
    
    def study(self, topic):
        print(topic, " completed")
    
    def think(self, idea):
        pass
    
    def change_id(self, new_id):
        self.id = new_id
        
        
class Human:
    def __init__(self):
        self.age = 0
        self.weigh = 0
        self.height = 0
        self.name = ''
        self.hp= 100
        
    def sleep(self, h):
        self.hp = self.hp + h
        
    def eat(self):
        self.weigh+=1 
        return 'healthy'
    
    def grow(self):
        res = self.eat()
        if res == 'healthy':
            self.height+=1
        else:
            pass
        
class MasterStudent(Student, Human):
    def __init__(self, id, name, major, gpa):
        Student.__init__(self, id, name, major, gpa)
        Human.__init__(self)
        
        
ms = MasterStudent('25B000001', 'Daulet', 'CS', 3.0)
ms.grow()
print(ms.height)
ms.study('PP2')

        
    
    
    