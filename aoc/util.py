import os 


def get_puzzle_input(day):
    """Return the input of the puzzle.
    
    Args:
        day (int): The number of the puzzle.

    Returns:
        :obj:`list` of :obj:`str`

    """

    file_name = 'day_{0:02d}.dat'.format(day)
    file_path = os.path.join(os.path.dirname(__file__), '..', 'data', file_name)

    with open(file_path, 'r') as fp:
        input_ = fp.readlines()
        
    return list(map(str.strip, input_))
