#setting more definitions for valid name
def valid_name(name):
    special_characters = "!@#$%^&*()_-=+|\":;~`?/><{]}[]] "" " 
    for character in name:
        if (character.isdigit() or character in special_characters or character == ""):
            return False
    return True

#making a for loop to find the biggest number in the array 
person_name_and_age = {}
    #asking for user input 
while True:
    while True:
            #asking for user input  
            name = input("Input a name: ")
            space_checker = not name.isspace()

            while not valid_name(name) or name.isspace():
                print("Do not include Special characters or numbers")
                name = input("Enter a name without special characters: ")

            while True:
                try: 
                    age = int(input("Input a age: "))                    
                    if age < 0 or age > 100: 
                        raise 
                    break
                except:
                    print("Enter a valid age ")
                
            #get the info into an array
            person_name_and_age[name] = age

            #ask if the user wants to continue with inputing age and names
            retry = input("Do you want to continue, yes or no? : ")
            break
    
    #if they say no display the name and age of the oldest person
    if retry == "no" or retry == "No" or retry == "NO":

        highest_value = max(person_name_and_age.values())
        highest_names = []

        for value in person_name_and_age: 
            if person_name_and_age[value] == highest_value: 
                highest_names.append(value)
        print(f"The person who is the oldest is: {','.join(highest_names)} they are {highest_value} years old.")
        break

    elif retry != "yes":
        print("Invalid")
        break