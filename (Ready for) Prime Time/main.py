def prime(n):
    final_list = []
    for i in range(2, n+1):
        if i%2 != 0 or i==2:
            counter = 0
            for x in range(2,i+1):
                if i%x == 0:
                    counter +=1
                if counter > 1:
                    break
            if counter == 1:
                final_list.append(i)
    return final_list