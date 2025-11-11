README: Running Polymer Analysis Script

This guide explains how to use the Python script `analyse_g.py` to compute and compare the radius of gyration (Rg^2) values for different polymer architectures.

📁 Directory Structure:
-----------------------
Place your directory in this format:

Polymerproject/
├── 02_Analysis/
│   ├── analyse_g.py
│   ├── mercedes_rg2.dat
│   ├── tree_rg2.dat
│   └── (your output will be shown here)
├── 01_run/
    ├── mercedes/
    │   └── rg2.dat
    ├── tree/
    │   └── rg2.dat

🚀 How to Run:
--------------
From within the `02_Analysis/` folder, run:

```bash
python analyse_g.py --mer ../01_run/mercedes/rg2.dat --tree ../01_run/tree/rg2.dat
```

🧮 Output:
----------
The script prints:
- ⟨Rg²⟩ for mercedes architecture
- ⟨Rg²⟩ for tree architecture
- g = Rg²_tree / Rg²_mercedes

📌 Notes:
---------
- Ensure Python 3 is installed.
- No external dependencies required.
- Input files must be in the correct format: lines of "<step> <Rg²>".

Created for validating simulation output with analytical expectations.
