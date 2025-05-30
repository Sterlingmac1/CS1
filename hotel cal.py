import random

def chorus():
    '''
    Prints the chorus of a song
    Args:
        None
    returns:
        print: Chorus
    '''
    print('''"Welcome to the Hotel California
Such a lovely place (such a lovely place)
Such a lovely face
Plenty of room at the Hotel California
Any time of year (any time of year)
You can find it here"''')
    
def sing_song():
    '''
    Uses the previos function to sing a song
    Args:
        None
    returns:
        print:entire song
    '''
    print('''
On a dark desert highway, cool wind in my hair
Warm smell of colitas rising up through the air
Up ahead in the distance, I saw a shimmering light
My head grew heavy and my sight grew dim, I had to stop for the night
There she stood in the doorway, I heard the mission bell
And I was thinkin' to myself, "This could be heaven or this could be hell"
Then she lit up a candle and she showed me the way
There were voices down the corridor, I thought I heard them say
    ''')
    chorus()
    print('''
Her mind is Tiffany-twisted, she got the Mercedes-Benz, uh
She got a lot of pretty, pretty boys that she calls friends
How they dance in the courtyard, sweet summer sweat
Some dance to remember, some dance to forget
So I called up the Captain, "Please bring me my wine"
He said, "We haven't had that spirit here since 1969"
And still, those voices are calling from far away
Wake you up in the middle of the night just to hear them say
    ''')
    chorus()
    print('''
Mirrors on the ceiling, the pink champagne on ice
And she said, "We are all just prisoners here of our own device"
And in the master's chambers, they gathered for the feast
They stab it with their steely knives, but they just can't kill the beast
Last thing I remember, I was running for the door
I had to find the passage back to the place I was before
"Relax, " said the night man, "We are programmed to receive
You can check out any time you like, but you can never leave"
    ''')
def add(a,b):
    '''
    Takes two numbers and prints their sum
    Args:
        a (int): first number
        b (int): second number
    Returns:
        print: sum of the two numbers 
    '''
    print(a+b)
def print_list(array):
    '''
    Takes a list and prints every element in that list individually(vertically)
    Args:
        array (list): given list to print
    Returns:
        print: each element in the list vertically
    '''
    for item in array:
        print(item)
def in_list(array, element):
    '''
    Takes a list and element and returnes a boolean based on if the element is in the list
    Args:
        array (list):
        element (any): 
    returns:
        bool: True/False if element in array
    '''
    return element in array
def is_integer(number):
    '''
    Takes one parameter and returns whether it is an integer
    Args
        number (any): parameter to check
    Returns:
        bool: True/False based on if number is an integer
    Raises:
        ValueError: if number is not an integer
    '''
    try:
        int(number)
        return True
    except ValueError:
        return False
def get_integers ():
    '''
    Uses user input to get an integer
    Args:
        None
    Returns:
        int: num given by user
        '''
    while True:
        a = input ('enter your first number')
        b = input ('enter your second number')
        if is_integer(a) and is_integer(b):
            return int(a), int(b)
def get_random():
    a,b = get_integers()
    print(random.randint(a,b))    
def count_vowels(string):
    '''
    Takes a string and returns the number of vowels in it
    Args:
        none
    Returns:
        the number of vowels in a sentence
    '''
    num_vowels = 0
    for character in string:
        if character in ['a','i','u','o','e']:
            num_vowels +=1
    return num_vowels
def subtract(x,y):
    '''
    subtracts two integers together
    Args:
        none
    Returns:
        the total number from the problem
    '''
    print(x-y)
def multiply (x,y):
    '''
    multiplies two integers together
    Args:
        none
    Returns
        the total number from the multiplication problem
    '''
    print(x*y)
def divide (x,y):
    '''
    divides two integers together
    Args:
        none
    Returns:
        the total number from the divide problem
    '''
    print (x/y)
def main():
    
    option = input ("What would you like to do? 1. Sing a song, 2. add, subtract, multiply or divide two numbers 3. Takes a list and prints every element in that list individually(vertically), 4. Takes a list and element and returnes a boolean based on if the element is in the list, 5. Takes one parameter and returns whether it is an integer ")
    if option == "1":
        sing_song()
    elif option == "2":
        a, b = get_integers()

        operation = input('+/-/*/|')

        if operation == "+":
            add(a, b)
        elif operation == '-':
            subtract(a, b)
        elif operation == '*':
            multiply(a, b)
    elif option == "3":
        my_list = [1, 2, 3, 4, 5]
        print_list(my_list)
    elif option == "4": 
        print(is_integer("3"))
        print(is_integer("hello"))
    elif option == "5": 
        get_random()
    elif option == "6":
        string = input('enter the text you would like to check for vowels: ')
        print (count_vowels(string))
    

main()

    









