import statistics
def qCorrelation(lst):
    regionA, regionB, regionC, regionD = 0, 0, 0, 0
    xMed = statistics.median([a[0] for a in lst])
    yMed = statistics.median([a[1] for a in lst])
    print("Median of x is: ", xMed)
    print("Median of x is: ", yMed)
    for value in lst:
        x, y = value[0], value[1]
        if x < xMed and y > yMed:
            regionA += 1
        elif x > xMed and y > yMed:
            regionB += 1
        elif x < xMed and y < yMed:
            regionC += 1
        elif x > xMed and y < yMed:
            regionD += 1
    print("Region A has: ", regionA, " points")
    print("Region B has: ", regionB, " points")
    print("Region C has: ", regionC, " points")
    print("Region D has: ", regionD, " points")
    q = (regionB+regionC-(regionA+regionD))/(regionA+regionB+regionC+regionD)
    print("This is q: ",q)

#qCorrelation([[1,20],[5,9],[6,6],[8,10],[9,5],[10,0],[11,9],[12,6],[13,5],[14,10],[16,5]])
qCorrelation([[86,177],[136,187],[8,130],[19,71],[88,151],[65,145],[105,137],[175,205],[57,113],[220,211],[25,93],[96,130],[95,118],[97,173],[141,139]])