def combsort(list1):
    gap = len(list1)
    shrink = float(1.3)
    sorted = False

    while sorted is False:
        gap = floor( gap / shrink)
        if gap > 1:
            sorted = False
        else:
            gap = 1
            sorted = True
        i = o
        while i + gap <len(list1):
            if (x**1/2(x**2 + y**2)) > ((x**1/2(x**2 + y**2))[i + gap])
