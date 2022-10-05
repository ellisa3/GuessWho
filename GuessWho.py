from images import * 
from random import *
# how to fix the window to the ideal place, and close the window???????????

# a list of the celebrity characters in our game
characters = ["Abraham Lincoln", "Elvis Presley", "Simone Biles", "Donald Trump", "Yuzuru Hanyu", "Katy Perry", "Michael Phelps", "Emma Watson", "Dwayne Johnson", "Steve Jobs"]

# feature= [business suit, female, teeth, glasses, alive] 0 = no, 1 = yes  each indicies mini list correspondes to the indices of the character in characters list, e.g. characters[0] = features[0]
features = [[1,0,0,0,0],[0,0,0,0,0],[0,1,1,0,1],[1,0,1,0,1],[0,0,0,0,1],[0,1,1,1,1],[0,0,1,0,1],[1,1,0,0,1],[0,0,1,1,1],[0,0,0,1,0]]

# a list of possible "yes' responses from user
yesList = ["yes","y","okay","ok","Sure","sure","YES","Yes","Yup","Yep","YUP","YEP","alive","Alive"]
noList = ["no","NO","No","n","N","nah","Nah","dead","Dead","nope","Nope"]

# a list of questions 
Question = ["Is your character wearing a business suit? ",
            "Is your character a female? ",
            "Is your character showing teeth? ",
            "Is your character wearing glasses? ",
            "Is your character alive? "]

# two lists of responses based on user's guess
AnswerNo = ["I'm not wearing a business suit.",
            "I'm male.",
            "I'm not showing teeth.",
            "I'm not wearing glasses",
            "I'm dead."]
AnswerYes = ["I'm wearing a business suit.",
            "I'm female.",
             "I'm showing teeth",
            "I'm wearing glasses.",
            "I'm alive."]

# a list of all the pixels of each character image in the window
pixList = [[0,200,0,200],[200,400,0,200],[0,200,200,400],[200,400,200,400],[0,200,400,600],[200,400,400,600],[0,200,600,800],[200,400,600,800],[0,200,800,1000],[200,400,800,1000]]

#def showReference(image):                                    # show reference picture for characters
    #image.show()
    
def intro():  # prints opening game statements
    print()
    print("🕹️ 🕹️ 🕹️ 🕹️  GUESS WHO!!! 🕹️ 🕹️ 🕹️ 🕹️ 🕹️")
    print("Please choose a celebrity shown in the window.")
    input("When you're ready, press <enter> to BEGIN!")
    print()
    

#def showQuestion (Questions):                                  # show question reference for user
    #Questions.show()

# This function returns a list of characters that are not the computer's chosen character based on the question asked 
def incorrectCharacter(qNumber,computerPersonIndex):
    blackList = []
    for i in range(10):
        if qNumber.isdigit() and features[i][int(qNumber)-1]!= features[computerPersonIndex][int(qNumber)-1]:
            blackList.append(i)
        elif qNumber in characters:
            blackList.append(characters.index(qNumber))
    return blackList

# This function turns black the image of the incorrect character 
def black(image, blackList):  
    for j in blackList: 
        miniRange = pixList[j]
        for x in range(miniRange[0],miniRange[1]):
            for y in range(miniRange[2],miniRange[3]):
                #r,g,b = image.getPixel(x,y)
                image.setPixel(x,y,(0,0,0))
    image.redraw()# do we need this???????

# This function handles the user's guessing. Based on the user's input, yields proper results
def yesOrNo(computerPersonIndex, image): 
    print("Choose one of the questions shown on screen to ask.")
    qNumber = input("Type in the character's name (spelling counts!) or type in the next question number >> ")
    count = 0
    miniList = features[computerPersonIndex]
    while True:
        if qNumber in characters:                               # if input is not a digit (eg, a name)
            if characters.index(qNumber) == computerPersonIndex:
                print("You got it!!! ❁◕ ‿ ◕❁")
                return count
            else:
                print("Nope. Try again. 👎")
                print()
                black(image, incorrectCharacter(qNumber,computerPersonIndex))  
        elif qNumber.isdigit() and int(qNumber) in range (1,6) and miniList[int(qNumber)-1] == 0: # if input is a digit 
            print("Nah, dude.", AnswerNo[int(qNumber)-1])
            print()
            black(image, incorrectCharacter(qNumber,computerPersonIndex))
        elif qNumber.isdigit() and int(qNumber) in range (1,6) and miniList[int(qNumber)-1] == 1:
            print("You betcha!", AnswerYes[int(qNumber)-1])
            print()
            black(image, incorrectCharacter(qNumber, computerPersonIndex))
        else:
            print("NO! That input was invalid. Try again. 👎")
            print()
        count += 1
            
        qNumber = input("Type in the character's name (spelling counts!) or type in the question number >> ")

# compare the attempts of the computer and of the user, print the winner who has fewer attempts
def winner(computerAttempts, userAttempts):
    if computerAttempts < userAttempts:
        print("I guessed your character with", computerAttempts, "guesses. It took you", userAttempts, ". You lost. ¯\(°_o)/¯")
    else:
        print("⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐")
        print("Congratulations.")
        print()
        print("You guessed my character in", userAttempts, "guesses. It took me", computerAttempts, "guesses. You win!")
        print()
        print("⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐")
    
# computer randomly chooses its character
def computerChoosePerson(): 
    computerPersonIndex = randrange(0,10)
    return computerPersonIndex

# computer asks questions based on the user's response   
def computerGuess(list):    #why automatically prompt the question?❓❓❓ can add black...
    attempts = 0
    featuresCopy = list[:]                                   # create a copy of features to manipulate later
    j = 0    
    while j < 5 and len(featuresCopy) > 1:                   # j goes through mini lists in feature list
        countList = []                                       # create empty list 
        for i in range (len(featuresCopy)):                  # i goes through the feature list
            countList.append(featuresCopy[i][j])             # add to countList the j'th entry of the i'th mini list in the featuresCopy list
        occurance = countList.count(0)                       # count how many times 0 occures in the countList
        occuranceYes = len(featuresCopy)-occurance           
        if occurance == (len(featuresCopy)//2) or occuranceYes == (len(featuresCopy)//2): 
                                                             # half and half situation so computer asks best question 
            ans = input(Question[j]) 
            print()
            if ans in yesList:
                attempts +=1
                h = 0
                while h < len(featuresCopy):
                        if featuresCopy[h][j] == 0:
                            del featuresCopy[h]
                            h = 0                            # h must start at 0 to accomdate shrinking featuresCopy list
                        else: 
                            h +=1
            elif ans in noList: # input is no
                attempts +=1
                h = 0                                
                while h < len(featuresCopy):
                        if featuresCopy[h][j] == 1:
                            del featuresCopy[h]
                            h = 0                            # h must start at 0 to accomdate shrinking featuresCopy list
                        else: 
                            h +=1
            j = 0                                            # because looking at new list (a shrunked featuresCopy), 
                                                             #must iterate from the beginning (i.e. business suit)
        else:
            j = j + 1                
    return featuresCopy[0], attempts

# This function returns the appropriate character's name
def getName(features, characters, shrunkList):              
    index = features.index(shrunkList)
    return characters[index]
       
# This function prints the character the user has chosen
def outro(name,attempts):                                            
    print("Your character is: >>>", name, "<<<")
    print("It took me", attempts, "guesses. Beat that!")
    
def main():
    image = FileImage('characterCollage.gif')               
    image.show() 
    #showReference(image)                                        # show character options   
    QuestionsReference = FileImage('questions.gif')     
                                      
    intro()                                                     # show prompt to start game: computer guesses
    shrunkList, computerAttempts = computerGuess(features)      # assign shrunkList to correct character 
    UserCharacter = getName(features, characters, shrunkList) 
    outro(UserCharacter, computerAttempts)                      # returns character's name (computer guess)
    print()
    print("^><^><^<^><^><^><^<^><^><^><^<^><^><^><^<^><^><^><^<^><^^><^><^<^><^<^><^^><^><^") # user guesses
    print()
    print("Now it's your turn to guess.")
    input("When you're ready to contiune playing, press <enter>")
    QuestionsReference.show(x=500, y =500)                                   # show question options
    computerCharacter = computerChoosePerson()                  # returns an index of computer character randomly
    print()
    userAttempts = yesOrNo(computerChoosePerson(), image)       # user guesses the computer's character
    winner(computerAttempts, userAttempts)                      # give the results of the games

if __name__ == "__main__":
    main()
    
