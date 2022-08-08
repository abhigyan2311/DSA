from interfaces.SpecialEntity import ISpecialEntity

class Snake(ISpecialEntity):
    def __init__(self, start: int, end: int) -> None:
        self._start = start
        self._end = end
        self._type = "SNAKE"
        self._id = "S#" + str(self._end)

    @property
    def start(self):
        return self._start

    @property
    def end(self):
        return self._end

    @property
    def se_id(self):
        return self._id