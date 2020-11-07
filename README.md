# buitri84

2019-07-30. Tri Bui.

This is a command line implementation of a Tic Tac Toe bot using the Minimax algorithm.
I did not try to make this into a web-based game yet since I want to focus on the algorithm, which is for me
the fun part.

As human, you are player X. The bot is player Y. You go first. If my implementation is correct, meaning that
both players are always attempting to play optimally, you should not be able to win. In fact, the game would
always end in a draw. Obviously, I encourage you to try playing sloppily to check that the bot is actually
making intentional (not random) moves. And yes, try to beat it too.

Data structure:
Since this is a limited game, I chose the simplest data structure for the board which does the job: a list of
9 elements with index from 0 to 8. Thus, the index for each position in the board would be as followed:
[ 0 1 2
  3 4 5
  6 7 8]

Algorithm:
I implement a minimax algortihm, with a weighting multiplier to reward longer game play (if the bot is losing) or faster win (if it is winning).
The pseudo code can be described as followed:

def minimax(state of board, player):
-    if game is over:
        return score
-    else, if game is not over:
-        for each move in all possible moves:
            assume that move is made
            append (value = minimax(new state of board, switch player) * weight factor) to a list of values
            also append the move just made to the list of moves
-        if player is the maximizing player:
            chose value = max in list of values
            chose best_move = the move corresponding to that value
-        else if player is the minimizing player:
            chose value = min value in list of values
            chose best_move = the move corresponding to that value
        return value, best_move

Thus, as can be seen above:
- Each time the minimax fuction is called recursively, the weight factor is multiplied with the returned value. I chose this factor to be ~0.9, thus
when applied to the maximizing player (ie. positive score) it reduces the score. Therefore, more calls to get to a final winning score would give
a final score lower than that with fewer calls. Similarly, when applied to the minimizing player, the weight increases the score.
Since it is ~0.9, it will never reverse the signs of the scores or mix them with 0 (which is the score for a draw)
- In the real code, to ensure the consistency of return values (as I am returning 2 values: value and best_moves), I ended up needing to
return a dummy value in the base case ie. in the base case, I return something like:
return score, -1
