import io

import pytest

from top_x_uids import validate_input_line, find_top_x_uids


def test_empty_input():
    file = io.StringIO('')
    result = find_top_x_uids(file, 5)
    assert result == 'No input lines found.'


def test_single_line_input_sanity():
    file = io.StringIO('123456 10')
    result = find_top_x_uids(file, 5)
    assert result == '123456'


def test_multiple_lines_input_sanity():
    file = io.StringIO('123456 10\n123457 20\n123458 30')
    result = find_top_x_uids(file, 2)
    assert result == '123457\n123458'


def test_non_numeric_value_input():
    file = io.StringIO('123456 abc')
    with pytest.raises(ValueError) as e:
        validate_input_line(file.readline())
    assert "error: not numeric value" in e.value.args[0]


def test_malformed_line_input_missing_value():
    file = io.StringIO('123456')
    with pytest.raises(ValueError) as e:
        validate_input_line(file.readline())
    assert "error: malformed input line" in e.value.args[0]


def test_malformed_line_input_extra_value():
    file = io.StringIO('123456 10 111')
    with pytest.raises(ValueError) as e:
        validate_input_line(file.readline())
    assert "error: malformed input line" in e.value.args[0]


def test_negative_values():
    file = io.StringIO('123 -1\n456 -2\n789 -3')
    result = find_top_x_uids(file, 2)
    assert result == '456\n123'


def test_x_bigger_than_file():
    file = io.StringIO('123456 10\n123457 20\n123458 30')
    result = find_top_x_uids(file, 10)
    assert result == '123456\n123457\n123458'
