# Authors: Jake O'Brien and Sarah Byrne
# Date: 04/12/2020 
# Description: Create a function of a hangman game

#Function to generate a random word
def rand_word(file_name):
  import random  #random module is used to pick something random
  with open(file_name,'r') as file:  
      my_list = []                       #appending the word on each line in the file to a list
      for line in file:
        my_list.append(line)
      random_numb= random.randint(1,855) #generating a random number to pick a random word in the list
      secret_word=my_list[random_numb].lower()
  return secret_word

#Function to create hangman game
def hangman(start_word,file_name):
  if start_word.lower()=='start': #function only works if 'start' is inputed into parentheses
    import time #time module is used to count how long something is on the screen
    import os #os module is used to clear screen
    import sys  #sys module provides functions and variables used to manipulate different parts of the runtime
    print('\t\t\t - Hangman Game -') # game heading
    print('_________________________________________') #game heading
    print('\n\t~ Please widen screen to play ~')  #recommendation to widen screen
    start_of_game = input('\n\t Press enter to start the game\n\n\t\t\t\t\t') #press enter to start game
    time.sleep(.0001) #once everything on page executed there is 0.0001 seconds until...
    os.system('clear') #this clears the screen
    for x in range (0,4):  #for x in range of 3 numbers, i.e. 3 dots
      z = ("Loading" + "." * x) #'loading' followed by dots multiplied by the position of x
      sys.stdout.write('\r'+z)  #write loading and dots after one another
      time.sleep(0.5) #0.5 secs between dots appearing
    time.sleep(1)
    os.system('clear')
    print('\t\t\t - Hangman Game -')  
    print('_________________________________________')
    print('\n\t\t\t ___________________'
          '\n\t\t\t/                   \ '  #explaining game rules
          '\n\t\t   |     HOW TO PLAY     |'
          '\n\t\t\t\___________________/')
    print("\n\nHelp save Bob from the hangman's noose"
    '\n\nGuess the word right, letter by letter to save Bob'
    '\n\nFail to do so, and Bob will meet his maker (not me)')
    time.sleep(6)
    os.system('clear') 
    print('\t\t\t - Hangman Game -') 
    print('_________________________________________')
    secret_word=rand_word(file_name) 
    letters = list(secret_word)      #turning each letter of the word into an element of a list
    letters.remove('\n')
    print('\n\t\t\t- Word Generated -')
    # print(secret_word) #used to test
    hidden_list = ['*']*(len(secret_word)-1) #creating a list of '*' with the same length as the word
    hidden_string = ''.join(hidden_list)    #joining hidden list together 
    print('\nWord: ', hidden_string)
    print('\n _'
        '\n| |_______________'  #hangman graphic
        '\n| |_______________|'              
        '\n| |               |'
        '\n| |'
        '\n| |'
        '\n| |'
        '\n| |'
        '\n| |'
        '\n| |'
        '\n| |'
        '\n| |'
        '\n| |'
        '\n| |'
        '\n| |'
        '\n| |'
        '\n| |'
        '\n| |'
        '\n| |')
    lives_numb=5  #chances player has is 5
    length_of_word = len(hidden_list)
    while lives_numb>0: #while chances > 0
      while length_of_word>0: #while length of word>0
        letter_input = input('\nEnter a letter: ').lower()  #user puts in letter
        time.sleep(.0001)
        os.system('clear')
        while letter_input.isalpha() == False:  #if user doesn't put in something in the alphabet
          letter_input = input('\nEnter a letter: ')  .lower()  # asks again
          time.sleep(.0001)
          os.system('clear')
        if letter_input not in letters: #if letter input not in word randomly chosen
          lives_numb-=1 #takes a chance away from count
          time.sleep(.0001)
          os.system('clear')
        elif letter_input in letters: #if letter input in random word
          for index in range(0,len(letters)): #for postion of letter in range of letters
            if letter_input==letters[index]:  #if letter inputted equals letter at one of the indexes
              hidden_list[index]=letter_input #hidden list changes at that index to letter inputted
              length_of_word-=1 #take hidden letter away from count
          print('\nWord: ',''.join(hidden_list))  #prints updated hidden list
        if lives_numb == 5: #if chances equals 5
          time.sleep(.0001)
          os.system('clear')
          print('\t\t\t - Hangman Game -')
          print('_________________________________________')
          print('\nWord: ',''.join(hidden_list))
          print('\nYou have',lives_numb,'lives left') #tells user how many lives they have left
          print('\n _'
          '\n| |_______________'
          '\n| |_______________|'  #graphics shown again            
          '\n| |               |'
          '\n| |'
          '\n| |'
          '\n| |'
          '\n| |'
          '\n| |'
          '\n| |'
          '\n| |'
          '\n| |'
          '\n| |'
          '\n| |'
          '\n| |'
          '\n| |'
          '\n| |'
          '\n| |'
          '\n| |')
        elif lives_numb == 4: #chances equals 4
          time.sleep(.0001)
          os.system('clear')
          print('\t\t\t - Hangman Game -')
          print('_________________________________________')
          print('\nWord: ',''.join(hidden_list))
          print('\nYou have',lives_numb,'lives left')
          print('\n _'
          '\n| |_______________'    #graphic change with loss of chance
          '\n| |_______________|'              
          '\n| |               |'
          '\n| |            ___|____'
          '\n| |           / x    x \ '
          '\n| |          |    ..    |'
          '\n| |          \  /\/\/\  /'
          '\n| |           \________/'
          '\n| |'
          '\n| |'
          '\n| |'
          '\n| |'
          '\n| |'
          '\n| |'
          '\n| |'
          '\n| |'
          '\n| |')
        elif lives_numb == 3:
          time.sleep(.0001)
          os.system('clear')
          print('\t\t\t - Hangman Game -')
          print('_________________________________________')
          print('\nWord: ',''.join(hidden_list))
          print('\nYou have',lives_numb,'lives left')
          print('\n _'
          '\n| |_______________'
          '\n| |_______________|'              
          '\n| |               |'
          '\n| |            ___|____'
          '\n| |           / x    x \ '
          '\n| |          |    ..    |'
          '\n| |          \  /\/\/\  /'
          '\n| |           \________/'
          '\n| |                |'
          '\n| |                |'
          '\n| |                |'
          '\n| |                |'
          '\n| |'
          '\n| |'
          '\n| |'
          '\n| |'
          '\n| |')
        elif lives_numb == 2:
          time.sleep(.0001)
          os.system('clear')
          print('\t\t\t - Hangman Game -')
          print('_________________________________________')
          print('\nWord: ',''.join(hidden_list))
          print('\nYou have',lives_numb,'lives left')
          print('\n _'
          '\n| |_______________'
          '\n| |_______________|'              
          '\n| |               |'
          '\n| |            ___|____'
          '\n| |           / x    x \ '
          '\n| |          |    ..    |'
          '\n| |          \  /\/\/\  /'
          '\n| |           \________/'
          '\n| |                |'
          '\n| |                |'
          '\n| |                |'
          '\n| |                |'
          '\n| |               / \ '
          '\n| |              /   \ '
          '\n| |             /     \ '
          '\n| |'
          '\n| |')
        elif lives_numb == 1:
          time.sleep(.0001)
          os.system('clear')
          print('\t\t\t - Hangman Game -')
          print('_________________________________________')
          print('\nWord: ',''.join(hidden_list))
          print('\nYou have',lives_numb,'lives left')
          print('\n _'
          '\n| |_______________'
          '\n| |_______________|'              
          '\n| |               |'
          '\n| |            ___|____'
          '\n| |           / x    x \ '
          '\n| |          |    ..    |'
          '\n| |          \  /\/\/\  /'
          '\n| |           \________/'
          '\n| |                |'
          '\n| |           _____|'
          '\n| |                |'
          '\n| |                |'
          '\n| |               / \ '
          '\n| |              /   \ '
          '\n| |             /     \ '
          '\n| |'
          '\n| |')
        elif lives_numb == 0:
          time.sleep(0.0001)
          os.system('clear')
          print('\t\t\t - Hangman Game -')
          print('_________________________________________')
          print('\nWord: ',''.join(hidden_list))
          print('\nYou have',lives_numb,'lives left')
          print('\n _'
          '\n| |_______________'
          '\n| |_______________|'              
          '\n| |               |'
          '\n| |            ___|____'
          '\n| |           / x    x \ '
          '\n| |          |    ..    |'
          '\n| |          \  /\/\/\  /'
          '\n| |           \________/'
          '\n| |                |'
          '\n| |           _____|____'
          '\n| |                |'
          '\n| |                |'
          '\n| |               / \ '
          '\n| |              /   \ '
          '\n| |             /     \ '
          '\n| |'
          '\n| |')
          time.sleep(2)
          os.system('clear')
          print('\t\t\t - Hangman Game -')
          print('_________________________________________')
          print('\n\n\n\t\tThe word to save Bob was:\n\n\t\t\t\t ',secret_word)  #tells user what the word was
          print('\n\n\t\t\t   \u2620  Loser \u2620') # print unicode emoji either side of 'loser'
          break #break loop
      if length_of_word==0: #if length of word equals 0, all letters are uncovered 
        time.sleep(3)
        os.system('clear')
        print('\t\t\t - Hangman Game -')
        print('_________________________________________')
        print('\n\t\tThe word to save Bob was:\n\n\t\t\t\t ',secret_word)
        print('\n\t\t\t\u2729 CONGRATULATIONS \u2729')  #unicode emoji either side of 'congratulations'
        print('\n\t\t\t\t\u263A Winner \u263A') #unicode either side of 'winner'
        time.sleep(3)
        os.system('clear')
        print('\n _'  #winning graphic
        '\n| |_______________'
        '\n| |_______________|          _______________' 
        '\n| |               |          |              |'
        '\n| |            ___|____      |  YOU SAVED   |'
        '\n| |           / _    _ \    /     ME!!      |'
        '\n| |          |    ..    |  /________________|'
        '\n| |          \  \____/  /'
        '\n| |           \________/'
        '\n| |                |'
        '\n| |           _____|_____'
        '\n| |                |'
        '\n| |                |'
        '\n| |               / \ '
        '\n| |              /   \ '
        '\n| |        _____/_____\_____ '
        '\n| |           |          |'
        '\n| |           |          |')
        break
    time.sleep(3)
    os.system('clear')
  #the function returns 'game over' surrounded by unicode
  print(' \u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728'
  '\n _______         ____            _    _       ______'
  '\n/       \       /    \          / \  / \      |' 
  '\n|              /______\        /   \/   \     |'
  '\n|     ____    /        \      /          \    |__'
  '\n|        |   /          \    /            \   |'
  '\n \_______/  /            \  /              \  |______ '
  '\n  _______                ______  _______   __________'
  '\n /       \  \        /   |       |      |  \        /'
  '\n |       |   \      /    |       |______/   \      / '
  '\n |       |    \    /     |___    |    \      \____/'
  '\n |       |     \  /      |       |     \       __ '
  '\n \_______/      \/       |______ |      \     |__|'
  '\n\n\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728\u2728')
  time.sleep(4)
  os.system('clear')
#Testing the function, function only works if 'start' is inputted in parentheses and a file contain one word on each line is inputted in parentheses
x = 0
import os
while x < 999:  # while x less than 999
  input_Y_or_N=input('\n\n\n\t\t\u23F3  Type Yes to play or No to quit \u23F3\n\n\t\t\t\t\t\t') #input to start
  if input_Y_or_N.lower()=='yes': #if input = yes
    os.system('clear')  #clear to start screen
    print(hangman('start','hangman.txt'))
  if x == 998:  #easter egg 
    print('\n\n\t\t\t\tGo Outside!!')
  elif input_Y_or_N.lower()=='no':  #if input = no
    os.system('clear')  #quit game
    break
  else: #anything else entered will clear
    os.system('clear')
  x+=1  #loop will start again
