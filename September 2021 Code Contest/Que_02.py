T=int(input())
lensubsets=[]
for i in range(T):
    N=int(input())
    set=[]
    for _ in range(N):
        set.append(_+1)
    set.sort()
    subset=[]
    for _ in set:
        if _/2 not in subset:
            subset.append(_)
    lensubsets.append(len(subset))

for _ in lensubsets:
    print(_)