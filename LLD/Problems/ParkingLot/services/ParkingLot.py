from datetime import datetime
from math import ceil
import threading
from typing import  List

from models.ParkingTicket import ParkingTicket
from models.Vehicle import Vehicle
from models.ParkingSpot import ParkingSpot
from models.ParkingFloor import ParkingFloor
from models.Address import Address

class ParkingLot:
    instance = None

    class _OnlyOne:
        def __init__(self, name: str, address: Address) -> None:
            self._name = name
            self._address= address
            self._parking_levels: List[ParkingFloor] = []
            self._lock = threading.Lock()
    
    def __init__(self, name: str, address: Address) -> None:
        # Singleton
        if not ParkingLot.instance:
            ParkingLot.instance = ParkingLot._OnlyOne(name, address)
        else:
            ParkingLot.instance._name = name
            ParkingLot.instance._address = address

    def add_parking_floor(self, name: str) -> ParkingFloor:
        parkingFloor = ParkingFloor(name)
        self.instance._parking_levels.append(parkingFloor)
        return parkingFloor
    
    def remove_parking_floor(self, parkingFloor: ParkingFloor) -> None:
        self.instance._parking_levels.remove(parkingFloor)

    def assign_ticket(self, vehicle: Vehicle) -> ParkingTicket:
        self.instance._lock.acquire()

        parking_spot = self.get_parking_spot_vehicle(vehicle)
        if not parking_spot: 
            self.instance._lock.release()
            raise Exception("Parking is full")

        parking_ticket = self.create_ticket(parking_spot, vehicle)
        self.instance._lock.release()
        return parking_ticket
    
    def pay_ticket(self, parkingTicket: ParkingTicket) -> float:
        self.instance._lock.acquire()

        end_time = datetime.now()
        duration = ceil((end_time - parkingTicket._issued_at).seconds/3600)
        parking_spot = parkingTicket._parking_spot
        
        amount = parking_spot.get_price(parking_spot._parking_type, duration)
        parkingTicket.close_ticket(amount, end_time)
        parking_spot.remove_vehicle()


        self.instance._lock.release()
        return amount

    def get_parking_spot_vehicle(self, vehicle: Vehicle) -> ParkingSpot:
        parking_spot = None
        for parkingFloor in self.instance._parking_levels:
            parking_spot = parkingFloor.get_relevant_spot(vehicle)
            if parking_spot: break
        return parking_spot
    
    def create_ticket(self, parkingSpot: ParkingSpot, vehicle: Vehicle):
        return ParkingTicket(vehicle, parkingSpot)