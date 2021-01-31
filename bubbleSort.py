def bubbleSort(arr):
    isSorted = False
    nth = 0
    length = len(arr) - 1

    while(not isSorted):
        #compare first and second n and n + 1
        #swap and then add one to nth term
        if(arr[nth] >= arr[nth + 1]):
            temp = arr[nth + 1]
            arr[nth + 1] = arr[nth]
            arr[nth] = temp

        nth = nth + 1

        if(nth == length):
            #loop until the end and restart loop
            length = length - 1
            nth = 0
        if(length == 0):
            isSorted = True
            return arr



if __name__ == "__main__":
    SortedArray = bubbleSort([15,18,65,89,101,599,654,12,1,88,36,69,12,14,3,66])
    print(SortedArray)