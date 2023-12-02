from main import numerize

def test_numerize():
    assert numerize(" ") == ""
    assert numerize("") == ""
    assert numerize("one") == "1"
    assert numerize("1") == "1"
    assert numerize("one1") == "11"
    assert numerize("1one") == "11"
    assert numerize("1one1") == "111"
    assert numerize("k") == ""
    assert numerize("kone") == "1"
    assert numerize("1k") == "1"
    assert numerize("kone1") == "11"
    assert numerize("k1one") == "11"
    assert numerize("1kone1") == "111"
    assert numerize("1konetwo1") == "1121"
    assert numerize("one1two2three3four4five5six6seven7eight8nine90") == "1122334455667788990"
    assert numerize("lone1twoz2threer3four4five5six6sevenr7eight8nine9l0iii") == "1122334455667788990"
    assert numerize("0x27lone1twoz2threer3four4five5six6sevenr7eight8nine9l0iii") == "0271122334455667788990"
    assert numerize("A27lone1twoz2threer3four4five5six6sevenr7eight8nine9l0iii") == "271122334455667788990"
    assert numerize("oneight") == "18"      # wft