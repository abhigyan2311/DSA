class Address:
    def __init__(self, country: str, state: str, city: str, street: str, pincode: str) -> None:
        self._country = country
        self._state = state
        self._city = city
        self._street = street
        self._pincode = pincode