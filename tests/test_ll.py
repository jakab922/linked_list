import linked_list as ll


def test_inits_correctly():
    s = ll.LL(data=1, nxt=2)
    assert s.data == 1 and s.nxt == 2
    s = ll.LL(1, 2)
    assert s.data == 1 and s.nxt == 2


def test_deletes_correctly():
    s = ll.LL(1, 2)
    s.delete()
    assert s.nxt is None and s.data is None

