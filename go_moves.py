
# My attempt at creating a game based on the classic "GO" board game
# Created by Peyton Kocher for my ENGR 102 Project

import random 


# Create a board using "lists within lists" so we can index the changes on the board

board = [                                         # Row visual:
    [".", ".", ".", ".", ".", ".", ".", ".", "."],     # 0
    [".", ".", ".", ".", ".", ".", ".", ".", "."],     # 1
    [".", ".", ".", ".", ".", ".", ".", ".", "."],     # 2
    [".", ".", ".", ".", ".", ".", ".", ".", "."],     # 3
    [".", ".", ".", ".", ".", ".", ".", ".", "."],     # 4
    [".", ".", ".", ".", ".", ".", ".", ".", "."],     # 5
    [".", ".", ".", ".", ".", ".", ".", ".", "."],     # 6
    [".", ".", ".", ".", ".", ".", ".", ".", "."],     # 7
    [".", ".", ".", ".", ".", ".", ".", ".", "."]      # 8
    ]

# Create two lists to label the columns and the rows
column_labels = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]

row_labels = ["1", "2", "3", "4", "5", "6", "7", "8", "9"] 

# Define the first player's piece

current_player = "X" 

# To make the game feel more real here's some silly phrases I made for invalid inputs -Peyton


############ INVALID PHRASES SECTION ############

taken_place_phrases = ["You can't just obliterate your opponent's piece from the board, but nice try", 
                       "Hey, the Aggie code of conduct says you can't cheat! Input a valid move or else.",
                       "Does that look like an empty spot? Try again"]


invalid_column_phrases = ["Do we need to go back to learning the alphabet? I guess it has been years since we reviewed it ... pleaser enter a valid letter (A-I)", 
                          "I alpha - bet you're not looking at the column options, please try again :)", 
                          "Please try and look at the column options ... if you can't get this, maybe UT will suit you better :)"]


invalid_row_phrases = ["I know this is a hard class but if you can't count from 1-9, maybe you should drop out ... you'll fit right into UT liberal arts though!", 
                       "Maybe looking at your fingers will help you count... please enter a number 1-9"]


game_over_phrases = ["Someone felt like giving up early hehe ... game over!", 
                     "It's ok you can stop playing ... not like we spent HOURS making this for you! Jk, hope it was fun :D",
                    "G A M E  O V E R\n...how sad"]

####### Algorithm #######

while True:
    # Randomly selects a phrase we created in the lists above:
    random_taken_place = random.choice(taken_place_phrases)
    random_invalid_column = random.choice(invalid_column_phrases)
    random_invalid_row = random.choice(invalid_row_phrases) 
    random_game_over = random.choice(game_over_phrases)

    # Join the column and row labels to the 9x9 matrix board and output / display the board to console.
	# Add the column labels A-I to the top of the board variable, matching the spacing of the  ".” s
	# Add the row labels 1-9 to the left of the board and correspond / increment the numbers beginning with 1 in the first row and 9 in the final row.
    
    print("                   " + " ".join(column_labels))
    for i in range(9):   

    #      ":>" indents the rows to the right in the terminal view (feel free to change it for diff UI)
        print(f"{row_labels[i]:>18} " + " ".join(board[i]))    # " ".join(board[i]) spaces out the dots of our board. The "i" denotes the "outer" part of our lists within lists, and our labels need to be here on the outside


    # Output to the console a message displaying that it’s the current_player ‘s turn to move. 
    print()
    print(f"{current_player}'s turn to play")
    print()     # whitespace for a slightly more aesthetic UI


    # Column (letter) input:

    # Create a user-entered column input, defined by the variable “letter” in which the user enters a column letter. Also create a user-entered row input, defined by “number_move” in which the user enters a row number.
    letter = input("Enter a column letter: ").upper()   # column list is in uppercase, so convert input

    
# Create a condition to check if either the user’s inputs contain “stop” and immediately end the game and show the final state of the board.
    # In case user enters various capitalization forms of “stop” , have the condition  automatically convert it to lowercase.

    if letter.lower() == "stop":
        print(random_game_over)
        break
    
    #Create a condition to check if letter or number_move is not within the labels we defined towards the beginning. 
    # For invalid entries, output to the console that this is an invalid move and make the player re-enter an input until it’s valid.
    if letter not in column_labels:
        print(random_invalid_column)
        print()
        continue

    # Row (number) input:
    # Check if the user entered "stop", to stop the game
    number_move = input("Enter a row number: ") 
    if number_move.lower() == "stop":
        print(random_game_over)
        break

    # Condition checking if the user input is not within the list we defined
    if number_move not in row_labels:
        print(random_invalid_row)
        print()
        continue

   # If letter and number_move are both within their defined labels, create a variable, “board_row” to take the user’s number input and convert it into an integer, and subtract it by 1, to start reindexing the blank space.
    if (letter in column_labels) and (number_move in row_labels):

        # Create a variable, “board_column” which takes the user’s input and indexes the inputted “letter” to the column_labels list.
        board_row = int(number_move) - 1     
        board_column = column_labels.index(letter) 

        # print(board_column) -- testing that user's letter input gets correctly defined

        # Nest these indexes to find the respective location in the lists. Check to see if this nested index location is equal to a “.” 
	    # If the location is a “.”, replace the “.” with the current_player’s piece
	    # If the nested index location does not equal the string “.” , output to the console that the place is invalid
        
        if board[board_row][board_column] == ".":
        #A1
            # Here is where the board actually updates to the user's "piece"
            board[board_row][board_column] = current_player
        
            # Checking which player's piece to input
            current_player = "O" if current_player == "X" else "X"  
    
    
    # Invalid inout phrases:
    else:
        print(taken_place_phrases)
        print() # whitespace

