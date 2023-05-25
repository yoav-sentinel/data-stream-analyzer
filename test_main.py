import io

import pytest

from top_x_uids import main


def test_valid_arguments_sanity(capsys, tmp_path):
    file = tmp_path / "input.txt"
    file.write_text("UID1 1.0\nUID2 2.0\n")
    main(['2', '-f', str(file)])
    captured = capsys.readouterr()
    print(captured.out)
    assert "UID1\nUID2" in captured.out


def test_missing_required_arguments(capsys):
    with pytest.raises(SystemExit) as e:
        main([])
    captured = capsys.readouterr()
    assert "error: the following arguments are required: x" in captured.err
    assert e.type == SystemExit
    assert e.value.code == 2


def test_invalid_x_argument(capsys):
    with pytest.raises(SystemExit) as e:
        main(['not_a_number'])
    captured = capsys.readouterr()
    assert "error: argument x: invalid int value" in captured.err
    assert e.type == SystemExit
    assert e.value.code == 2


def test_negative_x_argument(capsys):
    with pytest.raises(SystemExit) as e:
        main(['-1'])
    captured = capsys.readouterr()
    assert "error: x must be a positive number." in captured.out
    assert e.type == SystemExit
    assert e.value.code == 2


def test_nonexistent_file(capsys):
    with pytest.raises(SystemExit) as e:
        main(['10', '-f', 'nonexistent.txt'])
        # Check the output
    captured = capsys.readouterr()
    assert "error: file nonexistent.txt not found." in captured.out
    assert e.type == SystemExit
    assert e.value.code == 2


def test_no_file_and_no_input_stream(monkeypatch, capsys):
    monkeypatch.setattr('sys.stdin', io.StringIO(''))
    main(['10'])
    captured = capsys.readouterr()
    assert 'No input lines found.' in captured.out
