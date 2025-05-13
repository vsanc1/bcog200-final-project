# Ping Pong Game with Power Ups
<img width="671" alt="image" src="https://github.com/user-attachments/assets/ff5a8178-cfc4-4fd1-a0e3-ce08acaf55c7" />


This repository contains the code for my final project, a Ping Pong Game made with pygame. 

## What is this game?


## Installation 

#### Install the required dependencies
pip install pygame

#### Run the game in your terminal
python final_project.py




## Testing
- The game is simple, and does not require complex testing. To test, just ensure the below.
  - Upon running, you will see a introductory menu that explains the game and prompts you to press SPACE to begin.
  - After pressing SPACE and when running the game, you will see a screen with paddles and a ball.
  - You can control the left paddle with W and S, and the right paddle with your UP and DOWN arrow keys.
  - The paddles should not move off the screen.
  - The ball should bounce off the top and bottom, and reset in the middle if you do not hit it with a paddle and it goes behind/offscreen.
  - Movement of the ball and paddles should be smooth.
  - You will be playing against yourself, and there will be a scoreboard at the top of the screen. If you fail to hit a ball, the paddle that sent that ball gains a point.
  - Once you have reached a certain point threshold, a powerup will activate. There will be a sound effect.
  - If you level the scores, the powerup will dissapear after 10 seconds.

## Code structure
- src/ - Core implementation
  - final_project.py - the entire code for the ping pong game
- misc/ - Sounds and Images
  -       
## Controls
- W and S moves the left paddle UP (W) and DOWN (S)
- UP and DOWN arrow keys control the right paddle. 


