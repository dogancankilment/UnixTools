def function(size, list):
    save_list = []
    for current in range(0, size):
        if list[current] == 0 and list[current+1] == 0:
            index = current+1
            while list[index] == 0:
                index += 1
                if list[index] == 0:
                    save_list.append(list[index])