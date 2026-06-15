# Poker AI Analysis bot 
  This Poker bot takes in a state and reads the last move, the board and other data points that will be specified later to first calculate the equity on the board based on the player's hand and the board and also the hand strength. Then it will give that to the AI and prompt it to give advice/show mistakes made by the player and the recommended action the player should have taken and how it got to that conclusion while also estimating the ranges of what said players could have had. We decided to create a project like this because poker is a semi hard game to learn from scratch and how much to bet and when to quit and flop is not something intrinsically known so if we give a bot that can help a player analyze their game and give suggestions and tell a line of thinking it can help them improve on their game and tell them what mistakes they might be making often if the mistake comes up often in the mistakes listed

How to run it locally:
To run our project locally move the code to a local coding studio like VS Code as the UI will not work properly when run in GitHub CodeSpaces. After transferring gui.py to vs code change the apiurl variable with your github code space url and (ie. apiurl = "https://laughing-lamp-974gv5gr5q992777x-8000.app.github.dev")(you will need to do pip install requests on vs before you can run it and also have python installed). Afterwards you click run the code and the ui should pop up. You will then be prompted to put in the following things:
 - Player hand written number then suit (String ex: ad|qs) 
 - How many cards on the Board (int)
 - Board (String ex: (as 5c 9h)(can also be left blank and updated later if you input 0 for board size))
 - Position (String but only takes BTN,BB,SB,MP,UTG,CO)
 - Hero Stack or how much the player has (int)
 - Action History (Each player action will ask for the Name of player going (refer to yourself as “Hero” and others as given name later in opponents), the action (call, check, raise or fold), and the amount (if folded put  amount as 0))
 - Opponents (1-5) (Each one give a name, position, stack and any notes on said player’s playing style but can be left blank if you don’t know)
After inputting said things the program will run the initial through the AI for processing and give out:
The program will give out:
 - The last played action of the player
 - The estimated equity calculated
The AI will give out:
 - The recommended action 
 - Ranges the opponent likely has based off actions
 - Mistakes based off action
 - An explanation of how the game is going and analyzes and give the best strategy
 - Coach advice or what the bot suggest what you should have done with detail like how much you should raise by
 - Confidence in said advice
 - Its own calculated equity 
 - And rule based mistakes point out obvious things like not raising when the equity is so high.
The program will then prompt and as if you would like to update the game state. The things you can change are:
 - Board (input the whole changed board)
 - Pot size
 - And action rotation again in the same format as the beginning 
After updating it will merge said files and send it back to the AI so you can get more advice. If you want to start another new game, reload the whole program to analyze another game.

Research Paper:

If we were to go back and integrate our research paper we would kind of train the AI by flagging bad calls by the AI by using some math system where if the calculated equity didn’t match or have some other kind of analysis in the code that cross reference and if they don’t match we can tell the AI that the answer it gave might not be the best one. This could let the AI adapt to the many games instead of forgetting the games if we also include a way to store games in the future for the AI to remember. 

Working with an AI agent

Backend (Katie): 

What did you use the agent for?

I used the agent to give me a backbone of the code to give me a structure for the files and how to build the app. Then I started prompting about how they thought the structure would be helpful in the project and give me ideas of how to code it and what to add.

What worked well?

The AI gave answers that told what I should focus on and helped give imports and stuff that I had no idea about that were quite helpful.

What didn’t work:

The AI often forgot what it was talking about a couple of messages ago and went back and forth and it was also quite annoying because everytime I would go to continue to work on it I had to tell the AI specifically what i want the tree and ask how I should keep improving it and also the answers it gave, gave me a hard time because i never knew where it wanted me to put a fix into my code.

What did I learn about prompting?

I learned that prompting is quite tedious, but it feels good to finally figure out the problem after thoughtfully explaining the problem.
What would I do differently?

I would try not to debate from one chat because catching the ai up with what i had was annoying but also next time I wished I knew how specific I needed to talk to an AI because it first wanted to make a poker player before i told it it was analyzing and the original structure did not include AI because i forgot to talk about it.

Frontend (Wenqing): 

What did you use the agent for?

I used the agent to help me debug my code and make it more easily readable. I also used it to teach me how to use specific parts like how to connect the frontend to the backend and use stuff like requests and some of tkinter’s functionality

What worked well?

The AI gave detailed responses to how stuff should be fixed and ideas on how to improve some parts of the code

What didn’t work:

The AI would often give me code as a solution to some problem but that code would then break alot of the other sections of the UI which i found really frustrating to work with because every answer the AI give would create 3 more new problems

What did I learn about prompting?

I have to be really specific with what I want it to respond back with or else it would just give me stuff that either didn’t work, missed a features, or would just brick the rest of the code

What would I do differently?

I would try to use a different AI thats more suited towards coding and ask about what the front end could be sooner instead of spending a day trying to figure out how to use javascript to make a web UI instead of sticking to the local UI I already had. 

Video link :
https://drive.google.com/file/d/1YAQpaVK4qwx35DRKJuINbKld6uf5SpWD/view?usp=drive_link

Research paper citation:
Chialvo, D. R., & Bak, P. (1999, June). Learning from mistakes. ScienceDirect. https://www.sciencedirect.com/science/article/pii/S0306452298004722 
