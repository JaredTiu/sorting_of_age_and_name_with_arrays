#making a for loop to find the biggest number in the array 
def largest (array):
    biggest_number = array [0]

    for i in array: 
        if i > biggest_number: 
            biggest_number = i
        
    return biggest_number

person_age = []
person_name = {}
    #asking for user input 
while True:
    while True: 
    #setting a definition of a valid name and age
        try: 
            name = input("Input a name: ") 
            person_name = {
                "name": name
            }        

            while True: 
                age = input("Input a age: ")

                if len(age) == 2: 
                    break
                elif len(age) == 1: 
                    break
                person_age.append(age)

            #get the info into an array     
            #ask if the user wants to continue with inputing age and names
            retry = input("Do you want to continue: ")
            break
        except:
            print("INVALID")
#if they say no display the name and age of the oldest person
    if retry == "no":
        result = largest(person_age)
        print(result)
        break
    elif retry != "yes":
        print("Invalid")
        break   
result = largest(person_age)