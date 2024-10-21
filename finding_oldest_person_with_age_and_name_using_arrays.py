default_highest_age = -1
name_of_person_with_highest_age = ""
#making a for loop to find the biggest number in the array 
person_name_and_age = {}
    #asking for user input 
while True:
    while True: 
    #setting a definition of a valid name and age
        try: 
            name = input("Input a name: ")

            while True: 
                age = int(input("Input a age: "))

                if age < 0 or age > 100: 
                    raise
                break 

            #get the info into an array
            person_name_and_age = {
                "name": name,
                "age": age
            }        
            
            #ask if the user wants to continue with inputing age and names
            retry = input("Do you want to continue, yes or no? : ")
            break
        except:
            print("INVALID")
#if they say no display the name and age of the oldest person
    if retry == "no":
       for user_name, user_age in person_name_and_age.items(): 
           if user_age > default_highest_age:
                default_highest_age = user_age
                name_of_person_with_highest_age = user_name
                print(f"{name_of_person_with_highest_age} has the highest age, they are  {default_highest_age} years old." )
    elif retry != "yes":
        print("Invalid")
        break