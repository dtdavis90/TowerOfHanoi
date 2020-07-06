#tester
num_of_pucks = 3
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


class puck:
    value = 0
    current_spire = spire1
    previous_spire = spire1
    next_hop = spire1 
    lock_check = False


#grab puck object from top of given spire
def get_top(spire):
    if len(spire) > 0:
        return spire[len(spire)-1]
    else:
        return []

#set first puck to correct spire ensuring least number of moves to solve
def first_move(puck, spire):
    if len(spire) % 2 == 0:
        puck.next_hop = spire2
        puck.next_hop.append(get_top(spire1))
        puck.current_spire = spire2
    else:
        puck.next_hop = spire3
        puck.next_hop.append(get_top(spire1))
        puck.current_spire = spire3
    


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
    #print(f"current_stack_position: {current_stack_position}")




def create_pucks(num):
    num_counter = num
    for x in range(0, num):
        p = puck()
        p.value = num_counter
        spire1.append(p)
        win_setup.append(p)
        num_counter -= 1


#puck cannot move to previous spire or sit on puck of lesser value
def legal_move(puck, spire):
    if puck.current_spire is not spire and puck.previous_spire is not spire and puck.lock_check != True:
        if len(spire) != 0:
            check_puck = spire[len(spire)-1]
            if puck.value < check_puck.value  :
                return True
        elif len(spire) == 0:
            return  True
    else:
        return False

        
#return spire with puck containing num at top
def highest_number():
    highest = 0
    highest_value_spire = []
    simplified_list = []         #using this instead of highest_value_spire[] speeds up second for loop
    temp_list = [spire1, spire2, spire3]
    for item in temp_list:
        if item != []:
            highest_value_spire.append(item)
    for top in highest_value_spire:
        if get_top(top).value > highest:
            highest = get_top(top).value
            simplified_list.append(top)

    return get_top(get_top(simplified_list))


#return puck with value - 1 less than previous puck value
def dec_puck(num):
    temp_list = [spire1, spire2, spire3]
    check_list = []
    for item in temp_list:
        if item != []:
            if get_top(item).value == num:
                check_list = item
                return get_top(check_list)
    #this only runs if num not found
    if check_list == []:
        return 0
    
    
def move(puck):
    global counter
    global initial_move
    # not sure if this line still necessary
    if initial_move != True:           #this only runs first time 
        first_move(puck,spire1)
        spire1.pop()                   
        initial_move = True
        counter = counter + 1
        print(f"counter is : {counter}")
        print_spires()
        

    else:
        puck.previous_spire = puck.current_spire
        puck.current_spire = puck.next_hop
        puck.next_hop.append(puck)
        puck.previous_spire.pop()
        counter += 1
        print(f"counter is : {counter}")
        print_spires()                              #move fuckery. too much recursion
       

        

#never used. figure it out                
def win_condition():
    #global solved
    if spire3 == win_setup:
        #solved = True
        return True
    
#if puck sitting in proper position at spire3, it can no longer be moved
def lock_puck(puck, spire):
    global locked_counter
    global win_setup
    if spire == spire3:
       # if puck.value == 1 and pcuk.value == win_setup[locked_counter].value:

        if puck.value == win_setup[locked_counter].value:
            puck.lock_check = True
            locked_counter = locked_counter + 1


#i hate myself for this
def free_spire(puck):
    if puck.current_spire == spire1:
        if puck.previous_spire == spire1:            #initial condition for unmoved puck
            if not spire2:                           # check if spire2 & spire3 are empty with "not"
                puck.next_hop = spire2
            elif not spire3:
                puck.next_hop = spire3
        elif puck.previous_spire == spire2:
            puck.next_hop = spire3
        elif puck.previous_spire == spire3:
            puck.next_hop = spire2
    elif puck.current_spire == spire2:
        if puck.previous_spire == spire1:
            puck.next_hop = spire3
        elif puck.previous_spire == spire3:
            puck.next_hop = spire1
    elif puck.current_spire == spire3:
        if puck.previous_spire == spire1:
            puck.next_hop = spire2
        elif puck.previous_spire == spire2:
            puck.next_hop = spire1


# puck == 0 and 
   
def controller(puck):
    win_condition
    lock_puck(puck, puck.current_spire)
    free_spire(puck)
    if legal_move(puck, puck.next_hop):
        move(puck)
    else:
        find_legal_puck(puck)
        #handle next smallest puck not found or not legal move
        

        # this is repeated to handle lock_check failure
    # else:             
    #     puck = dec_puck(puck_decrement)
    #     while  puck == 0:
    #             puck_decrement = puck_decrement - 1
    #             puck = dec_puck(puck_decrement)    
    #     if puck != 0:
    #         move(puck)

        


    #handle illegal move and lock _puck failure [decrement]


def find_legal_puck(puck):
    puck_decrement = puck.value - 1
    puck = dec_puck(puck_decrement)
    while puck == 0:
            puck_decrement = puck_decrement - 1
            puck = dec_puck(puck_decrement)
            if puck != 0 and legal_move(puck, puck.next_hop) == True:
                return puck
    if puck != 0 and legal_move(puck, puck.next_hop) == True:
        return puck
    else :
        current_puck = puck





create_pucks(num_of_pucks)
current_puck = get_top(spire1)
print_spires()
try:
    while solved != True:
        controller(highest_number())
    print("Tower Solved")
except RecursionError:
    print("failed out")
print("counter is " + str(counter))
