#!/usr/bin/env python3
import argparse
import math
import json
import os
from collections import Counter, defaultdict
from tqdm import tqdm
import matplotlib.pyplot as plt
import networkx as nx

def load_pi_digits(filepath, limit=None):
    with open(filepath, "r") as f:
        digits = "".join(c for c in f.read() if c.isdigit())
        if limit:
            digits = digits[:limit]
    return digits

def compute_entropy(sequence):
    counts = Counter(sequence)
    probs = [count / len(sequence) for count in counts.values()]
    if not probs:
        return 0
    H = -sum(p * math.log(p, 2) for p in probs if p > 0)
    return H / math.log(len(counts), 2) if len(counts) > 1 else 0

def compute_alignment_coefficient(seq):
    return sum(int(d) for d in seq) / (9 * len(seq))

def compute_qeac(seq, seen_count):
    H_norm = compute_entropy(seq)
    A = compute_alignment_coefficient(seq)
    alpha, beta, gamma = 8, 12, 4
    qeac = alpha * H_norm + beta * seen_count + gamma * A
    return qeac, H_norm, seen_count, A

def find_candidates(pi_digits, top_per_length=50, positions_limit=None):
    candidates = []
    seen_counts = defaultdict(int)
    seen_positions = defaultdict(list)
    lengths = range(10, 16)

    for length in lengths:
        print(f"[Scanning] Length={length}")
        local_candidates = []
        for i in tqdm(range(0, len(pi_digits) - length + 1), desc=f"L{length}", leave=False):
            seq = pi_digits[i:i+length]
            seen_counts[seq] += 1
            if positions_limit is None or len(seen_positions[seq]) < positions_limit:
                seen_positions[seq].append(i)
            qeac, H, R, A = compute_qeac(seq, seen_counts[seq])
            missing = [d for d in "0123456789" if d not in seq]
            local_candidates.append({
                "sequence": seq,
                "qeac": qeac,
                "entropy": H,
                "recurrence": R,
                "alignment": A,
                "missing_digits": missing,
                "observed_count": seen_counts[seq],
                "positions": seen_positions[seq][:]
            })
        local_candidates.sort(key=lambda x: x["qeac"], reverse=True)
        candidates.extend(local_candidates[:top_per_length])

    return candidates

def visualize_network(candidates, mode="network", viz_limit=None):
    if not candidates:
        print("⚠️ No candidates to visualize.")
        return

    if viz_limit:
        candidates = sorted(candidates, key=lambda x: x['qeac'], reverse=True)[:viz_limit]
        print(f"📊 Visualization limited to top {viz_limit} candidates by QEAC.")

    if mode == "spiral":
        print("📊 Generating Pi-Spiral visualization...")
        plt.figure(figsize=(12, 12))
        n = len(candidates)
        for idx, cand in enumerate(candidates):
            angle = (cand["positions"][0] % 360) * math.pi / 180 if cand["positions"] else idx * 2 * math.pi / n
            r = cand["qeac"] / 10
            x, y = r * math.cos(angle), r * math.sin(angle)
            plt.scatter(x, y, s=40 + cand["qeac"] * 0.15, alpha=0.7,
                        c=[len(cand["missing_digits"])], cmap="plasma")
            if viz_limit and viz_limit <= 100:
                plt.text(x, y, cand["sequence"], fontsize=5, ha="center", va="center")
        plt.colorbar(label="Missing Digit Count")
        plt.title("Pi-Spiral Resonant Spigot Layout")
        plt.axis("off")
        plt.savefig("pi_spiral_network.png", dpi=300)
        plt.close()

    else:
        print("📊 Generating Resonant Spigot Network...")
        G = nx.Graph()
        for cand in candidates:
            G.add_node(cand["sequence"], 
                       qeac=cand["qeac"], 
                       missing=len(cand["missing_digits"]))
        for i, c1 in enumerate(candidates):
            for j, c2 in enumerate(candidates):
                if i < j and c1["positions"] and c2["positions"]:
                    dist = abs(c1["positions"][0] - c2["positions"][0])
                    if dist < 5000:
                        G.add_edge(c1["sequence"], c2["sequence"])
        pos = nx.spring_layout(G, k=0.5, iterations=40)
        plt.figure(figsize=(14, 14))
        nodes = nx.draw_networkx_nodes(
            G, pos,
            node_size=[40 + G.nodes[n]['qeac']*0.4 for n in G.nodes],
            node_color=[G.nodes[n]['missing'] for n in G.nodes],
            cmap=plt.cm.plasma, alpha=0.8
        )
        nx.draw_networkx_edges(G, pos, alpha=0.2, width=0.5)
        if viz_limit and viz_limit <= 50:
            nx.draw_networkx_labels(G, pos, font_size=6, font_color="white")
        plt.colorbar(nodes, label="Missing Digit Count")
        plt.title("Resonant Spigot Lattice Network")
        plt.axis("off")
        plt.savefig("pi_spigot_network.png", dpi=300)
        plt.close()

def export_results(candidates, outdir="spigots"):
    os.makedirs(outdir, exist_ok=True)
    main_json = os.path.join(outdir, "pi_candidates.json")
    with open(main_json, "w") as f:
        json.dump(candidates, f, indent=2)
    print(f"✅ Main results exported to {main_json}")

    for idx, cand in enumerate(candidates, 1):
        fname = os.path.join(outdir, f"spigot_{idx:03d}.json")
        with open(fname, "w") as f:
            json.dump(cand, f, indent=2)
    print(f"✅ {len(candidates)} individual spigot JSON files saved in {outdir}/")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--pi-file", required=True, help="Path to pi digits file")
    parser.add_argument("--limit", type=int, default=None, help="Limit number of pi digits loaded")
    parser.add_argument("--top-per-length", type=int, default=50, help="Top candidates per length")
    parser.add_argument("--viz", choices=["spiral", "network"], default="network", help="Visualization mode")
    parser.add_argument("--viz-limit", type=int, default=None, help="Limit number of candidates shown in visualization")
    parser.add_argument("--positions-limit", type=int, default=None, help="Max positions recorded per candidate")
    args = parser.parse_args()

    pi_digits = load_pi_digits(args.pi_file, args.limit)
    print(f"Loaded {len(pi_digits):,} digits of π for analysis.")

    candidates = find_candidates(pi_digits, args.top_per_length, args.positions_limit)
    visualize_network(candidates, mode=args.viz, viz_limit=args.viz_limit)
    export_results(candidates)

if __name__ == "__main__":
    main()

