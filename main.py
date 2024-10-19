# YOUR CODE HERE
lst1 = []
lst2 = []
n = int(input())

for i in range(n):
    v = int(input())
    lst1.append(v)
for i in range(n):
    v = int(input())
    lst2.append(v)
    
def summation(lst1,lst2):
    global n
    update_list = [0]*n 
    for i in range(n):
        update_list[i] = lst1[i]+lst2[i]
    return update_list

def find_min_max(update_list):
    return (min(update_list),max(update_list))    

print(summation(lst1,lst2))
print(find_min_max(summation(lst1,lst2)))
