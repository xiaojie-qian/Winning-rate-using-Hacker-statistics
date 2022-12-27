# winning-rate-using-Hacker-statistics
## Description: 
Imagine the following: you're walking up the empire state building to DataCamp HeadQuarters and you're playing a game with a friend.
You throw a die one hundred times.
- If it's 1 or 2 you'll go one step down.
- If it's 3, 4, or 5, you'll go one step up.
- If you throw a 6, you'll throw the die again and will walk up the resulting number of steps.
You can not go lower than step number 0. And also, you admit that you're a bit clumsy and have a chance of 0.1% of falling down the stairs when you make a move. (*Falling down means that you have to start again from step 0. With all of this in mind, you bet with your friend that you'll reach 60 steps high.*)

### How to solve?
What is the chance that you will win this bet? One way to solve it would be to calculate the chance analytically using equations. Another possible approach, is to simulate this process thousands of times, and see in what fraction of the simulations that you will reach 60 steps. This is a form of -hacker statistics-. Here, we're going to opt for the second approach.
