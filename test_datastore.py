from unittest.mock import mock_open, patch
import datastore

test_db = datastore.DataStore()

test_db.store = []
test_db._counter = 0

def test_create():
    m = mock_open()
    with patch("builtins.open", m):
        test_db.create("test1")

    assert any(item.get("attr") == "test1" for item in test_db.store)

def test_read(capsys):
    test_db.read()

    captured = capsys.readouterr()

    assert captured.out == "[{'id': 0, 'attr': 'test1'}]\n"

def test_update():
    m = mock_open()
    with patch("builtins.open", m):
        index = test_db._itemExists("0")
        test_db.update(index, "test_update")
    
    assert any(item.get("attr") == "test_update" for item in test_db.store)

def test_delete():
    m = mock_open()
    with patch("builtins.open", m):
        index = test_db._itemExists("0")
        test_db.delete(index)
    
    assert len(test_db.store) == 0