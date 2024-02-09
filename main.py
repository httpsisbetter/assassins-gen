import random
import os

names = ["Charles1", "Charles2", "Charles3", "Charles3", "Charles4", "Charles5"]

def create_target_files():
    if len(names) % 2 != 0:
        names.append("Eve")

    for name in names:
        target = random.choice([player for player in names if player != name])
        file_path = os.path.join(os.getcwd(), f"{name}_target.txt")
        with open(file_path, "w") as file:
            file.write(f"{name}'s target is {target}")

def main():
    create_target_files()

if __name__ == "__main__":
    main()
