import random as r 
import time as t
import tkinter as tk
import pygame as pyg

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
            "b2": "The squirell reads some feminist literature. It is 8 inches tall at most.",
            "p": "you remember the brainrot pigeon videos.  so does the pigeon.",
            "p1": "the pigeon takes a crap on your car while you weren't looking.  Chirp Chirp, Chud.",
            "p2": "the pigeon looks at you with disgust and hatred.  Mikah accepted it for who it was, apparently."}
        
        statement=print(dih[a])
        return(statement)
#hashtag awesome

def ts():
    print("the button works")

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
        rules.add_command(label="See Rules", command=ts)
        rules.add_command(label="Rodrick Rules", command=ts)
        rules.add_command(label="Exit", command=root.quit)
        rules.add_separator()
        
        status = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="see map")
        status.add_command(label="in progress", command = ts)
        
        root.mainloop()

enemy_catalog={
    "squirell": 20,
    "Pidgeon": 30,
    "Mikah": 80}

loot={
    "squirell": "nuts and a fry",
    "mikah": "wallet",
    "pigeon": "shiny pebbles"}

level = 1
health = 50 + 2*level
enemy_health=20  
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
                                t.sleep(5)
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
                            
                            print("You guessed wrong.  Mikah counterattacks.  He does 5 damage.")
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
                                        


itembag = []
kill_log = []


def sqf():
    
    enemy_health = enemy_catalog["squirell"]

    pyg.mixer.init()
    pyg.mixer.music.load("sb_goliath.mp3")
    pyg.mixer.music.play()


    # Keep the script running while the audio plays
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
        #defeated
        pyg.mixer.music.stop()
        print("You won the battle, but did you win the war...")
        t.sleep(3)
        sl = loot["squirell"]
        itembag.append(sl)
        kill_log.append("squirell")
        print(f"you loot {loot["squirell"]} from the squirell.  (s)he was vaccinated.")
        t.sleep(2)
        
    return level, itembag, kill_log, health

def pigeon(health):
    pHP = 30
    print("a pigeon dives for your hair in the name of Mikah.")
    pyg.mixer.init()
    pyg.mixer.music.load("sb_goliath.mp3")
    pyg.mixer.music.play()
    t.sleep(2)
    while pHP > 30:
        try:
            ber=int(input("type an even or odd number as a number: "))
            con=r.randint(0,1)
            if con == (ber % 2):
                print("Direct hit!  You do 5 damage to the pigeon.")
                pHP = pHP-5
                t.sleep(3)
                print(f"the pigeon has {pHP} health left.")
            else:
                print("Your attack missed!  Your army attacks:")
                t.sleep(3)
                atk=r.randint(1,5)
                pHP = pHP - atk
                print(f"Your army attacks, doing {atk} damage.  the pigeon has like {pHP} health left.")
                t.sleep(3)
                print("the pigeon attacks!  It dives toward you, dealing 3 damage!  BROOOOOOO!")
                health = health - 3
                print(f"You have {health} HP left.")
                t.sleep(2)
                pdi= r.randint(0,2)
                if pdi == 0:
                    rg("p")
                elif pdi == 1:
                    rg("p1")
                else:
                    rg("p2")

        except ValueError:
            print("You ain't all that and a bag of fries lil bro...")
            t.sleep(3)
            health = health - 3
            print("The pigeon takes the initiative since you wasted a turn, dealing 3 damage!")
            t.sleep(2)
            print(f"You have {health} HP left.  The pigeon grows bolder.")
    if pHP <= 0:
        print("The pigeon has been defeated!")
        pyg.mixer.music.stop()
        t.sleep(3)
        pyg.mixer.music.load("wse.mp3")
        pyg.mixer.music.play()
        print("You get a shiny pebble from the pigeon.  You lose it immediatly.")
    return health



def play_minigame(luck, items, remaining_dungeons, health):
    """AI-assisted. Guess a dungeon's hidden number to earn a luck item.

    Return (new_luck, item_name, dungeon_name) on success, otherwise None.
    The caller owns inventory and dungeon-list updates; inputs stay unchanged.
    """
    if not remaining_dungeons:
        print("All dungeons have already been captured.  Go face mikah you coward.")
        return None
    while True:
        print("Available dungeons: " + ", ".join(remaining_dungeons))
        selection = input("Choose a dungeon: ").strip().lower()
        matches = [name for name in remaining_dungeons if name.lower() == selection]
        if matches:
            dungeon = matches[0]
            break
        print("Choose one of the remaining dungeons.")
    print("you order your army foward to attack a Mikah Imperial Stronghold.")
    nSq = r.randint(0,1)
    nP = r.randint(0,1)

    if selection == "annex" and "annex" not in remaining_dungeons:
            annex(health, luck)
            

    rewards = {"squirell": ("Zach chestplate", 2), "Pidgeon": ("Campus lucky charm", 3)}
    item, bonus = rewards.get(dungeon, (f"{dungeon} luck token", 1))
    if item in items:
        print("You already own this dungeon's reward.")
        return None
    print(f"Dungeon complete! You earned {item} (+{bonus} luck).")
    return luck + bonus, item, dungeon

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
    return lives, luck

dl = ["annex", "Evans", "HECC Building", "Thompson Hall", "HALB", "Utility Plant"]
item_list = ["Spirit Stick", "bookworm's knife", "USB Drive", "keys", "Pure Silicon", "M1902 feild gun"]


def annex(health, level):
    print("You enter the Mikah stronghold of the annex building.  Sporadic fighting erupts around you and your small task force.")
    t.sleep(5)
    print("You recieve a radio message from the Dean: You must seize some spirit sticks stashed somewhere safe.")
    t.sleep(4)
    print("heres a pop up explaining a spirit stick, please read:")
    t.sleep(3)
    root = tk.Tk()
    img = tk.PhotoImage(file="annexobj.png")
    #mikah
    label = tk.Label(root, image=img)
    label.image = img
    label.pack()
    #mikah
    root.mainloop
        
    sqf(health)
    health = health + 10
    pigeon(health)
    
    print("XP gained: 5.  You leveled up! Due to Democrat Fiscal policy, your levels were given away")
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
    root.mainloop
    
    print("Queen Revillie herself gives you 2 levels because you were so brave.")
    level = level + 2
    health = health + 2*level
    item_bag.append(item_list[0])
    return(health, level)

def evans(health, level):
        print("You enter through a window like a boss. All the shy people are unimpressed.")
        t.sleep(3)
        print("your orders is to find the knife of a  bookworm.  Someone can't open a package...")
        squirel(health, level)
        print("With the first floor cleared, you move to the 4th level.  Thats where the heats at.")
        t.sleep(2)
        pigeon(health, level)
