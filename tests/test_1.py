import pytest
import t170222.answer as tan


@pytest.fixture
def folders():
    f = tan.read_file('./tests/example.json')
    return f


def test_1(folders):
    assert isinstance(folders, list)


def test_2(folders):
    res = tan.struct_to_list(folders)
    assert len(res) == 3


def test_3(folders):
    res = tan.struct_to_list(folders)
    assert res[0] == ('another_file', ['folder_1'])


def test_4(folders):
    res = tan.struct_to_list(folders)
    assert res[2] == ('file2', ['folder_1', 'inner_folder'])
