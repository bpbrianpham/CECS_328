
def linearSearch(a, key):
    n = len(a)
    for i in range(0, n):
        if key == a[i]:
            return True    
    
    return False

def binarySearch(a, key):
    beg = 0
    end = len(a) - 1
    while beg < end:
        mid = int((beg + end)/2)
        if key == a[mid]:
            return True
        elif key >= a[mid]:
            beg = mid + 1
        else:
            end = mid - 1
    return False