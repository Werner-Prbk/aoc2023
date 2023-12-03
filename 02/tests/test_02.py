from main import *

def test_parse_gameid():
    res = parse_line("Game 1: 1 blue")
    assert res["gameId"] == 1

    res = parse_line("Game 10: 1 blue")
    assert res["gameId"] == 10

def test_parse_sets():
    res = parse_line("Game 1: 1 blue, 2 yellow; 9 blue, 8 green")
    assert res["sets"][0] != None
    assert res["sets"][0]["blue"] == 1
    assert res["sets"][0]["yellow"] == 2
    assert res["sets"][1] != None
    assert res["sets"][1]["blue"] == 9
    assert res["sets"][1]["green"] == 8

def test_possible():
    line = parse_line("Game 119: 1 blue, 2 yellow; 9 blue, 8 green")
    res = get_possible_games([line], {"blue" : 1, "yellow" : 2, "green" : 8})
    assert len(res) == 0

    res = get_possible_games([line], { "blue" : 9, "yellow" : 2, "green" : 8})
    assert len(res) == 1
    assert res[0] == 119

    res = get_possible_games([line], { "blue" : 10, "yellow" : 2, "green" : 8})
    assert len(res) == 1

    res = get_possible_games([line], { "blue" : 10, "yellow" : 2, "green" : 8, "unknown" : 3})
    assert len(res) == 1