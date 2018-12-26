import pytest

import aoc.day_20 

TEST_EXAMPLES = (
    ('^WNE$', 3),
    ('^ENWWW(NEEE|SSE(EE|N))$', 10),
    ('^ENNWSWW(NEWS|)SSSEEN(WNSE|)EE(SWEN|)NNN$', 18),
    ('^ESSWWN(E|NNENN(EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)))$', 23),
    ('^WSSEESWWWNW(S|NENNEEEENN(ESSSSW(NWSW|SSEN)|WSWWN(E|WWS(E|SS))))$', 31),
)

@pytest.mark.parametrize('input_,expected', TEST_EXAMPLES)
def test_example_01(input_,expected):
    actual = aoc.day_20.route_lengths(input_[1:-1])

    assert max(actual) == expected
