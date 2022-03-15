def sol(page, n):
    queue = []
    count = 0

    for i in page:
        
        if i in queue:
            count += 1
        else:
            count += 6

            if len(queue) == n:
                queue.pop(0)
            
            queue.append(i)
    
    return count

page = 'BCBAEBCE'
n = 3

print(sol(page,n))

            

        