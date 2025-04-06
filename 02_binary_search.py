import time

a = [-1, 0, 3, 5, 6, 9, 10]

num = 11
l = 0
r = len(a) - 1
flag = True
print(a)

while l<=r:
    mid = (l+r)//2
    print("mid index", mid)
    print("mid element", a[mid])
    if a[mid] < num:
        l = mid + 1
        print("adjusting left")
    elif a[mid] > num:
        r = mid - 1
        print("adjusting right")
    else:
        print("matching")
        break
    print("altered", l, r)
    time.sleep(1)
