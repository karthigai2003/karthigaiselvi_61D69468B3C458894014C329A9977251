class Player:
    def play(self):
        print("The player is playing cricket.")

class Batsman(Player):
    def play(self):
        print("The batsman is batting.")

class Bowler(Player):
    def play(self):
        print("The bowler is bowling.")

if __name__ == "__main__":
    while True:
        print("Choose a player type:")
        print("1. Batsman")
        print("2. Bowler")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == "1":
            batsman = Batsman()
            batsman.play()
        elif choice == "2":
            bowler = Bowler()
            bowler.play()
        elif choice == "3":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")
