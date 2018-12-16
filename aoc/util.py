import os 


def get_puzzle_input(day, raw=False, suffix=None):
    """Return the input of the puzzle.
    
    Args:
        day (int): The number of the puzzle.
        suffix (str): Optional suffix to add to the data file name

    Returns:
        :obj:`list` of :obj:`str`

    """

    if suffix:
        file_name = 'day_{:02d}.{}.dat'.format(day, suffix)
    else:
        file_name = 'day_{:02d}.dat'.format(day)

    file_path = os.path.join(os.path.dirname(__file__), '..', 'data', file_name)

    with open(file_path, 'r') as fp:
        input_ = fp.readlines()
        
    if raw:
        return [str(line.replace('\n', '')) for line in input_]
    else:
        return list(map(str.strip, input_))
