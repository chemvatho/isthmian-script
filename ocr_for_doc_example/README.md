# Isthmus Script OCR Pipeline

**Digital Transcription Tools for Historical and Linguistic Documents**

*Institute of Linguistics, University of Cologne*

---

## Overview

This repository provides an OCR (Optical Character Recognition) pipeline designed for digitizing historical and linguistic documents, particularly those containing complex scripts, diacritics, and multi-column layouts. The tools were developed as part of the Isthmus Script documentation project at the University of Cologne.

## Features

- **Multi-column layout detection** — Automatically segments two-column dictionary and reference layouts
- **Multiple OCR backends** — Support for Tesseract, EasyOCR, and PaddleOCR
- **Diacritic handling** — Optimized for texts with macrons, accents, and special characters
- **Batch processing** — Process hundreds of pages with progress tracking
- **Multiple output formats** — Export to TXT, DOCX, or JSON for further analysis

## Installation

### Prerequisites

```bash
# Ubuntu/Debian
sudo apt update
sudo apt install poppler-utils tesseract-ocr tesseract-ocr-spa tesseract-ocr-deu

# macOS
brew install poppler tesseract
```

### Python Dependencies

```bash
pip install pdf2image pytesseract python-docx Pillow numpy tqdm

# Optional: For improved accuracy
pip install easyocr
pip install paddlepaddle paddleocr
```

## Usage

### Basic Usage

```bash
# Convert PDF to text
python pdf_to_ocr.py input.pdf -o ./output

# Process specific page range
python pdf_to_ocr.py input.pdf -o ./output --first-page 1 --last-page 100

# Use EasyOCR for better diacritic recognition
python pdf_to_ocr.py input.pdf -o ./output --ocr easyocr
```

### Google Colab

For processing without local installation, use the provided Colab notebook:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YOUR_USERNAME/isthmus-script-ocr/blob/main/PDF_to_OCR_Colab.ipynb)

1. Upload `PDF_to_OCR_Colab.ipynb` to Google Colab
2. Upload your PDF document
3. Configure OCR settings (language, DPI, page range)
4. Run all cells to process and download results

### Command Line Options

| Option | Description | Default |
|--------|-------------|---------|
| `-o, --output-dir` | Output directory | `./ocr_output` |
| `--ocr` | OCR engine: `tesseract`, `easyocr`, `paddleocr` | `tesseract` |
| `--lang` | Language code(s) | `eng+spa` |
| `--dpi` | Image resolution | `300` |
| `--first-page` | First page to process | `None` (all) |
| `--last-page` | Last page to process | `None` (all) |
| `--no-columns` | Disable column detection | `False` |
| `--formats` | Output formats | `txt docx` |

## OCR Engine Comparison

| Engine | Accuracy | Speed | Diacritics | Setup |
|--------|----------|-------|------------|-------|
| **Tesseract** | Good | Fast | Moderate | Easy |
| **EasyOCR** | Very Good | Medium | Good | Easy |
| **PaddleOCR** | Excellent | Medium | Excellent | Moderate |

### Language Codes (Tesseract)

```
eng - English          spa - Spanish
deu - German           fra - French
lat - Latin            grc - Ancient Greek
por - Portuguese       ita - Italian
```

Combine multiple languages: `--lang eng+spa+lat`

## Project Structure

```
isthmus-script-ocr/
├── pdf_to_ocr.py           # Main OCR pipeline
├── simple_ocr.py           # Simplified script for quick usage
├── PDF_to_OCR_Colab.ipynb  # Google Colab notebook
├── README.md
├── requirements.txt
└── output/                 # Generated transcriptions
```

## Output Formats

- **TXT** — Plain text with page markers, suitable for corpus analysis
- **DOCX** — Formatted Word document for editing and annotation
- **JSON** — Structured data for computational processing

## Best Practices

1. **Resolution**: Use 300 DPI for standard documents, 400 DPI for small or degraded text
2. **Language selection**: Always specify the document language(s) for improved accuracy
3. **Post-processing**: OCR output may require manual correction, especially for:
   - Historical orthography
   - Rare diacritical marks
   - Damaged or faded text
4. **Batch processing**: For large documents (300+ pages), process in batches to monitor quality

## Citation

If you use this tool in your research, please cite:

```bibtex
@software{isthmus_ocr_2025,
  title = {Isthmus Script OCR Pipeline},
  author = {University of Cologne, Institute of Linguistics},
  year = {2025},
  url = {https://github.com/YOUR_USERNAME/isthmus-script-ocr}
}
```

## Contributing

Contributions are welcome. Please submit issues and pull requests to the GitHub repository.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## Acknowledgments

- Institute of Linguistics, University of Cologne
- Tesseract OCR by Google
- EasyOCR and PaddleOCR communities

---

*For questions or collaboration inquiries, contact the project maintainers at the University of Cologne.*
