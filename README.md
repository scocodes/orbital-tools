orbital-tools

Reusable Python tools for orbital dynamics simulation, atmospheric modelling and numerical integration.

This package was developed to support computational aerospace projects involving:

* orbital propagation
* atmospheric drag modelling
* uncertainty analysis
* Monte Carlo simulation
* state estimation and tracking
* surrogate modelling workflows

Features

* Two-body orbital dynamics models
* Modular atmosphere models
* RK4 numerical integration utilities
* Reusable scientific computing architecture
* Lightweight and extensible design

Installation

Clone the repository and install in editable mode:
git clone https://github.com/YOUR_USERNAME/orbital-tools.git
cd orbital-tools
python -m pip install -e .

Project Structure 
orbital-tools/
├── pyproject.toml
├── README.md
└── src/
    └── orbital_tools/
        ├── __init__.py
        ├── atmosphere.py
        ├── dynamics.py
        └── integrators.py

Current Modules

dynamics.py

Orbital dynamics models and force calculations.

atmosphere.py

Atmospheric density model implementations.

integrators.py

Numerical integration routines including RK4 propagation.

LICENSE:

MIT