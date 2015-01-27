import sys

def partition_sort(A, L, R, C):
    if R - L <= 1: return A
    C[0] += R - L - 1
    pivot = A[L]
    i = L + 1
    for j in range(L + 1, R):
        if A[j] <= pivot:
            swap(A,j,i)
            i += 1
    swap(A,L,i-1)
    partition_sort(A, L, i - 1, C)
    partition_sort(A, i, R, C)
    return A

def swap(lst, index1, index2):
    lst[index1], lst[index2] = lst[index2], lst[index1]
    
with open(sys.argv[1]) as file:
    data = []
    for line in file:
        x = int(line)
        data.append(x)

count = [0]
partition_sort(data, 0, len(data), count)
print "comparison count is " + str(count[0])
