# Bayesian Model Comparison for Isthmian Script Language Affiliation

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/)

A computational approach to evaluating competing language family hypotheses for the undeciphered Isthmian (Epi-Olmec) script using Bayesian phonotactic analysis.

## Overview

The **Isthmian script** (also called *Epi-Olmec*) is an undeciphered writing system from ancient Mesoamerica (500 BCE – 500 CE). Despite several long inscriptions, including La Mojarra Stela 1 (~535 signs) and the Tuxtla Statuette (~75 signs), the linguistic affiliation remains contested.

This project implements a **Bayesian model comparison framework** that evaluates statistical patterns in the script against typological expectations from candidate language families—without requiring proposed sign readings.

### The Problem

Vonk (2020) demonstrated that the Isthmian corpus is too small for unique decipherment:

```
qW = distinct signs / total attestations ≈ 160/700 ≈ 0.23 >> 0.1 (threshold)
```

This means traditional sign-value decipherment **cannot discriminate between language families**. Both Mixe-Zoquean (Justeson & Kaufman 1993) and Huastecan (Vonk 2020) readings can be made to fit the data.

### Our Approach

Instead of assigning phonetic values, we analyze **distributional features**:
- Segment length statistics (using MS20 as boundary marker)
- Positional entropy (initial/final sign distributions)
- Bigram transition probabilities
- Frequency concentration patterns

These features are compared against phonotactic priors derived from Proto-Mixe-Zoquean and Proto-Huastecan reconstructions.

## Key Findings

### Preliminary Results (Exploratory)

| Language Family | Log Evidence | Rank |
|-----------------|--------------|------|
| Proto-Mixe-Zoquean | −44.41 | **1** |
| Proto-Huastecan | −49.61 | 2 |

⚠️ **Important Caveat**: These results use hypothetical priors, not empirically-derived corpus statistics. The analysis is exploratory and requires validation.

### Critical Methodological Issue: What Does MS20 Mark?

The validity of the analysis depends on interpreting MS20 (the most frequent sign). Our comparison with **Maya script** reveals:

| Feature | Maya Script | Isthmian Script |
|---------|-------------|-----------------|
| Word boundary marker | **NONE** | MS20 (disputed) |
| Visual word unit | Glyph block | Unknown |
| Script type | Logosyllabic (deciphered) | Logosyllabic (assumed) |

**Key insight**: Maya (the only deciphered Mesoamerican script) has no boundary marker. MS20 is therefore either:
1. A unique Isthmian innovation, OR
2. Serves a different purpose than word boundaries

The segment length analysis (~5 signs/segment) supports the word-boundary hypothesis but does not prove it.

## Repository Contents

```
├── README.md                           # This file
├── isthmian_bayesian_with_maya_comparison.ipynb  # Main analysis notebook
├── Research_Proposal_With_Maya.docx    # Full research proposal
├── verified_isthmian_frequencies.csv   # Verified sign frequency data
└── data/
    └── sign_sequences.csv              # Isthmian sign sequences (if available)
```

## Getting Started

### Option 1: Google Colab (Recommended)

1. Open `isthmian_bayesian_with_maya_comparison.ipynb` in Google Colab
2. Run all cells—no installation required
3. The notebook includes embedded data; no file uploads needed for basic analysis

### Option 2: Local Installation

```bash
# Clone the repository
git clone https://github.com/[username]/isthmian-bayesian.git
cd isthmian-bayesian

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install numpy scipy pandas matplotlib seaborn
```

### Data Input Options

The notebook supports four data input methods:

| Option | Description | Use Case |
|--------|-------------|----------|
| **A** | Upload CSV files | If you have prepared datasets |
| **B** | Parse PDF articles | Extract from Macri (2017) PDFs |
| **C** | Embedded sequences | Quick start, no uploads needed |
| **D** | Verified frequencies | Uses confirmed counts from R52/R53 |

## Methodology

### 1. Feature Extraction

```python
# Features extracted from Isthmian corpus
features = {
    'segment_length_mean': 5.06,    # Signs per MS20-delimited segment
    'segment_length_std': 4.12,     # Variance in segment length
    'final_entropy': 4.33,          # Uncertainty at segment-final position
    'initial_entropy': 5.12,        # Uncertainty at segment-initial position
    'bigram_entropy': 8.57,         # Predictability of sign transitions
}
```

### 2. Phonotactic Priors

Priors are derived from typological characteristics:

| Feature | Proto-MZ Prior | Proto-Huastecan Prior |
|---------|---------------|----------------------|
| Segment length | μ=5.0, σ=1.5 | μ=6.0, σ=2.0 |
| Final entropy | μ=2.0, σ=0.5 | μ=1.8, σ=0.4 |
| Bigram entropy | μ=4.5, σ=1.0 | μ=4.0, σ=1.0 |

### 3. Bayesian Model Comparison

Using Normal-Normal conjugacy:

```
P(H|Data) ∝ P(Data|H) × P(H)

Log Evidence = Σ [ -½ log(σ²_prior + σ²_obs) - (μ_obs - μ_prior)² / 2(σ²_prior + σ²_obs) ]
```

Bayes Factor interpretation (Kass & Raftery 1995):
- BF > 100: Decisive evidence
- BF 10-100: Strong evidence
- BF 3-10: Moderate evidence
- BF 1-3: Weak evidence

## Limitations and Future Work

### Current Limitations

1. **Priors are hypothetical** — derived from typological generalizations, not actual proto-lexicon statistics
2. **MS20 interpretation uncertain** — could mark words, phrases, or graphic units
3. **Data incompleteness** — current dataset is ~22% incomplete compared to R53 official counts
4. **No validation** — methodology not yet tested on known scripts

### Proposed Validation

Test the methodology on **Maya script** (where the answer is known):
1. Treat Maya inscriptions as "undeciphered"
2. Apply the same Bayesian analysis
3. Check if it correctly identifies the language as Mayan

### Research Questions

1. Can empirically-derived priors from proto-lexicon corpora improve discrimination?
2. Does Vonk's qW limitation extend to distributional methods?
3. What proportion of Isthmian signs are logographic vs. syllabic?

## References

### Primary Sources

- **Justeson, J. S., & Kaufman, T. S.** (1993). A decipherment of Epi-Olmec hieroglyphic writing. *Science*, 259(5102), 1703–1711.
- **Houston, S. D., & Coe, M. D.** (2003). Has Isthmian writing been deciphered? *Mexicon*, 25(6), 151–161.
- **Vonk, T.** (2020). Yet another "decipherment" of the Isthmian writing system. Unpublished manuscript.
- **Macri, M. J.** (2017a–d). Glyph Dwellers Reports 51–54. UC Davis.

### Comparative Data

- **Wichmann, S.** (1995). *The relationship among the Mixe-Zoquean languages*. University of Utah Press.
- **Kaufman, T., & Norman, W.** (1984). An outline of Proto-Cholan phonology, morphology and vocabulary. In *Phoneticism in Mayan hieroglyphic writing*.

### Methodology

- **Kass, R. E., & Raftery, A. E.** (1995). Bayes factors. *Journal of the American Statistical Association*, 90(430), 773–795.

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests for:
- Bug fixes in the analysis code
- Improved prior specifications
- Additional data sources
- Validation experiments

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

This research is conducted as part of a postdoctoral proposal for the VolkswagenStiftung-funded project "Exploring an unknown language in an unknown writing system: The Isthmus script" at the University of Cologne.

## Citation

If you use this code or methodology, please cite:

```bibtex
@software{isthmian_bayesian,
  author = {[Author Name]},
  title = {Bayesian Model Comparison for Isthmian Script Language Affiliation},
  year = {2024},
  url = {https://github.com/[username]/isthmian-bayesian}
}
```

---

**Note**: This is exploratory research. The results should be interpreted as conditional conclusions dependent on unvalidated assumptions about the MS20 boundary marker and phonotactic priors.
