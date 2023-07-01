import sorts
import copy


def split_set_of_elements(filename, count):
    with open(filename) as file:
        j = 0
        readed = ''
        while True:
            if readed == "\n":
                break
            a = list()
            digit = ''
            i = 0
            while i < count:
                readed = file.read(1)
                while readed.isdigit():
                    digit += readed
                    readed = file.read(1)
                a.append(digit)
                if readed == "\n":
                    break
                i += 1
                digit = ''
            yield a
            j += 1


def file_generator(size, filename):
    i = 0
    count = size
    names_array = list()
    gen = split_set_of_elements(filename, count)
    while True:
        name = str(i) + ".txt"
        with open(name, "w") as other:
            try:
                data = next(gen)
            except StopIteration:
                break
            names_array.append(name)
            for num in data:
                other.write(str(num) + " ")
        i += 1
    return names_array


def external_sort(filename):
    names = file_generator(1500, filename)
    digits_count = 0
    out = 'out.txt'
    out_array = list()
    for name in names:
        with open(name, 'r+') as file:
            file.seek(0)
            data = file.readlines()
            data = [int(x) for x in data[0].split(' ') if x]
            data = sorts.quick_sort(data)
            digits_count += len(data)
            file.seek(0)
            for digit in data:
                file.write(str(digit) + " ")
    with open(out, 'w') as file:
        i = 0
        while len(names) > 0:
            elements_arr = dict()
            for name in names:
                copynames = copy.copy(names)
                other = open(name)
                b = other.readlines()
                if len(b) == 0:
                    copynames.remove(name)
                    other.close()
                    continue
                data = [x for x in b[0].split(' ') if x]
                el = int(data[i])
                elements_arr[name] = el
                other.close()
                names = copy.copy(copynames)
            if len(elements_arr) == 0:
                break
            min_el = min(elements_arr, key=lambda _: elements_arr[_])
            out_array.append(elements_arr[min_el])
            file.write(str(elements_arr[min_el]) + " ")
            other = open(min_el, 'r+')
            b = other.readlines()
            other.close()
            data = [x for x in b[0].split(' ') if x]
            data.remove(str(elements_arr[min_el]))
            other = open(min_el, 'w')
            for num in data:
                other.write(num + " ")
            other.close()
    return out_array
