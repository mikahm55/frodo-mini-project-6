# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#, 
# Name:        Taylor Rogers, Abhi Thatavarthi, Mikah Matsuzawa
# Section:     204
# Assignment:  Frodo's Dungeon Quest -- Mini Project 6
# Date:        19 11 2026

#Mikah and Taylor
import random as r 
import time as t
import tkinter as tk
import pygame as pyg
import sys

health = 50
level = 0
luck = 1

def menu():
        root = tk.Tk()
        root.title("Tkinter Menu Example")
        root.geometry("400x300")
        
        # 1. Create the main menu bar and attach it to the window
        menubar = tk.Menu(root)
        root.config(menu=menubar)
        
        # 2. Create a "File" dropdown menu (tearoff=0 removes the dashed line)
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        
        # 3. Add clickable items and a divider to the "File" menu
        file_menu.add_command(label="Quit Game", command=sys.quit)
        file_menu.add_command(label="save", command=ts)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=root.quit)
        
        # 4. Create a "game" dropdown menu
        game_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="game", menu=game_menu)
        game_menu.add_command(label="Campaign", command=())
        game_menu.add_command(label="Training", command=train(level, luck))
        game_menu.add_command(label="Fight Big Mikah", command=mikah(level, luck))
        game_menu.add_separator()
        game_menu.add_command(label="Exit", command=root.quit)
        
        rules = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Rules", menu=rules)
        rules.add_command(label="See Rules", command=)
        rules.add_command(label="Rodrick Rules", command=)
        rules.add_command(label="Exit", command=root.quit)
        rules.add_separator()
        
        status = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="see map")
        status.add_command(label="in progress", command = ts)
        
        root.mainloop()


def train(level, luck):
    """AI-assisted. Play rock-paper-scissors for one life or one luck point.

    Return (lives, luck). Ties and losses leave both values unchanged.
    """
    choices = ("rock", "paper", "scissors")
    print("You go to ZACH 212 to train.  The lion doesn't go to the gym, so why should you?")
    t.sleep(3)
    print("The robotics club challenges you in a friendly manner.  They send a CLANKER")
    t.sleep(3)
    print("The robot imitates an engineering student.  It smells bad.")
    t.sleep(2)
    while True:
        player = input("Training: rock, paper, or scissors? ").strip().lower()
        if player in choices:
            break
        print("Choose rock, paper, or scissors.")
        #POV lesbians
    opponent = r.choice(choices)
    print(f"Your training opponent chose {opponent}.")
    winning_pairs = {("rock", "scissors"), ("paper", "rock"), ("scissors", "paper")}
    if player == opponent:
        print("A tie! Your lives and luck stay the same.  You remain at the bottom of the hypergamy chart.")
    elif (player, opponent) in winning_pairs:
        while True:
            reward = input("You won! gain levels or gain luck? (levels/luck): ").strip().lower()
            #gabe owners?
            if reward in ("life", "luck"):
                break
            print("Enter life or luck.")
        if reward == "levels":
            level = level + 1
            print(f"You gained 1 level, so you are at {level} levels.  You use a tax loophole so the feds don't tax it.")
            t.sleep(3)
            print("You get audited by the IRS.  you consider moving to a tax haven.")
        else:
            luck += 1
            print(f"Luck increased to {luck}.  She still blocked you on chess.com")
    else:
        print("You lost this practice round. Brutal.  Try again later, chudlet.")
    return health, level, luck

def mikah(luck, health):
        print("You approach true greatness.  The fate of the world rests in your hands.  No pressure")
        t.sleep(5)
        print("You go to the top floor of the Blocker building.  There, Mikah stands.  He's 167 cm tall and weighing 119 lbs.")
        t.sleep(4)
        print("Mikah turns around, and asks you why you are here.  You claim you're here on business.  Mikah understands.")
        t.sleep(3)
        print("Mikah asks: 'why would you, frodo, wanna stop me?'  You cite the popular support against the Mikah empire")
        t.sleep(5)
        print("Mikah says: So be it, Frodo.  You have made a mistake.  I have 1 million power in rise of kingdoms.")
        pyg.mixer.init()
        pyg.mixer.music.load("fbs.mp3")
        pyg.mixer.music.play()
        pyg.mixer.music.play(loops=67)
        t.sleep(4)
        print("The University tries using its 3-inch M1902 field gun on Mikah.  The gun jams once it realizes its pointed at King Mikah")
        t.sleep(4)
        print("Mikah's aura makes your armies attack's useless.  It seems only a critical hit can do the trick.")
        t.sleep(5)
        mhp = enemy_catalog["Mikah"]
        while mhp > 21 and health > 0:
                #vibecode
                print("You try your luck and rush the Dictator...")
                t.sleep(4)
                coin=r.randint(1,15)
                Mikah_luck = luck - 3
                
                if luck > (coin + Mikah_luck):
                        mhp=mhp-20
                        print(f"A lucky hit!  Mikah has {mhp} health left!")
                        t.sleep(4)
                else:
                        print(f"You missed!  Mikah chuckled.  He has {mhp} health left.")
                        t.sleep(4)
                        print("Mikah attacks next.  He pulls out an old penny.  It has been rigged to favor Big Mikah.  He flips it...")
                        t.sleep(4)
                        cf=r.randint(1,2)
                        ug=input("Heads or Tails? ")
                        if str(ug) == "Heads" or str(ug) == "Tails":
                                smth=r.randint(1,4)
                                if smth == cf:
                                        print("Mikah's attack backfires!  He takes 10 damage!  Mikah retrieves a Narnia themed bandaid.  It expired.")
                                        mhp = mhp-10
                                        t.sleep(4)
                                        print(f"Mikah has {mhp} health remaining.  You have {health} HP")
                                elif smth == 3:
                                        health = health - 8
                                        print(f"Mikah does 8 damage.  Your health insurance declines.  You have {health} HP left")
                                        
                                else: 
                                        health = health - 5
                                        print(f"Mikah does 5 damage.  That may leave a mark.  You have {health} HP left.")
                                        
                        else:
                                print("Mikah says you must pick one of the two.  The federal government takes away some of your free will.  Lizard people am I right?")
                                t.sleep(5)
                                health=health-4
                                print(f"Without your free will, you take 4 damage.  You now have {health} HP left.")
                                t.sleep(4)
                rg(str(r.randint(1,9)))
                t.sleep(5)
        if mhp == 20 and health > 0:
                pyg.mixer.music.stop()
                t.sleep(1)
                rg("10")
                t.sleep(5)
                print("Mikah laughes quietly.  He seems battered and on the verge of giving out.  He also has not slept for a long time...")
                t.sleep(4)
                print("Mikah glances at the figure he hallucinated behind you.  Mikah then sends your search history to the French Government.")
                t.sleep(5)
                print("You ask Mikah to surrender.  Mikah declines.  Despite the odds against him, Mikah is determined.")
                pyg.mixer.init()
                pyg.mixer.music.load("final.mp3")
                pyg.mixer.music.play()
                t.sleep(5)
                print("A different soundtrack is playing.  Only a super critical hit can stop Mikah now.")
                t.sleep(3)
                while mhp == 20 and health > 0:
                        #final phase
                        e=r.randint(1,6)
                        j=input("Guess a number between 1 and 6. Type an integer: ")
                        if e == j:
                                print("GREAT GUESS!  Mikah has been defeated!  He did not list you as the benficiary of his will...")
                                mhp = 0
                                t.sleep(1)
                                print("The rocket was launched, however Mikah's Aura wasn't around to protect the rocket.  It was intercepted with relative ease by the university.")
                                with open("final_report.txt", "w", encoding="utf-8") as fr:
                                        fr.write(f"{rg('final_vic')}\n")
                                        randy=r.randint(1,2)
                                        if randy == 1:
                                                fr.write(f"{rg('e2')}\n") 
                                        else:
                                                fr.write(f"{rg('e1')}\n")
                                        
                                        fr.write(f"{rg('eF')}\n")
                        else:
                            
                            print("You guessed wrong.  Mikah counterattacks.  It does 5 damage.")
                            health=health-5
                            t.sleep(3)
                            print(f"You have {health} HP remaining.  Use it wiser.")
                            p = str(r.randint(1,9))
                            rg(p)
        if health <= 0:
            print("Mikah defeated you!  Don't worry, you are not the first, nor the last. lmao")
            t.sleep(5)
            rg("eL")
            t.sleep(4)
            quit()
        return(health)

def play_song(enemy):
    if enemy == "squirell" or enemy == "pigeon":
        pyg.mixer.init()
        pyg.mixer.music.load("sb_goliath.mp3")
        pyg.mixer.music.play(loops=67)
    elif enemy == "mikah":
        pyg.mixer.init()
        pyg.mixer.music.load("fbs.mp3")
        pyg.mixer.music.play(loops=67)
    else:
        pyg.mixer.init()
        pyg.mixer.music.load("final.mp3")
        pyg.mixer.music.play(loops=67)

def frodo_attack(level):
    atk=r.randint(1,3)+level*2
    print(f"you attack, dealing {atk} damage")
    return atk


def use_item():
    print(1)


def level_up(level, new):
    level = level + new
    print("you leveled up!  ")

def start_turn():

def evans_library(health, level, damage):
    return health, level, luck, item
def utility_plant(health, level,damage):
    return health, level, luck, item
def choose_function(name):

def update_log():



def credit(win):

def print_log():

def start():
    try:

    execpt: 

def check_coin():
