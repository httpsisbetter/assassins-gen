import random
import os

names = ["bob1", "bob2", "bob3", "bob4", "bob5", "bob7"]


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
