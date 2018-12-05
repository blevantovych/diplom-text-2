def max_error(func, x_vals):
    y_vals = func(x_vals)
    neg_err = min(y_vals)
    pos_err = max(y_vals)

    if abs(neg_err) > pos_err:
        e_max = neg_err
    else:
        e_max = pos_err
    return e_max
