def funct(x):
    return x + 1


def test_first():
    assert funct(2) == 3


def test_temppath(tmp_path):
    print(tmp_path)