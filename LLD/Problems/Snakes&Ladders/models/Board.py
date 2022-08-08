class Board:
    def __init__(self, dimension) -> None:
        self._dimension = dimension
        self._special_entities = dict()
    
    @property
    def total_dimension(self):
        return self._dimension**2

    def add_special_entity(self, entity) -> None:
        self._special_entities[entity.start] = entity

    def has_special_entity(self, position: int) -> bool:
        return position in self._special_entities

    def get_special_entity(self, position):
        if position in self._special_entities:
            return self._special_entities[position]
        return None

    