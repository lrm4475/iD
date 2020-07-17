entries = [32, 14, 89, 62, 10, 20, 88, 40, 22, 91, 88, 65, 100]

# Linear Search
def linearsearch(values, key):
    answer = -1

    for value in values:
        if value == key:
            answer = key
            return answer

    return answer

#Binary Search
def binarysearch(array, x):
    low = 0
    high = len(array) - 1
    while low <= high:
        midpoint = ((low + high)/2)
        midpoint = int(midpoint)

        if array[midpoint] == x:
            return midpoint
        elif array[midpoint] > x:
            high = midpoint - 1
        elif array[midpoint] < x:
            low = midpoint + 1
        print(midpoint)

    return -1

def selectionSort(input):
    arrlen = len(input)

    print("Sorted array:")
    for x in range(0, arrlen):
        smallest = x
        for y in range(x + 1, arrlen):
            if(input[y] < input[smallest]):
                smallest = y
        temp = input[smallest]
        input[smallest] = input[x]
        input[x] = temp

    for i in range(arrlen):
        print(" ", input[i])

def main():
    index = linearsearch(entries, 88)
    print("Answer is: ", index)

    values = [1, 2, 3, 4, 5, 6, 7, 8, 10]
    value = binarysearch(values, 4)
    print("Value is: ", value)

    numbers = [3, 1, 9, 5, 6, 2, 2, 7, 8, 11]
    selectionSort(numbers)
main()
