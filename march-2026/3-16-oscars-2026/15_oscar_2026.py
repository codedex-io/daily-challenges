"""
This function tallies up points for an Academy Awards pool 
to see which friend predicted the most winners!
    
The Logic:
1. The Winners Circle: It stores a list of the actual 
   movie and actor winners for the night.
2. The Scoring Loop: It goes through each friend, grabbing 
   their name and their specific list of guesses.
3. The Tally: It compares each guess to the real winner. 
   If they match, that friend gets a point!
4. The Leaderboard: It keeps track of the 'max_score'. 
   If someone beats it, they become the new winner. 
   If there’s a draw, it marks it as a "Tie."
"""
def oscar_pool(predictions):
    # Write code below 💖
    winners = ["One Battle After Another", "Michael B. Jordan", "Jessie Buckley", "Paul Thomas Anderson"]
    max_score = -1
    winner_name = ""
    
    for friend in predictions:
        name = friend[0]
        preds = friend[1:]
        score = 0
        
        for i in range(len(winners)):
            if preds[i] == winners[i]:
                score += 1
                
        if score > max_score:
            max_score = score
            winner_name = name
        elif score == max_score:
            winner_name = "Tie"
            
    return winner_name
