import sys

def partition_sort(A, L, R, C):
    if R - L <= 1: return A
    swap(A,L,median3(A,L,R-1,((R-1+L)/2))) # swap median of 1st,last,middle indexes with left index
    C[0] += R - L - 1
    pivot = A[L] # make pivot leftmost element
    i = L + 1
    for j in range(L + 1, R):
        if A[j] <= pivot:
            swap(A,j,i)
            i += 1
    swap(A,L,i-1)
    partition_sort(A, L, i - 1, C)  # recurses over nums now left of pivot
    partition_sort(A, i, R, C)      # recurses over nums now right of pivot
    return A

def swap(lst, index1, index2): # swap two indices
    lst[index1], lst[index2] = lst[index2], lst[index1]
    
def median3(lst, a, b, c):
    if lst[a] <= lst[b]:
        if lst[b] <= lst[c]: return b
        elif lst[a] <= lst[c]: return c
        else: return a
    else:
        if lst[a] < lst[c]: return a
        elif lst[b] < lst[c]: return c
        else: return b
    
with open(sys.argv[1]) as file:
    data = []
    for line in file:
        x = int(line)
        data.append(x)

count = [0]
partition_sort(data, 0, len(data), count)
print "comparison count is " + str(count[0])
    
