# main.py
from Adventure import UndergroundCavernsAdventure, ForgottenTempleAdventure, Player

def start_game():
    print("Choose an adventure:")
    print("1. Forgotten Temple Adventure")
    print("2. Underground Caverns Adventure")
    

    adventure_choice = input("Enter the number of your chosen adventure: ")

    if adventure_choice == '1':
        forgotten_temple = ForgottenTempleAdventure()
        forgotten_temple.start_adventure()
    elif adventure_choice == '2':
        player1 = Player(name="Avatar Roshi")
        # Create an instance of the UndergroundCavernsAdventure
        adventure = UndergroundCavernsAdventure(player1)
        adventure.play()
    
    else:
        print("Invalid choice. Exiting the game.")

def play_adventure(adventure):
    print("\nStarting the adventure...\n")
    adventure.start_adventure()
    adventure.play()

if __name__ == "__main__":
    start_game()
