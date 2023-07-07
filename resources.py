def field_reset():
    global field
    field = [[' ']]
    for i in range(9):
        field.append(field[0] * 10)
    for i in range(9):
        field[0].append(field[0][0])

    pass

opposites = [
    ('8', '5'),
    ('8', '2'),
    ('4', '6'),
    ('6', '4'),
    ('2', '8'),
    ('5', '8'),
    ]

