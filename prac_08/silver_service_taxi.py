"""
CP1404/CP5632 Practical
Taxi class
"""
from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Represent a SilverServiceTaxi."""
    FLAGFALL = 4.50

    def __init__(self, name: str = '', fuel: int = 0, fanciness: float = 0):
        """Initialise a SilverServiceTaxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.PRICE_PER_KM *= fanciness

    def __str__(self):
        """Return a string representation of a SilverServiceTaxi."""
        return f"{super().__str__()}, {self.current_fare_distance}, ${self.PRICE_PER_KM:.2f}/km " \
               f"plus flagfall of ${self.FLAGFALL} "

    def get_fare(self):
        """Get the current fare."""
        return self.FLAGFALL + super().get_fare()
