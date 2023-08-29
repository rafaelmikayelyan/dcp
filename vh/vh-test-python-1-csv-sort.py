def sort_csv_columns(csv_data: str) -> str:
    lines = csv_data.splitlines()
    output = ''
    list_of_strings = []

    for i in lines:
      list_of_strings.append(i.split(','))

    col_length = len(list_of_strings)    
    row_length = len(list_of_strings[0])
    
    if row_length < 2:
      return csv_data

    sequence = sorted((name.lower(), index) for index, name in enumerate(list_of_strings[0]))
    
    for i in range(col_length):
      output += add_in_sequence(sequence, list_of_strings[i], row_length, i == 0)

    return output


def add_in_sequence(sequence: tuple, line: list, row_length: int, first_row: bool) -> str:
    string = ''
    
    if not first_row:
      string += '\n'

    for i in range(row_length):
      string += line[sequence[i][1]]
      
      if i < row_length - 1:
        string += ','

    return string
