import random

p1 = input("Who is the 1st student?\n")
p2 = input("Who is the 2nd student?\n")
p3 = input("Who is the 3rd student?\n")
p4 = input("Who is the 4th student?\n")
p5 = input("Who is the 5th student?\n")
p6 = input("Who is the 6th student?\n")
p7 = input("Who is the 7th student?\n")
p8 = input("Who is the 8th student?\n")
p9 = input("Who is the 9th student?\n")
p10 = input("Who is the 10th student?\n")
p11 = input("Who is the 11th student?\n")
p12 = input("Who is the 12th student?\n")
p13 = input("Who is the 13th student?\n")
p14 = input("Who is the 14th student?\n")
p15 = input("Who is the 15th student?\n")
p16 = input("Who is the 16th student?\n")

numberofdead = 0
round = 1
murderchance = 20
murdermethod = [" was stabbed to death", " was strangled to death", " was pushed and fell to their death", " was poisoned", " was shot in the heart with a nail gun", 
                " was electrocuted", " was bludgeoned to death", " was burned to death", " died to blood loss", " drowned", " died to an allergic reaction", " was hung",
                " had their neck snapped"]
safe = [" used the MonoMono machine", " ate a snack in the cafeteria", " took a walk around the school", " talked to another student", " took a rest in their dorm",
        " swam laps in the pool", " tried to find an exit (unsuccessfully)", " stood menacingly in the halls, looking at the mc constantly", " read in the library",
        " drew in the art room", " was on trash duty", " sat in the sauna", " watched a movie in the AV room", " played the piano", " practiced their archery skills"]
endingready = False

def rngplyr(exception: str, exception2: str) -> str:
    rp = random.choice([p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16])
    if rp == exception or rp == exception2:
        while rp == exception or rp == exception2:
            rp = random.choice([p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16])
    return rp

def kill():
    deceased = rngplyr(None, None)
    if "dead" in deceased:
        while "dead" in deceased:
            deceased = rngplyr(None, None)
            break
    else:
                        print(deceased + random.choice(murdermethod))
                        murderer = rngplyr(deceased, None)
                        if "dead" in murderer:
                            while "dead" in murderer:
                                murderer = rngplyr(deceased, None)
                        global p1
                        global p2
                        global p3
                        global p4
                        global p5
                        global p6
                        global p7
                        global p8
                        global p9
                        global p10
                        global p11
                        global p12
                        global p13
                        global p14
                        global p15
                        global p16
                        if deceased == p1:
                            p1 += " is dead"
                        elif deceased == p2:
                            p2 += " is dead"
                        elif deceased == p3:
                            p3 += " is dead"
                        elif deceased == p4:
                            p4 += " is dead"
                        elif deceased == p5:
                            p5 += " is dead"
                        elif deceased == p6:
                            p6 += " is dead"
                        elif deceased == p7:
                            p7 += " is dead"
                        elif deceased == p8:
                            p8 += " is dead"
                        elif deceased == p9:
                            p9 += " is dead"
                        elif deceased == p10:
                            p10 += " is dead"
                        elif deceased == p11:
                            p11 += " is dead"
                        elif deceased == p12:
                            p12 += " is dead"
                        elif deceased == p13:
                            p13 += " is dead"
                        elif deceased == p14:
                            p14 += " is dead"
                        elif deceased == p15:
                            p15 += " is dead"
                        elif deceased == p16:
                            p16 += " is dead"
                        global numberofdead
                        numberofdead = numberofdead + 1
                        input()
                        print("A class trial will now be held to determine who the blackened is.")
                        input()
                        if random.randint(1, 10) == 1:
                            print(f"Everyone guessed incorrectly. \033[31m{murderer}\033[0m was the blackened, and has been set free, while all others have been killed.\n----GAME OVER----\nPress enter to leave")
                            input()
                            exit()
                        else:
                            print(f"Everyone guessed correctly. \033[31m{murderer}\033[0m was the blackened, and has been killed. Congratulations, you live another day.")
                            if murderer == p1:
                                p1 += " is dead"
                            elif murderer == p2:
                                p2 += " is dead"
                            elif murderer == p3:
                                p3 += " is dead"
                            elif murderer == p4:
                                p4 += " is dead"
                            elif murderer == p5:
                                p5 += " is dead"
                            elif murderer == p6:
                                p6 += " is dead"
                            elif murderer == p7:
                                p7 += " is dead"
                            elif murderer == p8:
                                p8 += " is dead"
                            elif murderer == p9:
                                p9 += " is dead"
                            elif murderer == p10:
                                p10 += " is dead"
                            elif murderer == p11:
                                p11 += " is dead"
                            elif murderer == p12:
                                p12 += " is dead"
                            elif murderer == p13:
                                p13 += " is dead"
                            elif murderer == p14:
                                p14 += " is dead"
                            elif murderer == p15:
                                p15 += " is dead"
                            elif murderer == p16:
                                p16 += " is dead"
                            global round
                            round = round + 1
                            numberofdead = numberofdead + 1
                            input()




def safeinter(player: str) -> str:
    if "dead" in player:
        return player
    else:
        return player + random.choice(safe)

while numberofdead != 14:
    if p16 != None:
        print("Let the high school killing game begin! Puhuhuhuhuhuhu")
        input()
        print("---Day 1---")
        print(safeinter(p1))
        print(safeinter(p2))
        print(safeinter(p3))
        print(safeinter(p4))
        print(safeinter(p5))
        print(safeinter(p6))
        print(safeinter(p7))
        print(safeinter(p8))
        print(safeinter(p9))
        print(safeinter(p10))
        print(safeinter(p11))
        print(safeinter(p12))
        print(safeinter(p13))
        print(safeinter(p14))
        print(safeinter(p15))
        print(safeinter(p16))
        input()
        round = round + 1
        while numberofdead != 14:
            print("---Day " + str(round) + "---")
            if random.randint(1, murderchance) <= 15:
                print(safeinter(p1))
                print(safeinter(p2))
                print(safeinter(p3))
                print(safeinter(p4))
                print(safeinter(p5))
                print(safeinter(p6))
                print(safeinter(p7))
                print(safeinter(p8))
                print(safeinter(p9))
                print(safeinter(p10))
                print(safeinter(p11))
                print(safeinter(p12))
                print(safeinter(p13))
                print(safeinter(p14))
                print(safeinter(p15))
                print(safeinter(p16))
                input()
                round = round + 1
            else:
                kill()
        break

while True:
    if numberofdead == 14:
        survivor1 = rngplyr(None, None)
        if "dead" in survivor1:
            while "dead" in survivor1:
                survivor1 = rngplyr(None, None)
            continue
        survivor2 = rngplyr(survivor1, None)
        if "dead" in survivor2:
            while "dead" in survivor2:
                survivor2 = rngplyr(survivor1, None)
            continue
        endingready = True
        break

while endingready == True:
    print(f"The winners of the high school killing game are \033[32m{survivor1}\033[0m and \033[32m{survivor2}\033[0m. They are set free into the despair-filled world.\nPress enter to leave")
    input()
    exit()