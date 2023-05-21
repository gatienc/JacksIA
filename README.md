# KnucklebonesIA
disocver of reinforcement learning by training a model to play knuckelbones

rules: In Jacks, each player has a board with 9 dice that must be filled in completely to finish the game. The value of a dice is the number of points you will earn by placing it on your board. The first player to fill the entire board ends the game, and the winner is the one with the most points.

If you have to worry about your own board, you can still influence your opponent's board by removing dice. Indeed, if your opponent has a 2 (for example), you can also put a 2 on the same column to remove his.

It is also possible to multiply the value of your dice by placing several of the same value in the same column. For example, if you place two 3s in the same column, the total points for that column will be 12, not 6. To calculate the points, the game adds up the similar values, then multiplies the result by the number of occurrences of that value in the same column.

Some examples:

    Two 3s and a 5 in the same column gives 17 points. Calculation details: 2x(3+3) + 5
    Three 3 in the same column gives 27 points. Calculation detail : 3x(3+3+3)