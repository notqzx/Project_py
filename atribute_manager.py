def add_attribute(rows, value, func):
    for row in rows:
        row[value] = func(row)