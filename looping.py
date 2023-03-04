def oddevencheck(int):
    if int % 2 == 1:
        print(int, " adalah ganjil")
    else :
        print (int, " adalah genap")
        
for i in range(1, 100+1):
    oddevencheck(i)