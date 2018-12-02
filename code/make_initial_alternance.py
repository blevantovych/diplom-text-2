def make_initial_alternance(x, degree):
    alternance = [x[0]]  # add first
    busy = []
    for i in range(degree):
        rand_index = np.random.randint(1, len(x) - 1)
        while rand_index in busy:
            rand_index = np.random.randint(1, len(x) - 1)
        busy.append(rand_index)
        alternance.append(x[rand_index])
    alternance.append(x[len(x) - 1])  # add last
    alternance.sort()
    return alternance
