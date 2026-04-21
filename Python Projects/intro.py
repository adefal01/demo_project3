print("HELLO WORLD!")
# single line comment
'''
block style commenting
3 single quotes
too switch something to a comment highlight command forward slash
'''
x=10
y=1.5
z=2
x="hello"
# double slash gives no floating decimal, one always gives a floating decimal
x=100//10
print(x)
y=1.5
x=int(y)
print(x)

min_value=min(1,3)
min_value=min([4,3,5,6])
print(min_value)
r=2**4
r=pow(2,4)
print(r)
#if stateemnts dont have parenthesis or curly brackets no semi-colons
if x>10:
    x=5
    y=100
#compound if statements in python you write and or or
if x>10 and y<5:
    x=0
    y=100
if x>10 or y<5:
    x=0
    y=100
if x>10:
    print("x")
elif y>10:
    print ("y")
else:
    print("neither")
#for loop, process arrays and or lists, default starts at 0
for i in range(5):
    print(i)
#to change start value add start value can change increment by adding third parameter
lst=[1,2,3,4,5]
for i in range(1,len(lst),2):
    print(i,lst[i])
#default is start at 0 increment by 1
for i in range(len(lst)-1,-1,-1):
    print(i,lst[i])


