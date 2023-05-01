def decimal(a):
    s = str(a)
    c = int(s.split('.')[1])
    if c > 0:
        a = float(a)
        return(a)
    else:
        a = int(a)
        return(a)
