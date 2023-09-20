from itertools import zip_longest

# How to solve a problem:
    # Figure out what the input and its type are
    # Set up a function
    # Figure out what the output and its type are
    # Gather Your Knowledge
    # Gathers Your Constraints (Not always necessary) 
    # Determine a Logical way to solve the problem
        #Write each step out English
        #Write each step out in Python-esse (sudo-code)
    # Invoke and Test Your Function


# DESCRIPTION:
# Given two Arrays in which values are the power of each soldier, return true if you survive the attack or false if you perish.

# CONDITIONS

# Each soldier attacks the opposing soldier in the same index of the array. The survivor is the number with the highest value.
# If the value is the same they both perish
# If one of the values is empty(different array lengths) the non-empty value soldier survives.
# To survive the defending side must have more survivors than the attacking side.
# In case there are the same number of survivors in both sides, the winner is the team with the highest initial attack power. If the total attack power of both sides is the same return true.
# The initial attack power is the sum of all the values in each array.
# EXAMPLES

# attackers=[ 1, 3, 5, 7 ]   defenders=[ 2, 4, 6, 8 ]
# 0 survivors                4 survivors
# return true


# attackers=[ 1, 3, 5, 7 ]   defenders=[ 2, 4 ]
# 2 survivors  (16 damage)   2 survivors (6 damage)
# return false

# attackers=[ 1, 3, 5, 7 ]   defenders=[ 2, 4, 0, 8 ]
# 1 survivors                3 survivors
# return true

'''
input > array/list varying lengths
output true or false> number of survivors


empty indexes = lose to index with a survivor

surviving - defenders have more surivovrs than attacking side
true if defenders survive, true if survivors on both sides are tied and defenders have highest initial attack power, true if survivors on both sides are tied and if total attack power on both sides is the same

false = perish if attackers have more survivors, survivors on both sides are tied and attackers have the highest initial attack power


make function (alist, alist2)
compare first index value of each list to each other : alist[0] vs alist2[0]
remove the smaller value
move onto the next index and compare value
remove smaller value
...until end of array
calculate number of survivors
compare the number of survivors
return true or false


def check_survive(alist, alist2):
    def_surv = 0
    atk_surv = 0
    compare_list = list(zip_longest(alist ,alist2))
    for atk,def in compare_list:
        if atk > def:
            atk_surv += 1
        elif atk < def:
            def_surv += 1
        elif atk > 0 and def == None:
            atk_surv += 1
        elif def > 0 and atk == None:
            def_surv += 1
'''

attackers=[ 1, 3, 5, 7 ]
defenders=[ 2, 4, 6, 8 ]
# 0 survivors                4 survivors
# return true


attackers2=[ 1, 3, 5, 7 ]
defenders2=[ 2, 4 ]
# 2 survivors  (16 damage)   2 survivors (6 damage)
# return false

attackers3=[ 1, 3, 5, 7 ]
defenders3=[ 2, 4, 0, 8 ]
# 1 survivors                3 survivors
# return true



def check_surv(alist, alist2):
    def_surv = 0
    atk_surv = 0
    atk_power = sum(alist)
    def_power = sum(alist2)
    compare_list = list(zip_longest(alist ,alist2))
    for atk, def_ in compare_list:
        if def_ is None:
            atk_surv += 1
        elif atk is None:
            def_surv += 1
        elif atk > def_:
            atk_surv += 1
        elif atk < def_:
            def_surv += 1
    # print(atk_surv, def_surv)
    # print(f'Attacker Power: {atk_power} Defender Power: {def_power}')
    if atk_surv > def_surv:
        return False
    elif def_surv > atk_surv:
        return True
    elif atk_surv == def_surv:
        if atk_power > def_power:
            return False
        else:
            return True



print(check_surv(attackers, defenders))
print(check_surv(attackers2, defenders2))
print(check_surv(attackers3, defenders3))

# print(list(zip_longest([ 1, 3, 5, 7 ] ,[ 2, 4, 6])))

'''
Time Complexity

Overall: O(n)
def check_surv(alist, alist2):
    def_surv = 0 -> O(1)
    atk_surv = 0 -> O(1)
    atk_power = sum(alist) -> O(1) O(n)
    def_power = sum(alist2) -> O(1) O(n)
    compare_list = list(zip_longest(alist ,alist2)) -> O(1) zip = O(2n) O(n) = O(n)
    for atk, def_ in compare_list: -> O(n)
        if def_ is None: -> O(1)
            atk_surv += 1 -> O(1)
            continue -> O(1)
        elif atk is None: -> O(1)
            def_surv += 1 -> O(1)
            continue -> O(1)
        if atk > def_: -> O(1)
            atk_surv += 1 -> O(1)
        elif atk < def_: -> O(1)
            def_surv += 1 -> O(1)
    if atk_surv > def_surv: -> O(1)
        return False -> O(1)
    elif def_surv > atk_surv: -> O(1)
        return True -> O(1)
    elif atk_surv == def_surv: -> O(1)
        if atk_power > def_power: -> O(1)
            return False -> O(1)
        else: -> O(1)
            return True -> O(1)
'''