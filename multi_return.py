def stat (x):
    total_sum = 0


    for x in data:
        total_sum += x 

    N = len(data)

    mean = total_sum/N

    #return total_sum, mean

data = [1,2,3,4,5]

total_sum , mean = stat(data)

print(total_sum)
print(mean)