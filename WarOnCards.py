import random

rank_hierarchy = ['Ace', 'King', 'Queen', 'Joker', '10', '9', '8', '7', '6', '5', '4', '3', '2']
class Cards:
    def __init__(self, stack, rank) -> None:
        self.stack = stack
        self.rank = rank
        self.value = rank_hierarchy.index(rank)
        self.in_computer_bin = False
        self.in_player_bin = False
    

    def __repr__(self):
        return f"{self.stack, self.rank}"

class Decks:
    def __init__(self, user) -> None:
        self. name = user
        self.cards= []
        self.bin = []
    
    def __repr__(self):
        return f"{self.name}: Total cards = {len(self.cards)}"
    
def push(array: list, *items) -> None:
    for item in items:
        array.insert(0, item)

def pop(*array: list) -> None:
    for arr in array:
        arr.pop(0)



    
def main():
    playerName = input("Please enter your preferred username: ")
    all_cards: list[tuple[str, str]] = [('Diamond', 'Ace'), ('Diamond', 'King'), ('Diamond', 'Queen'), ('Diamond', 'Joker'), ('Diamond', '10'), ('Diamond', '9'), ('Diamond', '8'), ('Diamond', '7'), ('Diamond', '6'), ('Diamond', '5'), ('Diamond', '4'), ('Diamond', '3'), ('Diamond', '2'), ('Spade', 'Ace'), ('Spade', 'King'), ('Spade', 'Queen'), ('Spade', 'Joker'), ('Spade', '10'), ('Spade', '9'), ('Spade', '8'), ('Spade', '7'), ('Spade', '6'), ('Spade', '5'), ('Spade', '4'), ('Spade', '3'), ('Spade', '2'), ('Club', 'Ace'), ('Club', 'King'), ('Club', 'Queen'), ('Club', 'Joker'), ('Club', '10'), ('Club', '9'), ('Club', '8'), ('Club', '7'), ('Club', '6'), ('Club', '5'), ('Club', '4'), ('Club', '3'), ('Club', '2'), ('Hearts', 'Ace'), ('Hearts', 'King'), ('Hearts', 'Queen'), ('Hearts', 'Joker'), ('Hearts', '10'), ('Hearts', '9'), ('Hearts', '8'), ('Hearts', '7'), ('Hearts', '6'), ('Hearts', '5'), ('Hearts', '4'), ('Hearts', '3'), ('Hearts', '2')]
    random.shuffle(all_cards)
    playerDeck = Decks(playerName)           #add input method
    computerDeck=Decks("Computer")

    for i, card_set in enumerate(all_cards):
        if i % 2 != 0:
            playerDeck.cards.append(Cards(card_set[0], card_set[1]))
        else:
            computerDeck.cards.append(Cards(card_set[0], card_set[1]))

    print("*********************************************** GAME START ***********************************************")
    continue_game = True
    while continue_game:
        if len(playerDeck.cards) == 0:
            if len(playerDeck.bin) != 0:
                print("**********************************************************************************************************")
                print("Adding bin cards to the deck!")
                playerDeck.cards += playerDeck.bin
                playerDeck.bin.clear()
                continue
            else:
                if len(computerDeck.bin) != 0 or len(computerDeck.cards) != 0:
                    print("Oh no! You're out of cards!")
                    print("*********************************************** GAME OVER ***********************************************")
                    print("You Lose!")
                    break

        if len(computerDeck.cards) == 0:
            if len(computerDeck.bin) != 0:
                print("**********************************************************************************************************")
                print("Adding the computer's bin cards to the deck!")
                computerDeck.cards += computerDeck.bin
                computerDeck.bin.clear()
                continue
            else:
                if len(playerDeck.bin) != 0 or len(playerDeck.cards) != 0:
                    print("The Computer is out of Cards!")
                    print("*********************************************** GAME OVER ***********************************************")
                    print("Your Win!")
                    break
        print("**********************************************************************************************************")
        card_computer = computerDeck.cards[0]
        card_player = playerDeck.cards[0]
        print(f"Your Card: {card_player.rank} of {card_player.stack}")
        print(f"Computer's Card: {card_computer.rank} of {card_computer.stack}")

        if card_player.value < card_computer.value:
            print(f"**** You won this round!****\n Cards added to your bin: {card_player.rank} of {card_player.stack}, {card_computer.rank} of {card_computer.stack}")
            push(playerDeck.bin, card_player, card_computer)
            pop(playerDeck.cards, computerDeck.cards)

        elif card_computer.value < card_player.value:
            print(f"**** You lost this round!****\n Cards claimed by the computer: {card_player.rank} of {card_player.stack}, {card_computer.rank} of {card_computer.stack}")
            push(computerDeck.bin, card_player, card_computer)
            pop(playerDeck.cards, computerDeck.cards)
        else:
            print(f"Since both cards have equal rank {card_computer.rank} and {card_player.rank}.\nTHE SITUATION CALLS FOR A WAR!!")
            print("******** WAR BEGINS! ********")
            war_card_list = [card_player, card_computer]
            # Check before war starts
            if len(computerDeck.cards) < 4: 
                print("Not enough cards to continue the war!\nThe Player has won the game!")
                continue_game = False
                break
            elif len(playerDeck.cards) < 4:
                print("Not enough cards to continue the war!\nThe Computer has won the game!")
                continue_game = False
                break
            for index in range(1, 4):
                war_card_list.append(computerDeck.cards[index])
                war_card_list.append(playerDeck.cards[index])
                print(f"****KnockOut Phase {index}****\n{computerDeck.name}: {computerDeck.cards[index].rank} of {computerDeck.cards[index].stack}")
                print(f"{playerDeck.name}: {playerDeck.cards[index].rank} of {playerDeck.cards[index].stack}")
            else:
                deck_index: int = 4
                while True:
                    if deck_index >= len(computerDeck.cards) or deck_index >= len(playerDeck.cards):
                        print("Not enough cards to continue the war! Ending game.")
                        continue_game = False
                        break
                    wild_card_computer = computerDeck.cards[deck_index]
                    wild_card_player = playerDeck.cards[deck_index]
                    print(f"**** Final Battle! ****")
                    print(f"{computerDeck.name}: {wild_card_computer.rank} of {wild_card_computer.stack} V/S {playerDeck.name}: {wild_card_player.rank} of {wild_card_player.stack}")
                    if wild_card_computer.value > wild_card_player.value:
                        print(f"GG! YOU WON THE WAR!\nCards added to your bin: x{len(war_card_list)+2}")
                        war_card_list.append(wild_card_computer)
                        war_card_list.append(wild_card_player)
                        push(playerDeck.bin, *war_card_list)
                        break
                    elif wild_card_player.value > wild_card_computer.value:
                        print(f"NO! THE WAR WAS LOST!\nCards added to the Computer's bin: x{len(war_card_list)+2}")
                        war_card_list.append(wild_card_computer)
                        war_card_list.append(wild_card_player)
                        push(computerDeck.bin, *war_card_list)
                        break
                    else:
                        print("BOTH CARDS HAVE A SIMILAR RANK! THE WAR CONTINUES")
                        deck_index += 1
                for _ in range(deck_index+1):
                    if len(computerDeck.cards) > 0:
                        pop(computerDeck.cards)
                    if len(playerDeck.cards) > 0:
                        pop(playerDeck.cards)
        print("*********************************************** STATUS ***********************************************")
        print(f"{playerDeck.name}: Cards in Deck: {len(playerDeck.cards)}\nCards in bin: {len(playerDeck.bin)}")
        print(f"{computerDeck.name}: Cards in Deck: {len(computerDeck.cards)}\nCards in bin: {len(computerDeck.bin)}")
        if not continue_game:
            break
        nextGame = input("Do you wish to continue the game? (Y/N): ")
        if nextGame.lower()[0] == 'y':
            continue
        else:
            continue_game = False
            




if __name__ == "__main__":
    main()
