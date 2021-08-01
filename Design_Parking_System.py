class ParkingSystem(object):
    spots = {}

    def __init__(self, big: int, medium: int, small: int):
        """
        :type big: int
        :type medium: int
        :type small: int
        """
        self.spots[1] = big
        self.spots[2] = medium
        self.spots[3] = small

    def addCar(self, carType):
        """
        :type carType: int
        :rtype: bool
        """
        if self.spots[carType] > 0:
            self.spots[carType] -= 1
            return True
        return False

    #Best discussion solution
    '''
    __slots__ = ['_parking']
	
    def __init__(self, big: int, medium: int, small: int):
        self._parking = {
            1: big, 
            2: medium, 
            3: small
        }

    def addCar(self, carType: int) -> bool:
        available_spots = self._parking[carType]
        if available_spots:
            self._parking[carType] = available_spots - 1
            return True
    '''
        
# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)