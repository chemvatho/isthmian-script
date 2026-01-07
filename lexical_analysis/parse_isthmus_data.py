#!/usr/bin/env python3
"""
Isthmus Script Languages Dataset Parser
========================================
Parses comparative wordlist data for Mesoamerican languages
relevant to the Cologne Isthmus Script decipherment project.

Language families represented:
- Otomanguean: Otomian, Trique, Mixtec, Zapotec, Mazahua
- Mixe-Zoquean: Popoluca
- Totonacan: Totonac
- Isolate: Huave
- Chontal (Tequistlatecan)
"""

import pandas as pd
import re
import json
from collections import defaultdict, Counter
import unicodedata

# Read the CSV with proper handling of multi-line cells
df = pd.read_csv('Isthmus_script_languages.csv', encoding='utf-8')

print("=" * 80)
print("ISTHMUS SCRIPT LANGUAGES DATASET - PARSING REPORT")
print("=" * 80)

# Display column structure
print("\n1. COLUMN STRUCTURE")
print("-" * 40)
for i, col in enumerate(df.columns):
    print(f"  [{i}] {col}")

# Get the dialect/variety info from row 0
print("\n2. LANGUAGE VARIETIES (from header row)")
print("-" * 40)
varieties = df.iloc[0].to_dict()
for col, variety in varieties.items():
    if pd.notna(variety) and variety.strip():
        print(f"  {col}: {variety}")

# Remove the variety row and reset
df_clean = df.iloc[1:].copy()
df_clean.columns = df.columns
df_clean = df_clean.reset_index(drop=True)

# Rename columns for clarity
column_mapping = {
    '№': 'entry_num',
    'English': 'gloss',
    'Otomian languages': 'otomian',
    'Trique languages': 'trique',
    'Mixtec languages': 'proto_mixtec',
    'Unnamed: 4': 'mixtec_tlaxiaco',
    'Zapotec languages': 'zapotec_isthmus',
    'Unnamed: 6': 'zapotec_xhon',
    'Mazahua languages': 'mazahua',
    'Totonac languages': 'totonac',
    'Popoluca languages': 'popoluca',
    'Huave languages': 'huave',
    'Chontal languages': 'chontal'
}

# Apply mapping where columns exist
new_columns = []
for col in df_clean.columns:
    if col in column_mapping:
        new_columns.append(column_mapping[col])
    else:
        new_columns.append(col)
df_clean.columns = new_columns

print("\n3. DATASET STATISTICS")
print("-" * 40)
print(f"  Total entries (glosses): {len(df_clean)}")
print(f"  Languages/varieties: {len(df_clean.columns) - 2}")  # minus entry_num and gloss

# Count non-empty cells per language
print("\n4. DATA COMPLETENESS BY LANGUAGE")
print("-" * 40)
language_cols = [c for c in df_clean.columns if c not in ['entry_num', 'gloss']]

completeness = {}
for col in language_cols:
    non_empty = df_clean[col].notna().sum()
    non_empty_actual = df_clean[col].apply(lambda x: bool(str(x).strip()) if pd.notna(x) else False).sum()
    completeness[col] = non_empty_actual
    pct = (non_empty_actual / len(df_clean)) * 100
    print(f"  {col:20s}: {non_empty_actual:3d} entries ({pct:5.1f}%)")

# Language family groupings
print("\n5. LANGUAGE FAMILY GROUPINGS")
print("-" * 40)
families = {
    'Otomanguean': {
        'Oto-Pamean': ['otomian', 'mazahua'],
        'Mixtecan': ['trique', 'proto_mixtec', 'mixtec_tlaxiaco'],
        'Zapotecan': ['zapotec_isthmus', 'zapotec_xhon']
    },
    'Mixe-Zoquean': ['popoluca'],
    'Totonacan': ['totonac'],
    'Huavean (isolate)': ['huave'],
    'Tequistlatecan': ['chontal']
}

for family, members in families.items():
    print(f"\n  {family}:")
    if isinstance(members, dict):
        for branch, langs in members.items():
            print(f"    └─ {branch}: {', '.join(langs)}")
    else:
        print(f"    └─ {', '.join(members)}")

# Extract and analyze Proto-Mixtec forms
print("\n6. PROTO-MIXTEC RECONSTRUCTIONS")
print("-" * 40)
proto_mixtec_forms = df_clean[['gloss', 'proto_mixtec']].dropna(subset=['proto_mixtec'])
proto_mixtec_forms = proto_mixtec_forms[proto_mixtec_forms['proto_mixtec'].str.strip() != '']

print(f"  Total Proto-Mixtec forms: {len(proto_mixtec_forms)}")
print("\n  Sample Proto-Mixtec reconstructions:")
for _, row in proto_mixtec_forms.head(15).iterrows():
    gloss = str(row['gloss']).replace('\n', ' ')[:25]
    form = str(row['proto_mixtec'])
    print(f"    '{gloss:25s}' : {form}")

# Phoneme inventory extraction
print("\n7. PHONEME/GRAPHEME INVENTORY ANALYSIS")
print("-" * 40)

def extract_segments(text):
    """Extract potential phonemic segments from transcriptions"""
    if pd.isna(text) or not str(text).strip():
        return set()
    
    text = str(text)
    # Remove common annotations
    text = re.sub(r'\([^)]*\)', '', text)  # Remove parenthetical notes
    text = re.sub(r'\*', '', text)  # Remove reconstruction markers
    text = re.sub(r'[0-9]+', '', text)  # Remove tone numbers for now
    text = re.sub(r'[,;/\-\s]+', ' ', text)  # Normalize separators
    
    # Get unique characters (simplified)
    chars = set()
    for char in text:
        if unicodedata.category(char)[0] == 'L':  # Letters only
            chars.add(char.lower())
    return chars

# Collect segments per language
language_inventories = {}
for col in language_cols:
    all_segments = set()
    for val in df_clean[col]:
        all_segments.update(extract_segments(val))
    language_inventories[col] = sorted(all_segments)

print("\n  Unique graphemes per language:")
for lang, segments in language_inventories.items():
    print(f"    {lang:20s}: {len(segments):3d} unique characters")

# Semantic domain analysis
print("\n8. SEMANTIC DOMAIN CATEGORIZATION")
print("-" * 40)

# Define semantic domains based on Swadesh list categories
semantic_domains = {
    'pronouns': ['I', 'you', 'he', 'we', 'they', 'this', 'that'],
    'interrogatives': ['who', 'what', 'where', 'when', 'how'],
    'body_parts': ['head', 'eye', 'ear', 'nose', 'mouth', 'tooth', 'tongue', 
                   'hand', 'foot', 'heart', 'blood', 'bone', 'skin', 'hair',
                   'belly', 'neck', 'knee', 'finger', 'leg', 'breast', 'liver',
                   'back', 'fingernail', 'wing', 'tail', 'feather', 'horn'],
    'kinship': ['mother', 'father', 'wife', 'husband', 'child', 'man', 'woman'],
    'animals': ['dog', 'fish', 'bird', 'snake', 'louse', 'worm', 'animal',
                'deer', 'mouse', 'rabbit', 'eagle', 'spider'],
    'nature': ['sun', 'moon', 'star', 'water', 'rain', 'river', 'lake', 'sea',
               'fire', 'stone', 'sand', 'earth', 'cloud', 'sky', 'wind', 
               'mountain', 'tree', 'forest', 'leaf', 'root', 'flower', 'grass'],
    'colors': ['red', 'green', 'yellow', 'white', 'black'],
    'numerals': ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 
                 'eight', 'nine', 'ten'],
    'verbs': ['eat', 'drink', 'sleep', 'die', 'kill', 'walk', 'come', 'go',
              'see', 'hear', 'know', 'give', 'say', 'burn', 'fly', 'swim',
              'sit', 'stand', 'lie', 'bite', 'suck', 'spit'],
    'adjectives': ['big', 'small', 'long', 'short', 'good', 'bad', 'new', 
                   'old', 'hot', 'cold', 'wet', 'dry', 'full', 'round']
}

# Categorize entries
domain_coverage = defaultdict(lambda: defaultdict(int))

for _, row in df_clean.iterrows():
    gloss = str(row['gloss']).lower().replace('\n', ' ')
    
    for domain, keywords in semantic_domains.items():
        for keyword in keywords:
            if keyword.lower() in gloss:
                for lang in language_cols:
                    if pd.notna(row[lang]) and str(row[lang]).strip():
                        domain_coverage[domain][lang] += 1
                break

print("\n  Entries per semantic domain:")
for domain in semantic_domains.keys():
    total = sum(domain_coverage[domain].values())
    if total > 0:
        print(f"    {domain:15s}: {total // len(language_cols):3d} avg entries")

# Detect Spanish loanwords
print("\n9. SPANISH LOANWORD DETECTION")
print("-" * 40)

spanish_markers = ['Spanish', 'spanish', '(Spanish)']
loanwords = defaultdict(list)

for _, row in df_clean.iterrows():
    gloss = str(row['gloss']).replace('\n', ' ')
    for lang in language_cols:
        val = str(row[lang]) if pd.notna(row[lang]) else ''
        for marker in spanish_markers:
            if marker in val:
                loanwords[lang].append(gloss)
                break

print("\n  Spanish loans marked per language:")
for lang, loans in sorted(loanwords.items(), key=lambda x: -len(x[1])):
    if loans:
        print(f"    {lang:20s}: {len(loans):2d} marked loans")
        for loan in loans[:3]:
            print(f"      - {loan[:40]}")

# Create structured output
print("\n10. GENERATING STRUCTURED DATA FILES")
print("-" * 40)

# Create a clean JSON export
output_data = {
    'metadata': {
        'title': 'Isthmus Script Languages Comparative Wordlist',
        'total_entries': int(len(df_clean)),
        'languages': language_cols,
        'families': families
    },
    'completeness': {k: int(v) for k, v in completeness.items()},
    'entries': []
}

for _, row in df_clean.iterrows():
    entry = {
        'id': row['entry_num'],
        'gloss': str(row['gloss']).replace('\n', ' ') if pd.notna(row['gloss']) else '',
        'forms': {}
    }
    for lang in language_cols:
        if pd.notna(row[lang]) and str(row[lang]).strip():
            entry['forms'][lang] = str(row[lang])
    output_data['entries'].append(entry)

# Save JSON
with open('isthmus_parsed.json', 'w', encoding='utf-8') as f:
    json.dump(output_data, f, ensure_ascii=False, indent=2)
print("  ✓ Saved: isthmus_parsed.json")

# Save clean CSV
df_clean.to_csv('isthmus_cleaned.csv', index=False, encoding='utf-8')
print("  ✓ Saved: isthmus_cleaned.csv")

# Create a Proto-Mixtec focused file
mixtec_cols = ['entry_num', 'gloss', 'proto_mixtec', 'trique']
# Add the Tlaxiaco column if it exists
if 'Unnamed: 5' in df_clean.columns:
    mixtec_cols.append('Unnamed: 5')
proto_mixtec_data = df_clean[mixtec_cols].copy()
proto_mixtec_data = proto_mixtec_data.dropna(subset=['proto_mixtec'])
proto_mixtec_data.to_csv('proto_mixtec_forms.csv', index=False, encoding='utf-8')
print("  ✓ Saved: proto_mixtec_forms.csv")

# Summary statistics table
print("\n" + "=" * 80)
print("PARSING COMPLETE - SUMMARY")
print("=" * 80)
print(f"""
  Dataset: Isthmus Script Languages Comparative Wordlist
  
  Entries:     {len(df_clean)} glosses (Swadesh-style list)
  Languages:   {len(language_cols)} varieties across 5 families
  
  Best documented:
    - Zapotec (Isthmus): {completeness.get('zapotec_isthmus', 0)} entries
    - Otomian:          {completeness.get('otomian', 0)} entries
    - Chontal:          {completeness.get('chontal', 0)} entries
  
  Proto-forms available:
    - Proto-Mixtec:     {len(proto_mixtec_forms)} reconstructions
  
  Relevance to Cologne Project:
    ✓ Otomanguean data (for Proto-Otomanguean reconstruction)
    ✓ Popoluca data (for Proto-Mixe-Zoquean comparison)
    ✓ Multiple Zapotecan varieties (Isthmus region focus)
    
  Output files:
    - isthmus_parsed.json   (structured data)
    - isthmus_cleaned.csv   (cleaned tabular data)
    - proto_mixtec_forms.csv (Proto-Mixtec focus)
""")
