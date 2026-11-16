from statistics import mean, median
from dataset_helpers import apply_aggregations

def describe_values(rows, values):
    functions = {
        'count': len,
        'mean': mean,
        'median': median,
        'max': max
    }
    ans = apply_aggregations(rows, values, functions)
    return ans

def count_unique(rows, value):
    points = set()
    for row in rows:
        points.add(row[value])
    return len(points)

def top_n(rows, value, n):
    def by_field(row):
        return row[value]
    ordered = sorted(rows, key = by_field, reverse=True)
    return ordered[:n]