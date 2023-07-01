import random
import timeit
import b_tree


small_array = [5, 4, 8, 254, 3, 255, 69, 0, 0, -85]
big_array = [random.randint(-1000, 1000) for i in range(1000)]
very_big_array = [random.randint(-1000, 1000) for _ in range(10000)]
null_array = [0, 0, 0, 0, 0]
b_tree_degree = 2


def timer(funcname, array):
    if funcname == 'external_sort':
        print(funcname)
        array += ".txt"
        array = "small_array.txt"
        print(array)
        time = timeit.Timer('external_sort.external_sort()'.format(),
                            setup="import external_sort;").repeat(1, 3)
        print('s')
    else:
        setup = "from __main__ import {0}; from __main__ import {1};"
        time = timeit.Timer('{0}({1})'.format(funcname, array),
                            setup=setup.format(
                                funcname, array)).repeat(1, 3)
    return time[0]


def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        q = random.choice(array)
        less_numbers = []
        more_numbers = []
        equal_numbers = []
        for n in array:
            if n < q:
                less_numbers.append(n)
            elif n > q:
                more_numbers.append(n)
            else:
                equal_numbers.append(n)
        return quick_sort(less_numbers) + equal_numbers + quick_sort(
            more_numbers)


def merge_sort(array):
    if len(array) > 1:
        middle = len(array) // 2
        left_arr = array[:middle]
        right_arr = array[middle:]
        merge_sort(left_arr)
        merge_sort(right_arr)
        i = 0
        j = 0
        k = 0
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                array[k] = left_arr[i]
                i += 1
            else:
                array[k] = right_arr[j]
                j += 1
            k += 1
        while i < len(left_arr):
            array[k] = left_arr[i]
            i += 1
            k += 1
        while j < len(right_arr):
            array[k] = right_arr[j]
            j += 1
            k += 1
    return array


def heap_sort(array):
    def sift_down(parent, limit):
        item = array[parent]
        while True:
            child = (parent << 1) + 1
            if child >= limit:
                break
            if child + 1 < limit and array[child] < array[child + 1]:
                child += 1
            if item < array[child]:
                array[parent] = array[child]
                parent = child
            else:
                break
        array[parent] = item
    length = len(array)
    for index in range((length >> 1) - 1, -1, -1):
        sift_down(index, length)
    for index in range(length - 1, 0, -1):
        array[0], array[index] = array[index], array[0]
        sift_down(0, index)
    return array


def bubble_sort(array):
    for element in range(len(array) - 1, 0, -1):
        for i in range(element):
            if array[i] > array[i + 1]:
                temp = array[i]
                array[i] = array[i + 1]
                array[i + 1] = temp
    return array


def shell_sort(array):
    increment = len(array) // 2
    while increment > 0:
        for start in range(increment):
            insert_sort_with_step(array, start, increment)
        increment = increment // 2
    return array


def insert_sort_with_step(array, start, step):
    if len(array) == 0:
        return []
    for i in range(start + step, len(array), step):
        value = array[i]
        pos = i
        while pos >= step and array[pos - step] > value:
            array[pos] = array[pos - step]
            pos = pos - step
        array[pos] = value
    return array


def insert_sort_without_step(array):
    for i in range(1, len(array)):
        value = array[i]
        pos = i
        while pos >= 1 and array[pos - 1] > value:
            array[pos] = array[pos - 1]
            pos = pos - 1
        array[pos] = value
    return array


def b_tree_sort(array):
    global b_tree_degree
    tree = b_tree.BTree(b_tree_degree)
    for el in array:
        tree.insert_element(el)
    return tree.get_sorted_array()


def print_sorts(sorts_funcs, array_name, describe):
    max_time = 0
    min_time = 10000
    min_time_name = ''
    max_time_name = ''
    list_of_sorts = []
    all_time = dict()
    for sort_func in sorts_funcs:
        time = timer(sort_func, array_name)
        all_time[sort_func] = time
        if time <= min_time:
            min_time = time
            min_time_name = sort_func
            list_of_sorts.insert(0, sort_func)
        elif time >= max_time:
            max_time = time
            max_time_name = sort_func
            list_of_sorts.append(sort_func)
        print('{:^25} | {:^30} |  {:^20}'.format(sort_func, array_name, time))
    print(list_of_sorts)
    print('{} : {}, {}'.format('Минимальное время', min_time_name, min_time))
    print('{} : {}, {}'.format('Максимальное время', max_time_name, max_time))
    plot.make_plot(all_time, array_name + "(" + describe + ")")


def main():
    print("Введите минимальную степень дерева (B-tree) >= 2")
    global b_tree_degree
    b_tree_degree = input()
    sorts_funcs = ['insert_sort_without_step', 'shell_sort', 'heap_sort',
                   'merge_sort', 'quick_sort', 'b_tree_sort', 'bubble_sort']
    print('{:^25} | {:^30} |  {:^20}'.format('Название функции', 'Тип данных',
                                             'Среднее время работы'))
    print_sorts(sorts_funcs, "small_array", "10 элементов")
    print_sorts(sorts_funcs, "big_array", "1000 элементов")
    print_sorts(sorts_funcs, "very_big_array", "10.000 элементов")
    print_sorts(sorts_funcs, "null_array", "5 элементов")


if __name__ == "__main__":
    import plot
    main()
