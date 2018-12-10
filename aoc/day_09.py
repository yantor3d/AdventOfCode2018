"""Advent of Code 2018 day 09 - https://adventofcode.com/2018/day/9"""

import itertools 
import re
import time 

import aoc.util 

"""
Rules:
In turn, each player takes the next lowest numbered marble.

If the marble has a number that is a multiple of 23:
    The current player keeps the marble and adds it to their score.

    The current player also removes the marble 7 marbles counter-clockwise from
    the current marble from the circle and adds it to their score.

    The marble located immediately clockwise from the marble that was removed 
    becomes the current marble.

Otherwise:
    The current player puts the marble in the circle between the marbles that 
    are 1 and 2 marbles clockwise of the current marble. This marble becomes the
    current marble.

"""

CLOCKWISE = 0
COUNTER_CLOCKWISE = -1

PUZZLE_INPUT_REGEX = re.compile(r"(\d*) players; last marble is worth (\d*) points")


class CircleOfMarbles(object):
    """A linked list within a dict, anyone?"""

    def __init__(self, last_marble_worth):
        self.marbles = {m: [None, None] for m in range(last_marble_worth + 1)}

        self.marbles[0] = [0, 0]
        self.current_marble = 0 

        self.number_of_marbles_in_circle = 1

    def __len__(self):
        return self.number_of_marbles_in_circle

    def get_marble(self, m, n=1, direction=CLOCKWISE):
        """Get the marble a certain number of marbles away from the given marble.

        Args:
            m (int): Value of the marble
            n (int): Number of marbles to traverse
            direction (int): Direction of the traversal 
                -  0 clockwise
                - -1 counter clockwise)
        
        Returns:
            int 

        """

        if n == 0:
            return m 
        
        m = self.marbles[m][direction]
        return self.get_marble(m, n - 1, direction)

    def place_marble(self, marble):
        """Place the given marble in the circle.

        Args:
            marble (int): The worth of the marble.

        """

        marble_one = self.get_marble(self.current_marble, 1)
        marble_two = self.get_marble(self.current_marble, 2) 

        m0 = marble 
        m1 = marble_one
        m2 = marble_two

        self.marbles[m0] = [m2, m1]
        self.marbles[m1][CLOCKWISE] = m0
        self.marbles[m2][COUNTER_CLOCKWISE] = m0

        self.current_marble = marble
        self.number_of_marbles_in_circle += 1

    def remove_marble(self):
        """Return 7 marbles counter-clockwise from the current marble.

        Returns:
            int

        """

        marble = self.get_marble(self.current_marble, 7, COUNTER_CLOCKWISE)

        m = marble 
        n = self.get_marble(marble, 1, CLOCKWISE)
        p = self.get_marble(marble, 1, COUNTER_CLOCKWISE)

        self.marbles[m] = [None, None]
        self.marbles[n][COUNTER_CLOCKWISE] = p 
        self.marbles[p][CLOCKWISE] = n

        self.current_marble = n
        self.number_of_marbles_in_circle -= 1

        return m



def parse_input(line):
    [(number_of_players, last_marble_worth)] = PUZZLE_INPUT_REGEX.findall(line)

    return int(number_of_players), int(last_marble_worth)


def play_game(number_of_players, last_marble_worth):
    """Play the marble game and return the high score."""

    scores = {n: 0 for n in range(1, number_of_players + 1)}

    circle_of_marbles = CircleOfMarbles(last_marble_worth)
    marbles = itertools.islice(itertools.count(), 1, last_marble_worth + 1)
    players = itertools.cycle(range(1, number_of_players + 1))

    while True:
        current_player = next(players)

        try:
            marble = next(marbles)
        except StopIteration:
            break 

        is_multiple_of_twenty_three = marble % 23 == 0

        if is_multiple_of_twenty_three:
            removed_marble = circle_of_marbles.remove_marble()

            scores[current_player] += marble
            scores[current_player] += removed_marble
        else:
            circle_of_marbles.place_marble(marble)

    return max(scores.values())


def answer_part_01():
    """What is the winning Elf's score?"""

    input_, = aoc.util.get_puzzle_input(9)
    number_of_players, last_marble_worth = parse_input(input_)

    start_time = time.time()
    high_score = play_game(number_of_players, last_marble_worth)
    elapsed_time = time.time() - start_time

    print(f'Part one: {high_score} (took {elapsed_time:0.2f} seconds)')


def answer_part_02():
    """What would the new winning Elf's score be if the number of the last 
    marble were 100 times larger?
    
    """

    input_, = aoc.util.get_puzzle_input(9)
    number_of_players, last_marble_worth = parse_input(input_)

    start_time = time.time()
    high_score = play_game(number_of_players, last_marble_worth * 100)
    elapsed_time = time.time() - start_time

    print(f'Part two: {high_score} (took {elapsed_time:0.2f} seconds)')


def main():
    answer_part_01()
    answer_part_02()


if __name__ == "__main__":
    main()
