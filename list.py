# list in mutable means it can be modified
# it is array for python instead of array we use list defined inside the sqaure bracket

# assigning

list1=[1,2,3,4,"list",'python']
print(list1)
list1=[5,3.5,3]
print(list1)

list1[2:5]=[9,8,7,5] 
print( list1.count(5))
list2=[10,"rfsdf","sfsafde","ytre"]
list1.extend(list2)
print(list1)

word=[]
for i in 'bengalore':
    word.append(i)
print(word)

word=[]
final=[x for x in 'benagluru']
print(final)
choice=10
res=[x for x in range(choice) if x%2!=0]
print(res)

res=[ "even" if i %2==0  else "odd"  for i in range(10)]
print(res)

trans=[]
matrix=[[1,2,3,4],[5,6,7,8]]
for i in range(len(matrix[0])):
    ntr=[]
    for row in matrix:
        ntr.append(row[i])
    trans.append(ntr)
print(trans)


matrix=[[1,2,3,4],[5,6,7,8]]
trans=[[row[i]for row in matrix] for i in range(len(matrix))]
print(trans)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist=[x for x in fruits if x=="mango"]
print(newlist)
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
newlist=[x for x in fruits if "a" in x]
print(newlist)

newlist=[x for x in range(0,29,2)]
print(newlist)
newlist=[x.upper() for x in fruits]
print(newlist)
newlist1=['pavan' for c in fruits]
print(newlist1)
newlist=[x if x!="banana" else "orange" for x in fruits]
print(newlist)

def func(n):
    return abs(n-50)
number=[100,30,34,6,25,34]
number.sort(key=func)
print(number)
for i in range(10):
    if i%2!=0:
        print(i)


even=[x for x in range(10) if x%2!=0]
print(even )


