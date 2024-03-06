class Entry:
    def __init__(self, i_d, title, body):
        """

        :rtype: object
        """
        self.id = i_d
        self.title = title
        self.body = body


    def get_i_d(self):
        return self.id

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, _title):
        self._title = _title

    @property
    def body(self):
        return self._body

    @body.setter
    def body(self, _body):
        self._body = _body

    def __repr__(self):
        return f" {self.title}: {self.body}"
