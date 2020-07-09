num_of_pucks = 5
import sys
import inspect
counter = 0
locked_counter = 0
spire1 = []
spire2 = []
spire3 = []
win_setup = []
initial_move = False
check_legal_move = False
solved = False


class Puck:
    value = 0
    current_spire = spire1
    previous_spire = spire1
    next_hop = spire1 
    lock_check = False

#change num_of_pucks variable at top to create "num" pucks
def create_pucks(num):
    num_counter = num
    for x in range(0, num):
        p = Puck()
        p.value = num_counter
        spire1.append(p)
        win_setup.append(p)
        num_counter -= 1


#called in solution_controller to signal end. called in main while loop to run program               
def win_condition():
    global solved
    if spire3 == win_setup:
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
    global initial_move
    if initial_move != True:
        #this only runs first time 
        first_move_spire = first_move(puck,spire1)
        shift(puck, first_move_spire)                
        initial_move = True
        counter = counter + 1
        print(f"counter is : {counter}")
        print_spires()
    else:
        shift(puck, puck.next_hop)
        counter += 1
        print(f"counter is : {counter}")
        print_spires()                              


def shift(puck, spire):
    #changes values of puck's current and previous spires 
    # and appends() and pops() appropriate spires
    puck.previous_spire = puck.current_spire
    puck.current_spire = spire
    spire.append(puck)
    puck.previous_spire.pop()


def first_move(puck, spire):
    #only runs for first move of puck#1. sets first puck to 
    # correct spire ensuring least number of moves to solve
    if len(spire) % 2 == 0:
        return spire2
    return spire3
    


def get_top(spire):
    #grab puck object from top of given spire
    if len(spire) > 0:
        return spire[len(spire)-1]
    return []



def highest_number():
    #return spire with puck containing highest number at top
    temp_high_num = 0
    highest_num_puck = 0
    highest_value_spire = []
    simplified_list = []                         
    temp_list = [spire1, spire2, spire3]
    for item in temp_list:
        if item != []:
            highest_value_spire.append(item)
    for top in highest_value_spire:
        if get_top(top).value > temp_high_num:
            temp_high_num = get_top(top).value
            simplified_list.append(top)
    highest_num_puck = get_top(get_top(simplified_list))
    return highest_num_puck



def dec_puck(num):
    #return puck with value - 1 less than previous puck value
    temp_list = [spire1, spire2, spire3]
    check_list = []
    for item in temp_list:
        if item != []:
            check_list.append(item)
    for item in check_list:
        if get_top(item).value == num:
            return get_top(item)
    #this only runs if num not found
    return 0



def find_legal_puck(puck):
    #this will continue to decrement puck by calling
    #dec_puck() until it finds a puck that can legally move
    puck_decrement = puck.value - 1
    puck = dec_puck(puck_decrement)
    while puck == 0:
            puck_decrement = puck_decrement - 1
            puck = dec_puck(puck_decrement)
            if puck != 0 and legal_move(puck, puck.next_hop) == True:
                return puck
    set_next_hop(puck)
    if puck != 0 and legal_move(puck, puck.next_hop) == True:
        return puck
    else:
        
        while puck != 0 and legal_move(puck, puck.next_hop) != True or puck == 0:
            puck_decrement = puck_decrement - 1
            puck = dec_puck(puck_decrement)
            #next line will crash if puck is not found. puck == 0
            if puck != 0:
                set_next_hop(puck)
    return puck



def legal_move(puck, spire):
    #puck cannot move to previous spire or sit on puck of lesser value
    # if puck.lock_check:
    #     return False
    # if puck.current_spire is spire or 
    if puck.current_spire is not spire and puck.previous_spire is not spire and puck.lock_check != True:
        if len(spire) != 0 and spire[len(spire)-1].value > puck.value:
            return True
        elif len(spire) == 0:
            return  True
    else:
        return False



def lock_puck(puck, spire):
    #if puck sitting in proper position at spire3, it can no longer be moved
    global locked_counter
    global win_setup
    if spire == spire3 and puck.value == win_setup[locked_counter].value:
        puck.lock_check = True
        locked_counter = locked_counter + 1

   
#this prints just the value of the given puck
def print_spires():
    spire1P = []
    spire2P = []
    spire3P = []
    for x in spire1:
        spire1P.append(x.value)
    for x in spire2:
        spire2P.append(x.value)
    for x in spire3:
        spire3P.append(x.value)
    print(spire1P)
    print(spire2P)
    print(spire3P)



def set_next_hop(puck):
    spire_list = [spire1, spire2, spire3]
    for spire in spire_list:
        if spire != puck.previous_spire and spire != puck.current_spire:
            puck.next_hop = spire
    if puck.current_spire == spire1 and puck.previous_spire == spire1:
        if not spire2:
            puck.next_hop = spire2
        elif not spire3:
            puck.next_hop == spire3



create_pucks(num_of_pucks)
current_puck = get_top(spire1)
print_spires()
while solved != True:
    solution_controller(highest_number())
print("Tower Solved")

