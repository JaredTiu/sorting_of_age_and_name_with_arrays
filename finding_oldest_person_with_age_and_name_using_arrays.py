person_age_and_name = {}
#asking for user input 
while True: 
    #setting a definition of a valid name and age
    try: 
        while True:
            name = input("Input a name: ") 
            
            if name != int:
                print("Input a valid name: ")
            elif name == str:
                break
                
            while True: 
                age = input("Input a age: ")

                if len(age) == 2: 
                    break
                elif len(age) == 1: 
                    break

            #get the info into an array     
            person_age_and_name = {
                "name": name,
                "age": age
            }
            print(person_age_and_name ["name"])
            print(person_age_and_name ["age"])
    except:
        print("INVALID")    
#ask if the user wants to continue with inputing age and names 

#if they say no display the name and age of the oldest person
