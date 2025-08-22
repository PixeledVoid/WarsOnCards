
import random
from typing import List, Optional


class Card:
    """Represents a playing card with suit and rank."""

    SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    RANK_VALUES = {rank: i for i, rank in enumerate(RANKS, 2)}  # 2=2, 3=3, ..., Ace=14

    def __init__(self, suit: str, rank: str):
        self.suit = suit
        self.rank = rank
        self.value = self.RANK_VALUES[rank]

    def __str__(self) -> str:
        return f"{self.rank} of {self.suit}"

    def __repr__(self) -> str:
        return f"Card('{self.suit}', '{self.rank}')"


class Deck:
    """Represents a deck of cards with basic operations."""

    def __init__(self, cards: Optional[List[Card]] = None):
        self.cards = cards or []

    def __len__(self) -> int:
        return len(self.cards)

    def __bool__(self) -> bool:
        return len(self.cards) > 0

    def add_cards(self, *cards: Card) -> None:
        """Add cards to the bottom of the deck."""
        self.cards.extend(cards)

    def draw_card(self) -> Optional[Card]:
        """Draw a card from the top of the deck."""
        return self.cards.pop(0) if self.cards else None

    def shuffle(self) -> None:
        """Shuffle the deck."""
        random.shuffle(self.cards)

    @classmethod
    def create_standard_deck(cls) -> 'Deck':
        """Create a standard 52-card deck."""
        cards = [Card(suit, rank) for suit in Card.SUITS for rank in Card.RANKS]
        deck = cls(cards)
        deck.shuffle()
        return deck


class Player:
    """Represents a player in the war game."""

    def __init__(self, name: str):
        self.name = name
        self.deck = Deck()
        self.won_cards = Deck()

    def __str__(self) -> str:
        return f"{self.name}: {len(self.deck)} cards in deck, {len(self.won_cards)} cards won"

    def total_cards(self) -> int:
        """Return total number of cards player has."""
        return len(self.deck) + len(self.won_cards)

    def has_cards(self) -> bool:
        """Check if player has any cards left."""
        return self.total_cards() > 0

    def play_card(self) -> Optional[Card]:
        """Play a card from the deck."""
        if not self.deck and self.won_cards:
            self._shuffle_won_cards_to_deck()
        return self.deck.draw_card()

    def win_cards(self, *cards: Card) -> None:
        """Add won cards to the won cards pile."""
        self.won_cards.add_cards(*cards)

    def _shuffle_won_cards_to_deck(self) -> None:
        """Move won cards back to deck and shuffle."""
        self.deck.cards.extend(self.won_cards.cards)
        self.won_cards.cards.clear()
        self.deck.shuffle()
        print(f"{self.name} shuffles won cards back into deck!")


class WarGame:
    """Main game controller for the War card game."""

    def __init__(self, player_name: str = "Player"):
        self.player = Player(player_name)
        self.computer = Player("Computer")
        self._setup_game()

    def _setup_game(self) -> None:
        """Initialize the game by dealing cards."""
        deck = Deck.create_standard_deck()

        for i, card in enumerate(deck.cards):
            if i % 2 == 0:
                self.player.deck.add_cards(card)
            else:
                self.computer.deck.add_cards(card)

        print("=" * 60)
        print("GAME START")
        print("=" * 60)
        print(f"Cards dealt: {self.player.name} and {self.computer.name} each get 26 cards")

    def play_round(self) -> bool:
        """Play a single round. Returns True if game should continue."""
        if not self._check_game_state():
            return False

        player_card = self.player.play_card()
        computer_card = self.computer.play_card()

        if not player_card or not computer_card:
            return False

        print(f"\n{'-' * 50}")
        print(f"{self.player.name}: {player_card}")
        print(f"{self.computer.name}: {computer_card}")

        cards_on_table = [player_card, computer_card]

        if player_card.value > computer_card.value:
            self._player_wins_round(cards_on_table)
        elif computer_card.value > player_card.value:
            self._computer_wins_round(cards_on_table)
        else:
            self._handle_war(cards_on_table)

        self._display_status()
        return True

    def _player_wins_round(self, cards: List[Card]) -> None:
        """Handle player winning a round."""
        print(f"*** {self.player.name} wins this round! ***")
        self.player.win_cards(*cards)

    def _computer_wins_round(self, cards: List[Card]) -> None:
        """Handle computer winning a round."""
        print(f"*** {self.computer.name} wins this round! ***")
        self.computer.win_cards(*cards)

    def _handle_war(self, cards_on_table: List[Card]) -> None:
        """Handle war situation when cards are equal."""
        print("*** WAR! Both cards are equal! ***")

        war_cards_needed = 4

        if not self._can_fight_war(war_cards_needed):
            return

        war_cards = []
        for i in range(war_cards_needed):
            player_card = self.player.play_card()
            computer_card = self.computer.play_card()

            if not player_card or not computer_card:
                return

            war_cards.extend([player_card, computer_card])

            if i < war_cards_needed - 1:
                print(f"War card {i + 1}: {player_card} vs {computer_card}")
            else:
                print(f"Final battle: {player_card} vs {computer_card}")

                if player_card.value > computer_card.value:
                    all_cards = cards_on_table + war_cards
                    print(f"*** {self.player.name} wins the war! ({len(all_cards)} cards) ***")
                    self.player.win_cards(*all_cards)
                    return
                elif computer_card.value > player_card.value:
                    all_cards = cards_on_table + war_cards
                    print(f"*** {self.computer.name} wins the war! ({len(all_cards)} cards) ***")
                    self.computer.win_cards(*all_cards)
                    return
                else:
                    print("Another tie! War continues...")
                    cards_on_table.extend(war_cards)
                    self._handle_war(cards_on_table)
                    return

    def _can_fight_war(self, cards_needed: int) -> bool:
        """Check if both players can fight a war."""
        if self.player.total_cards() < cards_needed:
            print(f"{self.player.name} doesn't have enough cards for war!")
            print(f"*** {self.computer.name} wins the game! ***")
            return False

        if self.computer.total_cards() < cards_needed:
            print(f"{self.computer.name} doesn't have enough cards for war!")
            print(f"*** {self.player.name} wins the game! ***")
            return False

        return True

    def _check_game_state(self) -> bool:
        """Check if the game can continue."""
        if not self.player.has_cards():
            print(f"\n*** {self.computer.name} wins! {self.player.name} is out of cards! ***")
            return False

        if not self.computer.has_cards():
            print(f"\n*** {self.player.name} wins! {self.computer.name} is out of cards! ***")
            return False

        return True

    def _display_status(self) -> None:
        """Display current game status."""
        print(f"\nStatus:")
        print(f"  {self.player}")
        print(f"  {self.computer}")

    def play_game(self) -> None:
        """Play the complete game."""
        round_count = 0
        max_rounds = 1000

        while round_count < max_rounds:
            if not self.play_round():
                break

            round_count += 1

            user_input = input("\nPress Enter to continue (or 'q' to quit): ").strip().lower()
            if user_input == 'q':
                print("Game ended by user.")
                break

        if round_count >= max_rounds:
            print(f"\nGame ended after {max_rounds} rounds to prevent infinite loop.")
            winner = self.player if self.player.total_cards() > self.computer.total_cards() else self.computer
            print(f"*** {winner.name} wins with more cards! ***")

        print("\n" + "=" * 60)
        print("GAME OVER")
        print("=" * 60)


def main():
    """Main function to start the game."""
    print("Welcome to the War Card Game!")
    player_name = input("Enter your name: ").strip() or "Player"

    game = WarGame(player_name)
    game.play_game()


if __name__ == "__main__":
    main()
