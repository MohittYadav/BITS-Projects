This project implements a two-player Connect Four game where a human player competes against an AI opponent. The AI uses the Minimax algorithm with alpha-beta pruning and a fixed depth of 3 to make strategic moves. The game is built in Python 3 using NumPy for board representation and follows standard Connect Four rules on a 7x6 grid.
Key Features:
Grid Representation: 6×7 board using NumPy arrays

Human Input: Column selection with validation

AI Intelligence: Minimax algorithm with strategic evaluation

Game Logic: Turn-based gameplay with win/draw detection

Visual Output: Board display after each move

🧠 AI Implementation Details
Static Evaluation Function
The AI uses a sophisticated evaluation function that considers:

Center Control: Bonus points for pieces in center column

Window Scoring: Analyzes all possible 4-cell sequences

Threat Detection: Awards points for potential wins and blocks opponent threats

Strategic Positioning: Values partial sequences (2-in-a-row, 3-in-a-row)

Scoring Breakdown:
4 in a row: +100 points

3 in a row with empty space: +5 points

2 in a row with empty spaces: +2 points

Opponent has 3 in a row: -4 points (blocking)

Center column pieces: +3 points each

Minimax Algorithm
Depth Limit: Fixed depth of 3 for performance

Alpha-Beta Pruning: Optimizes search by eliminating unnecessary branches

Terminal States: Detects wins, losses, and draws

Move Exploration: Evaluates all valid columns at each decision point
🎮 How to Play
The game starts with an empty 7×6 grid

Players take turns dropping pieces into columns

Human Player (Player 1):

Enter column number (0-6) when prompted

Piece will fall to the lowest available row

AI Player (Player 2):

Automatically selects best move using Minimax

Displays "Player 2 Selection" when thinking

Winning Conditions:

Connect four pieces horizontally, vertically, or diagonally

Game ends immediately when a player wins

Draw if board fills completely

📊 Algorithm Performance
The Minimax algorithm with depth 3 provides:

Reasonable computation time for human-paced gameplay

Strategic decision making considering multiple future moves

Effective blocking of opponent threats

Opportunistic winning when chances arise
