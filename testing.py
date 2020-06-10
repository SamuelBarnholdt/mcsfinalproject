from measure import measure
from measurehills import measure_hills
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


def generate_hill_data(N, settings):
    results = []
    r, n, T, M = settings
    for i in range(N):
        results.append(measure_hills(generateGrid(r, n, T, M)))
    return results


def simulate_on_r_hill(N, rvals, nTM):
    results = []
    n, T, M = nTM
    for r in rvals:
        results.append(generate_hill_data(N, (r, n, T, M)))
    return results
