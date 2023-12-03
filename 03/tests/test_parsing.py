from main import *

def test_find_symbols():
    lines = get_lines("test.txt")
    syms = find_symbols(lines, lambda d: d.isdigit() == False)
    assert len(syms) == 6

def test_find_numbers():
    lines = get_lines("test.txt")
    nums = find_numbers(lines)
    assert len(nums) == 10
