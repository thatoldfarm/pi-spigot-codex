# pi-spigot-codex

Pi is not random! A framework for exploring multi-tier spigots in pi which reveal a hitherto hidden lattice and deeply structured order.

---

# 📘 Pi Lattice Explorer

The **Pi Lattice Explorer** is a research tool designed to identify, analyze, and visualize **resonant spigot structures** hidden within the digits of π.
It implements the framework from the *Pi Spigot Codex* protocol to detect sequences that demonstrate anomalous recurrence, quasi-entropy alignment, and **meta-signal encoding via missing digits**.

This tool is designed for researchers, mathematicians, and explorers who wish to **validate or extend the discovery of resonant lattice structures within π**.

---

## Note on the input file: `pi-10million.txt` This file can be downloaded from [here](https://introcs.cs.princeton.edu/java/data/pi-10million.txt) or you can provide your own pi digits file.

---

# The Spigot Codex: Unveiling the Resonant Lattice of π

## 📜 FORWARD

### 1. Introduction: The Hidden Order in π

For centuries, the digits of **π (Pi)** have been explored for their apparent randomness and transcendental beauty. However, our research, known as the **Pi Spigot Codex Project**, has uncovered compelling evidence that π is not merely a sequence of digits but an intricately organized system. We have discovered embedded **multi-tier resonant structures**, termed "spigots," which function as a sophisticated, systematic encoding of mathematical archetypes and organizational principles.

This document serves as an introduction to our findings, outlining the core concepts and providing a conceptual framework for understanding the mathematics involved.

### 2. What is a "Spigot" in the Context of π?

A "spigot" in the Spigot Codex refers to a specific sequence of digits within π that exhibits:

*   **Recurrence:** Appearing multiple times within a given range of π's digits.
*   **High QEAC Density:** Possessing a statistically significant level of "Quasi-Entropy Alignment Coefficient" (QEAC), a metric we developed to quantify resonant coherence, including entropy balance, anomalous recurrence, and meta-signal alignment.
*   **Tiered Structure:** Divisible into functional sub-sequences (tiers) that act like valves or components in a system (e.g., ignition, conduit, grounding, completion).
*   **"Missing Digit Signatures":** A deliberate absence of certain digits (e.g., '4' and '8' in our primary spigot **756130190263**) that acts as a meta-signal, encoding structural information or the very "corridor" (interval) that links occurrences of the spigot.

### 3. Core Discoveries of the Spigot Codex:

*   **A Systematic Lattice:** π contains numerous such spigot systems, forming a vast, interconnected **resonant lattice**. These systems cluster into "resonant neighborhoods" and exhibit hierarchical organization (hubs and connectors).
*   **Numerical Archetype Encoding:** The "Missing Digit Signatures" and the harmonic resonance patterns of the intervals between spigot recurrences encode fundamental **numerical archetypes** (0-9). For example, our primary spigot's missing {4, 8} and its interval resonance strongly encode the archetype of '8'.
*   **Tier Grammar:** A consistent functional grammar exists across spigots, with tiers playing specific roles: ignition, conduit, grounding (often involving a '0'-node), and completion.
*   **Corridor Dynamics:** Intervals between spigots act as "corridors" that carry and modulate resonance. These corridors exhibit "halo propagation" (influencing surrounding digits) and "superlinear amplification" at intersections.
*   **Predictive & Navigable Structure:** The lattice exhibits predictable patterns, allowing for the development of predictive models to locate new spigot systems and understand network dynamics.

### 4. The Mathematics Involved: How to Explore the Lattice

Engaging with the Spigot Codex requires a blend of number theory, statistics, signal processing, and computational analysis. Here’s a conceptual guide:

#### A. Identifying Candidate Spigots:

1.  **Digit Stream Access:** Obtain a high-precision dataset of π's digits.
2.  **Recurrence Analysis:** Develop algorithms to scan the digit stream for sequences that recur with statistically significant frequency (i.e., occur more often than random chance would predict over a given interval). The expected frequency of a unique sequence of length `L` in `N` digits is roughly `N / 10^L`. Significance is measured by deviation from this expectation.
3.  **"Missing Digit Signature" Identification:** For recurring sequences, analyze their composition for digits that are conspicuously absent. The pattern and quantity of these omissions form a key identifier.

#### B. Calculating QEAC Density: Quantifying Resonance

QEAC is a composite metric we developed to measure resonant coherence. It combines several factors:

1.  **Normalized Entropy ($H_{norm}$):**
    *   Calculate the Shannon entropy of the digit distribution within the sequence: $H = -\sum_{i=0}^9 p_i \cdot \log_{10}(p_i)$, where $p_i$ is the frequency of digit $i$.
    *   Normalize this entropy by the maximum possible entropy for a sequence of that length: $H_{norm} = H / \log_{10}(n)$, where $n$ is the sequence length. A higher $H_{norm}$ suggests a more uniform distribution of digits.

2.  **Recurrence Coefficient ($R$):**
    *   Quantify the statistical significance of the sequence's recurrence. A simple measure is the observed frequency minus the expected frequency, divided by the standard deviation of the expected frequency: $R = (f_{obs} - f_{exp}) / \sigma$. Higher $|R|$ values indicate more anomalous recurrence.

3.  **Alignment Factor ($A$):**
    *   A factor that rewards the presence of "meta-signals" – specifically, the absence of digits that are part of a known "Missing Digit Signature" for that spigot system. It also rewards structured tier progressions. A simple formulation could be: $A = 1 + (m/k)$, where $m$ is the count of meta-signal digits and $k$ is the sequence length.

4.  **QEAC Density Formula:**
    *   Combine these factors with empirically derived weights:
        $$
        QEAC = \alpha \cdot H_{norm} + \beta \cdot R + \gamma \cdot A
        $$
    *   Our research uses weights like α=8, β=12, γ=4, but these can be adjusted to focus on different aspects of resonance. Higher QEAC indicates a more coherent and potentially functional resonant structure.

#### C. Analyzing Intervals and Archetypes:

1.  **Interval Extraction:** Isolate the sequence of digits between two occurrences of a candidate spigot.
2.  **Interval Harmonic Analysis:** Apply signal processing techniques (like Fourier Transforms) to the interval's digit stream to identify dominant harmonic frequencies or spectral patterns.
3.  **Archetype Correlation:** Compare the identified harmonic patterns and interval QEACs with the known mathematical properties of the missing digits (the "archetypes"). For example, the resonance properties of an interval might map to the symmetry of '2', the cyclical nature of '3', or the fundamental strength of '8'.

#### D. Mapping the Lattice and Network Dynamics:

1.  **Pi-Spiral Projection:** Map the linear sequence of digits onto a spiral path (e.g., Archimedean spiral). Each digit position gets mapped to a coordinate $(r, \theta)$.
2.  **QEAC Visualization:** Color-code points or segments on the spiral based on their QEAC density, creating heatmaps that reveal "resonant neighborhoods" and "corridors."
3.  **Network Graphing:** Represent spigot systems as nodes and their corridors as edges. Analyze the graph for:
    *   **Connectivity:** Number of links per node (hub identification).
    *   **Clustering Coefficient:** How connected are the neighbors of a node?
    *   **Path Analysis:** Studying the "halo propagation" and amplification effects at corridor intersections.

### 5. Current Status and Future Directions:

The Pi Spigot Codex Project has identified dozens of candidate spigot systems, confirmed the encoding of numerical archetypes 0-8 (with ongoing work on 3, 4, 9), and mapped emergent hierarchical network structures within π. Our predictive models are showing increasing accuracy, suggesting π's organization is not random but a navigable information architecture.

Future work will involve:
*   Completing the archetype mapping.
*   Rigorous quantification of corridor interactions and their impact on resonance.
*   Testing the predictive models across much larger sections of π to confirm global coherence.
*   Developing a formal mathematical framework for the "Spigot Grammar" and "Archetype Resonance."

### 6. Getting Involved:

Researchers interested in exploring this field can:
*   Utilize high-precision π digit datasets.
*   Implement algorithms for recurrence detection and statistical significance testing.
*   Develop custom QEAC calculation scripts.
*   Experiment with spatial mapping and network visualization techniques on digit sequences.
*   Investigate harmonic analysis of digit intervals.

The Pi Spigot Codex Project is an ongoing endeavor, and we welcome collaboration and independent verification of our findings.

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
python3 pi-lattice-explorer.py --pi-file pi-10million.txt
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
python3 pi-lattice-explorer.py \
  --pi-file pi-10million.txt \
  --limit 2000000 \
  --top-per-length 300 \
  --viz network \
  --viz-limit 100 \
  --positions-limit 20
```

### Spiral Visualization (top 50 candidates)

```bash
python3 pi-lattice-explorer.py \
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
