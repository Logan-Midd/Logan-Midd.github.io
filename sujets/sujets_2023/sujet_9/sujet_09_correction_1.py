def multiplication(n1,n2):
    s=0
    if n1==0 or n2==0:
        return 0
    if n1<0:
        return -multiplication(-n1,n2)
    if n2<0:
        return -multiplication(n1,-n2)
    for i in range(n2):
        s = s+n1
    return s