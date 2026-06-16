class Car:
    def __init__(self, max_speed, unit):
        """
        Initializes the Car with a max speed and a unit (km/h or mph).
        """
        self.max_speed = max_speed
        self.unit = unit

    def __str__(self):
        """
        Returns the formatted string representation for the Car.
        """
        return f"Car with the maximum speed of {self.max_speed} {self.unit}"


class Boat:
    def __init__(self, max_speed):
        """
        Initializes the Boat with a max speed in knots.
        """
        self.max_speed = max_speed

    def __str__(self):
        """
        Returns the formatted string representation for the Boat.
        """
        return f"Boat with the maximum speed of {self.max_speed} knots"
