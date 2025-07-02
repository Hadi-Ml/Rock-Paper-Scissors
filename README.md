# Rock-Paper-Scissors-Lizard-Spock Game

A classic extended Rock-Paper-Scissors game implemented in **Python**, featuring the **"Lizard"** and **"Spock"** elements for added fun and strategy. Play against a computer opponent with adjustable difficulty levels.

---

## 🚀 Features

* **Extended Game Rules:** Includes the five elements: **Rock**, **Paper**, **Scissors**, **Lizard**, and **Spock**, following the popular Big Bang Theory variation.
* **Player vs. Computer:** Challenge an **AI** opponent.
* **Difficulty Levels:**
    * **Easy:** The computer makes completely **random choices**.
    * **Hard:** The computer attempts to make a **winning move** against your choice with a higher probability, offering a more **challenging** experience.
* **User-Friendly Interface:** Simple **command-line interface** for easy interaction.
* **Clear Rules Display:** The game rules are clearly explained at the start of each session.
* **Executable Version:** Play the game directly **without needing a Python environment** (Windows only).

---

## 🎮 Game Rules

The game follows these extended rules where each element beats two others and loses to two others:

* **Scissors** cuts **Paper**
* **Scissors** decapitates **Lizard**
* **Paper** covers **Rock**
* **Paper** disproves **Spock**
* **Rock** crushes **Scissors**
* **Rock** crushes **Lizard**
* **Lizard** poisons **Spock**
* **Lizard** eats **Paper**
* **Spock** smashes **Scissors**
* **Spock** vaporizes **Rock**

---

## ✨ How to Play

You have two options to play the game:

### Option 1: Using the Executable File (Recommended for Windows Users)

1.  **Download the Project:**
    * **Clone the repository:**
        ```bash
        git clone [https://github.com/YourUsername/RockPaperScissorsGame.git](https://github.com/YourUsername/RockPaperScissorsGame.git)
        ```
        (Replace `YourUsername` with your actual GitHub username and `RockPaperScissorsGame` with your repository name.)
    * Alternatively, you can download the project as a **ZIP file** directly from the GitHub page.

2.  **Locate and Run the Executable:**
    * Navigate to the downloaded project folder on your computer.
    * Find the **executable file** (e.g., `RockPaperScissorsGame.exe`) inside the folder.
    * Simply **double-click** the `.exe` file to start the game.
    * Follow the prompts in the command window to play.

### Option 2: Running from Source Code (Requires Python)

1.  **Clone the Repository (or Download):**
    ```bash
    git clone [https://github.com/YourUsername/RockPaperScissorsGame.git](https://github.com/YourUsername/RockPaperScissorsGame.git)
    ```
    (Replace `YourUsername` with your actual GitHub username and `RockPaperScissorsGame` with your repository name.)
    Alternatively, you can download the project as a **ZIP file**.

2.  **Navigate to the Project Directory:**
    ```bash
    cd RockPaperScissorsGame
    ```

3.  **Run the Game:**
    ```bash
    python rock_paper_scissors_game.py
    ```
    *(If your main game file is named differently, use `python your_actual_file_name.py`)*

4.  **Follow the Prompts:**
    * Enter your **name** when prompted.
    * Choose whether you want to **play** (`Yes` or `No`).
    * Select the **difficulty level** (`Easy` or `Hard`).
    * Enter your **choice** (Rock, Paper, Scissors, Spock, or Lizard).
    * The game will display the **results**, and you can choose to play again.

---

## 🛠️ Requirements

* **For running the executable:** No specific requirements (Windows OS).
* **For running from source code:**
    * **Python 3.x** (Tested with Python 3.8+)
    * No external libraries are required beyond Python's **built-in `random` module**.

---

## 📂 Project Structure

RockPaperScissorsGame/
├── rock_paper_scissors_game.py    # Main game logic and execution (Python source code)
├── RockPaperScissorsGame.exe      # Executable version for Windows
└── README.md                      # Project documentation (this file)

---

## 📝 Future Improvements (Ideas)

* **Score Tracking:** Keep track of player and computer scores across multiple rounds.
* **User Profiles:** Save player names and their win/loss records.
* **Graphical User Interface (GUI):** Implement a GUI using libraries like **Tkinter**, **PyGame**, or **PyQt** for a more visual experience.
* **Advanced AI:** Implement more sophisticated AI strategies (e.g., **pattern recognition**, **weighted choices** based on player history).
* **Multiplayer Mode:** Enable two players to play against each other on the same machine.

---

## 🤝 Contributing

Feel free to **fork** this repository, make **improvements**, and submit **pull requests**. Any **suggestions** or **bug reports** are welcome!

---

## 📄 License

This project is **open source** and available under the **[MIT License](https://opensource.org/licenses/MIT)**.

---
