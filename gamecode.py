import random as r 
import time as t
import tkinter as tk
import pygame as pyg
from PIL import Image, ImageSequence, ImageTk
def rg(a):
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
#hashtag awesome

dl = ["annex", "Evans", "HECC Building", "Thompson Hall", "HALB", "Utility Plant"]
item_list = ["Spirit Stick", "bookworm's knife", "USB Drive", "keys", "Pure Silicon", "M1902 feild gun"]
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
        file_menu.add_command(label="Quit Game", command=ts)
        file_menu.add_command(label="save", command=ts)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=root.quit)
        
        # 4. Create a "game" dropdown menu
        game_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="game", menu=game_menu)
        game_menu.add_command(label="Campaign", command=ts)
        game_menu.add_command(label="Training", command=ts)
        game_menu.add_command(label="Fight Big Mikah", command=ts)
        game_menu.add_separator()
        game_menu.add_command(label="Exit", command=root.quit)
        
        rules = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Rules", menu=rules)
        rules.add_command(label="See Rules", command=see_rules)
        rules.add_command(label="Rodrick Rules", command=ts)
        rules.add_command(label="Exit", command=root.quit)
        rules.add_separator()
        
        status = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="see map")
        
        root.mainloop()

enemy_catalog={
    "squirell": 20,
    "Pidgeon": 30,
    "Mikah": 80}
level = 1
health = 50 + 2*level
enemy_health=20  
def challenge_mikah(luck, health):
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



while enemy_health > 0:
    dice=input("guess a number between 1 and 5: ")
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
    root = tk.Tk()
    img = tk.PhotoImage(file="image.png")
    #mikah
    label = tk.Label(root, image=img)
    label.image = img
    label.pack()
    #mikah
    root.mainloop()
