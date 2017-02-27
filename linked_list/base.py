class LLBase(object):
    data, nxt = None, None

    def delete(self):
        self.data = None
        self.nxt = None

    def __str__(self):
        return str(self.data)

