# Card.py

from .Payment import Payment

class Card(Payment):
    def __init__(self, number: int, cvv: int, owner: str):
        super().__init__()
        self.number = number
        self.cvv = cvv
        self.owner = owner