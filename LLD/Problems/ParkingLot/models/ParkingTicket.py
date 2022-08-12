import uuid
from datetime import datetime

from models.ParkingSpot import ParkingSpot
from models.Vehicle import Vehicle

class ParkingTicket:
    def __init__(self, vehicle: Vehicle, parkingSpot: ParkingSpot) -> None:
        self._ticket_id = uuid.uuid4()
        self._issued_at = datetime.now()
        self._issued_for = vehicle
        self._parking_spot = parkingSpot
        self._paid_at = None
        self._amount = 0
        self._status = "ACTIVE"
    
    def close_ticket(self, amount: float, endTime: datetime):
        self._amount = amount
        self._paid_at = endTime
        self._status = "PAID"