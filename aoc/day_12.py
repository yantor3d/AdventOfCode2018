import aoc.util 


def parse_input(lines):
    lines = iter(lines)

    initial_state = next(lines)
    initial_state = initial_state.split(':')[-1].strip()
    state = dict(enumerate(initial_state))

    rules = {}

    # Skip blank line 
    next(lines)

    for line in lines:
        key, __, value = line.partition(' => ')

        rules[tuple(key)] = value

    return state, rules 


def evaluate(state):
    result = 0

    for n in sorted(state):
        if state[n] == '#':
            result += n 

    return result 


def tick(state, rules):
    old_state = state 
    n = min(old_state)
    old_state[n - 1] = '.'
    old_state[n - 2] = '.'
    n = max(old_state)
    old_state[n + 1] = '.'
    old_state[n + 2] = '.'
    new_state = dict(old_state)

    for n in sorted(old_state):
        rule = (
            old_state.get(n - 2, '.'), 
            old_state.get(n - 1, '.'),
            old_state.get(n + 0, '.'),
            old_state.get(n + 1, '.'),
            old_state.get(n + 2, '.'),
        )

        new_state[n] = rules.get(rule, '.')
        new_state.setdefault(n - 2, '.')
        new_state.setdefault(n - 1, '.')
        new_state.setdefault(n + 0, '.')
        new_state.setdefault(n + 1, '.')
        new_state.setdefault(n + 2, '.')

    return new_state


def answer_day_01():
    """After 20 generations, what is the sum of the numbers of all pots which contain a plant?"""

    puzzle_input = aoc.util.get_puzzle_input(12)
    state, rules = parse_input(puzzle_input)

    for _ in range(20):
        state = tick(state, rules)

    answer = evaluate(state)

    print(f'Part one: {answer}')


def answer_day_02():
    """After fifty billion (50000000000) generations, 
    what is the sum of the numbers of all pots which contain a plant?
    
    """

    puzzle_input = aoc.util.get_puzzle_input(12)
    state, rules = parse_input(puzzle_input)

    last_answer = 0
    deltas = []

    num_iterations = 50000000000

    for i in range(1, num_iterations + 1):
        state = tick(state, rules)
        answer = evaluate(state)

        delta = answer - last_answer
        deltas.append(delta)

        if len(deltas) > 10:
            if len(set(deltas[-10:])) == 1:
                answer = answer + (delta * (num_iterations - i))
                print("Cycle detected after", i, "iterations")
                break

        last_answer = answer 
    else:
        answer = evaluate(state)

    print(f'Part two: {answer}')


def main():
    answer_day_01()
    answer_day_02()


if __name__ == "__main__":
    main()
