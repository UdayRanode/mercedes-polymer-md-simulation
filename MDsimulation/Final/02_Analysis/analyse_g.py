#!/usr/bin/env python3
import argparse, numpy as np

def block_avg(x, block):
    n = (len(x)//block)*block
    if n == 0: return np.mean(x), np.std(x, ddof=1)/np.sqrt(max(1,len(x)))
    y = x[:n].reshape(-1, block).mean(axis=1)
    return y.mean(), y.std(ddof=1)/np.sqrt(len(y))

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--mer", required=True)
    p.add_argument("--tree", required=True)
    p.add_argument("--block", type=int, default=500)
    a = p.parse_args()
    tM, rgM = np.loadtxt(a.mer, unpack=True)
    tT, rgT = np.loadtxt(a.tree, unpack=True)
    mM, eM = block_avg(rgM, a.block)
    mT, eT = block_avg(rgT, a.block)
    g = mM/mT
    gerr = g * np.sqrt( (eM/mM)**2 + (eT/mT)**2 )
    print(f"<Rg^2>_mercedes = {mM:.6f} ± {eM:.6f}")
    print(f"<Rg^2>_tree     = {mT:.6f} ± {eT:.6f}")
    print(f"g = {g:.6f} ± {gerr:.6f}")

if __name__ == "__main__":
    main()
