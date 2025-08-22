# WarsOnCards
An interactive card game script written in python 3.13.  
Modules utilized: `typing`, `random`  
The game involves distributing a deck of **52** well shuffled cards between the player and computer, which then turns into a one-on-one showdown between the topmost cards in either deck.  
The cards are ranked in power as follows:  
  
|Cards (All Suits)|Power|
|:----| ----:|
|Ace|13|
|King|12|
|Queen|11|
|Joker|10|
|10|9|
|9|8|
|8|7|
|7|6|
|6|5|
|5|4|
|4|3|
|3|2|
|2|1|

During a normal round, players each draw the topmost card of their deck and compare the power. The winner is the one who has the card with the higher power!  
The cards are then stored in the winner's `won-card stack` or in short, a `bin`, which can't be immediately accessed until the players card stack runs out. In that case, the `bin-cards` are transferred to the main stack of cards! (This is not applicable if there is a `WAR!` event ongoing. In that case the player looses)  


If for some reason, the topmost card of the `main stack` of the player and the computer are similar in power, the situation calls for a `WAR!`  
In a `WAR!`, the players surrender their `initiation cards` (the cards that triggered the war), then each player picks out 3 cards from the top of their stack and  the 4th card enters the `Final Battle` to decide the `WAR!`. The winner of this confrontation take away the `initiation cards` + `2x (3 cards each)` + the cards participating in the `Final War` = x10 cards!  
(If the cards in the `Final Batlle` have similar power once again, then the `WAR!` continues... Requiring 4 cards per player, and the final winner takes all!)  
## Note:
- If either of the player(or computer) are short of the required amount of cards during a `WAR!`, they cannot access their `bin` to refill and immediately lose!


## Code Usage:
- Everything in the script is divided into perfectly resuable components and clear syntax.
- All cards are instances of the `Card()` object
- All Decks containing cards come under `Deck()` object
- Players are defined through the `Player()` object
- And the procedure of the game is defined in th `WarGame()` class.
- Feel free to use/copy the code for any purpose!

