T=int(input())
C=[]
for i in range(T):
    C.append(int(input()))
for N in C:  
    set=[]
    for _ in range(1,N+1):
        set.append(_)
    set.sort()
    subset=[]
    for _ in set:
        if _/2 not in subset:
            subset.append(_)
    print(len(subset))