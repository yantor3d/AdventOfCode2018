import aoc.day_04 

TEST_INPUT = (
    "[1518-11-01 00:00] Guard #10 begins shift",
    "[1518-11-01 00:05] falls asleep",
    "[1518-11-01 00:25] wakes up",
    "[1518-11-01 00:30] falls asleep",
    "[1518-11-01 00:55] wakes up",
    "[1518-11-01 23:58] Guard #99 begins shift",
    "[1518-11-02 00:40] falls asleep",
    "[1518-11-02 00:50] wakes up",
    "[1518-11-03 00:05] Guard #10 begins shift",
    "[1518-11-03 00:24] falls asleep",
    "[1518-11-03 00:29] wakes up",
    "[1518-11-04 00:02] Guard #99 begins shift",
    "[1518-11-04 00:36] falls asleep",
    "[1518-11-04 00:46] wakes up",
    "[1518-11-05 00:03] Guard #99 begins shift",
    "[1518-11-05 00:45] falls asleep",
    "[1518-11-05 00:55] wakes up",
)

TEST_DATA = list(aoc.day_04.get_shift_records(TEST_INPUT))


def test_01_guard_time_spent_asleep():
    minutes_alseep = aoc.day_04.get_guard_minutes_alseep(TEST_DATA)

    assert minutes_alseep[10] == 50
    assert minutes_alseep[99] == 30
    

def test_01_minute_guard_is_asleep_the_most_during():
    guard_id, minute = aoc.day_04.answer_part_01(TEST_DATA)

    assert guard_id == 10
    assert minute == 24


def test_02_minute_guard_is_asleep_the_most_during():
    guard_id, minute = aoc.day_04.answer_part_02(TEST_DATA)

    assert guard_id == 99
    assert minute == 45 
