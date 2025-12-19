# Soccer Match Schedule Optimizer

A branch-and-bound search algorithm with constraint satisfaction, this project generates optimal soccer game schedules under real-world constraints such as team availability, field times, and referee assignments.

This project was developed as a term assignment (Sep–Dec 2024) by a 5→3 member team. The goal was to implement an AI-based scheduler capable of solving complex constraint satisfaction problems using advanced algorithmic techniques.

**Key Features:**

- Constraint-based scheduling using branch-and-bound optimization
- Recursive backtracking with intelligent pruning (84.8% efficiency)
- Dual-layer constraint system (hard + soft constraints)
- Tested on 10+ real-world scenarios with varied complexity

### Algorithm Design
Implemented a custom **branch-and-bound search algorithm** with:
- **Recursive backtracking** for complete state-space exploration
- **Upper bound pruning** to eliminate suboptimal branches
- **Heuristic filtering** (f_bound) removing worst 40% of candidates
- **Evaluation function** minimizing weighted penalty scores

### Constraint Modeling
- **Hard Constraints**: Slot capacity limits, non-overlapping assignments, city-specific rules (10+ constraints)
- **Soft Constraints**: Slot preferences, pairing preferences, minimum fill requirements (weighted penalties)
- **State Management**: Deep-copy isolation preventing shared state bugs

### Data Structures
- **AND-Tree**: Custom tree nodes representing partial schedule states
- **State-Space Representation**: Slots, games, practices with assignment tracking
- **Constraint Framework**: Modular hard/soft constraint validation

## Getting Started

### Prerequisites
```bash
Python 3.11 or higher
```

### Clone the Repository
```bash
git clone https://github.com/dylanrylee/soccer-games-scheduler.git
cd soccer-games-scheduler
```

### Run the Program
```bash
python main.py <input_file> <w_min_filled> <w_pref> <w_pair> <w_sec_diff> <pen_game_min> <pen_practice_min> <pen_not_paired> <pen_section>
```

**Example:**
```bash
python main.py CPSC433F24-SmallInput1.txt 1 1 1 1 1 1 1 1
```

### Command Line Arguments

| Argument | Description |
|----------|-------------|
| `input_file` | Path to input file containing scheduling data |
| `w_min_filled` | Weight for minimum slot fill penalty |
| `w_pref` | Weight for slot preference violations |
| `w_pair` | Weight for pairing preference violations |
| `w_sec_diff` | Weight for section difference violations |
| `pen_game_min` | Penalty per game below minimum |
| `pen_practice_min` | Penalty per practice below minimum |
| `pen_not_paired` | Penalty for unpaired items |
| `pen_section` | Penalty for section conflicts |

## Performance

### Small Input Example
- **Input**: 4 games, 2 practices, 5 time slots
- **Result**: Optimal solution found (score: 6)
- **Efficiency**: 46 nodes explored, 39 pruned (84.8%)
- **Runtime**: < 1 second

### Large Input Characteristics
- **Input**: 49 games, 134 practices, 36 time slots
- **Note**: Exhaustive search may take extended time due to exponential complexity
- **Recommendation**: For production, implement time limits or hybrid approaches

## Project Structure

```
soccer-games-scheduler/
├── and_tree_node.py          # AND-tree node implementation
├── hard_constraints.py        # Mandatory constraint validation
├── soft_constraints.py        # Penalty-based optimization
├── scheduler_structures.py    # Core data structures (Slot, Game, Practice)
├── search_process.py          # Branch-and-bound algorithm
├── main.py                    # Entry point and input parsing
├── test.py                    # Test utilities
├── .gitignore                 # Git ignore rules
└── README.md                  # This file
```

## Algorithm Overview

The scheduler uses **branch-and-bound** optimization:

1. **Expand**: Generate child nodes by assigning games/practices to slots
2. **Filter**: Apply f_bound to keep only top 60% of candidates
3. **Evaluate**: Score nodes using soft constraint penalties
4. **Prune**: Eliminate branches worse than current best solution
5. **Backtrack**: Recursively explore remaining branches
6. **Return**: Best complete schedule found

## Testing

Run on provided test inputs:
```bash
# Small test case
python main.py CPSC433F24-SmallInput1.txt 1 1 1 1 1 1 1 1

# Large test cases
python main.py CPSC433F24-LargeInput1.txt 1 1 1 1 1 1 1 1
python main.py CPSC433F24-LargeInput2.txt 1 1 1 1 1 1 1 1
```

## Key Concepts Demonstrated

- Branch-and-bound optimization
- Constraint satisfaction problems (CSP)
- Depth-first search with backtracking
- Heuristic pruning strategies
- State-space exploration
- NP-hard problem solving

## Input File Format

Input files should contain sections for:
- Game slots (day, time, max, min)
- Practice slots (day, time, max, min)
- Games (identifier, league, age/tier, division)
- Practices (identifier, associated game, type)
- Not compatible (conflicting pairs)
- Unwanted (item, slot to avoid)
- Preferences (item, preferred slot, penalty)
- Pair preferences (items that should be together)
- Partial assignments (pre-assigned items)

See `CPSC433F24-SmallInput1.txt` for example format.

## Contributors

Developed by a collaborative team (5→3 members) for CPSC 433, University of Calgary, Fall 2024.

## License

This project is available for educational and portfolio purposes.

---

**Note**: This scheduler guarantees finding optimal solutions but may require significant runtime for large problem instances (183+ items). For production use on large datasets, consider implementing time limits or iterative deepening strategies.
