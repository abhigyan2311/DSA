import time
from enums.VehicleType import VehicleType
from models.Vehicle import Vehicle
from enums.ParkingSpotType import ParkingSpotType
from models.ParkingSpot import ParkingSpot
from models.Address import Address
from services.ParkingLot import ParkingLot

parking_lot_name = "Abhigyan's Parking Lot"
address = Address("India", "UP", "Noida", "Cleo", "201301")

parkingLot = ParkingLot(parking_lot_name, address)

# Level 0
parkingFloor1 = parkingLot.add_parking_floor("LVL0")
parkingSpot1 = ParkingSpot(ParkingSpotType.TWO_WHEELER)
parkingSpot2 = ParkingSpot(ParkingSpotType.TWO_WHEELER)
parkingSpot3 = ParkingSpot(ParkingSpotType.TWO_WHEELER)
parkingFloor1.add_parking_spot(parkingSpot1)
parkingFloor1.add_parking_spot(parkingSpot2)
parkingFloor1.add_parking_spot(parkingSpot3)

# Level 1
parkingFloor2 = parkingLot.add_parking_floor("LVL1")
parkingSpot4 = ParkingSpot(ParkingSpotType.SEDAN)
parkingSpot5 = ParkingSpot(ParkingSpotType.SEDAN)
parkingSpot6 = ParkingSpot(ParkingSpotType.SEDAN)
parkingFloor2.add_parking_spot(parkingSpot4)
parkingFloor2.add_parking_spot(parkingSpot5)
parkingFloor2.add_parking_spot(parkingSpot6)

# Level 2
parkingFloor3 = parkingLot.add_parking_floor("LVL2")
parkingSpot7 = ParkingSpot(ParkingSpotType.MEDIUM)
parkingSpot8 = ParkingSpot(ParkingSpotType.MEDIUM)
parkingSpot9 = ParkingSpot(ParkingSpotType.MEDIUM)
parkingFloor3.add_parking_spot(parkingSpot7)
parkingFloor3.add_parking_spot(parkingSpot8)
parkingFloor3.add_parking_spot(parkingSpot9)

# Level 3
parkingFloor4 = parkingLot.add_parking_floor("LVL3")
parkingSpot10 = ParkingSpot(ParkingSpotType.LARGE)
parkingSpot11 = ParkingSpot(ParkingSpotType.LARGE)
parkingSpot12 = ParkingSpot(ParkingSpotType.LARGE)
parkingFloor4.add_parking_spot(parkingSpot10)
parkingFloor4.add_parking_spot(parkingSpot11)
parkingFloor4.add_parking_spot(parkingSpot12)

# Vehicle 1
v1 = Vehicle("UP16123", VehicleType.TWO_WHEELER)
v2 = Vehicle("UP16456", VehicleType.TWO_WHEELER)
v3 = Vehicle("UP16678", VehicleType.TWO_WHEELER)

ticket1 = parkingLot.assign_ticket(v1)
ticket2 = parkingLot.assign_ticket(v2)
ticket3 = parkingLot.assign_ticket(v3)

time.sleep(1)

print(f"Vehicle: {ticket1._issued_for._license} - Amount to Pay: {parkingLot.pay_ticket(ticket1)}")
print(f"Vehicle: {ticket2._issued_for._license} - Amount to Pay: {parkingLot.pay_ticket(ticket2)}")
print(f"Vehicle: {ticket3._issued_for._license} - Amount to Pay: {parkingLot.pay_ticket(ticket3)}")

