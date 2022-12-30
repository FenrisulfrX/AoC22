score = []

def calc_score(opp_move, my_move):
        global score
        
        # ROCK    = A, X = 1 Point
        # PAPER   = B, Y = 2 Points
        # SCISSOR = C, Z = 3 Points
    
        if opp_move == "A" and my_move == "X":
                score.append(3)

        if opp_move == "A" and my_move == "Y":
                score.append(1)
                score.append(3)

        if opp_move == "A" and my_move == "Z":
                score.append(2)
                score.append(6)

        if opp_move == "B" and my_move == "X":
                score.append(1)

        if opp_move == "B" and my_move == "Y":
                score.append(2)
                score.append(3)

        if opp_move == "B" and my_move == "Z":
                score.append(3)
                score.append(6)

        if opp_move == "C" and my_move == "X":
                score.append(2)

        if opp_move == "C" and my_move == "Y":
                score.append(3)
                score.append(3)
        
        if opp_move == "C" and my_move == "Z":
                score.append(1)
                score.append(6)

	
with open("rps.txt") as file:
        for line in file:
                line.strip()
                moves = line.split(" ")
                calc_score(opp_move = moves[0].strip(), my_move = moves[1].strip())


print(sum(score))


