def array_of_array_products(arr):
    arr_length = len(arr)
    arr_result = []

    for i in range(arr_length):
        result = 1
        for j in range(arr_length):
            if i != j:
                result *= arr[j]
        arr_result.append(result)
    return arr_result


def array_of_array_products_v2(arr):
    arr_length = len(arr)
    arr_result = [0,0,0]

    result = 1
    for i in range(arr_length):
        arr_result[i] = result
        result *= arr[i]
        print("arr_result: " + str(arr_result))

    result = 1
    for i in range (arr_length - 1, -1, -1):
        arr_result[i] *= result
        result *= arr[i]
        print("arr_result2: " + str(arr_result))


    return arr_result

if __name__ == '__main__':
    arr = [8, 10, 2]
    print(array_of_array_products(arr))
    print(array_of_array_products_v2(arr))


