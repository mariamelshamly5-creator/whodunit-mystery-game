# 🕵️ Whodunit — The Mystery Deduction Game

A social-deduction party game built in Python. Players are secretly assigned a role — one of them is the **culprit**, the rest are **innocent detectives**. Everyone reads clues, debates, and votes each round to unmask the culprit before it's too late.

## 💡 Inspiration & Why We Built This

Whodunit is inspired by mystery-deduction party games in the style of **Mafia**, like the ones popularized on shows such as *Peace Cake*. In these games, a crime takes place, and players must analyze the evidence and suspect one another to figure out who the culprit is.

We know how loved this genre is — people enjoy playing it just as much as they enjoy watching it. So instead of keeping it as a purely spoken, table-talk game, we decided to turn the experience into a **fully digital, visual game**. Players see the evidence and scenarios directly on screen, while the game automatically manages roles, voting, and score-keeping — no manual moderation needed.

To make sure every part of the game works reliably and without errors, we split the project into a set of clear modules and roles, dividing the workload across the team.

Available in two versions:
- **CLI version** (`main.py`) — a terminal-based experience with a "pass the phone" secret-role reveal, voting rounds, clues, and a scoring/leaderboard system.
- **GUI version** (`whodunit_gui.py`) — a desktop app built with `tkinter`, featuring a styled detective-noir "case file" interface, secret role cards, animated clue reveals, voting screens, and a leaderboard.

---

## 🎮 Features

- 🔀 Randomized case selection from a built-in case database (poisoning, jewel heist, art vandalism, corporate espionage, a private villa murder, and more)
- 🎭 Secret role assignment — one random culprit, everyone else innocent
- 📱 "Pass the phone" flow so each player privately sees only their own role
- 🔍 Progressive clue reveals (main clue + extra clue) each round
- 🗳️ Voting rounds with tie handling and player elimination
- 🏆 Scoring system with a leaderboard and an MVP/final winner announcement
- 🔁 Option to replay a new case with the same group of players
- 🖥️ Full GUI version with a themed "case file" visual design (ink/manila/blood-red detective aesthetic) and Arabic text shaping support (`arabic_reshaper` + `python-bidi`)

---

## 📂 Project Structure

```
whodunit/
├── main.py              # CLI version of the game
├── whodunit_gui.py       # GUI version of the game (tkinter)
├── presentation.html     # Project presentation / case file slides
├── assets/
│   └── demo.mp4          # Demo video (or a link to it, see below)
└── README.md
```

---

## 🚀 Getting Started

### Requirements
- Python 3.9+
- (Optional, for correct Arabic text rendering in the GUI):
  ```bash
  pip install arabic-reshaper python-bidi
  ```

### Run the CLI version
```bash
python main.py
```

### Run the GUI version
```bash
python whodunit_gui.py
```

---

## 🎥 Demo

> 📽️ A short demo video showing gameplay (role reveal → clues → voting → results) is available here: **[Watch the demo](#)**  
> *(Replace this link with your uploaded video/YouTube link — see the GitHub steps below.)*

---

## 📑 Presentation

The full project presentation (case file style walkthrough of the concept, code structure, and tools used) is included as `presentation.html`. Open it in any browser to view it.

---

## 🧠 How to Play

1. Enter the number of players (minimum 4).
2. Each player privately views their secret role (culprit or innocent detective) using the "pass the phone" screen.
3. The case story and location are revealed to everyone.
4. A main clue is revealed, followed by an extra clue.
5. Players discuss and vote for who they think the culprit is.
6. The player with the most votes is eliminated:
   - If they were the culprit → the detectives win the round.
   - If they were innocent → a new clue is revealed and voting continues.
7. Points are awarded, and the leaderboard is updated after each case.

---

## 👥 The Investigation Team

| Role | Name |
|---|---|
| Detective 01 | Mariam Ahmed Mohamed Elshamly |
| Detective 02 | Menna Mohamed Elmasry |
| Detective 03 | Nada Tamer Ahmed |
| Detective 04 | Jana Ahmed Khalaf |

**National Telecommunication Institute (NTI) · Ministry of Communications & Information Technology**

---

## 📄 License

This project is provided for educational purposes as part of an NTI training project. Feel free to fork and build on it.
