mainMenuRepeat = 1
while mainMenuRepeat == 1 :
    print("""\nWelcome to the calculator program.
  1. Add
  2. Subtract
  3. Divide
  4. Multiply
  5. Exit """)
    menuSelect = int(input("Enter a number: ")) 
          
    if menuSelect == 1 :
            mainMenuRepeat = 2
            while mainMenuRepeat == 2 :
                numberAdd1 = int(input("Enter the first number: "))
                numberAdd2 = int(input("Enter the second number: "))
                print(numberAdd1,"+",numberAdd2,"=",numberAdd1 + numberAdd2)
                print("\n1. Main Menu\n2. Repeat")      
                mainMenuRepeat = int(input("Enter a number: "))
                      
    elif menuSelect == 2 : 
            mainMenuRepeat = 2
            while mainMenuRepeat == 2 :
                numberAdd1 = int(input("Enter the first number: "))
                numberAdd2 = int(input("Enter the second number: "))
                print(numberAdd1,"-",numberAdd2,"=",numberAdd1 - numberAdd2)
                print("\n1. Main Menu\n2. Repeat")      
                mainMenuRepeat = int(input("Enter a number: "))
             
    elif menuSelect == 3 :
            mainMenuRepeat = 2
            while mainMenuRepeat == 2 :
                numberAdd1 = int(input("Enter the first number: "))
                numberAdd2 = int(input("Enter the second number: "))
                print(numberAdd1,"/",numberAdd2,"=",numberAdd1 / numberAdd2)
                print("\n1. Main Menu\n2. Repeat")      
                mainMenuRepeat = int(input("Enter a number: "))
           
    elif menuSelect == 4 : 
            mainMenuRepeat = 2
            while mainMenuRepeat == 2 :
                numberAdd1 = int(input("Enter the first number: "))
                numberAdd2 = int(input("Enter the second number: "))
                print(numberAdd1,"*",numberAdd2,"=",numberAdd1 * numberAdd2)
                print("\n1. Main Menu\n2. Repeat")      
                mainMenuRepeat = int(input("Enter a number: "))
            
    elif menuSelect == 5 :  
        mainMenuRepeat = 2
        print("\nGoodbye")
    else: 
        print("\nNOT AN OPTION")
    
    

       
        
    
    
    