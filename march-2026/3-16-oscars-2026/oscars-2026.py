def oscar_pool(predictions):
  # first we define the list of oscar winners
  # and we setup three variables for the winning friend or tie
  oscar_winners = ["One Battle After Another", "Michael B. Jordan", "Jessie Buckley", "Paul Thomas Anderson"]
  winning_friend = ""
  winning_score = -1
  tie = False

  # for each prediction
  for prediction in predictions:
    score = 0
    # we set the name of the friend as the first element in the array
    friend = prediction[0]
    # then to avoid confusion we set remaining predictions 
    # by removing the name of the friend
    prediction = prediction[1:]

    # then we calculate the score by checking if the predictions correspond
    for i in range(len(prediction)):
      if prediction[i] == oscar_winners[i]:
        score += 1
    
    # if current score is highest than the current highest score
    # we set the friend as the new winning friend
    if score > winning_score:
      winning_score = score
      winning_friend = friend
      tie = False
    # if two friends have the same score, we set tie to True
    elif score == winning_score:
      tie = True

  # if tie is True the we return "Tie", otherwise we return the winning friend's name
  return "Tie" if tie else winning_friend