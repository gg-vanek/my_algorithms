def quik_sort(a, sorting_func=lambda a, b: a < b, sort_start=0, sort_end=-1):

    if sort_end == -1:
        sort_end = len(a) - 1

    if sort_start >= sort_end:
        return

    main_pointer = sort_start
    help_pointer = sort_end

    while main_pointer != help_pointer:
        if help_pointer > main_pointer:
            if sorting_func(a[main_pointer], a[help_pointer]):
                help_pointer -= 1
            else:
                a[main_pointer], a[help_pointer] = a[help_pointer], a[main_pointer]
                main_pointer, help_pointer = help_pointer, main_pointer
                help_pointer += 1
        elif help_pointer < main_pointer:
            if sorting_func(a[help_pointer], a[main_pointer]):
                help_pointer += 1
            else:
                a[main_pointer], a[help_pointer] = a[help_pointer], a[main_pointer]
                main_pointer, help_pointer = help_pointer, main_pointer
                help_pointer -= 1

    if main_pointer != 0:
        quik_sort(a, sorting_func, sort_start=sort_start, sort_end=main_pointer-1)
    if main_pointer != len(a) -1:
        quik_sort(a, sorting_func, sort_start=main_pointer+1, sort_end=sort_end)

    return a

if __name__ == '__main__':
    a = [5, 0, 3, 8, 0, 9, 100, 234234, -1, -100]
    print(a)
    quik_sort(a)
    print(a)
