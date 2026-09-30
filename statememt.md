# GameArena – Project Statement

## 1. Project Title

**GameArena – Python-Based Game and Score Management System**

---

## 2. Problem Statement

A basic console-based game generally focuses only on gameplay and does not provide a structured system for managing player information, analyzing performance, storing previous game results, or displaying player rankings.

GameArena addresses this problem by combining gameplay with player management, statistics, persistent result storage, input validation, and leaderboard functionality in one modular Python application.

---

## 3. Project Scope

The scope of GameArena includes:

- Implementing the Snake-Water-Gun game.
- Supporting multiple rounds in a single game session.
- Managing player information and scores.
- Calculating game statistics and win percentage.
- Storing game results using a JSON file.
- Loading and displaying previously stored results.
- Providing a leaderboard based on recorded wins.
- Validating user inputs and handling invalid data.

The current project is designed as a local, console-based Python application.

---

## 4. Target Users

GameArena is intended for:

- Students learning Python programming.
- Beginners interested in modular programming.
- Users who want to play a simple console-based game.
- Users who want to track basic game performance and previous results.

---

## 5. High-Level Features

### 1. Game Management
- Start a new game.
- Select Snake, Water, or Gun.
- Generate a computer choice.
- Determine the result of each round.
- Support multiple rounds.

### 2. Player Management
- Enter and store the player's name.
- Track wins, losses, and draws.
- Calculate total games played.

### 3. Statistics
- Display total games.
- Display wins, losses, and draws.
- Calculate and display win percentage.

### 4. Result Storage
- Save completed game results.
- Store records in `results.json`.
- Load previously saved records.

### 5. Leaderboard
- Display previous player records.
- Sort records according to number of wins.

### 6. Validation and Error Handling
- Validate menu choices.
- Validate game choices.
- Validate number of rounds.
- Handle missing or invalid JSON data.

---

## 6. Expected Outcome

The expected outcome of the project is a functional and modular Python application that demonstrates how a simple game can be developed into a structured software system.

The application should allow users to play the game, view their performance statistics, store their results, and access a leaderboard of previous game records.