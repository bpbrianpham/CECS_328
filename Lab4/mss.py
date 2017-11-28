def mssBigOofN(a):
    temp = a[0]
    mss = temp
    for i in range(1, len(a)):
        temp = temp + a[i]
        if (mss < temp):
            mss = temp
        if (temp < 0):
            temp = 0
    return mss

def mssBigOofLogN(a):