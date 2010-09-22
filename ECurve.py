# Authors: Pete Jensen, Natasha Mandryk (math)
# Get Ready to Branch
import math

from Point import Point

##
# ECurve
#
# Usage:
# 
# import ECurve
# e7 = ECurve(7, 12, 7)
# print e7
# print e7.points
#
class ECurve:
    def __init__(self, p, a, b):
        # Ensure that the passed value of p is indeed prime.
        if (not self.__isPrime(p)):
            raise BaseException(str(p) + " is not Prime")	

        # Define basic variables, coefficients and prime p.
        # (y^2 mod p) = (x^3 + ax + b) mod p
        self.__a = a # The coefficient: a
        self.__b = b # The coefficient: b
        self.__p = p # The prime p.
        self.__INIFINITY = Point(None, None)

        self.points = [] # Create an array that will contain all Points
                            # on this Curve.

        self.__findPoints() # Find all points on this curve.

        return

    ##
    # isPrime
    # 
    # Determine if the passed value is a prime number.
    def __isPrime(self, aValue):
       # TODO: Mathematically this should start at the sqrt then work it's way up.
       for i in range(1, aValue):
           if (i <> 1) and (i <> aValue):
               if (((aValue * 1.0) / (i * 1.0)) % 1 == 0):
                   return False
       return True

    ##
    # __findPoints
    #
    # The purpose of this method is to determine from (0,0) to (p - 1, p - 1)
    # Currently this is simply a trivial brute force algorithm to find all of
    # the points on the curve.
    #
    # Since as mentioned above, we're checking all points from
    # (0, 0) to (p-1, p-1) the running time of this algorithm is (p - 1) ^ 2
    # Therefore the algorithm is of O(n^2)
    #
    def __findPoints(self):
 
        # Here lies a VERY hacky O(n^2) algorithm to find all points on
        # the given p, a, b : e-curve.
        for x in range(0, self.__p):
            for y in range(0, self.__p):
                if self.onCurve(x, y) == True:
                    self.points.append( Point(x,y) )
 
    ##
    # __str__
    #
    # Returns a basic string representation of the Curve.
    # (e.g) Given, a = 1, b = 1, p = 23; this function returns the string
    # "E_23(1, 1)"
    #
    # @param
    # self - THIS curve.
    #
    # @returns
    # The string representation of this curve.
    def __str__(self):
        return "E_" + str(self.__p) + \
               "(" + str(self.__a) + ", " + str(self.__b) + ")"
 
    def __repr__(self):
        return str(self)
 
    def __inverseSlope(self, n):
        for a in range(0, self.__p):
            if ( (n * a) % self.__p == 1):
                return a
    ##
    # onCurve
    #
    # This method determines weather or not a given (x, y) point IS or
    # is NOT on THIS curve.
    #
    # @param
    # x - The x-coordinate
    # y - The y-coordinate
    #
    # @return
    # A boolean True, yes (x, y) IS on the curve.
    # A boolean False, no (x, y) is NOT on the curve.
    def onCurve(self, x, y):
        return ((y ** 2) % self.__p) ==\
               ((((x ** 3) + self.__a * x + self.__b) % self.__p) )
 
    # Obsolete
    def __specialSlope(self, point):
        return ((3.0 * point.getX() ** 2) + self.__a) * self.__inverseSlope(2 * point.getY())
 
    def addPoints(self, pointP, pointQ):
 
        # Set up an initial value for lamda
        lamda = 0
 
        #
        # Take care of the identity: The case where either or both points are
        # at INFINITY. We handle it here, and return. PERIOD.
        #
        # P + Point(None, None) => P
        # Q + Point(None, None) => Q
        #
        # NOTE: Point(None, None) = self.__INIFINITY
        # lets, call self.__INIFINITY, "INFINITY" for the rest of this note.
        #
        # Lastly: INFINITY + INFINITY => INFINITY
        if (pointP == self.__INIFINITY and pointQ == self.__INIFINITY):
            return self.__INIFINITY
        elif (pointP == self.__INIFINITY):
            if (self.onCurve(pointQ.getX(), pointQ.getY())):
                return pointQ
        elif (pointQ == self.__INIFINITY):
            if (self.onCurve(pointP.getX(), pointP.getY())):
                return pointP
 
        ## We know now, that neither point is @ INFINITY.
 
        # Make sure point P is on the curve.
        if (self.onCurve(pointP.getX(), pointP.getY()) == False):
            raise BaseException("Point: " + str(pointP) + "not on curve.")
 
        # Make sure point Q is on the curve.
        elif (self.onCurve(pointQ.getX(), pointQ.getY()) == False):
            raise BaseException("Point: " + str(pointQ) + "not on curve.")
 
        ## We know here, that both points are indeed ON the curve.
 
        # The next case is when x-coordinates are
        # equal & y-coordinates unequal. We return a point @ INFINITY.
        #
        # x1 == x2 AND y1 <> y2 ==> INFINITY
        if (pointP.getX() == pointQ.getX() and \
            pointP.getY() <> pointQ.getY()):
                return self.__INIFINITY
 
        # (x1, y1) <> (x2, y2)
        if (pointP != pointQ):
 
            # Compute the rise & the run. Numerator & Denominator respectively.
            rise = (pointQ.getY() ) - pointP.getY()
            run = (pointQ.getX() ) - pointP.getX()
 
            # Set the lamda for P <> Q
            lamda = (self.__inverseSlope( run ) * rise)
        else:
            # Set the lamda for P == Q
            lamda = (3 * pointP.getX() ** 2 + self.__a) * self.__inverseSlope(2 * pointP.getY())
 
        x3 = (lamda ** 2.0 - pointP.getX() - pointQ.getX()) % (self.__p)
        y3 = ((lamda * (pointP.getX() - x3) - pointP.getY() ) % self.__p )
 
        # Return the computed point.
        return Point(x3, y3)
