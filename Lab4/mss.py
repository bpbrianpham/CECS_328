import statistics

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

def mssBigOofNLogN(a, left, right):
    maxLeft = 0
    maxRight = 0
    
    middle = (left + right)//2

    if (left == right):
        return a[left-1]

    leftArray = mssBigOofNLogN(a, left, middle)
    rightArray = mssBigOofNLogN(a, middle+1, right)

    leftTemp = 0
    rightTemp = 0
    for i in range(middle, left-1, -1):
        leftTemp = leftTemp + a[i]
        if leftTemp > maxLeft:
            maxLeft = leftTemp
    
    for i in range(middle+1, right):
        rightTemp = rightTemp + a[i]
        if rightTemp > maxRight:
            maxRight = rightTemp  

    return max(maxLeft + maxRight,rightArray, leftArray)