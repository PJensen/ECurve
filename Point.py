class Point:
    def __init__(self, x, y):
        # Initialize x-coord, y-coord.
        self.__x = x
        self.__y = y

        return

    def getSlope(self, pointB):

        # Make sure the slope isn't undefined.
        if (self.__x == pointB.getX()):
            raise BaseException("Infinite Slope.")

        # y2 - y1        
        rise = pointB.getY() - self.getY()

        # x2 - x1        
        run = pointB.getX() - self.getX()

        # (y2 - y1) / (x2 - x1)        
        return rise / run

    def getPoint(self):

        # Return the tuple representing the point.\
        return (self.__x, self.__y)

    def getX(self):

        # Return the x-coord (only)        
        return self.__x

    def getY(self):

        # Return the y-coord (only)
        return self.__y

    def __getitem__(self, index):
        if index == 0:
            return self.__x
        elif index == 1:
            return self.__y
        else:
            raise BaseException("Index " + str(index) + " out of bounds.")

    def resetX(self, newX):

        # Reset only the x-coordinate.        
        self.__x = newX

    def resetY(self, newY):

        # Reset only the y-coordinate.        
        self.__y = newY

    def resetP(self, newX, newY):

        # Reset both x, y values.
        self.__x = newX
        self.__y = newY

    def __eq__(self, b):
        if self.__x == b.getX() and self.__y == b.getY():
            return True
        else:
            return False

    def __str__(self):

        # Return the tuple (x, y) as a string.
        return str((self.__x, self.__y))

    def __repr__(self):

        # Return the string representation of the point.
        # @See __repr__ from global module index.
        return str(self)
