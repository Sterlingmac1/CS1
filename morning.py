import time 

print ("alarm")                                                 #displays the message "ALARM"

while True:                                                     #forever loop                      
    snooze =str.lower(input("snooze? y/n: "))                   #stores user response in variable snooze and convert to lower case

    if snooze == "y":                                           #if the user snoozes
        print("sleep for 5 more minutes")                       #display message 
        time.sleep(2)                                           #wait 2 seconds
        print("alarm")                                          #display message
    elif snooze == "n":                                         #if user doesn't snooze
        print("get up")                                         #display message
        break                                                   #end forever loop
    else:                                                       #if user response with anything else
        print("invalid response")                               #display message                              
print("take a shower")                                          #display message                                       

while True:                                                     #forever loop
    brush_teeth = input ("should brush teeth? y/n: ").lower()   #stores user response in variable should brush teeth and convert to lower case

    if brush_teeth == "y":                                      #if user y
        print("brush teeth")                                    #display message
        print("take shower")                                    #display message
        break                                                   #end forever loop
    elif brush_teeth == "n":                                    #if user response with n
        print("take shower")                                    #display message
        break                                                   #end loop
    else:                                                       #if user response anything else
        print("invalid response")                               #display message 
print("wear black shirt")                                       #display message 

while True:                                                     #forever loop
    wear_black_shirt = input ("wear black shirt? y/n: ").lower()#stores user response in variable wear black shirt and convert to lower case

    if wear_black_shirt == "y":                                 #if the user wear black shirt
        print("put on shirt")                                   #display message
        break                                                   #end forever loop
    elif wear_black_shirt == "n":                               #if user doesn't wear black shirt
        print("put on white shirt")                             #display message
        break                                                   #end forever loop
    else:                                                       #if user response with anything else
        print("invalid response")                               #display message
print("eat at home")                                            #display message

while True:                                                     #forver loop
    eat_at_home = input("Should eat at home? y/n: ").lower()    #stores user response in variable should eat at home and convert to lower case

    if eat_at_home == "y":                                      
        print("make breakfast")
        print("eat at home")
        break
    elif eat_at_home == "n":
        print("eat at school")
        break
    else:
        print("invalid response")
print("drive to school")

while True:
    drive_to_school = input("should drive in car to school? y/n: ").lower()

    if drive_to_school == "y":
        print("drive to school")
        break
    elif drive_to_school == "n":
        print("take the bus")
        break
    else:
        print("invalid response")





