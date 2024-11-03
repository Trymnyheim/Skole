# https://open.kattis.com/problems/rankproblem

from sys import stdin

def main():
    n, m = [int(x) for x in next(stdin).rstrip().split(" ")]

    # Put teams in a list in ranked order
    ranked = []
    for i in range(1, n + 1):
        team = "T" + str(i)
        ranked.append(team)

    # Calls update_ranked for each "game"-line in input
    for _ in range(m):
        winner, loser = next(stdin).rstrip().split(" ")
        update_ranked(ranked, winner, loser)
    
    # Output
    for team in ranked:
        print(team, end=" ")
      

# If the loser of the match appears before the winner, winner bubbles down to losers index
def update_ranked(ranked, winner, loser):
    w_ind = -1
    l_ind = -1
    for i, team in enumerate(ranked):
        if l_ind != -1 and w_ind == -1:
            ranked[i], ranked[i-1] = ranked[i-1], ranked[i]
        if team == winner:
            w_ind = i
        if team == loser:
            l_ind = i
    

if __name__ == "__main__":
    main()



    