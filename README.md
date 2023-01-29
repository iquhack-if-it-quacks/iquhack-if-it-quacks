# iquhack-if-it-quacks

Name of the Project: Tic Tac Toe Game with Quantum Kernel Machine Learning

Contributors: 

Overview: Tic Tac Toe is a fun game in which two players alternate plays to try and fill a row, column, or diagonal with three O's or three X's drawn in the spaces of a grid of nine squares. In case you cannot find a friend to play with you, we created an AI to play against you. 

Our AI uses a quantum machine to maximize its playing ability. You might think you know how to play Tic Tac Toe, but you will be bamboozled by the higher level plays of our machine.

Installation instruction:  
Before running our code: install the following libraries: 
qiskit
scikit-learn
flask 
qiskit mache learning 

[ASK SHAYAN]

Methods: 

Challenges: We encountered a particular challenge while translating from classical machine learning to quantum ML algorithms. We started by training a classical model to test the effectiveness of our front-end and back-end code. After this step, we began implementing the Quantum Support Vector Classifier, but this algorithm only operates as a binary classifier, making it difficult to transition from our classical multiclass classifier to quantum computing algorithms. We approached this challenge by adding two quantum binary classifiers, although this reduced the accuracy of our quantum model.

Future Steps: The game can be realized by utilizing non-binary quantum classification algorithms (such as the variational quantum classifier), which has the potential to exhibit better performance on both classical and quantum hardware. Quantum Machine Learning (QML) is a rapidly advancing field of research, making the optimization and training of a quantum model for a simple game like tic-tac-toe an intriguing research topic.

Our experience at MIT iQuHack 2023: 
Team “If It Quacks Like a Duck, If It Hacks Like a Duck…” had a great time developing this project. It was our first time doing a hackathon, and you know what people say about first time’s… they happen in libraries at MIT. 

Excited that our Covalent/IBM prompt was open-ended, we ended up spending too long deliberating a project idea. We eventually settled on quantum classification modeling

References:

Li, Weikang, and Dong-Ling Deng. "Recent advances for quantum classifiers." Science China Physics, Mechanics & Astronomy 65.2 (2022): 220301.
