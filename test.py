import sys
import inspect
num_of_pucks = 5
counter = 0
locked_counter = 0
spire1 = []
spire2 = []
spire3 = []
spire_list = []
win_setup = []
initial_move_made = False
check_legal_move = False
solved = False


class Puck:
    def __init__(self, value, lock_check, spire_initializer):
        self.value = value
        self.lock_check = lock_check
        self.current_spire = spire_initializer
        self.previous_spire = spire_initializer
        self.next_hop = spire_initializer

class Spire:
    def __init__(self, name, elements):
        self.name = name
        self.elements = elements


#change num_of_pucks variable at top to create "num" pucks
def create_pucks(num):
    global spire_list
    for x in reversed(range(1, num+1)):
        p = Puck(x, False, spire_list[0])
        spire_list[0].elements.append(p)


    
def create_spires(num):
    global spire_list
    for x in range(0, num):
        spire  = Spire(0, [])
        spire.name = x
        spire_list.append(spire)


#called in solution_controller to signal end. called in main while loop to run program               
def win_condition():                                                                                   #possible spire method
    global solved
    if spire_list[len(spire_list)-1] == win_setup:
        solved = True


def solution_controller(puck):
    win_condition()
    if solved != True:
        lock_puck(puck, puck.current_spire)
        set_next_hop(puck)
        if legal_move(puck, puck.next_hop):
           move_controller(puck)
        else:
            next_puck = find_legal_puck(puck)
            move_controller(next_puck)

#handles movement of pucks at high level
def move_controller(puck):
    global counter
    global initial_move_made
    if initial_move_made != True:
        #this only runs first time
        puck.next_hop = initial_move(puck, spire_list[0])
        shift(puck, puck.next_hop)                
        initial_move_made = True
        counter = counter + 1
        print_spires()
        print(f"counter is : {counter}")
    else:
        shift(puck, puck.next_hop)
        counter += 1
        print_spires()
        print(f"counter is : {counter}")                              


def shift(puck, spire):
    #changes values of puck's current and previous spires 
    # and appends() and pops() appropriate spires
    puck.previous_spire = puck.current_spire
    puck.current_spire = spire
    spire.elements.append(puck)
    puck.previous_spire.elements.pop()


def initial_move(puck, spire):
    #only runs for first move of puck#1. sets first puck to 
    # correct spire ensuring least number of moves to solve
    global spire_list
    if len(spire.elements) % 2 == 0:
        return spire_list[1]
    return spire_list[len(spire_list)-1]
    


def get_top(spire):                                                                                           #spire method
    #grab puck object from top of given spire
    if len(spire) > 0:
        return spire[len(spire)-1]
    return []



def highest_number():
    global spire_list
    highest = 0
    for spire in spire_list:
        if spire.elements == []:
            continue
        elif highest == 0:
            highest = get_top(spire.elements)
        elif get_top(spire.elements).value > highest.value:
            highest = get_top(spire.elements)
    return highest
    



def dec_puck(spire_check_list):
    #will eventually replace highest_puck()
    num_list = {}
    cheat_list = {}
    #i will remove cheat when i get method to work and i've had coffee or liqour
    index = 0
    for spire in spire_check_list:
        num_list[index] = spire.elements.value
        cheat_list[index] = spire.elements
        index += 1
    for x in range(0,len(num_list)-1):
        highest_puck_index = max(num_list, key=num_list.get)
        if legal_move(cheat_list.pop(highest_puck_index))
        #need to look over this when i get home
        
                          
     



def find_legal_puck(puck):
    global spire_list
    check_list = []
    for spire in spire_list:
        if spire == []:
            continue
        check_list.append(spire)
    dec_puck(check_list)




def legal_move(puck, spire):
    #puck cannot move to previous spire or sit on puck of lesser value
    if puck.current_spire is not spire and puck.previous_spire is not spire and puck.lock_check != True:
        if len(spire.elements) != 0 and spire.elements[len(spire.elements)-1].value > puck.value:
            return True
        elif len(spire.elements) == 0:
            return  True
    return False



def lock_puck(puck, spire):
    #if puck sitting in proper position at final spire, it can no longer be moved
    global locked_counter
    global win_setup
    global spire_list
    if spire == spire_list[len(spire_list)-1] and puck.value == win_setup[locked_counter].value:
        puck.lock_check = True
        locked_counter = locked_counter + 1



def print_spires():
    #prints spires with puck values
    global spire_list
    for spire in spire_list:
        print(f"{spire.name} [", end ="")
        for puck in spire.elements:
            print(f"{puck.value}", end ="")
        print("]\n")


def set_next_hop(puck):
    global spire_list
    break_for = False
    for spire in spire_list:
        if spire != puck.previous_spire and spire != puck.current_spire and break_for != True:
            puck.next_hop = spire
            break_for = True
            #using break_for is probably terrible
    


create_spires(3)
create_pucks(num_of_pucks)
#current_puck = get_top(spire1)

# print_spires()
# while solved != True:
#     solution_controller(highest_number())
# print("Tower Solved")

