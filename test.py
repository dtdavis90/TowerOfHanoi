import sys
import inspect
num_of_pucks = 3
counter = 0
locked_counter = 0
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
    global win_setup
    for x in range(0, num):
        spire  = Spire(0, [])
        spire.name = x
        spire_list.append(spire)


#called in solution_controller to signal end. called in main while loop to run program      
def set_win_condition():
    global spire_list
    for puck in spire_list[0].elements:
        win_setup.append(puck)

def check_win_condition():                                                                                   #possible spire method
    global solved
    global spire_list
    if spire_list[len(spire_list)-1].elements == win_setup:
        solved = True


def solution_controller(puck):
    
    if solved != True:
        move_controller(puck)
        check_win_condition()


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
    
def find_legal_puck():
    global spire_list
    check_list = []
    for spire in spire_list:
        if spire.elements == []:
            continue
        check_list.append(spire)
    new_puck = next_puck(check_list)
    return new_puck


def next_puck(spire_check_list):
    puck_value_list = {}
    puck_list = {}
    index = 0
    for spire in spire_check_list:
        puck_value_list[index] = spire.elements[len(spire.elements)-1].value
        puck_list[index] = (spire.elements[len(spire.elements)-1])
        index += 1

    highest_puck_index = max(puck_value_list, key=puck_value_list.get)

    for x in range(0, len(puck_value_list)):
        puck = puck_list[highest_puck_index]
        lock_puck(puck)
        set_next_hop(puck)
        if(legal_move(puck)):
            return puck
        puck_list.pop(highest_puck_index)
        puck_value_list.pop(highest_puck_index)
        highest_puck_index = max(puck_value_list, key=puck_value_list.get)
    

def legal_move(puck):
    #puck cannot move to previous spire or sit on puck of lesser value
    spire = puck.next_hop
    if spire == None:
        return False
    if puck.current_spire is not spire and puck.previous_spire is not spire and puck.lock_check != True:
        if len(spire.elements) != 0 and spire.elements[len(spire.elements)-1].value > puck.value:
            return True
        elif len(spire.elements) == 0:
            return  True
    return False


def lock_puck(puck):
    #if puck sitting in proper position at final spire, it can no longer be moved
    global locked_counter
    global win_setup
    global spire_list
    spire = puck.current_spire
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
    break_if = False
    if puck.previous_spire is puck.current_spire:
        puck.next_hop = find_empty_spire(spire_list)
        break_if = True
    for spire in spire_list:          
        if spire != puck.previous_spire and spire != puck.current_spire and break_if != True:
            puck.next_hop = spire
            break_if = True
            #using break_if is probably terrible

def find_empty_spire(spire_list):
    #helper method for set_next_hop
    for spire in spire_list:
        if spire.elements == []:
            return spire
        




create_spires(3)
create_pucks(num_of_pucks)
set_win_condition()
print_spires()
while solved != True:
    solution_controller(find_legal_puck())
print("Tower Solved")
