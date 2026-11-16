def filter_rows(rows, condition):
    filtered = []
    for row in rows:
        if condition(row):
            filtered.append(row)
    return filtered

def group_by_attributes(rows, values):
    groups = {}
    for row in rows:
        group_values = []
        for value in values:
            group_values.append(row[value])
        group_key = tuple(group_values)
        if group_key not in groups:
            groups[group_key] = []
        groups[group_key].append(row)
    return groups

def apply_aggregations(rows, values , functions):
    points = []
    ans = {}
    for row in rows:
        points.append(row[values])
    for func in functions:
        ans[func] = functions[func](points)
    return ans