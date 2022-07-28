def williams_sort(sorting_array, sorting_func=lambda a, b: a < b):
    array_len = len(sorting_array)
    tree_len = 0

    current_element_index = 0
    while tree_len < array_len:
        # поместить в дерево
        tree_len += 1
        current_element_index = tree_len - 1
        # починить дерево
        while True:
            if current_element_index == 0:
                break
            # если текущий элемент больше
            elif sorting_func(sorting_array[(current_element_index - 1) // 2], sorting_array[current_element_index]):
                sorting_array[(current_element_index - 1) // 2], sorting_array[current_element_index] = \
                    sorting_array[current_element_index], sorting_array[(current_element_index - 1) // 2]
                current_element_index = (current_element_index - 1) // 2
            else:
                break

    while tree_len > 0:
        # берем первый элемент и меняем с последним, уменьшая длину дерева
        sorting_array[0], sorting_array[tree_len - 1] = sorting_array[tree_len - 1], sorting_array[0]
        tree_len -= 1

        # чиним дерево
        current_element_index = 0
        while True:
            # если находимся внизу дерева
            # тоесть если следующий переход выкинет нас из дерева
            if current_element_index * 2 + 1 > tree_len - 1:
                break

            # если левая ветка больше
            elif sorting_func(sorting_array[current_element_index], sorting_array[current_element_index * 2 + 1]):

                # если существует правая ветка and правая больше левой
                if current_element_index * 2 + 2 < tree_len and \
                        sorting_func(sorting_array[current_element_index * 2 + 1],
                                     sorting_array[current_element_index * 2 + 2]):
                    sorting_array[current_element_index * 2 + 2], sorting_array[current_element_index] = \
                        sorting_array[current_element_index], sorting_array[current_element_index * 2 + 2]
                    current_element_index = current_element_index * 2 + 2

                # если правой ветки нет или левая больше (или равна) правой
                else:
                    sorting_array[current_element_index * 2 + 1], sorting_array[current_element_index] = \
                        sorting_array[current_element_index], sorting_array[current_element_index * 2 + 1]
                    current_element_index = current_element_index * 2 + 1

            # если существует правая ветка и она больше текущей
            elif current_element_index * 2 + 2 < tree_len and \
                    sorting_func(sorting_array[current_element_index], sorting_array[current_element_index * 2 + 2]):
                sorting_array[current_element_index * 2 + 2], sorting_array[current_element_index] = \
                    sorting_array[current_element_index], sorting_array[current_element_index * 2 + 2]
                current_element_index = current_element_index * 2 + 2
            # иначе дальше опускать не нужно
            else:
                break
    return sorting_array


if __name__ == '__main__':
    a = [1, 5, 4, 3, 6, 7, 8, 8, 9, 0]
    print(a)
    print(williams_sort(a))
