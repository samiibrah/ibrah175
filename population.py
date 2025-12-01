def population(s, m, b):
    s = 0.1 * s - 0.0002 * s * m
    m = -0.05 * m + 0.0001 * s * m - 0.0025 * m * b
    b = -0.1 * b + 0.0002 * m * b

    return populations
