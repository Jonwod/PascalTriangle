def pascal_triangle(depth):
    """ Returns a list of rows of numbers in the triangle, from small to large"""
    triangle = [[1]]
    for _ in range(0, depth):
        prev_row = triangle[-1]
        this_row = []
        this_row.append(1)
        for x in range(0, len(prev_row) - 1):
            this_row.append(prev_row[x] + prev_row[x+1])
        this_row.append(1)
        triangle.append(this_row)
    return triangle


def print_triangle(triangle):
    # A 'cell' either contains a number, or space.
    # The triangle will be correctly formatted as long as the maximum number
    # of digits in a number is <= cell_width
    cell_width = 3
    def make_cell(num):
        s = str(num)
        while len(s) < cell_width:
            if len(s) % 2 == 0:
                s = s + ' '
            else:
                s = ' ' + s
        return s

    empty_cell = ''.join([' ']*cell_width)
    base_cells = 2 * len(triangle[-1]) - 1
    for row in triangle:
        row_cells = 2 * len(row) - 1
        side_space = int(base_cells - row_cells / 2)
        cells = [empty_cell]*side_space
        for x in range(0, len(row)):
            cells.append(make_cell(row[x]))
            if x < len(row) - 1:
                cells.append(empty_cell)        
        cells.extend([' ']*side_space)
        print(''.join(cells))


p_tri = pascal_triangle(11)
print_triangle(p_tri)