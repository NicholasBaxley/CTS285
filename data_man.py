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
    print(pattern)
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
                        print(pattern)                     
                        print("Correct!")  
                        loop = 3
                        
                        return 1
                    
                else:
                    print(pattern)
                    print()
                    print("Sorry, thats wrong.")
                    print(f"The answer was {answer:.0f} and the remainder was {remainder:.0f}")
                    loop = 3
                    
                    return 0
                
            else:
                print(pattern)
                print("Your guess must be a number!")
      
def answerChecker(x, y): # The menu option that lets you try to solve questions.
    print(pattern)
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
            print(pattern)
            print("Correct!")  
    else: 
        print(pattern)
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
                        print(pattern)
                        print("Correct!")  
                else:
                    print()
                    print(pattern)
                    print("Sorry, thats wrong.")
                    print(f"The answer was {answer:.0f} and the remainder was {remainder}")
                loop = 3
            else:
                print("Your guess must be a number!")
    totalQuestions += 1 
    while True:
        repeat = input("Do you want to play again?\n\n1) Yes\n2) No\n\n")
        if repeat == "1" or repeat == "2":   
            break
        else:
            print(pattern)
            print("Not an option!")
    if repeat == "1":
        answerChecker(correctAnswers, totalQuestions)
    if repeat == "2":
        print(pattern)
        print(f'You guessed {correctAnswers} out of {totalQuestions} questions correctly!')
        print()
        menu()
        
    
    
    
            
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
    while True:
        guess = input()
        if not isNumber(guess):
            print(pattern)
            print("Not a number! Try again")
            print()
            continue
        else:
            guess = int(guess)
            break        
    return guess

def memoryBank(): # Starts the memory bank game
    count = 0
    total = 0
    print(pattern)
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
            print(pattern)
            print("Correct!")
            count += 1
        else:
            print(pattern)
            print("Wrong! You get one more chance.")
            guess = guessFunction()
            if guess == answer[0]:
                print(pattern)
                print("Correct!")
                count += 1
            else:
                print(pattern)
                print("Sorry the answer was ",answer[0],".",sep="")
        total += 1
        while True:
            repeat = input("Do you want to play again?\n\n1) Yes\n2) No\n\n")
            if repeat == "1" or repeat == "2":   
                break
            else:
                print(pattern)
                print("Not an option!")
        if repeat == "2":
            print()
            print(pattern)
            menu()
            break
        print(pattern)
        
def memBkRandomQuestion(): # Generates the random question for memory bank
    operators = ["+","-","x"]
    x = random.randint(1, 99)
    y = random.choice(operators)
    z = random.randint(1, 99)
    question = [x,y,z]
    answer = questionSolver(question)  
    
    return question, answer

def numberGuessor(): # Starts the Number Guessor game
    attempts = 0
    answer = random.randint(1, 99)
    print(pattern)
    print("Guess the correct number from 1-99!")
    # Makes sure guess is a number
    while True:
        while True:
            guess = input()
            if isNumber(guess):
                guess = int(guess)
                break
            else:
                print("Please enter a number!")
        # Makes you keep guessing and counts guesses as attempts
        attempts += 1
        if guess == answer:
            print(pattern)
            print(f"Congrats! You guessed correctly in {attempts} attempts!")          
        else:
            print(pattern)
            print("Sorry thats incorrect. Please guess again.")
            numberCloseness(answer, guess)
            continue
        # Asks if you want to play again
        while True:
            repeat = input("Do you want to play again?\n\n1) Yes\n2) No\n\n")
            if repeat == "1":   
                numberGuessor()
                break
            elif repeat == "2":
                print()
                print(pattern)
                menu()
                break
            else:
                print(pattern)
                print("Not an option!")
  
# Determines how close the guess is to the answer in number guessor
# and the closer the number is to the guess the better the hint is.                                
def numberCloseness(answer, guess):
    difference = abs(answer - guess)
    
    if difference > 50:
        sideDifference = 20
        offset = 12
    elif difference > 40:
        sideDifference = 18
        offset = 10
    elif difference > 30:
        sideDifference = 14
        offset = 6
    elif difference > 20:
        sideDifference = 12
        offset = 5
    elif difference > 10:
        sideDifference = 10
        offset = 3
    else:
        sideDifference = 1
        offset = 1

    leftSide  = (answer - sideDifference) + random.randint(-offset, offset)
    rightSide = (answer + sideDifference) + random.randint(-offset, offset)
    
    if rightSide > 99:
        rightSide = 99
    if leftSide < 1:
        leftSide = 1        
    print()
    print(f"Answer is bewteen {leftSide} and {rightSide}.")
    
def menu(): #Main menu of the program, all games should lead back to here
    print("What do you want to do?")
    print("""
1) Answer Checker 
2) Memory Bank
3) Number Guessor
4) Exit
         """)   
    menu = int(input())   
    if menu == 1:
        x = 0
        y = 0
        print("Format must be ( [Number] {Operator} [Number] = [Number])")
        answerChecker(x, y)
    elif menu == 2:
        memoryBank()
    elif menu == 3:
        numberGuessor()
    else: 
        print("GoodBye.")

pattern = "-"
pattern *= 40    
menu()