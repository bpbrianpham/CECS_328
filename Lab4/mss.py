def mssBigOofN(a):
    temp = a[0]
    mss = temp
    for i in range(1, len(a)):
        if (temp < 0):
            temp = 0
        temp = temp + a[i]
        if (mss < temp):
            mss = temp
        
    return mss

#def mssBigOofLogN(a):