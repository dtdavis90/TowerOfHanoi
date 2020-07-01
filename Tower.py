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

def first_move(spire):
    win_setup = spire1
    if len(spire) % 2 == 0:
        spire2.append(get_top(spire1))
    else:
        spire3.append(get_top(spire1))
    spire1.pop()


#return spire with highest(largest) number
def highest_number(num):
    highest = num
    highest_value_spire = []
    temp_list = [spire1, spire2, spire3]
    for item in temp_list:
        if item != []:
            temp_value_holder = get_top(item)
            if temp_value_holder.value == highest:
                #highest = temp_value_holder.value
                highest_value_spire.append(item)
# need to handle if num is not found at top of a spire
    return highest_value_spire[len(highest_value_spire)-1]


    

def print_spires():
    print(spire1)
    print(spire2)
    print(spire3)



def create_pucks(num):
    num_counter = num
    for x in range(0, num):
        p = puck()
        p.value = num_counter
        spire1.append(p)
        num_counter -= 1


def legal_move(puck, spire):
    if puck.current_spire is not spire and puck.previous_spire is not spire :
        if len(spire) != 0:
            check_puck = spire[len(spire)-1]
    
            if puck.value > check_puck.value  :
                return True
        elif len(spire) == 0:
            return  True
    else:
        return False
    
    

def move(puck):
    global counter
    global initial_move
    win_condition()
    puck_decrement = puck.value - 1
    puck_increment = puck.value + 1
    if initial_move == False:
        first_move(spire1)
        initial_move = True
        counter = counter + 1
        #call move() with puck increment
    else:
        print("got into else")
        free_spire(puck)
        print("next hop is: " + str(puck.next_hop))
        print("puck value is: " + str(puck.value))
        print("Top of next_hop spire is: " + str(get_top(puck.next_hop)))
        if puck.lock_check == False:
            if legal_move(puck, puck.next_hop):
                puck.previous_spire = puck.current_spire
                puck.current_spire = puck.next_hop
                puck.next_hop.append(puck)
                puck.previous_spire.pop()
                counter += 1
                #call move(highest(with puck increment)) 
            else:
             
        # else, call move with smaller puck
        # decrement puck
        # get spire by puck value
        # vall get_top of that spire
        # use that puck to call move()
                return 0



def win_condition():
    if spire3 == win_setup:
        solved = True
    
    
def lock_puck(puck, spire):
    if spire == spire3 and puck.value == win_setup[locked_counter]:
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
    

create_pucks(3)
highest_number()

move(spire1[2])
move(spire1[1])

print_spires()
print("counter is " + str(counter))


