counter = 0
locked_counter = 0
spire1 = []
spire2 = []
spire3 = []
win_setup = []
initial_move = False
check_legal_move = False
solved = False
max_num = None


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

def first_move(puck, spire):
    if len(spire) % 2 == 0:
        puck.next_hop = spire2
        puck.next_hop.append(get_top(spire1))
        puck.current_spire = spire2
    else:
        puck.next_hop = spire3
        puck.next_hop.append(get_top(spire1))
        puck.current_spire = spire3
    


#return spire with puck containing num at top
def highest_number(num):
    global max_num
    highest_value_spire = []
    temp_list = [spire1, spire2, spire3]
    for item in temp_list:
        if item != []:
            temp_value_holder = get_top(item)
            if temp_value_holder.value == num:
                highest_value_spire.append(item)
    # need to handle if num is not found at top of a spire
    if num > max_num:
       num = num - 1 
       move(highest_number(num))
    elif highest_value_spire == []:
        num = num + 1
        move(highest_number(num))
        
    else:
        highest = get_top(get_top(highest_value_spire))
        return highest



    

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




def create_pucks(num):
    num_counter = num
    for x in range(0, num):
        p = puck()
        p.value = num_counter
        spire1.append(p)
        win_setup.append(p)
        num_counter -= 1


def legal_move(puck, spire):
    if puck.current_spire is not spire and puck.previous_spire is not spire :
        if len(spire) != 0:
            check_puck = spire[len(spire)-1]
            #print(f"check_puck:{check_puck.value} puck: {puck.value}")
            if puck.value < check_puck.value  :
                return True
        elif len(spire) == 0:
            return  True
    else:
        return False
    
    

def move(puck):
    global counter
    global initial_move
    win_condition()
    if puck != None:
        puck_decrement = puck.value - 1
        puck_increment = puck.value + 1
        lock_puck(puck, puck.current_spire)
        if initial_move != True:

            first_move(puck,spire1)
            spire1.pop()
            initial_move = True
            counter = counter + 1
            print(f"counter is : {counter}")
            print_spires()
            move(highest_number(puck_increment))

        else:
            free_spire(puck)
            if puck.lock_check == False:
                if legal_move(puck, puck.next_hop):
                    puck.previous_spire = puck.current_spire
                    puck.current_spire = puck.next_hop
                    puck.next_hop.append(puck)
                    puck.previous_spire.pop()
                    counter += 1
                    print(f"counter is : {counter}")
                    print_spires()
                    move(highest_number(puck_increment))
                elif puck_decrement == 0:
                    move(highest_number(puck_increment))
                else:
                    move(highest_number(puck_decrement))
            else:
                move(highest_number(puck_decrement))
        # else, call move with smaller puck
        # decrement puck
        # get spire by puck value
        # vall get_top of that spire
        # use that puck to call move()
                



def win_condition():
    if spire3 == win_setup:
        solved = True
    
    
def lock_puck(puck, spire):
    global locked_counter
    global win_setup
    if spire == spire3:
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
   
    

create_pucks(3)
max_num = win_setup[0].value

print_spires()


move(highest_number(1))

# move(spire1[2])
# move(spire1[1])

print("counter is " + str(counter))


