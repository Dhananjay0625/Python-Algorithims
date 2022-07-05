a = [
        [1,2,3],
        [4,5,6],
        [9,8,9]
    ]
    
left_diag = 0
right_diag = 0
count = 0
  
for i in a:
    for j in range(len(i)):
        if j == a.index(i):
            left_diag += i[j]
    
            
        if j == ((len(i) - a.index(i)) - 1):
            right_diag += i[j]

            
print(left_diag)
print(right_diag)