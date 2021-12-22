import time, os, random, webbrowser
from gtts import gTTS
from tkinter import *


root = Tk()

root.geometry("100x100")

start = Button(root,text = "Start",bd = "5", command = root.destroy)
start.pack(side="top")

def pokeRoll():
    webbrowser.open("https://www.pokemon.com/us/pokedex/")
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=oHg5SJYRHA0")
    
pokedex = Button(root,text = "Pokedex",bd="5",command =pokeRoll)
pokedex.pack(side="top")


root.mainloop()

welcome = gTTS(text="Think of a pokemon you want me to guess, answer yes or no to my questions and i will guess your pokemon")
mememe = gTTS(text = "Make sure your pokemon is in the range 1-100")
welcome.save("start.mp3")
mememe.save("caution.mp3")
os.system("start.mp3")
time.sleep(7)
os.system("caution.mp3")
time.sleep(5)


def pokemonCollection():
    key = list(pokemon.keys())
    file = open("pokemonCollection.txt", "a")
    file.write("\n" + str(key[-1]))
    x = random.randint(0, 1000)
    if x == 5:
        webbrowser.open("https://www.youtube.com/watch?v=oHg5SJYRHA0")


def remove():
    if len(pokemon) == 1:
                key = list(pokemon.keys())
                pokeBowl=gTTS(text="you're thinking of "+ str(key[-1]), lang="en", slow=False)
                pokeBowl.save("pokeBowl.mp3")
                os.system("pokeBowl.mp3")
                time.sleep(2)
                os.system("collectiont.mp3")
                pokemonCollection()
                exit()

def guesser(question, value):
    if question == "yes":
        for x in list(pokemon):
            if value not in pokemon[x]:
                del[pokemon[x]]
                remove()
                
            
    elif question == "no":
        for x in list(pokemon):
            if value in pokemon[x]:
                del[pokemon[x]]
                remove()
    return question

def pokeType(types):
  mp3 = gTTS(text = "is your pokemon a " + types + " type?")
  mp3.save("type.mp3")
  os.system("type.mp3")
  question = input("")
  return question

def pokeStage(stage):
    mp3 = gTTS(text = "is your pokemon a " + stage + " pokemon?")
    mp3.save("stage.mp3")
    os.system("stage.mp3")
    question = input("")
    return question
    
                
            
pokemon = {'squirtle' : ["water", "firstPartner","firstStage","moreEvo","blue"],
           'charmander ' : ["fire", "firstPartner","firstStage","difEvoType","moreEvo","orange"],
           "wartortle" : ["water", "secondStage","blue"],
           "charmeleon" : ["fire","secondStage","difEvoType","red"],
           "bulbasaur" : ["grass","poison", "firstPartner", "hasPlant","firstStage","moreEvo","green"],
           "ivysaur" : ["grass", "hasPlant", "poison","2types","secondStage","green"],
           "venusuar" : ["grass", "canMegaEvolve", "hasPlant", "poison","2types","thirdStage","green"],
           "mega-venusaur":["grass", "mega", "hasPlant", "poison","2types","finalStage","green"],
           "blastoise" : ["water", "canMegaEvolve","thirdStage","blue"],
           "mega-blastoise" : ["water", "mega","finalStage","blue"],
           "charizard" : ["fire", "flying", "canMegaEvolve","2types","thirdStage","difEvoType","orange"],
           "mega-charizard-x" : ["fire", "dragon", "mega","2types","finalStage","black"],
           "mega-charizard-y" : ["fire", "flying", "mega","2types","finalStage","orange"],
           "caterpie" : ["bug","firstStage","difEvoType","moreEvo","green"],
           "metapod" : ["bug","secondStage","difEvoType","green"],
           "butterfree" : ["bug", "flying","2types","thirdStage","finalStage","purple"],
           "weedle" : ["bug", "poison","2types","firstStage","moreEvo","brown"],
           "kakuna" : ["bug", "poison","2types","secondStage","yellow"],
           "beedrill" : ["bug", "poison", "canMegaEvolve","2types","thirdStage","yellow"],
           "mega-beedrill" : ["bug","poison","mega","2types","finalStage","yellow"],
           "pidgey" : ["normal", "flying","2types","firstStage","moreEvo","brown"],
           "pidgeotto" : ["normal", "flying","2types","secondStage","brown"],
           "pidgeot" : ["normal", "flying","2types","thirdStage","brown"],
           "mega-pidgeot" : ["normal","flying","mega","2types","finalStage","brown"],
           "rattata" : ["normal","firstStage","purple"],
           "raticate" : ["normal","secondStage","finalStage","brown"],
           "spearow" : ["normal", "flying","firstStage","brown","2types"],
           "fearow" : ["normal", "flying","2types","secondStage","finalStage","brown"],
           "ekans" : ["poison","firstStage","purple"],
           "arbok" : ["poison","secondStage","finalStage","purple"],
           "pikachu" : ["eletric","secondStage","yellow"],
           "raichu" : ["eletric","thirdStage","finalStage","yellow"],
           "sandshrew" : ["ground", "firstStage","brown"],
           "sandslash" : ["ground", "secondStage","finalStage","brown"],
           "nidoran-female" : ["poison", "firstStage","female","difEvoType","moreEvo","blue"],
           "nidorina" : ["poison", "secondStage","female","difEvoType","blue"],
           "nidoqueen" : ["poison", "ground", "thirdStage","finalStage","female","2types","blue"],
           "nidoran-male" : ["poison", "firstStage","male","difEvoType","moreEvo","purple"],
           "nidoran" : ["poison", "secondStage","male","difEvoType","purple"],
           "nidoking" : ["poison", "ground", "thirdStage","finalStage","male","2types","purple"],
           "clefairy" : ["fairy", "firstStage","pink"],
           "clefable" : ["fairy","secondStage","finalStage","pink"],
           "vulpix" : ["fire", "firstStage","orange"],
           "ninetales" : ["fire", "secondStage","finalStage","brown"],
           "jigglypuff" : ["normal", "fairy", "firstStage","2types","pink"],
           "wigglytuff" : ["normal","fairy","secondStage","finalStage","2types","pink"],
           "zubat" : ["poison","flying","firstStage","2types","blue"],
           "golbat" : ["poison","flying","secondStage","finalStage","2types","blue"],
           "oddish" : ["grass","poison","firstStage","2types","blue"],
           "gloom" : ["grass","poison","secondStage","2types","blue"],
           "vileplume" : ["grass","poison","thirdStage","finalStage","2types","blue"],
           "paras" : ["bug","grass","firstStage","2types","orange"],
           "parasect" : ["bug","grass","secondStage","finalStage","2types","orange"],
           "venonat" : ["bug","poison","firstStage","2types","purple"],
           "venomoth" : ["bug","poison","secondStage","finalStage","2types","purple"],
           "diglett" : ["ground","firstStage","brown"],
           "dugtrio" : ["ground","secondStage","finalStage","brown"],
           "meowth" : ["normal","firstStage","brown"],
           "persian" : ["normal","secondStage","finalStage","brown"],
           "psyduck" : ["water","firstStage","yellow"],
           "golduck" : ["water","secondStage","finalStage","blue"],
           "mankey" : ["fighting","firstStage","brown"],
           "primeape" : ["fighting","secondStage","finalStage","brown"],
           "growlithe" : ["fire","firstStage","orange"],
           "arcanine" : ["fire","secondStage","finalStage","orange"],
           "poliwag" : ["water","firstStage","difEvoType","moreEvo","blue"],
           "poliwhirl" : ["water","secondStage","difEvoType"," blue"],
           "poliwrath" : ["water","fighting","thirdStage","finalStage","2types","blue"],
           "abra" : ["psychic","firstStage","moreEvo","yellow"],
           "kadabra" : ["psychic","secondStage","yellow"],
           "alakazam" : ["psychic","thirdStage","canMegaEvolve","yellow"],
           "mega-alakazam" : ["psychic","mega","finalStage","yellow"],
           "machop" : ["fighting", "firstStage","moreEvo","gray"],
           "machoke" : ["fighting","secondStage","gray"],
           "machamp" : ["fighting","thirdStage","finalStage","gray"],
           "bellsprout" : ["grass","poison","firstStage","2types","moreEvo","yellow"],
           "weepinbell" : ["grass","poison","secondStage","2types","yellow"],
           "victreebel" : ["grass","poison","thirdStage","finalStage","2types","yellow"],
           "tentacool" : ["water","poison","firstStage","2types","blue"],
           "tentacruel" : ["water","poison","secondStage","2types","blue","finalStage"],
           "geodude" : ["rock","ground","firstStage","brown","2types","moreEvo"],
           "graveler" : ["rock","ground","secondStage","brown","2types"],
           "golem" : ["rock","ground","thirdStage","finalStage","green","2types"],
           "ponyta" : ["fire","firstStage","brown"],
           "rapidash" : ["fire","secondStage","brown","finalStage"],
           "slowpoke" : ["water","psychic","2types","firstStage","pink"],
           "slowbro" : ["water","psychic","2types","secondStage","canMegaEvolve","pink"],
           "magnemite" : ["steel","electric","2types","firstStage","moreEvo","gray"],
           "magneton" : ["steel","electric","2types","secondStage","gray"],
           "farfetch'd" :["normal","flying","2types","firstStage","brown","finalStage"],
           "doduo" : ["normal","flying","2types","firstStage","brown","unnatrual"],
           "dodrio" : ["normal","flying","2types","secondStage","finalStage","brown","unnatrual"],
           "seel" : ["water","firstStage","difEvoType","white"],
           "dewgong" : ["water","ice","2types","white","secondStage","finalStage"],
           "grimer" : ["poison","firstStage","purple"],
           "muk" : ["poison","secondStage","finalStage","purple"],
           "shelder" : ["water","firstStage","purple","difEvoType"],
           "cloyster" : ["water","secondStage","ice","2types","finalStage","purple"],
           "ghastly" : ["ghost","poison","2types","moreEvo","firstStage","black"],
           "haunter" : ["ghost","poison","2types","secondStage","purple"],
           "gengar" : ["ghost","poison","2types","thirdStage","purple","canMegaEvolve"],
           "mega-gengar" : ["ghost","poison","2types","mega","finalStage","purple"],
           "onix" : ["rock","ground","gray","2types","difEvoType","firstStage"],
           "drowzee" : ["psychic","firstStage","yellow"],
           "hypno" : ["psychic","secondStage","finalStage","yellow"],
           "krabby" : ["water","firstStage","orange"],
           "kingler" : ["water","secondStage","finalStage","orange"],
           "voltorb" : ["electric","firstStage","red"]}
           

def normal():
    return guesser(pokeType("normal"), "normal")
def fire():
    return guesser(pokeType("fire"), "fire")
def water():
    return guesser(pokeType("water"), "water")
def grass():
    return guesser(pokeType("grass"), "grass")
def electric():
    return guesser(pokeType("electric"), "electric")
def ice():
    return guesser(pokeType("ice"), "ice")
def fighting():
    return guesser(pokeType("fighting"), "fighting")
def poison():
    return guesser(pokeType("poison"), "poison")
def ground():
    return guesser(pokeType("ground"), "ground")
def flying():
    return guesser(pokeType("flying"), "flying")
def psychic():
    return guesser(pokeType("psychic"), "psychic")
def bug():
    return guesser(pokeType("bug"), "bug")
def rock():
    return guesser(pokeType("rock"), "rock")
def ghost():
    return guesser(pokeType("ghost"), "ghost")
def dark():
    return guesser(pokeType("dark"), "dark")
def dragon():
    return guesser(pokeType("dragon"), "dragon")
def steel():
    return guesser(pokeType("steel"), "steel")
def fairy():
    return guesser(pokeType("fairy"), "fairy")

def firstStage():
    return guesser(pokeStage("first Stage"), "firstStage")
def secondStage():
    return guesser(pokeStage("second Stage"),"secondStage")
def thirdStage():
    return guesser(pokeStage("third Stage"),"thirdStage")
def canMegaEvolve():
    return guesser(pokeStage("mega evolving"),"canMegaEvolve")
def mega():
    return guesser(pokeStage("mega evolved"),"mega")
def finalStage():
    return guesser(pokeStage("final stage"),"finalStage")
def male():
    return guesser(pokeStage("male"),"male")
def female():
    return guesser(pokeStage("female"),"female")
def partner():
    return guesser(pokeStage("first partner"),"firstPartner")
def differentEvoType():
    return guesser(pokeStage("Evolve into a different type"),"difEvoType")
def moreEvo():
    return guesser(pokeStage("evolve more than once"),"moreEvo")
def unnatrual():
    return guessor(pokeSage("unnatrual number of body parts (at least 2)"),"more")

def red():
    return guessor(pokeStage("red"),"red")
def orange():
    return guessor(pokeStage("orange"),"orange")
def yellow():
    return guessor(pokeStage("yellow"),"yellow")
def green():
    return guessor(pokeStage("green"),"green")
def purple():
    return guessor(pokeStage("purple"),"purple")
def blue():
    return guessor(pokeStage("blue"),"blue")
def pink():
    return guessor(pokeStage("pink"),"pink")
def brown():
    return guessor(pokeStage("brown"),"brown")
def black():
    return guessor(pokeStage("black"),"black")
def gray():
    return guessor(pokeStage("gray"),"gray")
def white():
    return guessor(pokeStage("white"),"white")

pokeTypes = [normal, fire, water, grass, electric, ice, fighting,
             poison, ground, flying, psychic, bug,rock, ghost, dark
             ,dragon,steel, fairy ]

pokeStages = [firstStage, secondStage, thirdStage, canMegaEvolve,
              mega,finalStage,male,female, partner, differentEvoType,
              moreEvo,unnatrual]
pokeColors = [red,orange,yellow,green,blue,purple,pink,brown,black,gray,white]


n = 0
t2 = False

typey2 = gTTS(text="is your pokemon of 2 types?")
typey2.save("twoTypes.mp3")
os.system("twoTypes.mp3")
is2types = input("")

if is2types == "yes":
    t2 = True
    guesser(is2types, "2types")



while True:
    typey = pokeTypes[random.randint(0, len(pokeTypes) - 1)]
    pokeTypes.remove(typey)
    if typey() == "yes":
        if t2 == True:
            n +=1
        else:
            break
    if n == 2:
        break
        
n = 0
while len(pokemon) > 1:
    annoyingVariableNameLoL = pokeStages[random.randint(0, len(pokeStages)-1)]
    pokeStages.remove(annoyingVariableNameLoL)
    annoyingVariableNameLoL()
    
    




    

    


