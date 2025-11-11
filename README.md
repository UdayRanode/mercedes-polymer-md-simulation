README: Mercedes Polymer Project – Analytical & MD Simulation
==============================================================

This repository combines **analytical modeling** and **molecular dynamics (MD) simulations** for the study of mercedes-shaped polymer architectures.

📁 Repository Structure
-----------------------
```
mercedes-polymer-md-simulation/
├── Analytic/                  # Contains Python scripts for analytical computations
│   ├── analyze_theta.py       # Computes angle distribution or metrics
│   ├── analyze_tree.py        # Computes Rg² for tree-like polymers
│   └── compare_results.py     # Compares analytical vs. MD simulation results
│
├── MDSimulationFinal/
│   ├── 01_run/                # Contains MD simulation setups
│   │   ├── linear/
│   │   ├── mercedes/
│   │   ├── molecule/
│   │   └── tree/
│   ├── 02_Analysis/           # Post-processing and analysis scripts
│   │   ├── analyse_g.py
│   │   └── README.txt         # Instructions for analysis
│   └── README.md              # MD-specific README
│
└── README.md                  # General README (this file)
```

🔬 Objective
------------
The aim is to simulate and analyze the structural properties (e.g. radius of gyration Rg²) of mercedes and other polymeric topologies, comparing results from:
- Theoretical analytical models
- LAMMPS-based molecular dynamics simulations

⚙️ How to Use This Repository
-----------------------------
### 1. Analytical Work
Navigate to the `Analytic/` folder and run:
```bash
python analyze_theta.py
python analyze_tree.py
python compare_results.py
```

### 2. MD Simulations
Navigate into any architecture under `MDSimulationFinal/01_run/` and submit jobs using:
```bash
sbatch run.slurm
```
Monitor output using:
```bash
tail -f job.out
```

### 3. Post-Simulation Analysis
After simulations finish, use the `analyse_g.py` script inside `02_Analysis/` to compute `g = Rg²_mercedes / Rg²_tree`:
```bash
python analyse_g.py --mer ../01_run/mercedes/rg2.dat --tree ../01_run/tree/rg2.dat
```

💡 Notes
---------
- Python 3 is required (no extra packages needed).
- LAMMPS installation with necessary packages is expected.
- `g` value is computed for several architecture pairs. Closest matching results:
  1. mercedes & linear
  2. molecule & linear
  3. mercedes & tree
  4. molecule & tree

📎 License & Contributions
--------------------------
Open for academic and personal use. Feel free to contribute improvements or extensions via pull requests.
