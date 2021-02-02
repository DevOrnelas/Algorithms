def selection_sort(A):
    for i in range(len(A)): 
        min_idx = i 
        for j in range(i+1, len(A)): 
            if A[min_idx] > A[j]: 
                min_idx = j 
        A[i], A[min_idx] = A[min_idx], A[i] 
    return A
if __name__ == "__main__":
    sortedArr = selection_sort([43,52,526,2,53,12,56,99,9,15])
    print(sortedArr)