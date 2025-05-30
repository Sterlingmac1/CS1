def add_entry (websites, usernames, passwords):
    '''
    Adds an entry to the parallel array of websites, usernames, and passwords
    Args:
        websites (list): the list of websites
        usernames (list): the list of usernames
        passwords (list): the list of passwords
    Returns:
        parallel array: newly added to array of websites, usernames, and passwords    
    '''
    website = input("enter the name of website")
    username = input("enter your username")
    password = input("enter your password")
    websites.append(website)
    usernames.append(username)
    passwords.append(password)

def print_entry(website, username, password):
	print(f"website: {website}; username: {username}, Passord: {password}")

def get_index (websites):
      while True:
        website = input ("enter your website")
        
        if website in websites:
            return websites.index(website)
'''
Forever loop:
If website is in websites:
Return index of website in websites
Else:
    Print not in websites
'''  
def enter_password (tries):    
    for i in range(tries)
        password_keeper_password = input("type in your password")
            if password_keeper_password == secret_password:
            else:
                print(f"inccorect password. You have 3 tries left")
        print ("to many tries you will be kicked out")
        exit()
safe_passwords = ["pancake_lover","Wyatt123", "charmy24","buger5","happyman1"]
def main():
    websites = []
    usernames = []
    passwords = []

    add_entry(websites, usernames, passwords)

    while True:
        option = input ('''what option would you like? Enter "q" to quit.
1. Add an entry
2. print a specific website with its corresponding username and password
3. print all the websites, usernames, and passwords
                                     
Enter here ''').lower()
        
        if option == "q":
            break
        elif option == "1":
            add_entry(websites, usernames, passwords)
        elif option == "2":
            index = get_index(websites)
            print_entry(websites[index], usernames[index], passwords[index])
        elif option == "3":
            for index in range(len(websites)):
                print_entry(websites[index], usernames[index], passwords[index])
        elif option == "4":
            print (random.choice)(safe_passwords)
main()

def enter_password():
    while true:
        password_for_password_keeper = input
        if password_for_password_keeper == (Sterling McCall)
def generate_password(length=5): 





