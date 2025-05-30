import random  # Imports random

print("Hello human, I am the magic 8 ball!")                                                     # Displays the message

responses = ["yes", "no", "maybe", "ask later"]                                                  # Creates a list of possible responses

question_words = ["when", "which", "is", "where", "who", "what","whose", "will"]              # Creates a list of words that are common in questions


while True:                                                                                  # Forever loop 
    question = str.lower(input("Ask Any Question! "))                                        # Sets question to user input and makes it lowercase
    first_word = question.split()[0]                                                          # Sets first_word to the first word of the question
    
    if question == "stop":                                                                   # If the question equals "stop", break the loop and end the program
        break                                                                                # a break in code
    elif "?" in question and first_word in question_words:                                     # If it's a question and starts with a valid question word
        print(random.choice(responses))                                                      # Display a random response from the list
    else:                                                                                     # If the input is not a valid question
        print("that is not a question")                                                      # Displays the message 
