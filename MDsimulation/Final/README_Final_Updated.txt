README: MD Simulation and Radius of Gyration Analysis
======================================================

This repository includes two core components:

1. **Molecular Dynamics (MD) Simulation using LAMMPS**
2. **Post-simulation Analysis using a Python Script**

📁 Directory Structure:
-----------------------
Organize your project as follows:

Polymerproject/
├── 01_run/
│   ├── mercedes/
│   │   ├── data.lmp
│   │   ├── in.poly
│   │   ├── run.slurm         <-- Submit this to SLURM
│   │   └── rg2.dat           <-- Output file
│   ├── tree/
│   │   ├── data.lmp
│   │   ├── in.poly
│   │   ├── run.slurm         <-- Submit this to SLURM
│   │   └── rg2.dat           <-- Output file
│   ├── linear/
│   │   ├── data.lmp
│   │   ├── in.poly
│   │   ├── run.slurm         <-- Submit this to SLURM
│   │   └── rg2.dat           <-- Output file
│   └── molecule/
│       ├── data.lmp
│       ├── in.poly
│       ├── run.slurm         <-- Submit this to SLURM
│       └── rg2.dat           <-- Output file
├── 02_Analysis/
│   ├── analyse_g.py
│   ├── [arch1]_rg2.dat      <-- Copy from ../01_run/[arch1]/rg2.dat
│   ├── [arch2]_rg2.dat      <-- Copy from ../01_run/[arch2]/rg2.dat
│   └── (outputs displayed here)

🖥️ Submitting the Job:
-----------------------
To launch an MD simulation on an HPC with SLURM:

1. Navigate into one of the architecture directories: `mercedes/`, `tree/`, `linear/`, or `molecule/`.
2. Submit the job using:

```bash
sbatch run.slurm
```

3. Monitor output with:

```bash
tail -f job.out
```

🚀 Running the Analysis:
------------------------
Once both simulations are done and `rg2.dat` files are generated, go to `02_Analysis/` and run:

```bash
python analyse_g.py --mer ../01_run/[arch1]/rg2.dat --tree ../01_run/[arch2]/rg2.dat
```

Where `[arch1]` and `[arch2]` are any two architectures to compare, e.g., `mercedes` and `linear`.

📊 Recommended Comparison Pairs (in order of closeness of g-value):
-------------------------------------------------------------------
1. mercedes and linear     (closest to expected g)
2. molecule and linear
3. mercedes and molecule
4. molecule and tree       (least close match)

🧮 Output:
----------
The script prints:
- ⟨Rg²⟩ for architecture 1
- ⟨Rg²⟩ for architecture 2
- g = Rg²_arch1 / Rg²_arch2

📌 Notes:
---------
- Python 3 is required (no additional packages needed).
- Ensure your LAMMPS build supports the required bond styles.
- Topology and data files are critical—do not modify unless needed.
- Simulation and analysis outputs should be version-controlled for reproducibility.

Created for validating MD simulation results against analytical predictions.
