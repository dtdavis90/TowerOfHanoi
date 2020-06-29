counter = 0
spire1 = []
spire2 = []
spire3 = []
initial_move = False
check_legal_move = False


class puck:
    value = 0
    current_spire = spire1
    previous_spire = spire1


def get_top(spire):
    if len(spire) > 0:
        return spire[len(spire)-1]
    else:
        return 0

def first_move(spire):
    if len(spire) % 2 == 0:
        spire2.append(get_top(spire1))
    else:
        spire3.append(get_top(spire1))
    spire1.pop()


def highest_number():
    num1 = get_top(spire1)
    num2 = get_top(spire2)
    num3 = get_top(spire3)
    return max(num1, num2, num3)


def print_spires():
    print(spire1)
    print(spire2)
    print(spire3)



def create_pucks(num):
    num_counter = num
    for x in range(0, num):
        p = puck()
        p.value = num_counter
        spire1.append(p.value)
        num_counter -= 1

def legal_move(puck, spire):
    if puck.current_spire != spire and puck.previous_spire != spire :
        check_legal_move = True

def move(puck):
    global counter
    global initial_move
    if initial_move == False:
        first_move(spire1)
        initial_move = True
    counter += 1
        
def lock_puck(puck):
   # if puck is in correct position at spire3 
    






# print_spires()
# first_move(spire1)
# print_spires()
# print(f"Counter = {counter}")
create_pucks(3)
#print_spires()
move(highest_number)
print_spires()
print(counter)
