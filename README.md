# iQuHACK 2023: Tic Tac Toe Quantum Machine Learning Solver
## Group Name: If It Quacks Like a Duck, If It Hacks Like a Duck...

## Overview 
Tic Tac Toe is a fun game in which two players alternate plays to try and fill a row, column, or diagonal with three O's or three X's drawn in the spaces of a grid of nine squares. In case you cannot find a friend to play with you, we created an AI to play against you. 

Our AI uses a quantum machine to maximize its playing ability. You might think you know how to play tic tac toe, but you will be bamboozled by the higher level plays of our machine.

## Installation Instruction  
Before running our code: install the following libraries: 
- qiskit
- scikit-learn
- flask 
- qiskit_machine_learning

Note: we trained two models in different Jupitor notebooks, and then the models are loaded into the server to respond to API call from the front-end.

## Methods 
Our goal in iQuHACK was to learn more about quantum classification algorithms, to realize this goal, we studied the quantum classification applications of tic tac toe. We used classical classification algorithms to have a baseline, ensuring that classification algorithms could be utilized in solving tic tac toe. We then used an algorithmic method to create a dataset of game state and their corresponding results. Finally, we trained Quantum Support Vector Classifier (QSVC) to detect winning and losing game states. The ultimate goal was to the run QSVC algorithm on the IBMQ provided backend.


<p align="center">
  <img src="https://github.com/iquhack-if-it-quacks/iquhack-if-it-quacks/blob/main/demo.gif" alt="Demo" />
</p>


## Challenges
We started by training a classical model to test the effectiveness of classification algorithms in modeling a tic tac toe game. After this step, we began implementing the QSVC, but this algorithm only operates as a binary classifier, making it difficult to transition from our classical multiclass classifier to quantum computing algorithms. We approached this challenge by adding two quantum binary classifiers, although this reduced the accuracy of our quantum model.

## Future Steps 
The game can be realized by utilizing non-binary quantum classification algorithms (such as the variational quantum classifier), which has the potential to exhibit better performance on both classical and quantum hardware. Quantum Machine Learning (QML) is a rapidly advancing field of research, making the optimization and training of a quantum model for a simple game like tic-tac-toe an intriguing research topic.

## Our experience at MIT iQuHack 2023 
Team ???If It Quacks Like a Duck, If It Hacks Like a Duck?????? had a great time developing this project. Before iQuHACK, most of team members had never written code for a quantum computer, although we were all interested in learning more. Throughout the past 24 hours, we got the opportunity to explore the vast applications and potential of quantum computing. We can now proudly say that we (tried, so hard to) have a functional quantum program, which we developed in the face of several challenges and roadbumps along the way.

## References

Li, Weikang, and Dong-Ling Deng. "Recent advances for quantum classifiers." Science China Physics, Mechanics & Astronomy 65.2 (2022): 220301.

