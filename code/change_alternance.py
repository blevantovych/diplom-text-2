def change_alternance(err_func, alternance, x_vals):
    x_err = x_of_max_error(err_func, x_vals)
    temp = alternance[:]
    temp.append(x_err)
    temp.sort()
    index_of_x_err = temp.index(x_err)
    if index_of_x_err != 0 and index_of_x_err != (len(temp) - 1):
        if sign(err_func(temp[index_of_x_err])) == sign(err_func(temp[index_of_x_err - 1])):
            del temp[index_of_x_err - 1]

        else:
            del temp[index_of_x_err + 1]

    elif index_of_x_err == 0:
        if sign(err_func(temp[index_of_x_err])) == sign(err_func(temp[1])):
            del temp[1]
        else:
            del temp[len(temp) - 1]
    elif index_of_x_err == (len(temp) - 1):
        if sign(err_func(temp[index_of_x_err])) == sign(err_func(temp[index_of_x_err - 1])):
            del temp[index_of_x_err - 1]
        else:
            del temp[0]
    return temp
