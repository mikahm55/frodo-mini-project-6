# Frodo's Adventure - original code by teammate 1
# // TO-DO: Add the full team header before submission.
import random as r 
import time as t
import tkinter as tk
import pygame as pyg
def rg(a):
        """Team-written. Teammate 1: look up and display a story message by its key."""
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
            "10":"This battle seems to have developed not necessarily to Mikahs advantage.",
            "fv": "You passed the test.  The marine next to you has eaten five crayons.  You proceed",
            "final_vic": "Mikahs rocket, and with it his dreams, have shattered.  You feel victorius, since you saved A&M",
            "e1": "Mikah's rocket was aimed at space.  He was gonna launch an EMP at the satillite networks, oblierating the internet. He was gonna conquer the world",
            "e2": "Mikah's rocket was aimed at his opps. He was simply trying to protect himself.  Now his opps publish scathing information about Mikah.  Big sad.",
            "e3": "Mikahs rocket was aimed at an entity residing in an abandoned house. You realize that it was a trap.  The apocalyspe has begun.",
            "eF": "Mikah flees north, towards hillsboro.  The fight is not over yet.  Mikah will return in GAME 2! Comes out when Half life 3 does.",
            "eL": "Mikahs rocket hits Mikahs opps.  Mikah's opps quickly switch sides, and Mikah rules the world by 2050.  Glory to Mikah.",
            "b": "The squirell looks at you with anger. Mikah bribed it with a fry",
            "b1": "The squirell has webassign homework to do.  It fights you anyway",
            "b2": "The squirell reads some feminist literature. It is 8 inches tall at most."
            }
        
        statement=print(dih[a])
        return(statement)
def read_guess(prompt="Guess a number between 1 and 5: "):
    """AI-assisted. Return a valid integer guess, retrying bad input."""
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
    """AI-assisted. Return remaining enemy HP and actual damage dealt."""
    damage = enemy_health if guess == r.randint(1, 5) else r.randint(1, 5)
    remaining = max(0, enemy_health - damage)
    return remaining, enemy_health - remaining



def show_map():
    """AI-assisted. Display the supplied campus map until its window closes."""
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
    # // TO-DO: Team member: training restores lives OR gives a small luck boost.
    # Notes suggest rock-paper-scissors or trivia; decide the exact rules.
    pass


def play_minigame(luck, items, remaining_dungeons):
    # // TO-DO: Team member: implement planned minigames that award luck items.
    # Update the possessed-items dictionary and remaining-dungeons list.
    pass


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


#hashtag awesome
enemy_catalog={
    "squirell": 20,
    "Pidgeon": 30,
    "Mikah": 80}

gr = True
pyg.mixer.init()
pyg.mixer.music.load("sb_goliath.mp3")
pyg.mixer.music.play()


# Keep the script running while the audio plays

print("You are playing as Frodo.  Frodo has been tasked to prevent a mikah takeover.  The reason appears political...")
t.sleep(2)
print("You exit Butler Hall, texting John.  He left his backpack there and you have it now. You are being escorted by the corp of cadets")
print("If you feel unsafe while travelling, call 979-845-6789.  This summons the corp escort services.")
t.sleep(4)
print("Anyway, Mikah's forces intercepted your communications!  Mikah has sent a squirell to block your path!")
t.sleep(2)


level = 1
health = 50 + 2*level
enemy_health=20
# // TO-DO: Team-written: extend this existing battle loop into the planned
# turn loop (menu, training, minigames, final challenge, status/rules/quit).
# Track lives/luck/items/completed dungeons and log actions and results.
# Include meaningful list append/removal, dictionary updates, and loop-else.
while enemy_health > 0:
    dice=read_guess()
    if float(dice) >= 1 and float(dice) <= 5:
        h=r.randint(1,5)
        if float(dice)==h:
            print("critical hit!")
            enemy_health = 0
            print("enemy defeated in one blow")
        else:
            print("you failed to score a critical hit!  Your army attacks:")
            rh=r.randint(1,5)
            print(f"You dealt {rh} damage to the enemy!")
            enemy_health=enemy_health-rh
            if enemy_health < 0:
                enemy_health = 0
            print(f"Enemy has {enemy_health} left")
            t.sleep(2)
            print("The enemy attacks!")
            ea=1
            health = health - ea
            print(f"You have {health} HP left, since the enemy did {ea} damage")
            t.sleep(2)
            ri=r.randint(-3,-1)
            if ri == -3:
                print(rg("b"))
            elif ri == -2:
                print(rg("b1"))
            else:
                print(rg("b2"))
            t.sleep(1)
    else:
        print("you tried to pick a number outside the allowed constraints...")
        
    
if enemy_health <= 0:
    gr = False
    pyg.mixer.music.stop()
    print("You won the battle, but did you win the war...")
    t.sleep(3)
    print("XP gained: 5.  You leveled up! Due to Democrat Fiscal policy, your levels were given away")
    pyg.mixer.music.load("wse.mp3")
    pyg.mixer.music.play()
    t.sleep(4)
    print('Incoming transmission...')
    t.sleep(4)
    print("Status Report:  Current Map of A&M as of 11/20/2026")
    t.sleep(2)
    show_map()
