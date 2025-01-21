# Turtle Snake Game

A colorful implementation of the classic Snake game using Python's Turtle graphics library with object-oriented design principles.

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Turtle](https://img.shields.io/badge/Turtle-Graphics-green)
![OOP](https://img.shields.io/badge/OOP-Design-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 🎯 Overview

This project reimagines the classic Snake game with unique features:
1. Rainbow-colored snake segments using RGB color generation
2. Dynamic speed increase based on score
3. Collision detection with walls, food, and snake body
4. Real-time score tracking

## 🎮 Game Features

### Visual Elements
- Black background with maroon borders
- Colorful snake with randomly colored segments
- Blue circular food particles
- Clean score display
- Game over screen

### Game Mechanics
- Snake grows with each food collection
- Speed increases progressively with score
- Wall collision detection
- Self-collision detection
- Smooth movement animations

## 🔧 Technical Components

### Snake Implementation
```python
class Snake:
    def __init__(self):
        self.snake = []
        self.sleep_parameter = 0.08  # Controls game speed
        self.initial_setup()

    def create_snake_part(self):
        # Generate random RGB colors for each segment
        color = (random.randint(100,255),
                random.randint(100,255),
                random.randint(100,255))
```

### Game Screen Management
```python
class GameScreen:
    def __init__(self):
        self.screen = Screen()
        self.initial_setup()

    def initial_setup(self):
        self.screen.setup(width=600, height=600)
        self.screen.bgcolor("black")
```

### Key Features
1. **Movement System**
   - Smooth continuous movement
   - Left/right turning controls
   - Segment following behavior

2. **Food System**
   - Random spawn locations
   - Collision avoidance with snake
   - Score increment on collection

3. **Scoring System**
   - Real-time score display
   - Speed adjustment based on score
   - Game over notification

## 💻 Implementation Details

### Class Structure
- `Snake`: Core snake mechanics and movement
- `Food`: Food spawning and placement
- `Wall`: Game boundary creation
- `ScoreBoard`: Score tracking and display
- `GameScreen`: Game window management

### Controls
- `A`: Turn Left
- `D`: Turn Right

## 🚀 Usage

1. Install Python (3.8 or higher)

2. Run the game:
```bash
python main.py
```

3. Play using A/D keys to navigate and collect food

## 🎯 Game Rules

1. Control the snake to collect blue food particles
2. Avoid hitting the walls
3. Avoid colliding with your own tail
4. Score increases with each food collection
5. Snake moves faster as score increases

## 🛠️ Project Structure

```
snake_game/
├── main.py          # Game loop and collision detection
├── snake.py         # Snake class implementation
├── food.py          # Food spawning mechanics
├── wall.py          # Boundary creation
├── scoreboard.py    # Score tracking
└── screen.py        # Game screen setup
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Author

Burak TÜZEL

