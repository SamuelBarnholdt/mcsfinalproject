from measure import measure
from cavegen import generateGrid


def generate_data(N, settings):
    results = []
    r, n, T, M = settings
    for i in range(N):
        results.append(measure(generateGrid(r, n, T, M)))
    return results


def simulate_on_r(N, rvals, nTM):
    results = []
    n, T, M = nTM
    for r in rvals:
        results.append(generate_data(N, (r, n, T, M)))
    return results
