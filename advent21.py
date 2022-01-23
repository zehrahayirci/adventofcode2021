

def part1(player_1,player_2):
    player_1 = 6
    point_1 = 0 
    player_2 = 10
    point_2 = 0 
    i = 1
    dice = 1 
    while(point_1 < 1000 and point_2 <1000):
        points = dice + dice+1 + dice+2
        if i % 2 == 1:
            player_1 = (player_1 + points) %10
            if player_1 == 0:
                player_1=10
            point_1+=player_1
        else:
            player_2 = (player_2+ points) % 10
            if player_2 == 0:
                player_2=10
            point_2+=player_2
        i+=1
        dice +=3
        dice = dice % 100
        if dice == 0:
            dice = 100
    print(min(point_1,point_2)*3*(i-1))

def iterate_universe(universe):
    possibilities = {3:1,4:3,5:6,6:7,7:6,8:3,9:1}

    for t in range(2):
        next_universe = {}
        for cur_state in universe:
            for posib in possibilities:
                next_state = (cur_state[0] + posib) % 10
                if next_state == 0:
                    next_state = 10
                next_point = cur_state[1] + next_state
                if (next_state, next_point) not in next_universe:
                    next_universe[(next_state, next_point)] = possibilities[posib]*universe[cur_state]
                else:
                    next_universe[(next_state, next_point)] += possibilities[posib]*universe[cur_state]
    return next_universe

def find_winners(universe):
    winner = 0
    next_universe = {}
    for cur_state in universe:
        if cur_state[1]>=21:
            winner += universe[cur_state]
        else:
            next_universe[cur_state] = universe[cur_state]
    return winner, next_universe

def part_2(player_1,player_2):
    universe_1 = {(player_1,0): 1}
    universe_2 = {(player_2,0):1}

    one_won = 0
    two_won = 0

    i = 1
    while len(universe_1)>0 and len(universe_2)>0:
        if i%2 == 1:
            universe_1 = iterate_universe(universe_1)
            winners, universe_1 = find_winners(universe_1)
            loosers_2 = sum(universe_2.values())
            one_won += winners*loosers_2
        else:
            universe_2 = iterate_universe(universe_2)
            winners, universe_2 = find_winners(universe_2)
            loosers_1 = sum(universe_1.values())
            two_won += winners*loosers_1

        
        i+=1
    print(max(one_won, two_won))



    #print(universe_1.values())
    #print()

   

if __name__ == "__main__":
    part1(6,10)
    part_2(6,10)


