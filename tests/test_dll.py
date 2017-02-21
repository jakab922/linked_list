import linked_list as ll


def test_inits_correctly():
    s = ll.DLL(data=1, prev=2, nxt=3)
    assert s.data == 1 and s.prev == 2 and s.nxt == 3
    s = ll.DLL(1, 2, 3)
    assert s.data == 1 and s.prev == 2 and s.nxt == 3


def test_deletes_correctly():
    s = ll.DLL(1, 2, 3)
    s.delete()
    assert s.data is None and s.nxt is None and s.prev is None

