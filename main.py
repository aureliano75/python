from sys import exit
import colorama
from colorama import Fore, Back, Style
colorama.init()

inventory = ["torch","bandage"]
chest = ["sword","bandage"]
table = ["key"]
health = 3

def useone():
  global health
  action = input("Use item: ")
  if action == "bandage":
    if health < 3:
      health += 1
      inventory.remove('bandage')
      print("Knight: ", "\"I feel better.\"")
      print("Health + 1")
      print("------------------------------------")
      one();
    elif health == 3:
     print("Health is full!")
     print("------------------------------------")
     one();
  elif action == ("torch"):
    print("Knight","\"Finally I can see!\"")
    print("------------------------------------")
    inventory.remove('torch')
    two();
  else:
    print("The knight doesn't have any " + str(action) + ", try again!")
    one();

def usetwo():
  global health
  action = input("Use item: ")
  if action == "bandage":
    if "bandage" in inventory:
      if health < 3:
        health += 1
        inventory.remove('bandage')
        print("\"I feel better.\"")
        print("Health + 1")
        one();
      elif health == 3:
        print("Health is full!")
        two();
    elif "bandage" not in inventory:
      print("The knight doesn't have any bandages left.")
      two;
  else:
    print("The knight doesn't have any " + str(action) + ", try again!")
    usetwo();

def damage():
  try: 
    global health
    health = health - 1
    print("Health - 1")
    if health == 0:
      print("The knight has died. Please restart.")
  except:
    print("Error, restarting...")
    inventory = ["torch","bandage"]
    chest = ["sword","bandage"]
    table = ["key"]
    health = 3

def checkstatus():
  global health
  print("************************************")
  print("Inventory: ")
  print(*inventory, sep = ", ") 
  print("Health: " + str(health))
  print("************************************")

def one():
  print("Knight: ", "\"Where... Where am I?\"")

  print("1 > Look around")
  print("2 > Explore in the darkness")
  print("3 > Use item")
  print("4 > Health and inventory")

  action = input("Do: ")

  if action == "1":
    print("------------------------------------")
    print("Knight: ", "\"I can't see anything...\"")
    print("------------------------------------")
    one();
  elif action == "2":
    print("------------------------------------")
    print("Knight: ", "\"OUCH! There's something lurking in the darkness. Better find some light sources.\"")
    damage();
    print("------------------------------------")
    one();
  elif action == "3":
    useone();
  elif action == "4":
    checkstatus(); 
    one();
  else:
    print("Invalid option.")
    print("------------------------------------")
    one();

def two():
  print("With the glimmer of the torch, the knight sees a steel door and a wooden door in front of him.")

  print("1 > Try the steel door")
  print("2 > Try the wooden door")
  print("3 > Use item")
  print("4 > Health and inventory")

  action = input("Do: ")
  print("------------------------------------")

  if action == "1":
    if "key" in inventory:
      inventory.remove("key")
      print("The knight opened the steel door.")
      print("------------------------------------")
      four();
    elif "key" not in inventory:
      print("Knight: ", "\"It seems the steel door is locked...\"")
      print("------------------------------------")
      two();
  elif action == "2":
    three();
  elif action == "3":
    usetwo();
  elif action == "4":
    checkstatus();
    two();
  else:
    print("Invalid option.")
    print("------------------------------------")
    two();


def start():
  print("------------------------------------")
  print("A knight wakes up in a dungeon.")
  print( "Surrounded by darkness.")
  print("------------------------------------")
  one();

def three():
  global chest
  global table
  print("Knight: ", "\"Hmmm... It's not as big as I thought.\"")
  print("1 > Search the chest")
  print("2 > Check out the table")
  print("3 > Look at the painting")
  print("4 > Leave the room")

  action = input("Do: ")

  if action == "1":
    if not chest:
      print("The chest is empty.")
      three();
    else:
      print("Knight: ","\"The chest is locked with a combination lock.\"")
      passcode = input("Enter the combination (8 digits): ")
      if passcode == "14960109":
        inventory.append("bandage")
        inventory.append("sword")
        print("*Bandage added to inventory")
        print("*Sword added to inventory")
        chest.remove("sword")
        chest.remove("bandage")
        print("------------------------------------")
        three();
      else:
        print("Wrong combination!")
        three();
  elif action == "2":
    if not table:
      print("Knight: ", "\"I just searched the drawer.\"")
      print("------------------------------------")
      three();
    else:
      inventory.append("key")
      print("*Key added to inventory")
      print("------------------------------------")
      three();
  elif action == "3":
    print("Knight: ", "\"Interesting... A portrait of King Russo, 1496 - Jan - 9th.\"")
    print("------------------------------------")
    three();
  elif action == "4":
    print("------------------------------------")
    two();
  else:
    print("Invalid option.")
    print("------------------------------------")
    three();

def four():
  print("Behind the steel door，a golden hallway, magnificant and luxurious.")
  print("Another door wide open on the other side of the hallway, bright as day.")
  print("Between the knight and the his way, sleeps a vicious beast, guarding the door of light. Surrounding the beast, the bones of a thousand fallen knights.")
  print("1 > Slay the beast")
  print("2 > Sneak pass the beast")
  print("3 > Leave the room")

  action = input("Do: ")
  print("------------------------------------")

  if action == "1":
    if "sword" in inventory:
      print("The beast was ruthless, but the knight fought valiantly.")
      print("As the beast fell, the magic of the dungeon fades, revealing the stairs to the world above.")
      print("A princess rushes out of the door of light, hugging the exhausted knight.")
      print("\"You've saved me, my fearless knight,","says the princess.")
      print("\"You've slayed the beast, set me free.\"")
      print("The knight suddenly remembers his quest：slay the beast, save the princess.")
      print("Thousands of knights wakes up in the dungeon with no memory.")
      print("Prophesy says only the bravest one could slay the beast, save the princess.")
      print(Fore.GREEN +"Congrats! The knight has prevailed!")
      print("------------------------------------")
    elif "sword" not in inventory:
      print("The knight fought valiantly, but the beast was ruthless.")
      print("Without a weapon, the knight stood no chance.")
      print(Fore.RED +"The knight has died. Please restart.")
      print("------------------------------------")
      exit(0)
  elif action == "2":
    print("The knight sneakes pass the beast and approaches the door of light.")
    print("Scared and exausted, the knight thought he was finally free.")
    print("Before the knight could walk into the light, princess rushes out of the door of light, cheers with excitement.")
    print("\"You've saved me, my fearless knight,","says the princess.")
    print("\"You've slayed the beast, set me free.\"")
    print("The beast wakes with the cheers of the princess, killing her instantly.")
    print("The knight suddenly remembers his quest：slay the beast, save the princess.")
    print("Thousands of knights wakes up in the dungeon with no memory.")
    print("Prophesy says only the bravest one could slay the beast, save the princess.")
    print("But it's all too late.")
    print(Fore.RED +"The princess has died. Game over.")
    print("------------------------------------")
    exit(0)
  elif action == "3":
    two();
  else:
    print("Invalid option.")
    print("------------------------------------")
    four();

start();