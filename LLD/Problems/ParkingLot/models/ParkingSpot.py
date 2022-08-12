import uuid
from enums.ParkingSpotType import ParkingSpotType
from models.Vehicle import Vehicle

'''
    TODO: Extend for diferrent types of parking spots
'''

PARKING_SPOT_PRICES = {
    ParkingSpotType.TWO_WHEELER: 0.05,
    ParkingSpotType.SEDAN: 0.075,
    ParkingSpotType.MEDIUM: 0.09,
    ParkingSpotType.LARGE: 0.10,
}

class ParkingSpot:
    def __init__(self, parking_type: str) -> None:
        self._id = uuid.uuid4()
        self._parking_type = parking_type
        self._is_free = True
        self._assigned_vehicle = None
    
    @property
    def is_free(self) -> bool:
        return self._is_free
    
    def assign_vehicle(self, vehicle: Vehicle) -> None:
        self._assigned_vehicle = vehicle
        self._is_free = False
    
    def remove_vehicle(self) -> None:
        self._assigned_vehicle = None
        self._is_free = True

    def get_price(self, parkingType: str, duration: int) -> float:
        return PARKING_SPOT_PRICES[parkingType]*duration