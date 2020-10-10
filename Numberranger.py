def solution(area):
    numsq = []
    panels = []
    for i in range(2, int(area**0.5)+1):#makes sure everything that just happened in range of 2 was inside of the default solar area
        sq = i**2
        numsq.append(sq)
    numsq.reverse()
    numsq.append(4) # sets output length of list
    for o in range(3):
        numsq.append(1)
    for p in numsq:
        if p <= area:
            panels.append(p)
            area -= p
        elif area == 0:
            break
    return panels #sends output to google/from module