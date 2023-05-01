def drawline(symb='_-',times=20,split=0):                                        #function to draw a line
    for i in range(times):
        if i == times//2:
            if split == 2:
                print()
        print(symb,end='')
    print()

def decimalcheck(num):                                                           #function to remove the decimal point from an integer
    str = str(num)
    check = int(str.split('.')[1])
    if check > 0:
        num = float(num)
        return(num)
    else:
        num = int(num)
        return(num)
