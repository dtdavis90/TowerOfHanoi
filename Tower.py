counter = 0
spire1 = [3,2,1]
spire2 = []
spire3 = []

def get_top(spire):
    if(len(spire)>0):
        return spire[len(spire)-1]
    else:
        return 0

def first_move(spire):
    global counter
    if (len(spire) % 2 == 0):
        spire2.append(get_top(spire1))
    else:
        spire3.append(get_top(spire1))
    spire1.pop()
    counter += 1

def highest_number():
    num1 = get_top(spire1)
    num2 = get_top(spire2)
    num3 = get_top(spire3)
    return max(num1, num2, num3)


def print_spires():
    print(spire1)
    print(spire2)
    print(spire3)

# print_spires()
# first_move(spire1)
# print_spires()
# print(f"Counter = {counter}")
print(highest_number())
