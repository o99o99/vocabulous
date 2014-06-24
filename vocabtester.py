#EDIT DEFAULT DICTIONARY HERE:
filename = "words.txt"



############################################################
##                       PLEASE NOTE:                     ##
##       This program should be run in the Windows        ##
##          command window, not the Python IDLE.          ##
############################################################



#                       CHANGELOG:
#
############################################################
#
#    1.4.1
#
#-Fixed bug causing crash at final test when no words were wrong
#                           
#    1.4
#
#-Added cls function to save typing
#
#    1.3
#
#-Added support for .vocab files
#
#    1.2
#
#-Added new final test
#       -Test on all words got wrong
#       -Added information text RE this
#-Fixed 2 looping issues
#-Minor "time.sleep", "print()" and "cls" edits
#
############################################################




###                  BEGIN PROGRAM:                      ###
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

import time
import os
print(" __ __   ___      __   ____  ____   __ __  _       ___   __ __  _____")
print("|  T  | /   \    /  ] /    ||    \ |  |  || |     /   \ |  T  T/ ___/")
print("|  |  |Y     Y  /  / /  o  ||  o  )|  |  || |    Y     Y|  |  (   \_ ")
print("|  |  ||  O  | /  /  |     ||     T|  |  || l    |  O  ||  |  |\__  \ ")
print("|     |      |/  \_  |  |  ||  O  ||  :  || |    |     ||  :  |/  \ |")
print(" \   / l     !\     ||  |  ||     |l     || |___ |l     !l     |    |")
print("  \_/   \___/  \____||__|__|l_____j \__,_jl_____j \___/  \__,_j \___j\n")
print("1.4                                                       OWAIN BATES\n")
time.sleep(1)
print("    Written by Owain Bates using Python 3.3.3")
print("    With thanks to bedekelly and zahlman\n")
print("    PLEASE MAXIMISE THIS WINDOW NOW\n")
time.sleep(1)
print()
print()
changefile = 0
while changefile != 1 and changefile !=  2:
    changefile = int(input("Type 1 select a dictionary, or type 2 to use the default dictionary words.txt: "))
    print()
    print()
    print()
    print()
    print()
    contsetup = 1
    while contsetup ==1:
        try:
            if changefile == 1:
                time.sleep(0.5)
                done =0
                if done == 0:
                    
                    print("""   You can add your own dictionary now.

    INSTRUCTIONS FOR CREATING DICTIONARIES:
    

    1. Create a file in the same directory as this program.
       You can create it in another directory if you really want
       to, but you will have to enter the full file path below.

       Make the file in notepad, and save it as either .txt or
       .vocab
 
    
    2. Add your vocab. Make sure there is a new word each line.
       Do not leave empty lines, and do not have more than one
       word per line. You may have 1 OR 2 definitions per word.
       Any more than this will not work

       It should be in the following format:
       
           word:definition
           word:definition,definition2
           word:definition

        Note that "word" can be anything at all, but the
        definitions must be strictly formatted. To answer
        a question correctly, you must type EXACTLY what
        you put for "definition" or (if applicable) "definition2".


    3.  Do not leave a space either side of the colon and (if
        applicable) the comma. You may leave a space where
        necessary if the definition consists of two words.

        
    4.  If you enter a word on two separate lines, the program
        will overwrite the first one with the second.

           
    5. The program is case sensitive. Only capitalise definitions
       that should be capitalised.


    6. Be careful when saving the file. Only ANSI and UTF-8 .txt
       formats are supported. Words with foreign characters will
       not appear at all using ANSI, and foreign characters will
       not render in other encoding formats.

    7. If you want to change the default dictionary, edit the
       first line of this code in the Python IDLE.
       
                    """)
                    print()
                    print()
                    print()
                    print()
                    input("Press enter to continue")

                    print()
                    textitems = os.listdir()
                    newlist = []
                    for names in textitems:
                        if names.endswith(".txt") or names.endswith(".vocab"):
                            newlist.append(names)
                    time.sleep(0.5)
                    print("Now choose a file.")
                    print()
                    time.sleep(0.5)
                    print("The following text files are present in this directory: ", newlist)
                    print()
                else:
                    pass
                time.sleep(1)
                filename = input("Enter the file name you want: ")
                if not filename.endswith(".txt") and not filename.endswith(".vocab"):
                    filename = filename + ".txt"
                    pass
                else:
                    pass
                done=1
                print()
                time.sleep(1)
                print()
            elif changefile == 2:
                time.sleep(1)
                print()
                contsetup =2
            else:
                time.sleep(0.5)
                print("Invalid choice. Try again.")
                print()
                contsetup =2

            with open(filename) as file:
                if changefile == 1 or changefile == 2:
                    print("The dictionary at", filename, "has been selected.")
                else:
                    pass
                mdict={}
                for line in file:
                    a, b = line.strip().split(':')
                    if "," in b:
                        b, c = b.split(",")
                        adefs = (b,c)
                        mdict[a] = adefs
                    else:
                        mdict[a] = b
                    contsetup = 2

        except ValueError:
            print()
            time.sleep(1)
            if contsetup !=2:
                input("MAJOR FORMATTING ERROR")
                input("""Whoops - that file doesn't seem to be formatted correctly. I'll repeat the
instructions for you! Press enter to try again.""")
                cls()
            elif contsetup ==2:
                time.sleep(1)
                print()
                print("MINOR FORMATTING ERROR - NON FATAL")
                print("That file may have minor formatting issues.")
                print("Attempting to continue, however you may notice")
                print("a few problems with vocab. If this is the case,")
                print("please check over your custom dictionary for any")
                print("formatting errors.")
                time.sleep(1.5)
            else:
                pass
            print()
            print()
            print()
            print()
            print()
            time.sleep(0.5)

        except FileNotFoundError:
            time.sleep(1)
            if contsetup !=2:
                input
                input("FILE ADDRESS ERROR")
                input("""Whoops - that file doesn't exist. I'll repeat the
instructions for you! Press enter to try again.""")
                cls()
            else:
                pass
            print()
            print()
            print()
            print()
            print()
            time.sleep(0.50)
            

time.sleep(0.5)
print()
print("The file has been successfully accessed!")
dictlen = len(mdict)
print()
time.sleep(0.5)
print("There are", dictlen, "words in the dictionary.")
print()
print()
print()
time.sleep(1)
print("SETUP COMPLETE!")
time.sleep(0.5)
input("Press enter to continue")
cls()

playagain = 1
finalconf = 0

totalwrongdict = {}


print("You can play as many games as you like. At the end,")
print("you will be tested on every single word you got ")
print("wrong, until you get them all correct!")
time.sleep(1)
print()
print()
       
while playagain == 1 and finalconf!=1:
    time.sleep(1)

    if playagain != 1:
        break
    else:
        pass
    print()
    
    cont = 1
    wrongdict = {}
    score = 0
    qnum = 0
    wrongnum = 0
    lifelimit = 0
    gamemode = 0
    questionlimit = 0
    starttime = 0
    endtime = 0
              
    while gamemode != 1 and gamemode != 2 and gamemode != 3:
        print("Please select your game mode.")
        time.sleep(0.5)
        print()
        print("In survival mode, the game ends after you lose all you lives.")
        print()
        print("In unlimited mode, the game goes on forever, until you type 'end'.")
        print()
        print("In test mode, you will be given a set number of questions to answer")
        print("against the clock.")
        print()
        gamemode = int(input("Press 1 to play survival, 2 to play unlimited or 3 to do a test: "))
        print()
        time.sleep(0.5)
        if gamemode == 1:
            while lifelimit < 1:
                print("Now select your number of lives.")
                lifelimit = int(input("This must be greater than 0: "))
                cls()
                print()
                if lifelimit < 1:
                    print("Invalid number. Try again.")
        elif gamemode ==2:
            cls()
            print("To end your game on unlimited mode, type 'end'.")
        elif gamemode ==3:
            while questionlimit < 1:
                print("Select number of questions.")
                questionlimit = int(input("This must be greater than 0: "))
                cls()
                print()
                if questionlimit < 1:
                    print("Invalid number. Try again.")
        else:
            print("Invalid game mode. Try again.")
            time.sleep(1)
            cls()
            print()

    time.sleep(0.5)
    starttime = time.time()
    while cont ==1:
        
        from random import choice
        
#Ask words
        print()
        q = choice(list(mdict.keys()))
        res = input('{0} is: '.format(q))
        qnum = qnum+1
        if res == "end" and gamemode == 2:
            print()
            time.sleep(0.3)
            cls()
            qnum = qnum-1
            break
        if res in mdict[q] and res != "":
            if gamemode != 3:
                time.sleep(0.3)
                print("Correct Answer!")
            else:
                pass
            score = score+1
        elif res not in mdict[q] or res == "":
            if gamemode != 3:
                time.sleep(0.7)
                print("Incorrect! The correct answer was:", mdict[q])
            else:
                pass
            if q not in wrongdict:
                wrongdict[q] = mdict[q]
            else:
                pass
            if q not in totalwrongdict:
                totalwrongdict[q] = mdict[q]
            else:
                pass
            wrongnum = wrongnum + 1
#Loop/End        
        if int(wrongnum) >= lifelimit and gamemode == 1:
            print()
            print()
            time.sleep(0.5)
            print("You have lost all", lifelimit, "lives!")
            time.sleep(1.5)
            cls()
            print()
            print("""
  ____   ____  ___ ___    ___       ___   __ __    ___  ____  
 /    T /    T|   T   T  /  _]     /   \ |  T  |  /  _]|    \ 
Y   __jY  o  || _   _ | /  [_     Y     Y|  |  | /  [_ |  D  )
|  T  ||     ||  \_/  |Y    _]    |  O  ||  |  |Y    _]|    / 
|  l_ ||  _  ||   |   ||   [_     |     |l  :  !|   [_ |    \ 
|     ||  |  ||   |   ||     T    l     ! \   / |     T|  .  Y
l___,_jl__j__jl___j___jl_____j     \___/   \_/  l_____jl__j\_j
                                                          """)
            print()
            time.sleep(0.8)
            input("Press enter to continue")
            cls()
            
            print()
            cont = 2
        elif gamemode == 3 and qnum == questionlimit:
            endtime = time.time()
            timetaken = endtime-starttime
            timetaken = round(timetaken, 2)
            try:
                tpw = timetaken/score
            except ZeroDivisionError:
                twp = 0
            tpw = round(tpw, 2)
            print("The test is complete!")
            input("Press enter to continue")
            cls()
            cont = 2
        else:
            cont = 1
    try:       
        percent = (round((100/qnum)*score))
    except ZeroDivisionError:
        percent = 0
   
    time.sleep(1)
    print()
    print()
    print("CALCULATING SCORE!")
    time.sleep(1.5)
    if gamemode == 1:
        print()
        print("Your final score on survival mode was:", score, "/", qnum) 
        if percent < 100:
            print("or", percent, "%")
        else:
            print("""


 d888    .d8888b.   .d8888b.  d88b   d88P
d8888   d88P  Y88b d88P  Y88b Y88P  d88P 
  888   888    888 888    888      d88P  
  888   888    888 888    888     d88P   
  888   888    888 888    888    d88P    
  888   888    888 888    888   d88P     
  888   Y88b  d88P Y88b  d88P  d88P  d88b
8888888  "Y8888P"   "Y8888P"  d88P   Y88P


""")
        time.sleep(1)
        print()
        if wrongnum > 0:
            print("INCORRECT ANSWERS:")
            time.sleep(0.5)
            print()
            print("You got the following words wrong. They are listed with")
            print("their correct meainings: ")
            print()
            time.sleep(0.5)
            for key, value in wrongdict.items():
                print("{} : {}".format(key,value))
            print()
            print("Learn them!")
        elif wrongnum < 1:
            pass
    elif gamemode == 2:
        print()
        try:
            print("Your final score on unlimited mode was:", score, "/", qnum)
            if percent < 100:
                print("or", percent, "%")
            else:
                print("""


 d888    .d8888b.   .d8888b.  d88b   d88P
d8888   d88P  Y88b d88P  Y88b Y88P  d88P 
  888   888    888 888    888      d88P  
  888   888    888 888    888     d88P   
  888   888    888 888    888    d88P    
  888   888    888 888    888   d88P     
  888   Y88b  d88P Y88b  d88P  d88P  d88b
8888888  "Y8888P"   "Y8888P"  d88P   Y88P


""")
        except ZeroDivisionError:
            print("You didn't answer any questions!")
        except NameError:
            print("You didn't answer anything!")
        time.sleep(0.5)
        time.sleep(0.5)
        print()
        if wrongnum > 0:
            print("INCORRECT ANSWERS:")
            time.sleep(0.5)
            print()
            print("You got the following words wrong. They are listed with")
            print("their correct meainings: ")
            print()
            time.sleep(0.5)
            for key, value in wrongdict.items():
                print("{} : {}".format(key,value))
            time.sleep(1.5)
            print()
            print("Learn them!")
        elif wrongnum < 1:
            pass
    elif gamemode == 3:
        print
        print("Your final score on the test was:", score, "/", qnum) 
        if percent < 100:
            print("or", percent, "%")
        else:
            print("""


 d888    .d8888b.   .d8888b.  d88b   d88P
d8888   d88P  Y88b d88P  Y88b Y88P  d88P 
  888   888    888 888    888      d88P  
  888   888    888 888    888     d88P   
  888   888    888 888    888    d88P    
  888   888    888 888    888   d88P     
  888   Y88b  d88P Y88b  d88P  d88P  d88b
8888888  "Y8888P"   "Y8888P"  d88P   Y88P


""")
        print("You took ", timetaken, "seconds!")
        if tpw != 0:
            print("Taking", tpw, "seconds per word!")
        else:
            pass
        time.sleep(0.5)
        time.sleep(0.5)
        print()
        if wrongnum > 0:
            print("INCORRECT ANSWERS:")
            time.sleep(0.5)
            print()
            print("You got the following words wrong. They are listed with")
            print("their correct meainings: ")
            print()
            time.sleep(0.5)
            for key, value in wrongdict.items():
                print("{} : {}".format(key,value))
            time.sleep(1.5)
            print()
            print("Learn them!")
        elif wrongnum < 1:
            pass
        
    if percent == 100:
        comment = """



You got a perfect score! Congratulations! Try a new set of words, or play again to revise more!"""
    elif 100 > percent >= 90:
        comment = "Excellent score, well done! Play again to get an even better score!"
    elif 90 > percent >= 75:
        comment = "You got a decent score! Maybe you should try again to do better!"
    elif 75 > percent >= 60:
        comment = "You did okay, but you need to practise the words more!"
    elif 60 > percent >= 45:
        comment = "You didn't do too well. You need to learn these words better!"
    elif 45 > percent > 0:
        comment = "That was a pretty poor performance! Try again!"
    elif percent == 0:
        comment = "Pathetic! You scored nothing! You need to try again!"
        
    print()
    time.sleep(1)
    print(comment)
    print()
    print()
    time.sleep(0.5)
    try:
        finalconf = int(input("Press enter to play again! Press 1 to exit "))
    except ValueError:
        finalconf = 0
    time.sleep(0.3)
    cls()
    if finalconf == 1:
        break
print()
time.sleep(0.5)
if len(totalwrongdict) > 0:
    print()
    print()
    print()
    print("Here is a list of every incorrect word from this session.")
    print("Take note of them if you want to revise them.")
    time.sleep(0.3)
    print()
    for key, value in totalwrongdict.items():
        print("{} : {}".format(key,value))
    time.sleep(2)
    playagain = 2
    
    
    finconf = 0
    fintest = 1
    print()
    print("You will now take a final test on all of these words. They")
    print("will not be removed from the list until you answer them")
    print("correctly. This could take a long time!")
    print()
    input("Press enter to take the test: ")
    finaldict = {}
    finaldict = totalwrongdict.copy()
    cls()
    while fintest == 1:
        print()
        q = choice(list(totalwrongdict.keys()))
        res = input('{0} is: '.format(q))
        if res == "end":
            print()
            time.sleep(0.3)
            fintest = 0
            finconf = 1
            break
        elif res in totalwrongdict[q] and res != "":
            time.sleep(0.3)
            print("Correct Answer!")
            del totalwrongdict[q]
        elif res not in totalwrongdict[q] or res == "":
            time.sleep(0.7)
            print("Incorrect! The correct answer was:", mdict[q])
    
        lengdi = len(totalwrongdict)  
        if lengdi == 0:
            fintest = 0
            break
        else:
            pass
    
            
    time.sleep(1)
    print()
    print("Well done, you finally got them all right!")
    time.sleep(0.5)
    print("Here is that list once more:")
    time.sleep(1)
    print()
    for key, value in finaldict.items():
        print("{} : {}".format(key,value))
    time.sleep(2)
    
    print()
else:
    print("You got nothing wrong at all! Well done!")
    time.sleep(1)
    print()
input("Press enter to exit")

        




