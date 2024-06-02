class Player:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.experience = 0
        self.achievements = []

    def complete_challenge(self, challenge):
        # Update player's experience and achievements
        self.experience += challenge.experience_reward
        if challenge.achievement:
            self.achievements.append(challenge.achievement)

class Challenge:
    def __init__(self, description, code_to_fix, solution, experience_reward, achievement=None):
        self.description = description
        self.code_to_fix = code_to_fix
        self.solution = solution
        self.experience_reward = experience_reward
        self.achievement = achievement

    def solve(self, player_code):
        # Check if player's code matches the solution
        if player_code == self.solution:
            return True
        else:
            return False

class Level:
    def __init__(self, level_number, challenges):
        self.level_number = level_number
        self.challenges = challenges

    def start(self):
        print(f"Welcome to Level {self.level_number}!")
        for challenge in self.challenges:
            print(challenge.description)
            player_code = input("Enter your Python code: ")
            if challenge.solve(player_code):
                print("Challenge complete!")
                player.complete_challenge(challenge)
            else:
                print("Incorrect solution. Try again.")

# Example usage
player = Player("Player 1")

challenge1 = Challenge("Fix the syntax error", "print('Hello, world!'", "print('Hello, world!')", 50, "Syntax Master")
challenge2 = Challenge("Create a function to calculate the factorial of a number", "def factorial(n):", "def factorial(n):\n    if n == 0:\n        return 1\n    else:\n        return n * factorial(n-1)", 100, "Factorial Expert")

level1 = Level(1, [challenge1])
level2 = Level(2, [challenge2])

levels = [level1, level2]

for level in levels:
    level.start()
