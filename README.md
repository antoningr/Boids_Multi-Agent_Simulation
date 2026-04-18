# 🐦 Boids Multi-Agent Simulation (Craig Reynolds Model)

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?logo=python&logoColor=white)](https://www.python.org/) 
[![Pygame](https://img.shields.io/badge/Pygame-2.x-00AA00?logo=pygame&logoColor=white)](https://www.pygame.org/) 
[![Simulation](https://img.shields.io/badge/Multi--Agent-Boids-blue)](#) 
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)


This project is a Python implementation of a **multi-agent simulation** inspired by Craig Reynolds’ famous **Boids model**, which simulates realistic flocking behavior such as bird flocks, fish schools, or swarm intelligence.

Each agent (boid) follows three simple rules:

* **Separation** → avoid crowding nearby agents
* **Alignment** → align direction with nearby agents
* **Cohesion** → move toward the center of nearby agents

From these simple rules, complex and realistic flocking behavior emerges.

---

## 🎥 Preview

Example:

boids_simulation.gif

---

## 🚀 Features

* Multi-agent flocking simulation
* Realistic bird-like movement
* Three core behavioral rules
* Boundary collision (bounce on screen edges)
* Smooth real-time animation
* Configurable parameters (speed, radius, force)

---

## 🧠 Concept

This simulation is based on **emergent behavior**:

> Simple local rules → complex global behavior

Instead of controlling each bird individually, each agent makes decisions based only on its neighbors.

Used in:

* Artificial life simulations
* Crowd simulation
* Game AI
* Robotics swarms
* Complex systems research

---

## 🛠️ Requirements

Make sure Python 3.7+ is installed.

Install dependencies:

```bash
pip install pygame
```

---

## ▶️ How to Run

Clone the repository:

```bash
git clone https://github.com/antoningr/boids-simulation.git
cd boids-simulation
```

Run the simulation:

```bash
python main.py
```

---

## ⚙️ Configuration

You can modify parameters in the script:

```python
NB_BIRDS = 150
MAX_SPEED = 4.5
MAX_SPEED = 4.5
MAX_FORCE = 0.09
SEPARATION_RADIUS = 22
ALIGNMENT_RADIUS = 60
COHESION_RADIUS = 110
```

Changing these values will affect the flock behavior.

---

## 📚 Inspiration

* Craig Reynolds (Boids algorithm, 1986)
* Artificial Life research
* Swarm intelligence systems

---

## 🔬 Possible Improvements

* Obstacle avoidance
* Predator-prey simulation
* Mouse-controlled leader boid
* Trails behind birds
* 3D simulation
* Machine learning agents

---

## 📄 License

MIT License.

---

## 👨‍💻 Author

Created as a learning project on multi-agent systems and emergent behavior.

---