hh = input("enter hours:")
rr = input("enter rate:")
def computepay(hrs, rate) :
    h = float(hrs)
    r = float(rate)
    if h > 40 :
        lr = r * 1.5
        lh = h - 40
        g = r * 40
        og = lr * lh
        gg = g + og
    else :
        gg = h * r
    return(gg)
print("pay",computepay(hh,rr))
