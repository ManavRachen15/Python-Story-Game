import random,time

global health
health = 30

chance = None 

#fight scenes
def subh(x):
   global health
   health = health - x
   print (health)

def addh(x):
   global health
   if health >= 30:
      health = 30
   health = health + x
   print (health)

def fight():
   if choice == "attack":
    chance = random.randint (1,6)
    if chance <= 3:
        print("\nYou lost health from the fight")
        subh(5)
    elif chance > 3:
        time.sleep(2)
        print("\nyou killed the enemy")
        print("\nThe enemy disintagrated and turned into dust your path was clear")

def sins():
   chance = None 
   if choice == "attack":
    chance = random.randint (1,10)
    if chance <= 5:
        subh(15)
        print("\nYou lost health from the fight and you lose the weapon")
    elif chance == "6,7,8":
       print("you killed the sin")
   if chance == "9 or 10":
      print("you killed the sin and collected there special weapon")
      print("how how have you a pithetic human defeat a god. he disntagrates to dust and gets blown away")

def lord():
   if choice == "attack":
      chance = random.randint (1,1)
   if chance == "1":
      print("Congratulations you have killed lord valad and his sins you stopped his war over middle earth")
   
#text files for the characters and intro
txt_file= open("intro.txt", "r")
h = txt_file.read()
print(h)
txt_file.close()

Class = input("")
if Class == ("tank"):
    text_file=open("tank.txt","r")
    for line in range(9):
        x = text_file.readline()
        print(x)
        time.sleep(2)
    text_file.close()
elif Class == ("assassin"):
    text_file=open("assassin.txt","r")
    for line in range(8):
        x = text_file.readline()
        print(x)
        time.sleep(2)
    text_file.close()
elif Class == ("wizard"):
    text_file=open("wizard.txt","r")
    for line in range(6):
        x = text_file.readline()
        print(x)
        time.sleep(2)
    text_file.close()
    
print("\n\nyou have entered the realm of middle earth")
c1 = input("\nyour mission should you choose to accept, is to save an new born from the lord VALAR, do you accept? (y/n")

if c1 == "n":
    print("Thanks to you middle earth has been rulled over")
    

if c1 == "y":
    print("\nYou have just been teleported to middle earth where would you like to go north or east")
    input("n  e)")
    if "n" or "e":
        print("\nyou are walking on a deserted train line the time is 11:00 pm you sence something around you but you dont know what it is the fog is making it hard for you to see there is a vile smell coming from behind you")

time.sleep(2)

print("\nyou have been approached by a demon thats in a shape of a dog you only have two choices run away or attack with you bare knuckles")
choice = input("attack or run")

if choice == "attack":
    chance = random.randint (1,6)
    if chance <= 3:
        subh(5)
        print("\nYou lost 5 health from the fight the demon ran away")
    elif chance > 3:
        time.sleep(2)
        print("\nyou killed the demon")
        print("\nThe demon disintagrated and turned into dust your path was clear")
if choice == "run":
    print("\nThe dog has lost your scent and vanished in thin air")
    
time.sleep(2)

print("\nyou walked for 2 hours running low on food and water you see an ambanded hut surrounded by orcs what do u do attack, distract or sneak past the orcs")
choice = input("attack, distract or sneak")

if choice == "attack":
   print("\nThe orcs gained amour and weapons and prepared to attack")
   time.sleep(2)
   fight()
    
if choice == "distract":
   print("\nyou created a diversion with a rock the orcs are gone temporarily")

if choice == "sneak":
   print("\nyou snook past the orcs sussecfully and approached the hut")

time.sleep(2)

print("\nyou entered the hut slowley with out alerting the orcs you feel an omnipotent presence and an faint whisper saying the forest you look to your right and you see a map of a strange castle you take the map just in case it might be useful, below it has a a chest containing 3 items a bow, sword and a spade what will you choose if you choose sword type in attack")
choice = input("bow, sword or spade")

if choice == "bow":
   print("\nGreat choice adventurer")
   time.sleep(2)
   print("you pick up the bow and through the window you see the captain of the orcs you climb on top of the hut you take aim and shoot the captian the arrow whistled through the air and stabs the captain through the heart. the orcs run to the dead captain this gives you a great optunity to escape into the forest.")
   
if choice == "attack":
   print("\nGreat choice adventurer")
   time.sleep(2)
   print("you pick up the sword you killed many orcs in the proccess until you saw the captian carrying an axe")
   
   if choice == "attack":
    chance = random.randint (1,6)
    if chance <= 3:
        subh(10)
        print("\nYou lost health from the fight")
    elif chance > 3:
        time.sleep(2)
        print("you killed the capatain and gained a new weapon but now all the rest of the orcs are chasing you into the forest")
        
if choice == "spade":
   print("\nGreat choice adventurer")
   time.sleep(2)
   print("you pick up the spade you dig under the floor boards of the hut and escape to the forest however the orcs found the hole and now are following your trail")
time.sleep(2)

print("\nThe forest was a dark gloomy with wisperes flowing through the trees carried by the wind and a strong scent of nature spreads through the forest. you hear the same whisper u heard previosuly this time it sounded clearer it said follow the trees it will create a path. The trees opened up to a path that took you to the ents the keepers of the forest they spoke saying the world is in trouble there is one who can save us all and thats the new born child in the castle of VALAD this ring the ents replayed this can save this world all you have to do is place this ring on the new borns finger now go from here i hate humans.")
time.sleep(2)
      
print("\nyou found a health potion would you like to use it, it will recover 10 health")
choice = input("yes or no")


time.sleep(2)


if choice == "yes":
      addh(10)
if choice == "no":
      print("\nwhere would you like to travel")
      choice = input("w e")
time.sleep(2)




print("\nOn the map there is text written saying there are 3 deadly sins the most powerful servants to VALAR will rise and stop the one who tries rescuing the new born child the names of these sins are called dunger, mealder and finally the strongest of them the leader malace.")

print("\nwhile on your path walking out of the forest a lightning bolt struck down infront of you the one mealder stands in front of you with his mighty sword and shield all you have is an axe killing him may allow you to collect his weapon what do you do")
while True:
   choice = input("attack or run")
   if choice == "run":
      print("\nThe sin casted a spell you cant run away you must fight")
      continue
   elif choice == "attack":
      sins()
      break

time.sleep(2)   

print("\nThe magical barrier has been disarmed you can continue your journey saving the new born you look at the map and it said you need to collect the magical boots of middle earth to save the new born you see a health postion next to a tree what do you do")
#health()

print("\nYou travel to the cave and the signs say beware of the traps mwahahahahah you travel further into the cave you step on a pressure pad what do you do")
choice = input("run straight or run out")
if choice == "run straight":
   print("\nthe cave got blocked behind you you need to find another way out, you find a key next to a dead skeleton")
if choice == "run out":
   print("\nthe cave is blocked you missed the trap all you have to do is walk further into the cave and you find a key next to a dead skeleton")

time.sleep(2)
print("\nyou continue the journey and stumble apon a chest you tried to open it but it was locked then you reliased that you have a key you iserted the key and the chest opened with the magical boots in them you put them on and you were able to walk on any surface as well as up walls and roofs.")

time.sleep(2)

print("\nAnother sin entered the cave behind you this time it was dunger his weapon is a staff you what do you do")
sins()

time.sleep(2)
print("\nyou barley escape the cave with your life as you continue your journey getting closer and closer to the castl you find a shop/bar you eneter the shop and speak to the owner he sells you health pots, ale and food. you have many weapons on you the bow for example would you like t sell it for health potions?")
choice = input("yes or no")
addh(10)
time.sleep(2)
print("\nyou leave the shop and you continu the quest")

print("you apprach the last castle a demon gaurad appraches in front of you its not letting you enter the bridge of the castle what do you do")
choice = input("attack or sneak")

if choice == "sneak":
   print("There is no other path to the castle you must fight")
   input("attack")

if choice == "attack":
   print("pick yout weapon staff, sword, bow")
   input("staff, sword or bow")
   fight()

print("you start to walk on the bridge but you started to feel something a tremour everythingt around you was rumbling as you looked behind you a stampeid of demons and orcs are after you those orcs where from the hut they followed you all the way. as you started to run the final sin appeard infront of you on the bridge he laughed and roared all the orcs and demons stopped and disentagrated the last sin killed them. He repied saying those minnions started to annoy me, there he was the strongest sin malace his weapon of choice a ball whip with a hooked blade at the front.")  
choice = input ("attack")
sins()

time.sleep(2)

print("you reach the castle doors you touch it and get zaped by some electrcity there is a tower with a window on top you climb the tower with your magical boots and you climb imto the tower and a demon guard stand in front of the tower door")
choice = input("attack")
fight()

print("you sneak down the stairs and you hear a baby cry you track where the crying came from but the door is locked suddenly you get teloported to a room infront of you is lord valar you must kill him to save the baby")
choice = input("attack")
lord()

print("you find the key after defeating valad, you open the door to the room the baby was in but you see that he was a dragon you put the holy ring on his pinky and he turned into a human the war has stopped and middle earth has been saved thank you for playing.")

input("press enter to escape")



   





    




 
