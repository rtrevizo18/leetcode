from math import ceil
def minParkingLots(buses: int, cars: int, largeLots: int, smallLots: int):
  if (buses > largeLots):
    return -1
  
  lotsUsed = buses
  largeLotsLeft = largeLots - buses

  maxCarsInLargeLots = min(cars, largeLotsLeft * 3)

  remainingCars = cars - maxCarsInLargeLots

  lotsUsed += ceil(maxCarsInLargeLots / 3)

  if(remainingCars > smallLots):
    return -1
  lotsUsed += remainingCars

  return lotsUsed

# function minParkingLots(buses, cars, largeLots, smallLots) {
#   // Check if we have enough large lots for buses
#   if (buses > largeLots) {
#     return -1;
#   }
#   // Fill up large lots with buses
#   let usedLots = buses;

#   let freeLargeLots = largeLots - buses;
#   let capacityInLargeLots = freeLargeLots * 3;

#   let carsInLargeLots = Math.min(cars, capacityInLargeLots);

#   usedLots += Math.ceil(carsInLargeLots / 3);
#   cars -= carsInLargeLots;

#   if (cars > smallLots) return -1;

#   usedLots += cars;

#   return usedLots;
# }

if __name__ == '__main__':
  result1 = minParkingLots(2, 8, 5, 3)
  result2 = minParkingLots(4, 2, 3, 5)
  result3 = minParkingLots(1, 5, 2, 1)

  assert result1 == 5
  assert result2 == -1
  assert result3 == -1