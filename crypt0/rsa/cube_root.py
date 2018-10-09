def cuberoot(x):
    lw=0
    hi=x
    last=0
    while(lw<=hi):
        mid=(lw+hi)/2
        if(mid**3<=x):
            last=mid
            lw=mid+1
        else: hi=mid-1
    return last
