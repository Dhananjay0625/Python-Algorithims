def plusMinus():
    ar = [-4, 3, -9, 0, 4, 1]

    pos = 0
    neg = 0
    zero = 0

    for i in ar:
        if i > 0:
            pos+=1
        elif i < 0:
            neg+=1
        elif i == 0:
            zero+=1
            
    print(f"{pos/len(ar):.6f}")
    print(f"{neg/len(ar):.6f}")
    print(f"{zero/len(ar):.6f}")

plusMinus()