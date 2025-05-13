# Ping Pong Game with Power Ups
<img width="671" alt="image" src="https://github.com/user-attachments/assets/ff5a8178-cfc4-4fd1-a0e3-ce08acaf55c7" />


This repository contains the code for my final project, a Ping Pong Game made with pygame. 

## What is this game?

This is my take on the classic Ping Pong. It is a simple Ping Pong Game made with pygame, but the twist is that it has 
a powerup built into it. You play against yourself or with a friend. When you miss hitting the ball with the paddle, the
other side's score goes up. When one side has 3 more points than the other, a power up takes place automatically and lasts
10 seconds if you level the scores to be less than 3 apart! I added music, a cute background, and sound effects for a 
personal touch. 

- Other details:
  - Object oriented program with objects: Ball and Paddles
  - Main game loop function that implements a majority of the code:
    - paddle controls 
    - ball movement logic
    - ball paddle interaction 
    - paddle powerup logic
  - Intro Screen function
    

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
- Core implementation
  - final_project.py - the entire code for the ping pong game
- Sounds and Images
  - background2.jpg - the background
  - music.mp3 - background music
  - powr_up.mp3 - power up sound effect
## Controls
- W and S moves the left paddle UP (W) and DOWN (S)
- UP and DOWN arrow keys control the right paddle. 


