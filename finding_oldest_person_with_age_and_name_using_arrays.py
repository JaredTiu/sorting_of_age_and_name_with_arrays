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
            person_name_and_age[name] = age
            #ask if the user wants to continue with inputing age and names
            retry = input("Do you want to continue, yes or no? : ")
            break
        except:
            print("INVALID")
#if they say no display the name and age of the oldest person
    if retry == "no":

        highest_value = max(person_name_and_age.values())
        highest_names = []

        for key in person_name_and_age: 
            if person_name_and_age[key] == highest_value: 
                highest_names.append(key)
        print(f"The person who is the oldest is: {highest_names} They are {highest_value} years old.")
        break
    
    elif retry != "yes":
        print("Invalid")
        break