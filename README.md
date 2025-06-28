# ⚽ Soccer Games Scheduler

**AI-Driven Scheduler for Soccer Matches**  
Built using Python and an And-Tree-based constraint satisfaction model, this project generates optimized soccer game schedules under real-world constraints such as team availability, field times, and referee assignments.

## 📌 Project Overview

This project was developed as a term assignment (Sep–Dec 2024) by a 5→3 member team. The goal was to implement an AI-based scheduler capable of solving complex constraint-based problems using algorithmic techniques.

**Key Features:**

- ✅ Constraint-based scheduling using a custom AI model
- 🤖 And-Tree search logic for efficient backtracking and pruning
- 📐 Formal mathematical model to define problem state and transitions
- 📊 Tested on 10+ real-world scenarios with varied constraints

## 🧠 Technical Highlights

- **Algorithm Design**: Developed a custom And-Tree-based search algorithm to represent the state space and recursively enforce hard constraints.
- **Constraint Modeling**: Included team match limits, venue availability, non-overlapping times, and referee assignments.
- **State Transitions**: Modeled actions (e.g., assigning a team or field) as state transitions validated by constraint functions.
- **Test Suite**: Evaluated on multiple test cases to measure solution validity and efficiency.

## 🛠️ Tech Stack

- **Language**: Python
- **Paradigms**: AI search algorithms, constraint satisfaction, functional programming
- **Tools**: NumPy, Matplotlib (for visualization), custom testing framework

## 🚀 Getting Started

### Clone the Repository

```bash
git clone https://github.com/dylanrylee/soccer-games-scheduler.git
cd soccer-games-scheduler
```

### Run the Program
```
python main.py
```
