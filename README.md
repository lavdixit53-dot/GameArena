# GameArena – Python-Based Game and Score Management System

## 1. Project Overview

GameArena is a modular Python-based game and score management system built around the Snake-Water-Gun game.

The project goes beyond a basic game by providing player management, multiple-round gameplay, statistics generation, persistent JSON storage, input validation, and a leaderboard system.

The main objective of the project is to demonstrate Python programming concepts through a structured, modular, and user-friendly application.

---

## 2. Problem Statement

A basic console game usually focuses only on gameplay and does not provide a structured way to manage player information, analyze performance, store previous results, or display rankings.

GameArena addresses this limitation by integrating gameplay with player management, statistics, persistent storage, and leaderboard functionality in a single modular application.

---

## 3. Objectives

The main objectives of GameArena are:

- To implement a functional Snake-Water-Gun game using Python.
- To allow users to play multiple rounds.
- To maintain player-wise scores and game statistics.
- To calculate the player's win percentage.
- To store game results permanently using JSON.
- To provide a leaderboard based on recorded wins.
- To implement input validation and error handling.
- To demonstrate modular Python programming.


## 4. Key Features

### 🎮 Game Module
- Snake-Water-Gun gameplay.
- Computer generates its choice randomly.
- Automatic result calculation.
- Support for multiple rounds.

### 👤 Player Management
- Accepts player name.
- Maintains wins, losses, and draws.
- Calculates total games played.

### 📊 Statistics
- Displays:
  - Total games
  - Wins
  - Losses
  - Draws
  - Win percentage

### 🏆 Leaderboard
- Displays previously recorded players.
- Sorts players according to number of wins.
- Provides a simple ranking view.

### 💾 Persistent Storage
- Game results are stored in `results.json`.
- Previous records can be loaded when the application starts.
- Data remains available after the program is closed.

### ✅ Validation and Error Handling
- Invalid game choices are rejected.
- Number of rounds is restricted to the valid range.
- Invalid or corrupted JSON data is handled safely.

---

## 5. Functional Requirements

The system provides the following major functional modules:

1. **Game Management**
   - Start a new game.
   - Select Snake, Water, or Gun.
   - Generate computer choice.
   - Determine the game result.

2. **Player and Statistics Management**
   - Store player name.
   - Maintain wins, losses, and draws.
   - Calculate total games and win percentage.

3. **Result and Leaderboard Management**
   - Save game results.
   - Load previous records.
   - Display leaderboard.

4. **Input Validation**
   - Validate menu choices.
   - Validate game choices.
   - Validate number of rounds.

---

## 6. Non-Functional Requirements

### Usability
The application provides a simple menu-driven console interface that can be operated by a beginner.

### Reliability
The system validates user input and handles invalid or corrupted stored data without terminating unexpectedly.

### Maintainability
The project is divided into separate Python modules, making individual components easier to understand and modify.

### Resource Efficiency
The application uses lightweight Python modules and JSON storage without requiring an external database.

---

## 7. Technologies and Tools

| Technology / Tool | Purpose |
|---|---|
| Python | Core programming language |
| VS Code | Development environment |
| JSON | Persistent data storage |
| Git | Version control |
| GitHub | Source-code repository |

No external Python packages are required.

---

## 8. Project Architecture

The application follows a modular architecture.

```text
                 USER
                   │
                   ▼
              main.py
          Main Controller
                   │
       ┌───────────┼───────────┐
       │           │           │
       ▼           ▼           ▼
 validator.py   game.py    player.py
       │           │           │
       │           └─────┬─────┘
       │                 │
       │                 ▼
       │          statistics.py
       │                 │
       │                 ▼
       │            storage.py
       │                 │
       │                 ▼
       │            results.json
       │
       └──────────► leaderboard.py