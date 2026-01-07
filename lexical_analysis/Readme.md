# Isthmus Script Languages Dataset Analysis Report

**For the Cologne University Isthmus Script Decipherment Project**

---

## Executive Summary

This report presents a comprehensive parsing and analysis of the comparative wordlist dataset containing lexical data from 11 language varieties across 5 Mesoamerican language families. The dataset is directly relevant to the VolkswagenStiftung-funded project "Exploring an unknown language in an unknown writing system: The Isthmus script."

## Dataset Overview

| Metric | Value |
|--------|-------|
| **Total entries** | 240 glosses (extended Swadesh list) |
| **Language varieties** | 11 |
| **Language families** | 5 |
| **Proto-forms available** | 72 (Proto-Mixtec) |

## Language Family Structure

```
Otomanguean
├── Oto-Pamean
│   ├── Otomian (various) ............ 99.6% complete
│   └── Mazahua (Central) ............ 37.5% complete
├── Mixtecan
│   ├── Proto-Mixtec ................. 30.0% (reconstructions)
│   ├── Trique (San Juan Copala) ..... 86.2% complete
│   └── Mixtec (Tlaxiaco/Putla) ...... 95.4% complete
└── Zapotecan
    ├── Zapotec (Isthmus) ............ 91.7% complete
    └── Zapotec (Xhon) ............... 67.5% complete

Mixe-Zoquean
└── Popoluca (various) ............... 54.6% complete

Totonacan
└── Totonac (various) ................ 77.1% complete

Huavean (isolate)
└── Huave (various) .................. 62.1% complete

Tequistlatecan
└── Chontal (various) ................ 94.2% complete
```

![Language Family Structure Summary](https://github.com/chemvatho/isthmian-script/blob/main/lexical_analysis/analysis_summary_figure.png)



## Phoneme Inventories

### Proto-Mixtec Reconstruction Phonemes
Based on 72 attested reconstructions in the dataset:

| Segment | Frequency | Type |
|---------|-----------|------|
| *ʔ | 46 | Glottal stop |
| *u | 31 | Vowel |
| *y | 28 | Consonant |
| *ɨ | 27 | High central vowel |
| *w | 22 | Consonant |
| *e | 22 | Vowel |
| *k | 18 | Consonant |
| *t | 17 | Consonant |

### Sound Correspondences: Proto-Mixtec → Daughter Languages

| Proto-Mixtec | Tlaxiaco/Putla Mixtec | Notes |
|--------------|----------------------|-------|
| *k | k (78%), n, ' | Regular retention |
| *t | t (53%), ch, l | Occasional affrication |
| *w | v (36%), u (23%) | Spirantization common |
| *y | y (32%), ñ (18%) | Nasalization pattern |
| *ʔ | ' (76%) | Regular retention |
| *ɨ | ɨ (57%), u, i | Some merger |

## Cross-Family Sound Correspondences

### Otomian ↔ Isthmus Zapotec
| Pattern | Count | Example gloss |
|---------|-------|---------------|
| n : n | 10 | - |
| t : r | 9 | - |
| j : r | 7 | - |
| h : r | 7 | - |

### Otomian ↔ Mazahua (same branch)
| Pattern | Count | Notes |
|---------|-------|-------|
| h : j | 6 | Regular correspondence |
| ts : s | 4 | Deaffrication in Mazahua |
| x : x | 4 | Retention |
| d : nd | 4 | Prenasalization |

## Semantic Domain Coverage

| Domain | Entries | Avg forms/entry | Reconstruction utility |
|--------|---------|-----------------|----------------------|
| Animals | 5 | 10.2 | ★★★★★ Excellent |
| Nature | 10 | 9.7 | ★★★★★ Excellent |
| Kinship | 7 | 9.7 | ★★★★★ Excellent |
| Colors | 5 | 9.4 | ★★★★☆ Very good |
| Numerals | 15 | 9.3 | ★★★★☆ Very good |
| Body parts | 16 | 9.1 | ★★★★☆ Very good |
| Actions | 15 | 8.5 | ★★★★☆ Very good |
| Basic vocabulary | 20 | 8.0 | ★★★★☆ Very good |

## Spanish Loanwords Detected

Evidence of post-contact borrowing:

| Language | Loans marked | Examples |
|----------|-------------|----------|
| Isthmus Zapotec | 5 | lake, ice, green, needle |
| Chontal | 4 | some, eagle, body |
| Popoluca | 3 | animal, bad, needle |
| Otomian | 1 | grass |

## Relevance to Cologne Project Tasks

### For Proto-Otomanguean Reconstruction
- ✅ 72 Proto-Mixtec forms provide calibration data
- ✅ Otomian data (99.6%) enables Oto-Pamean comparison
- ✅ Zapotecan varieties allow internal reconstruction
- ⚠️ Mazahua gaps limit full Oto-Pamean picture

### For Proto-Mixe-Zoquean Reconstruction
- ✅ Popoluca data available (131 entries)
- ⚠️ Single variety limits internal comparison
- 📌 Recommend cross-referencing with Wichmann (1995)

### For Proto-Huastecan Reconstruction
- ❌ No Huastecan data in this dataset
- 📌 Requires separate data collection (see Norcliffe 2003)

## Output Files Generated

| File | Description |
|------|-------------|
| `isthmus_parsed.json` | Complete structured dataset with metadata |
| `isthmus_cleaned.csv` | Cleaned tabular format |
| `proto_mixtec_analysis.csv` | Proto-Mixtec forms with daughter reflexes |
| `cognate_candidates.csv` | Cross-family similarity candidates |
| `linguistic_analysis.json` | Phoneme inventories and statistics |

## Recommended Next Steps

1. **Expand cognate identification**: Cross-reference with Kaufman's OMED (2021) for Proto-Otomanguean
2. **Mixe-Zoquean comparison**: Match Popoluca forms against Wichmann's ~600 Proto-Mixe-Zoquean reconstructions
3. **Formal correspondence tables**: Build publishable sound correspondence charts
4. **Gap filling**: Seek additional Mazahua and Popoluca data to strengthen reconstruction base

---

*Analysis conducted: January 2026*
*Dataset source: Isthmus_script_languages.csv*
