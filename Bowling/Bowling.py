
from Score import BowlingScore


testScore1 = "X X X X X X X X X X X X" #300
testScore2 = "9- 9- 9- 9- 9- 9- 9- 9- 9- 9-" #90
testScore3 = "5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5-" #150 (In interest of time, I'm saying syntax for bonus spare throw is x-)
testScore4 = "X X 54 3/ X 43 7/ 5/ 81 42" #145
testScore5 = "X -4 42 -/ X 43 7- 5/ 81 42" #108

print("Test 1")
score = BowlingScore(testScore1)
print(testScore1 + " => " + str(score.ScoreGame()))

print("\nTest 2")
score = BowlingScore(testScore2)
print(testScore2 + " => " + str(score.ScoreGame()))

print("\nTest 3")
score = BowlingScore(testScore3)
print(testScore3 + " => " + str(score.ScoreGame()))

print("\nTest 4")
score = BowlingScore(testScore4)
print(testScore4 + " => " + str(score.ScoreGame()))

print("\nTest 5")
score = BowlingScore(testScore5)
print(testScore5 + " => " + str(score.ScoreGame()))