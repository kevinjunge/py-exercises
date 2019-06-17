def divBy7():
    l = []
    for i in range(2000,3201):
        if i %7 == 0 and i % 5 !=0:
            #print(i,end=",")
            l.append(str(i))
    q = ','.join(l)
    return q
print(divBy7())
#print()
# --------------------------------------
def fact(i):
    result = 1
    l=[]
    for x in range(1,i+1):
        result *= x
        l.append(str(result))
    return ','.join(l)
print(fact(8))
# --------------------------------------
def diction(i):
    d = {}
    for x in range(1,i+1):
        d[x]=x*x
    return d
print(diction(8))
# --------------------------------------
def listAndTuple(inp):
    l = inp.split(',')
    t = tuple(l)
    return l,t
x=input("string for list and tuple:")
print(listAndTuple(x)[0])
print(listAndTuple(x)[1])
# --------------------------------------
class upperCase(object):
    def __init__(self):
        self.s = ""
# --------------------------------------
    def getString(self):
        self.s = input("get string: ")
# --------------------------------------
    def printString(self):
        print(self.s.upper())
t1 = upperCase()
t1.getString()
t1.printString()
# --------------------------------------
import math
def sqRt(inp):
    C = 50
    H= 30
    z=inp.split(",")
    l=[]
    for i in range(len(z)):
        x=int(math.sqrt((C*2*int(z[i]))/H))
        l.append(str(x))
    return ','.join(l)
print(sqRt("100,150,180"))
# --------------------------------------
def twoDArray(x,y):
    l=[]
    r = []
    for i in range(x):
        for j in range(y):
            r.append(i*j)
        l.append(r)
        r=[]
    return l
print(twoDArray(3,5))
# --------------------------------------
def sortWords(inp):
    l=inp.split(',')
    sorted_l= sorted(l)
    return ','.join(sorted_l)
print(sortWords("without,hello,bag,world"))
# --------------------------------------
def capAll():
    lines=[]
    while True:
        i=input()
        if len(i)==0:
            break
        else:
            lines.append(i)
    cap_l=[]
    for i in range(len(lines)):
        cap_l.append(lines[i].upper())
    return '\n'.join(cap_l)
print(capAll())
# --------------------------------------
def sortDistinct(inp):
    l=inp.split(' ')
    # s=sorted(l)
    newL=[]
    for i in range(len(l)):
        if inp.count(l[i]) > 1 and newL.count(l[i]) ==0:
            newL.append(l[i])
        elif inp.count(l[i]) == 1:
            newL.append(l[i])
    return ' '.join(sorted(newL))
x="hello world and practice makes perfect and hello world again"
print(sortDistinct(x))
# --------------------------------------
import math
def binDivBy5(inp):
    l = inp.split(',')
    result = []
    for i in range(len(l)):
        x = list(l[i])
        x.reverse()
        y = 0
        for q in range(4):
            if int(x[q]) == 1:
                y += math.pow(2, q)
        if y % 5 == 0:
            result.append(l[i])
    return ','.join(result)
print(binDivBy5("0100,0011,1010,1001"))
# --------------------------------------
def eachIsEven():
    result = []
    for i in range(1000,3001):
        l=list(str(i))
        count = 0
        for x in range(len(l)):
            if int(l[x]) %2 == 0:
                count+=1
        if count == len(l):
            result.append(str(i))
    return ','.join(result)
print(eachIsEven())
# --------------------------------------
def lettersAndNums(inp):
    LETTERS = 0
    DIGITS = 0
    l = list(inp)
    for i in range(len(l)):
        if l[i].isdigit():
            DIGITS += 1
        elif l[i].isalpha():
            # print(l[i])
            LETTERS += 1
    return LETTERS, DIGITS
print("LETTERS " + str(lettersAndNums("hello world! 123")[0]))
print("DIGITS " + str(lettersAndNums("hello world! 123")[1]))
# --------------------------------------
def upperAndLower(inp):
    UPPER = 0
    LOWER = 0
    l = list(inp)
    for i in range(len(l)):
        if l[i].isupper():
            UPPER += 1
        elif l[i].islower():
            # print(l[i])
            LOWER += 1
    return UPPER, LOWER
print("UPPER " + str(upperAndLower("Hello world! 123")[0]))
print("LOWER " + str(upperAndLower("Hello world! 123")[1]))
# --------------------------------------
def computeVal(inp):
    x = 0
    l = []
    for i in range(1,5):
        j=1
        while j<=i:
            l.append(str(inp))
            j+=1
        x += int(''.join(l))
        l=[]
    return x
print(computeVal(9))
# --------------------------------------
def findOdd(inp):
    l=inp.split(',')
    # my solution
    r=[]
    for i in range(len(l)):
       if int(l[i]) % 2 != 0:
           r.append(l[i])
    # alternatively,
    odds = [x for x in l if int(x) % 2 !=0]
    return ','.join(odds)
print(findOdd("1,2,3,4,5,6,7,8,9"))
# --------------------------------------
def netAmount():
    D = 0
    W = 0
    while True:
        x = input("net amount: ").split(" ")
        if x[0] == "D":
            D += int(x[1])
        elif x[0] == "W":
            W += int(x[1])
        else:
            break
    return D-W
print(netAmount())
# --------------------------------------
import re
def checkPswd(inp):
    l = inp.split(',')
    result=[]
    sp=['$','#','@']
    for i in range(len(l)):
        if len(l[i]) > 5 and len(l[i]) <13 and (l[i].count('$') or l[i].count('#') or l[i].count('@') >0):
            pswd = list(l[i])
            lower = 0
            upper = 0
            num = 0
            for t in range(len(pswd)):
                if lower > 0 and upper > 0 and num > 0:
                    break
                if lower <1:
                    if pswd[t].islower():
                        lower+=1
                if upper <1:
                    if pswd[t].isupper():
                        upper+=1
                if num <1:
                    if pswd[t].isnumeric():
                        num +=1
            if lower > 0 and upper > 0 and num > 0:
                result.append(l[i])
    return ','.join(result)
print(checkPswd("ABd1234@1,a F1#,2w3E*,2We3345"))
# --------------------------------------
import re
def sortByNAS():
    l=[]
    while True:
        x=input("name, age and score: ")
        if not x:
           break
        else:
            l.append(tuple(x.split(',')))
            print(l)
    sorted_l = sorted(l)
    return sorted_l
print(sortByNAS())
Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85
# --------------------------------------
import re
class divBy7(object):
    def __init__(self):
        self.n = 0
    def genNumbers(self):
        l=[]
        for i in range(0,self.n+1):
            if i %7==0:
                l.append(str(i))
        return ','.join(l) # ???????
# --------------------------------------
# def zxc(inp):????????
# --------------------------------------
def asd(inp=""):
    l=inp.split(' ')
    r=[]
    for i in range(len(l)):
        x=l.count(l[i])
        u=l[i]+":"+str(x)
        if r.count(u)==0:
            r.append(u)
    return '\n'.join(r)
print(asd("New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."))
# --------------------------------------
def sq(i):
    return i**2
print(sq(3))
# --------------------------------------
def docBuiltIn(inp):
    return inp.__doc__
print(docBuiltIn(tuple))
# --------------------------------------
class Car(object):
    # Define the class parameter "name"
    name="Car"
    def __init__(self, name=None):
        #self.name is the instance parameter
        self.name = name
Mustang = Car("mustang")
print(Mustang.name, Car.name, "hgjk")
# --------------------------------------
