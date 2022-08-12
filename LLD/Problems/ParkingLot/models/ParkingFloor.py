from typing import Dict

from enums.ParkingSpotType import ParkingSpotType
from enums.VehicleType import VehicleType
from models.Vehicle import Vehicle
from models.ParkingSpot import ParkingSpot

class ParkingFloor:
    def __init__(self, name: str) -> None:
        self._name = name
        self._parking_spots: Dict[ParkingSpotType, Dict[str, ParkingSpot]] = {
            ParkingSpotType.TWO_WHEELER: {},
            ParkingSpotType.SEDAN: {},
            ParkingSpotType.MEDIUM: {},
            ParkingSpotType.LARGE: {},
        }
    
    def add_parking_spot(self, parkingSpot: ParkingSpot):
        self._parking_spots[parkingSpot._parking_type][parkingSpot._id] = parkingSpot
    
    def get_relevant_spot(self, vehicle: Vehicle) -> ParkingSpot:
        vehicle_type = vehicle._vehicle_type
        parking_slot_type = self.get_corrent_parking_spot_type(vehicle_type)
        relevant_parking_slots= self._parking_spots[parking_slot_type]
        relevant_slot = None
        for parking_slot in relevant_parking_slots:
            if relevant_parking_slots[parking_slot]._is_free == True:
                relevant_slot = relevant_parking_slots[parking_slot]
                relevant_slot.assign_vehicle(vehicle)
                break
        return relevant_slot
    
    def get_corrent_parking_spot_type(self, vehicleType: VehicleType) -> ParkingSpotType:
        if vehicleType == VehicleType.TWO_WHEELER: return ParkingSpotType.TWO_WHEELER
        elif vehicleType == VehicleType.SEDAN: return ParkingSpotType.SEDAN
        elif vehicleType == VehicleType.SUV: return ParkingSpotType.MEDIUM
        elif vehicleType == VehicleType.VAN: return ParkingSpotType.LARGE
        return None
    
    # def is_full(self) -> bool:
    #     count = 0
    #     for key in self._parking_spots:
    #         if self._parking_spots[key]: count += len(self._parking_spots[key])
    #     return count == 0