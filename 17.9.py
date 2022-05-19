array = input('Введите числа через пробел от 0 до 100: ').split()
L = list(map(int, array)) 

def merge_sort(L):  
    if len(L) < 2:  
        return L[:]  
    else:
        middle = len(L) // 2  
        left = merge_sort(L[:middle])  
        right = merge_sort(L[middle:])  
        return merge(left, right)  

def merge(left, right): 
    result = [] 
    i, j = 0, 0  

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result
print('Отсортированный массив:', merge_sort(L))
print('Количество элементов в  массиве:', len(merge_sort(L)))

def binary_search(L, element, left, right):
    if left > right: 
        return False  

    middle = (right + left) // 2  
    if L[middle] == element: 
        return middle  
    elif element < L[middle]:  
        return binary_search(L, element, left, middle - 1)
    else: 
        return binary_search(L, element, middle + 1, right)

while True:
    try:
        element = int(input('Введите число от 0 до 100: '))
        if element < 0 or element > 100:
            raise Exception
        break
    except ValueError:
        print('Ошибка, повторите ввод.')
    except Exception:
        print('Неверный диапазон чисел. Повторите ввод.')

print(binary_search(L, element, 0, len(L)))
