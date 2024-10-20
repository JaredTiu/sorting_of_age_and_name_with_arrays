#asking for user input 
for i in range(2): 
    try:  
        name = input("Input a name: ") 

        while True: 
            age = int(input("input a age: "))

            if len(age) != 2: 
                print("INVALID")
    except:
        print("Invalid") 
        

#setting a definition of a valid name and age 

#get the info into an array 

#ask if the user wants to continue with inputing age and names 

#if they say no display the name and age of the oldest person

