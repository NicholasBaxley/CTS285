import random

def checkQuestion(question): # Checks to make sure the question is in the correct format.
    operators = ["+","-","/","*","x"]
    if not isNumber(question[0]):
       return False        
    elif not isNumber(question[2]):
        return False     
    elif not isNumber(question[-1]):
        return False    
    elif question[1] not in operators:
        return False      
    elif question[3] != "=":
        return False  
    elif len(question) > 5 or len(question) < 5:
        return False
    return True
    
def isNumber(s): # Checks to see if a object is a number 
    try:
        float(s)
        
        return True
    
    except ValueError:
        
        return False

def strgToNum(question): # Converts all number strings to number floats
    question[0] = float(question[0])
    question[2] = float(question[2])
    question[4] = float(question[4]) 
    
    return question

def checkRemainder(remainder, question, answer):
    # Checks to see if you know the remainder of the answer if right returns 1
    # if wrong returns 0
    print("Good job on guessing the correct answer, now for the remainder")
    loop = 2
    while loop == 2:
            print()
            print("The question is:")
            for i in question:
                print(i, end=" ")
            print(int(answer), "R: ? ")
            guess = input("What is the remainder? R: ")           
            if isNumber(guess):
                guess = int(guess)
                if remainder == guess:                        
                        print("Correct!")  
                        loop = 3
                        
                        return 1
                    
                else:
                    print()
                    print("Sorry, thats wrong.")
                    print("The answer was",answer)
                    loop = 3
                    
                    return 0
                
            else:
                print("Your guess must be a number!")
      
def answerChecker(x, y): # The menu option that lets you try to solve questions.
    correctAnswers = x
    totalQuestions = y
    loop = 1
    while loop == 1:
        
        print("Input question (Without Remainder): ")
        question = input().split()
        
        # Makes sure the question is in correct format
        if checkQuestion(question):
            question = strgToNum(question)   
            guess = question[4]
            loop = 2
        else:
            print("Incorrect format! Format must be ( [Number] {Operator} [Number] = [Number])")
            continue
    
    # Gets the answer and remainder from the inputted list
    answerList = questionSolver(question)
    answer = answerList[0]
    remainder = answerList[1]
    
    # Checks to see if you answer is correct and adds to the scoreboard
    question.pop()
    if answer == guess:    
        if remainder > 0: 
            correctAnswers += checkRemainder(remainder, question, answer)
        else:
            correctAnswers += 1
            print("Correct!")  
    else: 
        print("Wrong answer, One more guess!.", end="")
        while loop == 2:
            print()
            print("The question is:")
            for i in question:
                print(i, end=" ")
            print("?")
            guess = input()           
            if isNumber(guess):
                guess = int(guess)
                if answer == guess:
                    if remainder > 0: 
                        correctAnswers += checkRemainder(remainder, question, answer)
                    else:
                        correctAnswers += 1
                        print("Correct!")  
                else:
                    print()
                    print("Sorry, thats wrong.")
                    print("The answer was",answer)
                loop = 3
            else:
                print("Your guess must be a number!")
    totalQuestions += 1
    
    if totalQuestions == 10:
        print("You guessed",correctAnswers,"out of",totalQuestions)
        menu()
    else:
        answerChecker(correctAnswers, totalQuestions)
            
def questionSolver(question): # Solves questions and returns the answer as answer[0] 
                              # and remainder if neccesary as answer[1]
    answer = []
    if question[1] == "+":
        answer.append(question[0] + question[2]) 
        answer.append(0)
    elif question[1] == "-":
        answer.append(question[0] - question[2]) 
        answer.append(0)
    elif question[1] == "*" or question[1] == "x":
        answer.append(question[0] * question[2]) 
        answer.append(0)
    elif question[1] == "/":
        answer.append(question[0] // question[2]) 
        answer.append(question[0] % question[2])
        
    return answer

def guessFunction(): # Retreives a guess from user and makes sure its a number
    guess = input()
    if not isNumber(guess):
        print("Not a number! Try again")
        print()
    else:
        guess = int(guess)
    
    return guess

def memoryBank(): #Starts the memory bank game
    count = 0
    total = 0
    print()
    print("Welcome to Memory Bank!")
    while True:
        question, answer = memBkRandomQuestion()       
        print("Your question is: ",end="")
        for i in question:
            print(f"{i} ",end="")
        print("= ? ")
        print()
        guess = guessFunction()
        if guess == answer[0]:
            print("Correct!")
            count += 1
        else:
            print("Wrong! You get one more chance.")
            guess = guessFunction()
            if guess == answer[0]:
                print("Correct!")
                count += 1
            else:
                print("Sorry the answer was ",answer[0],".",sep="")
        total += 1
        print("Would you like to play again?")
        print("""
1) Yes
2) No""")
        playagain = int(input())
        if playagain == 2:
            print("You guessed",count,"correct out of",total)
            menu()
            break
        

def memBkRandomQuestion(): #Generates the random question for memory bank
    operators = ["+","-","x"]
    x = random.randint(1, 99)
    y = random.choice(operators)
    z = random.randint(1, 99)
    question = [x,y,z]
    answer = questionSolver(question)  
    
    return question, answer

def menu(): #Main menu of the program, all games should lead back to here
    print("What do you want to do?")
    print("""
1) AnswerChecker 
2) MemoryBank
3) Exit
         """)   
    menu = int(input())   
    if menu == 1:
        x = 0
        y = 0
        print("Format must be ( [Number] {Operator} [Number] = [Number])")
        answerChecker(x, y)
    elif menu == 2:
        memoryBank()
    else:
        print("GoodBye.")
menu()
            