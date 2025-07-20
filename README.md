# Flappy Bird Neuroevolution

A population-based machine learning implementation for autonomous Flappy Bird gameplay using custom neural networks and genetic algorithms.

## Overview

This project implements an AI system that learns to play Flappy Bird through evolutionary computation rather than traditional supervised learning methods. The system employs a population of neural network-controlled agents that evolve over generations to maximize survival time in the game environment.

## Demonstration

<div align="center">
  <video width="480" height="640" controls>
    <source src="vid/Screen Recording 2025-07-21 at 1.41.18 AM.mov" type="video/mp4">
    Your browser does not support the video tag.
  </video>
  <p><em>AI agents learning to navigate through pipes over multiple generations</em></p>
</div>

## Technical Implementation

### Architecture

The system consists of several core components:

- **Game Engine**: Built on pygame, implementing standard Flappy Bird mechanics with collision detection and physics simulation
- **Neural Network**: Custom feedforward network implementation with sigmoid activation functions
- **Population Management**: Genetic algorithm with speciation for maintaining diversity
- **Vision System**: Three-input sensory system providing distance measurements to environmental obstacles

### Neural Network Structure

Each agent utilizes a minimal neural network architecture:
- **Input Layer**: 3 nodes (distance to top pipe, horizontal distance to pipe, distance to bottom pipe) + 1 bias node
- **Output Layer**: 1 node (binary action decision)
- **Activation**: Sigmoid function for output layer
- **Weights**: Initialized randomly in range [-1, 1]

### Evolutionary Algorithm

The system implements speciation-based evolution:
- **Population Size**: 100 agents per generation
- **Selection**: Fitness-proportionate selection within species
- **Mutation**: Weight perturbation with 10% probability of complete replacement
- **Speciation**: Automatic clustering based on weight similarity
- **Staleness Elimination**: Species are removed after 8 generations without improvement

### Vision System

Agents perceive their environment through three normalized distance measurements:
1. Vertical distance to upper pipe boundary
2. Horizontal distance to nearest pipe
3. Vertical distance to lower pipe boundary

Values are normalized to [0, 1] range using a 500-pixel reference distance.

## Installation

### Requirements

```
python >= 3.6
pygame >= 2.0.0
```

### Setup

```bash
git clone https://github.com/Rishi-raj3017/RL-in-flappy-bird.git
cd RL-in-flappy-bird
pip install pygame
python main.py
```

## Usage

Execute `main.py` to begin training. The system will:

1. Initialize a population of 100 random agents
2. Run each generation until all agents die
3. Apply natural selection and generate offspring
4. Repeat the process across generations

### Monitoring Progress

- Console output displays generation progression and population statistics
- Visual debug lines show each agent's vision system
- Agent colors are randomly assigned for visual differentiation

## Performance Characteristics

### Convergence Behavior

- **Early Generations**: Random, erratic movement patterns
- **Mid Training**: Basic pipe avoidance emerges
- **Advanced Generations**: Consistent navigation and optimal timing

### Computational Complexity

- **Per Frame**: O(n) where n = population size
- **Per Generation**: O(n²) for speciation operations
- **Memory Usage**: Linear with population size and network complexity

## File Structure

```
├── main.py           # Primary execution loop and game logic
├── player.py         # Agent class with neural network integration
├── brain.py          # Neural network implementation
├── population.py     # Population management and evolution
├── species.py        # Species clustering and selection
├── components.py     # Game environment objects
├── config.py         # Global constants and display settings
├── node.py           # Neural network node implementation
└── connection.py     # Neural network connection implementation
```

## Configuration Parameters

Key parameters can be modified in the respective files:

- **Population size**: `population.py` line 11
- **Mutation rates**: `connection.py` lines 10-11
- **Network topology**: `brain.py` lines 15-27
- **Vision normalization**: `player.py` lines 66-76
- **Game physics**: `components.py` and `player.py`

## Research Applications

This implementation serves as a foundation for:

- Comparative studies between evolutionary and gradient-based learning
- Investigation of population diversity effects on convergence
- Analysis of minimal network architectures for game AI
- Exploration of vision system design for autonomous agents

## License

MIT License - see repository for full details.

## Contributing

Contributions focused on algorithmic improvements, performance optimization, or extended analysis capabilities are welcome through standard pull request procedures. 