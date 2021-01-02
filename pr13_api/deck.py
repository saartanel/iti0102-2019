"""Deck."""
from typing import Optional, List
import requests
import random


class Card:
    """Simple dataclass for holding card information."""

    def __init__(self, value: str, suit: str, code: str):
        """Constructor."""
        self.value = value
        self.suit = suit
        self.code = code
        self.top_down = False
        self.remaining = 0

    def __str__(self):
        """Str."""
        if not self.top_down:
            return self.code
        if self.top_down:
            return "??"

    def __repr__(self) -> str:
        """Repr."""
        return self.code

    def __eq__(self, o) -> bool:
        """Eq."""
        if isinstance(o, Card) and o.suit == self.suit and o.value == self.value:
            return True


class Deck:
    """Deck."""

    DECK_BASE_API = "https://deckofcardsapi.com/api/deck/"

    def __init__(self, deck_count: int = 1, shuffle: bool = False):
        """Constructor."""
        self._backup_deck = self._generate_backup_pile() * deck_count
        self.deck_count = deck_count
        self.is_shuffled = shuffle
        self.request = None
        self.api_check = False
        self._request(self.DECK_BASE_API)

    def shuffle(self) -> None:
        """Shuffle the deck."""
        requests.get(f"{self.DECK_BASE_API}/{self.deck_id}/shuffle/")

    def draw_card(self, top_down: bool = False) -> Optional[Card]:
        """
        Draw card from the deck.

        :return: card instance.
        """
        if self.api_check and self.deck_id and self.remaining:
            if self.remaining >= 0:
                request = requests.get(f"{self.DECK_BASE_API}{self.deck_id}/draw/?count={self.deck_count}").json()
                if not request["cards"]:
                    return None
                card = request["cards"][0]
                value = card["value"]
                suit = card["suit"]
                code = card["code"]
                # print(f"value: {value}, suit: {suit}, code: {code}")
                self.remaining -= 1
                card = Card(value, suit, code)
                self._backup_deck.remove(card)
                return card
        else:
            if not self._backup_deck:
                return None
            card = random.choice(self._backup_deck)
            self._backup_deck.remove(card)
            self.remaining = len(self._backup_deck)
            return card

    def _request(self, url: str) -> dict:
        """Update deck."""
        try:
            self.request = requests.get(f"{url}new/")
        except requests.exceptions.ConnectionError as e:
            print(e)
        if self.request is not None and self.request.status_code == requests.codes.ok:
            self.api_check = True
            self.result = requests.get(f"{url}new/?deck_count={self.deck_count}").json()
            if self.is_shuffled:
                self.result = requests.get(f"{url}new/shuffle/?deck_count={self.deck_count}").json()
            self.deck_id = self.result.get("deck_id", None)
            self.remaining = self.result.get("remaining", None)
            return self.result
        else:
            self.remaining = len(self._backup_deck)

    @staticmethod
    def _generate_backup_pile() -> List[Card]:
        """Generate backup pile."""
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'JACK', 'QUEEN', 'KING', 'ACE']
        suits = ['SPADES', 'DIAMONDS', 'HEARTS', 'CLUBS']
        backup_deck = []
        for suit in suits:
            for value in values:
                if value == "10":
                    code = f"0{suit[0]}"
                    backup_deck.append(Card(value, suit, code))
                else:
                    backup_deck.append(Card(value, suit, f"{value[0]}{suit[0]}"))
        return backup_deck


if __name__ == '__main__':
    d = Deck(shuffle=True, deck_count=2)
    print(d._backup_deck)
