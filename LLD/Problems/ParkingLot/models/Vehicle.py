class Vehicle:
    def __init__(self, license: str, vehicleType: str) -> None:
        self._license = license
        self._vehicle_type = vehicleType
        self._parking_ticket = None

    def assign_ticket(self, parkingTicket):
        self._parking_ticket = parkingTicket