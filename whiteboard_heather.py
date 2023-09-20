def war(alist_1, alist_2):
    attackers_survivors = 0
    defenders_survivors = 0
    sum_survivors = sum(alist_1)
    sum_defenders = sum(alist_2)
    while len(alist_1) < len(alist_2):
        alist_1.append(0)
    while len(alist_2) < len(alist_1):
        alist_2.append(0)
    alist_3 = alist_1 + alist_2
    k = len(alist_3)//2
    right_point = k
    left_point = 0
    while right_point <= len(alist_3)-1:
        if alist_3[left_point] < alist_3[right_point]:
            defenders_survivors += 1
            left_point += 1
            right_point += 1
        elif alist_3[right_point] < alist_3[left_point]:
            attackers_survivors += 1
            right_point += 1
            left_point += 1
        else:
            pass
    print(f"(ATK Survivors: {attackers_survivors}, DEF Survivors: {defenders_survivors}, ATK sum: {sum_survivors}, DEF sum: {sum_defenders})")
    if defenders_survivors == attackers_survivors:
        if sum_survivors > sum_defenders:
            return False
        elif sum_survivors < sum_defenders:
            return True
        else:
            return True
    elif defenders_survivors > attackers_survivors:
        return True
    elif defenders_survivors < attackers_survivors:
        return False