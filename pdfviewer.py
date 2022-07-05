h = [1,3,1,3,1,4,1,3,2,5,5,5,5,1,1,5,5,1,5,2,5,5,5,5,5,5]

str = "manik"
asc = []

for i in str:
    b = ord(i)
    
    no = (ord(i)-ord("a")) + 1

    asc.append(no)
    
height = []

for i in asc:
    height.append(h[i-1])
    
max_height = max(height)

print(max_height * len(str))