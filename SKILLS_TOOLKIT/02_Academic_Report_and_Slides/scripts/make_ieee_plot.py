#!/usr/bin/env python3
"""
Scientific & Publication-Ready Plot Generator.
Uses SciencePlots (IEEE / Nature / Science style) with fallback to clean high-DPI matplotlib.
"""

import sys
import os
import argparse
import numpy as np
import matplotlib.pyplot as plt

def generate_scientific_plot(output_path: str = "ieee_publication_plot.png", title: str = "Model Performance Evaluation"):
    # Try using SciencePlots
    try:
        import scienceplots
        plt.style.use(['science', 'no-latex', 'grid'])
        print("[+] Applied style: ['science', 'no-latex', 'grid']")
    except Exception as e:
        print(f"[-] SciencePlots fallback to standard clean style ({e})")
        plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
        plt.rcParams['font.family'] = 'serif'
        plt.rcParams['font.size'] = 11

    fig, ax = plt.subplots(figsize=(6.5, 4.2), dpi=300)

    # Sample data: Convergence of 3 algorithms
    epochs = np.arange(1, 21)
    acc_ga = 0.75 + 0.16 / (1 + np.exp(-(epochs - 6) / 2.2))
    acc_sa = 0.70 + 0.17 / (1 + np.exp(-(epochs - 10) / 3.0))
    acc_hc = 0.72 + 0.13 / (1 + np.exp(-(epochs - 4) / 1.5))
    acc_hc[8:] = acc_hc[8] # Stuck in local optimum

    ax.plot(epochs, acc_ga, 'o-', color='#0C5DA5', label='Genetic Algorithm (Pop=20, Mut=0.10)', linewidth=2.0, markersize=5)
    ax.plot(epochs, acc_sa, 's--', color='#00B945', label='Simulated Annealing (Geometric)', linewidth=1.8, markersize=4)
    ax.plot(epochs, acc_hc, '^:', color='#FF2C00', label='Hill Climbing (Random Restarts)', linewidth=1.8, markersize=4)

    ax.set_xlabel('Iteration / Generation', fontsize=11, fontweight='bold')
    ax.set_ylabel('Objective Fitness (7-Fold CV Accuracy)', fontsize=11, fontweight='bold')
    ax.set_title(title, fontsize=12, fontweight='bold', pad=12)
    ax.legend(frameon=True, framealpha=0.9, loc='lower right', fontsize=9)
    ax.set_ylim(0.68, 0.94)

    # Save outputs
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    pdf_path = os.path.splitext(output_path)[0] + ".pdf"
    plt.savefig(pdf_path, bbox_inches='tight')
    plt.close()

    print(f"[+] High-resolution PNG saved: {output_path} (300 DPI)")
    print(f"[+] Vector PDF saved: {pdf_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate scientific publication plot.")
    parser.add_argument("--output", default="ieee_publication_plot.png", help="Output PNG path")
    parser.add_argument("--title", default="Scientific Optimization Convergence (IEEE Format)", help="Plot title")
    args = parser.parse_args()
    generate_scientific_plot(args.output, args.title)
