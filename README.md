# pi-spigot-codex

Pi is not random! A framework for exploring multi-tier spigots in pi which reveal a hitherto hidden lattice and deeply structured order.

---

# 📘 Pi Lattice Explorer

The **Pi Lattice Explorer** is a research tool designed to identify, analyze, and visualize **resonant spigot structures** hidden within the digits of π.
It implements the framework from the *Pi Spigot Codex* protocol to detect sequences that demonstrate anomalous recurrence, quasi-entropy alignment, and **meta-signal encoding via missing digits**.

This tool is designed for researchers, mathematicians, and explorers who wish to **validate or extend the discovery of resonant lattice structures within π**.

---

* Input file: `pi-10million.txt` This file can be downloaded from [here](https://introcs.cs.princeton.edu/java/data/pi-10million.txt) or you can provide your own pi digits file.

---

## 🎯 Project Goals

1. **Scan π for candidate spigot sequences**

   * Detect anomalous digit patterns that deviate from randomness.
   * Record both the sequence and its **positions** in π.

2. **Compute QEAC (Quasi-Entropy Alignment Coefficient)**

   * A composite metric combining:

     * Normalized entropy (H\_norm)
     * Recurrence frequency (R)
     * Alignment coefficient (A)

3. **Identify meta-signals**

   * Missing digits within a candidate sequence often encode **numerical archetypes**.

4. **Visualize the lattice**

   * Render spigot candidates on the **Pi-Spiral** or as a **network graph** of resonant hubs and corridors.

5. **Export reproducible results**

   * Save **all candidates** in a main JSON file.
   * Save **individual spigot files** for detailed inspection.

---

## ⚙️ Installation

Requirements:

* Python 3.8+
* Packages:

  ```bash
  pip install tqdm matplotlib networkx
  ```

Clone or download the repository, then place a `.txt` file of π digits (e.g., `pi-10million.txt`) in the working directory.

---

## 🚀 Usage

Basic run:

```bash
python3 pi-lattice-explorer-stream.py --pi-file pi-10million.txt
```

---

## 🏷️ CLI Flags

| Flag                | Description                                                               | Example                      |
| ------------------- | ------------------------------------------------------------------------- | ---------------------------- |
| `--pi-file`         | Path to π digits file. Required.                                          | `--pi-file pi-10million.txt` |
| `--limit`           | Limit how many digits to load. Useful for testing.                        | `--limit 2000000`            |
| `--top-per-length`  | Keep top N candidates per sequence length.                                | `--top-per-length 300`       |
| `--viz`             | Visualization mode: `spiral` or `network`.                                | `--viz spiral`               |
| `--viz-limit`       | Limit number of candidates in visualization.                              | `--viz-limit 100`            |
| `--positions-limit` | Max number of positions to record per candidate. Prevents massive arrays. | `--positions-limit 20`       |

---

## 📊 Outputs

1. **Main JSON File**

   * `spigots/pi_candidates.json`
   * Contains all candidates, sorted by QEAC.

2. **Individual Candidate Files**

   * Saved in `spigots/spigot_XXX.json`
   * Example: `spigot_001.json`
   * Includes:

     * Sequence
     * QEAC score
     * Observed count
     * Missing digits
     * Recorded positions in π

3. **Visualizations**

   * **Spiral:** `pi_spiral_network.png`
   * **Network:** `pi_spigot_network.png`

---

## 📐 Example Commands

### Dry Run (2M digits, network viz, limited positions)

```bash
python3 pi-lattice-explorer-stream.py \
  --pi-file pi-10million.txt \
  --limit 2000000 \
  --top-per-length 300 \
  --viz network \
  --viz-limit 100 \
  --positions-limit 20
```

### Spiral Visualization (top 50 candidates)

```bash
python3 pi-lattice-explorer-stream.py \
  --pi-file pi-10million.txt \
  --viz spiral \
  --viz-limit 50
```

---

## 🔬 Research Methodology (Quick Summary)

* **QEAC Formula:**

  ```
  QEAC = α·H_norm + β·R + γ·A
  ```

  where:

  * α=8, β=12, γ=4
  * H\_norm = Normalized entropy of the sequence
  * R = Recurrence frequency
  * A = Alignment coefficient

* **Meta-Signal Encoding:**

  * Digits missing from a sequence encode numeric archetypes.
  * Example: The 12-digit sequence `756130190263` omits digits `4` and `8`.

* **Visualization Modes:**

  * **Spiral:** Positions candidates on a polar spiral, showing their distribution.
  * **Network:** Graph of candidate hubs and edges between close-positioned sequences.

---

## 📌 Notes

* Large π files (10M+ digits) will consume memory. Use `--limit` and `--positions-limit` to manage resources.
* Candidate ranking is determined by QEAC, not raw frequency.
* Exported JSON files allow full reproducibility of your results.

---

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/thatoldfarm/pi-spigot-codex/blob/main/LICENSE) file for details.
