import collections
import datetime 
import operator
import re
import sys

import aoc.util

ShiftRecord = collections.namedtuple('ShiftRecord', 'guard_id timestamp is_awake')

shift_record_regex = re.compile(r'\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2})\] (.*)')
guard_id_regex = re.compile(r'.* #(\d+) .*')


def parse_timestamp(timestamp):
    """Parse the timestamp from the log line.

    Args:
        timestamp (str):

    Returns:
        datetime.datetime

    """

    return datetime.datetime.strptime(timestamp, r'%Y-%m-%d %H:%M')


def parse_shift_record(record_str):
    """Parse the shift record log line.

    Args:
        record_str (str):

    Returns:
        ShiftRecord

    """

    _, timestamp, activity, _ = shift_record_regex.split(record_str)

    if activity == 'falls asleep':
        guard_id = None
        is_awake = False
    elif activity == 'wakes up':
        guard_id = None
        is_awake = True
    else:
        guard_id = int(*guard_id_regex.findall(activity))
        is_awake = True

    return ShiftRecord(
        guard_id, 
        parse_timestamp(timestamp), 
        is_awake
    )


def get_shift_records(lines):
    """Yield the each shift record from the log.

    Args:
        lines (:obj:`list` of :obj:`str`): Lines of the shift log.

    Yields:
        ShiftRecord

    """

    shift_records = iter(parse_shift_record(line) for line in lines)
    shift_records = iter(sorted(shift_records, key=operator.attrgetter('timestamp')))

    def iter_shift_record(records, guard_id=None):
        try:
            record = next(records)
        except StopIteration:
            pass
        else:
            if record.guard_id is not None:
                yield from iter_shift_record(records, record.guard_id)
            else:
                yield record._replace(guard_id=guard_id)
                yield from iter_shift_record(records, guard_id)

    yield from iter_shift_record(shift_records)


def get_guard_minutes_alseep(records):
    """Return the number of minutes each guard spent asleep during their shift.

    Args:
        records (:obj:`iterable` of ShiftRecord)

    Returns:
        dict (int: int): guard id: number of minutes spent asleep

    """

    result = collections.Counter()

    def record_nap(guard_id, duration_of_nap):
        result[guard_id] += duration_of_nap
        return result[guard_id]

    records = iter(records)

    while True:
        try:
            asleep = next(records)
            awake = next(records)
        except StopIteration:
            break

        nap = awake.timestamp.minute - asleep.timestamp.minute
        guard_id = awake.guard_id 

        result[guard_id] += nap
        
    return result


def get_guard_minute_by_minute(records):
    """Record the minute by minute state of each guard.

    Args:
        records (:obj:`iterable` of ShiftRecord)

    Returns:
        dict (int: dict(int: bool)): guard id: minute: awake/asleep

    """

    result = collections.defaultdict(collections.Counter)

    records = iter(records)
    
    while True:
        try:
            asleep = next(records)
            awake = next(records)
        except StopIteration:
            break

        asleep_during = range(asleep.timestamp.minute, awake.timestamp.minute)
        guard_id = awake.guard_id 
        result[guard_id].update(asleep_during)

    return result 


def answer_part_01(records=None):
    """Find the minute the guard who is asleep the most is usually asleep."""

    if records is None:
        input_ = aoc.util.get_puzzle_input(4)
        records = list(get_shift_records(input_))

    minutes_asleep = get_guard_minutes_alseep(records)
    [[guard_id, __]] = minutes_asleep.most_common(1)

    usually_asleep_at = get_guard_minute_by_minute(records)
    [[minute, __]] = usually_asleep_at[guard_id].most_common(1)

    return guard_id, minute
    

def answer_part_02(records=None):
    """Find the minute any guard is asleep the most."""

    if records is None:
        input_ = aoc.util.get_puzzle_input(4)
        records = list(get_shift_records(input_))

    usually_asleep_at = get_guard_minute_by_minute(records)

    asleep_the_most_at = {
        id_: max(asleep_at.items(), key=operator.itemgetter(1))
        for id_, asleep_at in usually_asleep_at.items()
    }

    guard_id = max(asleep_the_most_at, key=lambda g: asleep_the_most_at[g][1])
    minute = asleep_the_most_at[guard_id][0]

    return guard_id, minute


def main():
    sys.setrecursionlimit(5000)

    guard_id, minute = answer_part_01()
    answer_01 = guard_id * minute 
    print(f"Part one: {guard_id} * {minute} = {answer_01}")

    guard_id, minute = answer_part_02()
    answer_02 = guard_id * minute
    print(f"Part two: {guard_id} * {minute} = {answer_02}")


if __name__ == "__main__":
    main()
