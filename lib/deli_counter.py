
katz_deli = []

OTHER_DELI = ["Logan", "Avi", "Spencer"]
ANOTHER_DELI = ["Amanda", "Annette", "Ruchi", "Jason", "Logan", "Spencer", "Avi", "Joe", "Rachel", "Lindsey"]

def line(katz_deli):
    if len(katz_deli)==0:
        print("The line is currently empty.")
    else:
        print("The line is currently:",end='')
        for index,n in enumerate(katz_deli):
            print(f"{''} {index+ 1}. {n}",end ='')
        print()
line(katz_deli)
line(ANOTHER_DELI)
line(OTHER_DELI)


def take_a_number(katz_deli,name):
    katz_deli.append(name)
    position=len(katz_deli) 
    # for index,n in  enumerate(katz_deli):
    print(f"Welcome, {name}. You are number {position } in line.")
        
    return katz_deli

take_a_number(katz_deli,'Bon')


    

def now_serving(my_data):
    if len(my_data) == 0:
        print("There is nobody waiting to be served!")
    else:
            next_person=my_data.pop(0)
            print(f"Currently serving {next_person}.")
        
        
    return my_data

    

now_serving(my_data=["Bon", "Collins", "Alice", "Bob"])

