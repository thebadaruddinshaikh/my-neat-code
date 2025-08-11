
def solve(starts, ends):
    end = max(ends)
    processes = list(zip(starts, ends))
    processes.sort(key = lambda x:(x[0], -x[1]))
    
    ans = []
    ans.append(processes[0])

    i = 0
    interval = []
    while i < len(processes):
        if ans[-1][1] == end:
            break
    
        if processes[i][0] <= ans[-1][1]:
            if not interval:
                interval = processes[i]
            elif interval[1] < processes[i][1]:
                interval = processes[i]
            i+=1
        elif interval:
            ans.append(interval)
            interval = []
        
        

    return ans


print(solve([1,2,3,4], [2,3,5,5]))
        
