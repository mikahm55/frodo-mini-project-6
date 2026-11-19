# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#, 
# Name:        Taylor Rogers, Abhi Thatavarthi, Mikah Matsuzawa
# Section:     204
# Assignment:  Frodo's Dungeon Quest -- Mini Project 6
# Date:        19 11 2026

import random as r
import time as t
import tkinter as tk
import pygame as pyg

def rg(a):
    """Team-written. Mikah: look up and display a story message by its key."""
    dih = {
        "0": "high command congratulates you for your victory.  It goes on your resume.",
        "1": "You feel that Mikah is your superior.",
        "2": "Mikah seems rejuvinated, perhaps a comeback is in order",
        "3": "Mikah checks his phone.  She has not responded",
        "4": "You get a notification.  Its from bro asking if 19 and 13 is an acceptable age gap",
        "5": "A thunderstorm warning has been issued for your area. You dress nicely",
        "6": "Mikah makes a joke.  It can't be aired on CNN",
        "7": "Mikah is smarter than you.  You contemplate surrender",
        "8": "Mikah sends an SOS signal.  He is left on read",
        "9": "You check your phone. A canvas notification!  You failed the last engineering quiz.",
        "10": "This battle seems to have developed not necessarily to Mikahs advantage.",
        "fv": "You passed the test.  The marine next to you has eaten five crayons.  You proceed",
        "final_vic": "Mikahs rocket, and with it his dreams, have shattered.  You feel victorius, since you saved A&M",
        "e1": "Mikah's rocket was aimed at space.  He was gonna launch an EMP at the satillite networks, oblierating the internet. He was gonna conquer the world",
        "e2": "Mikah's rocket was aimed at his opps. He was simply trying to protect himself.  Now his opps publish scathing information about Mikah.  Big sad.",
        "e3": "Mikahs rocket was aimed at an entity residing in an abandoned house. You realize that it was a trap.  The apocalyspe has begun.",
        "eF": "Mikah flees north, towards hillsboro.  The fight is not over yet.  Mikah will return in GAME 2! Comes out when Half life 3 does.",
        "eL": "Mikahs rocket hits Mikahs opps.  Mikah's opps quickly switch sides, and Mikah rules the world by 2050.  Glory to Mikah.",
        "b": "The squirell looks at you with anger. Mikah bribed it with a fry",
        "b1": "The squirell has webassign homework to do.  It fights you anyway",
        "b2": "The squirell reads some feminist literature. It is 8 inches tall at most.",
    }

    statement = print(dih[a])
    return statement


def read_guess(prompt="Guess a number between 1 and 5: "):
    """Team-written. Returns a valid integer guess, retrying bad input."""
    while True:
        try:
            guess = int(input(prompt))
        except ValueError:
            print("Enter a whole number from 1 to 5.")
            continue
        if 1 <= guess <= 5:
            return guess
        print("Enter a whole number from 1 to 5.")


def resolve_attack(guess, enemy_health):
    """Team-written. Returns remaining enemy HP and actual damage dealt."""
    damage = enemy_health if guess == r.randint(1, 5) else r.randint(1, 5)
    remaining = max(0, enemy_health - damage)
    return remaining, enemy_health - remaining


def show_map():
    """Team-written. Mikah: Displays a custom-made original map image"""
    root = tk.Tk()
    root.title("Frodo's Adventure - close this map to continue")
    picture = tk.PhotoImage(file="image.png")
    tk.Label(root, image=picture).pack()
    root.mainloop()


# Planned features from the handwritten notes. Team members fill these in.
# // TO-DO: Every teammate must implement at least one Team-written function.


def display_menu(luck):
    # // TO-DO: Show training, minigames, challenge Mikah, rules, status, quit.
    # Return the player's validated choice to the team's turn loop.
    pass


def show_status(items, luck, completed_dungeons, lives, turn_number):
    # // TO-DO: Display the state listed in Part 3 of the handwritten plan.
    pass


def train(lives, luck):
    """AI-assisted. Play rock-paper-scissors for one life or one luck point.

    Return (lives, luck). Ties and losses leave both values unchanged.
    """
    choices = ("rock", "paper", "scissors")
    while True:
        player = input("Training: rock, paper, or scissors? ").strip().lower()
        if player in choices:
            break
        print("Choose rock, paper, or scissors.")
    opponent = r.choice(choices)
    print(f"Your training opponent chose {opponent}.")
    winning_pairs = {("rock", "scissors"), ("paper", "rock"), ("scissors", "paper")}
    if player == opponent:
        print("A tie! Your lives and luck stay the same.")
    elif (player, opponent) in winning_pairs:
        while True:
            reward = input("You won! Restore one life or gain one luck? (life/luck): ").strip().lower()
            if reward in ("life", "luck"):
                break
            print("Enter life or luck.")
        if reward == "life":
            lives = min(3, lives + 1)
            print(f"Lives: {lives}/3.")
        else:
            luck += 1
            print(f"Luck increased to {luck}.")
    else:
        print("You lost this practice round. Try training again next turn.")
    return lives, luck


def play_minigame(luck, items, remaining_dungeons):
    """AI-assisted. Guess a dungeon's hidden number to earn a luck item.

    Return (new_luck, item_name, dungeon_name) on success, otherwise None.
    The caller owns inventory and dungeon-list updates; inputs stay unchanged.
    """
    if not remaining_dungeons:
        print("All dungeons have already been completed.")
        return None
    while True:
        print("Available dungeons: " + ", ".join(remaining_dungeons))
        selection = input("Choose a dungeon: ").strip().lower()
        matches = [name for name in remaining_dungeons if name.lower() == selection]
        if matches:
            dungeon = matches[0]
            break
        print("Choose one of the remaining dungeons.")
    print("Guess the hidden number from 1 to 5. You have three attempts.")
    target = r.randint(1, 5)
    for attempt in range(3):
        guess = read_guess(f"Attempt {attempt + 1}/3: ")
        if guess == target:
            break
        print("Too low." if guess < target else "Too high.")
    else:
        print(f"The number was {target}. You can retry this dungeon next turn.")
        return None
    rewards = {"squirell": ("Zach chestplate", 2), "Pidgeon": ("Campus lucky charm", 3)}
    item, bonus = rewards.get(dungeon, (f"{dungeon} luck token", 1))
    if item in items:
        print("You already own this dungeon's reward.")
        return None
    print(f"Dungeon complete! You earned {item} (+{bonus} luck).")
    return luck + bonus, item, dungeon


def challenge_mikah(luck):
    # // TO-DO: Team member: one final challenge, three coin-flip wins in a row.
    # Luck influences flips. Return whether Frodo wins.
    pass


def read_game_data(filename):
    # // TO-DO: Team-written file reading: load your own game data/save file.
    pass


def write_turn(filename, turn, action, result):
    # // TO-DO: Team-written file writing: log each turn's action and result.
    pass


def write_summary(filename, stats):
    # // TO-DO: Team-written file writing: calculate and log the final summary.
    pass


enemy_catalog = {"squirell": 20, "Pidgeon": 30, "Mikah": 80}

gr = True
pyg.mixer.init()
pyg.mixer.music.load("sb_goliath.mp3")
pyg.mixer.music.play()

print(
    "You are playing as Frodo.  Frodo has been tasked to prevent a mikah takeover.  The reason appears political..."
)
t.sleep(2)
print(
    "You exit Butler Hall, texting John.  He left his backpack there and you have it now. You are being escorted by the corp of cadets"
)
print(
    "If you feel unsafe while travelling, call 979-845-6789.  This summons the corp escort services."
)
t.sleep(4)
print(
    "Anyway, Mikah's forces intercepted your communications!  Mikah has sent a squirell to block your path!"
)
t.sleep(2)


level = 1
health = 50 + 2 * level
lives = 3
luck = 0
items = {}
remaining_dungeons = list(enemy_catalog)[:-1]
completed_dungeons = []
turn_log = []
turn_number = 0
challenge_attempted = False
won = False
outcome = "quit"
enemy_health = enemy_catalog[remaining_dungeons[0]]

while gr and lives > 0 and not won:
    print(f"\nTurn {turn_number + 1} | HP: {health} | Lives: {lives} | Luck: {luck}")
    print("attack / train / minigame / challenge / rules / status / map / quit")
    choice = input("Choose an action: ").strip().lower()
    if choice == "quit":
        gr = False
        outcome = "quit"
        continue
    elif choice == "rules":
        print("Frodo must stop Mikah's takeover of Texas A&M.")
        print("Train to recover lives or gain luck; minigames award luck items.")
        print("Attack guesses 1-5: match the roll for a critical hit;")
        print("otherwise deal 1-5 damage and surviving enemies deal 1 HP.")
        print("Losing all HP costs a life. Zero lives ends the game.")
        print("Challenge Mikah once: win three coin flips in a row to win.")
        print("Rules, status, and map do not spend a turn. Close the map to continue.")
        continue
    elif choice == "status":
        print(f"Possessed items: {items}")
        print(f"Completed dungeons: {completed_dungeons}")
        print(f"Remaining dungeons: {remaining_dungeons}")
        print(f"Mikah challenge attempted: {challenge_attempted}")
        continue
    elif choice == "map":
        show_map()
        continue
    elif choice == "train":
        result = train(lives, luck)
        if result is None:
            print("// TO-DO: The team still needs to implement training.")
            continue
        lives, luck = result
        action_result = f"Training: lives={lives}, luck={luck}"
    elif choice == "minigame":
        result = play_minigame(luck, items.copy(), remaining_dungeons.copy())
        if result is None:
            print("No dungeon completed this time.")
            continue
        new_luck, item, dungeon = result
        if dungeon not in remaining_dungeons:
            print("That dungeon is unavailable or already completed.")
            continue
        items[item] = new_luck - luck
        luck = new_luck
        remaining_dungeons.remove(dungeon)
        completed_dungeons.append(dungeon)
        enemy_health = enemy_catalog[remaining_dungeons[0]] if remaining_dungeons else 0
        action_result = f"Completed {dungeon}; received {item}; luck={luck}"
    elif choice == "challenge":
        if challenge_attempted:
            print("Mikah can only be challenged once.")
            continue
        result = challenge_mikah(luck)
        if result is None:
            print("// TO-DO: The team still needs to implement the coin flips.")
            continue
        challenge_attempted = True
        won = result
        gr = False
        outcome = "win" if won else "loss"
        action_result = f"Mikah challenge: {outcome}"
    elif choice == "attack":
        if not remaining_dungeons:
            print("All dungeons are completed. Prepare for or challenge Mikah.")
            continue
        enemy = remaining_dungeons[0]
        print(f"Facing {enemy}: {enemy_health} HP")
        dice = read_guess()
        h = r.randint(1, 5)
        if dice == h:
            print("critical hit! Enemy defeated in one blow")
            enemy_health = 0
        else:
            rh = r.randint(1, 5)
            enemy_health = max(0, enemy_health - rh)
            print(f"You dealt {rh} damage! Enemy has {enemy_health} HP left.")
            if enemy_health > 0:
                health -= 1
                print(f"The enemy deals 1 damage. You have {health} HP left.")
                if enemy == "squirell":
                    rg(r.choice(["b", "b1", "b2"]))
        if enemy_health == 0:
            remaining_dungeons.remove(enemy)
            completed_dungeons.append(enemy)
            print(f"You won the battle against {enemy}, but did you win the war...")
            level += 1
            enemy_health = (
                enemy_catalog[remaining_dungeons[0]] if remaining_dungeons else 0
            )
        if health <= 0:
            lives -= 1
            if lives > 0:
                health = 50 + 2 * level
                print(f"Lost a life. {lives} lives remain; HP restored to {health}.")
            else:
                outcome = "loss"
        action_result = (
            f"Attacked {enemy}: enemy HP={enemy_health}, HP={health}, lives={lives}"
        )
    else:
        print("Choose one of the listed actions.")
        continue

    turn_number += 1
    turn_log.append((turn_number, choice, action_result))
    print(action_result)

pyg.mixer.music.stop()
if won:
    rg("final_vic")
elif outcome == "loss":
    rg("eL")
else:
    print("You left the adventure.")
print(f"Turns played: {turn_number}; dungeons completed: {len(completed_dungeons)}")
