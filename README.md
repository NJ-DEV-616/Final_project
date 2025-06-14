# 🎮 Tic Tac Toe - Python Console Game

Welcome to **Tic Tac Toe**, a Python-based console game built as a final project for Stanford's [Code in Place](https://codeinplace.stanford.edu/) program!  
This game supports **Player vs Player** and **Player vs Computer** modes with **three difficulty levels** for the computer: Easy, Medium, and Hard.

---

## 📚 Table of Contents

- [📌 Features](#-features)
- [📂 Project Structure](#-project-structure)
- [🛠 Installation & Run](#-installation--run)
- [🚧 Future Improvements](#-future-improvements)
- [🤝 Contributing](#-contributing)
- [🧾 License](#-license)
- [🙏 Final Note](#-final-note)
- [📸 Sample Game Board](#-sample-game-board)

---

## 📌 Features

- ✅ **Two Game Modes**:
  - **Player vs Player**
  - **Player vs Computer**
- 🧠 **Three Difficulty Levels (PvC)**:
  - **Easy**: Random moves
  - **Medium**: Blocks player's win and tries to win
  - **Hard**: *(To be implemented)*
- 🧼 **Input validation** and clear game prompts
- 📐 **3x3 ASCII console game board**
- 🎯 **Win/draw detection logic**

---

## 📂 Project Structure

- `main()` — Starts the game and handles mode selection  
- `pvp()` — Handles **Player vs Player** logic  
- `pvc()` — Handles **Player vs Computer** logic  
- `input_validation()` — Ensures valid user input for rows, columns, difficulty  
- `check_winner()` — Checks rows, columns, and diagonals for a win  
- `display_game_board()` — Formats and prints the game board  
- `computer_move_easy()` — Makes random valid moves  
- `computer_move_medium()` — Blocks player wins and tries to win  
- `computer_move_hard()` — *(Currently a placeholder)*  

---

## 🛠 Installation & Run

1. Make sure you have **Python 3** installed.  
2. Save the script as `tic_tac_toe.py`.  
3. Run the game in terminal:
   ```bash
   python tic_tac_toe.py
   ```
4. Follow the on-screen prompts to select:
   - Game mode (PvP or PvC)
   - Difficulty level (if PvC)
   - Row and column inputs (1–3)

---

## 🚧 Future Improvements

- ♟️ Implement `computer_move_hard()` using **Minimax** for unbeatable AI  
- 🎨 Add **GUI support** using `tkinter` or `pygame`  
- 📊 Include **score tracking**, restart option, and round history  
- 🌐 Add **online multiplayer** using sockets or web APIs  

---

## 🤝 Contributing

1. Fork the repository  
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Make your changes  
4. Push your branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request — contributions are welcome!

---

## 🧾 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙏 Final Note

Developed as my **final project** for **Stanford's Code in Place 2025**.  
Thanks to the instructors, section leaders, and fellow learners for your amazing support and mentorship!

> *“Games don’t just entertain—they teach us logic, patience, and creativity.”* 💡

---

## 📸 Sample Game Board

```
 O | X | O
---|---|---
 X | O | X
---|---|---
 X | O | O
```

---

🎉 Feel free to fork, improve, and make this game your own. Happy coding!
