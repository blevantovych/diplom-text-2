import spline_minmax


def checkIfErrorsOk(specified_precision, approximation, epsilon=0.01):
    for approx in approximation:
        if abs(specified_precision - approx["max_error"]) > epsilon:
            return False
    return True


def main(func, deg, start, end, r):
    mu_left = 0
    mu_right = 0
    prev_specified_precision = 0
    precision = 0.0009
    mu = 0.1

    approximation = spline_minmax.main(func, deg, start, end, precision, mu)
    k = len(approximation)
    while k != r or not checkIfErrorsOk(mu, approximation):
        if k > r:
            mu_left = mu
            if mu_right != 0:
                mu = (mu + mu_right) / 2
            else:
                mu *= 1.1

        if k == r:
            mu_right = mu
            if mu_left != 0:
                mu = (mu + mu_left) / 2
            else:
                mu *= 0.9
        if k < r:
            mu_right = mu
            if mu_left != 0:
                mu = (mu + mu_left) / 2
            else:
                mu *= 0.9

        approximation = spline_minmax.main(func, deg, start, end, precision, mu)

        if len(approximation) == r and abs(prev_specified_precision - mu) < 0.000001:
            return approximation

        prev_specified_precision = mu

        k = len(approximation)

    return approximation
