import random
class Player:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health

    def award_health_points(self, points):
        self.health += points


class UndergroundCavernsAdventure:
   
    description = "A vast network of dark and winding caverns beneath the earth's surface, illuminated only by the glow of bioluminescent fungi."

    def __init__(self, player):
        self.player = player

    def search_for_city(self):
        print("You venture into the underground caverns.")
        print("Bioluminescent fungi light your way as you seek a lost civilization's city.")
        print("What will you do?")

        for attempt in range(4):  # Allow three attempts
            user_input = input("Type 'explore' to continue searching or 'exit' to leave: ").lower()

            if user_input == 'exit':
                print("You decide to leave the caverns.")
                break
            elif user_input == 'explore':
                if self.generate_random_number():
                    self.give_hint()
                    break
            else:
                print("Invalid command. Type 'explore' or 'exit'.")

        print("You've exhausted your attempts. The caverns remain a mystery.")

    def generate_random_number(self):
        random_number = random.randint(1, 10)

        for guess_attempt in range(4):
            user_guess = int(input(f"Attempt {guess_attempt + 1}: Guess the random number (between 1 and 10): "))

            if user_guess == random_number:
                print("Congratulations! You guessed the correct number.")
                self.player.award_health_points(20)  # Award health points for successful guess
                print(f"Your health points: {self.player.health}")
                return True  # Signal that the correct number was guessed

            elif guess_attempt < 3:
                print(f"Sorry, that's not correct. Try again!")

        print(f"Sorry, the correct number was {random_number}. Better luck next time!")
        return False

    def give_hint(self):
        print("A mysterious voice echoes through the caverns.")
        print("Hint: The hidden city lies behind the waterfall.")
        print("You feel a surge of energy as if the caverns are guiding you.")
        self.player.award_health_points(10)  # Award health points for receiving a hint
        print(f"Your health points: {self.player.health}")

# Additional code for the underground caverns adventure can be added here.

if __name__ == "__main__":
    # Create a player instance
    player = Player(name="Adventurer")

    # Create an instance of the UndergroundCavernsAdventure
    adventure = UndergroundCavernsAdventure(player)

    # Start the adventure
    adventure.search_for_city()