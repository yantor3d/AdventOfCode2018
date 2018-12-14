import os 


def get_puzzle_input(day, raw=False, test_data=False):
    """Return the input of the puzzle.
    
    Args:
        day (int): The number of the puzzle.
        test_data (bool): If True, return the test data for the puzzle.

    Returns:
        :obj:`list` of :obj:`str`

    """

    if test_data:
        file_name = 'day_{:02d}.{}.dat'.format(day, test_data)
    else:
        file_name = 'day_{:02d}.dat'.format(day)

    file_path = os.path.join(os.path.dirname(__file__), '..', 'data', file_name)

    with open(file_path, 'r') as fp:
        input_ = fp.readlines()
        
    if raw:
        return [str(line.replace('\n', '')) for line in input_]
    else:
        return list(map(str.strip, input_))
