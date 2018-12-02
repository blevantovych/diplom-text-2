def pol(t, degree, f_discrete):
    x = Symbol('x')
    e = Symbol('e')
    vars_str = ' '.join(['a' + str(i) for i in range(degree + 1)])
    variables = symbols(vars_str)
    eqs = []

    for i in range(degree + 2):
        eqs.append(make_eq(variables, t[i], f_discrete(t[i])) + e)
        e *= -1
    if degree % 2 == 1:
        e *= -1

    solution = solve(eqs, variables + (e,))

    error_on_iteration = solution[e]
    polynom = x - x
    for i, v in enumerate(variables):
        polynom += solution[v] * x ** i

    return [polynom, error_on_iteration]
