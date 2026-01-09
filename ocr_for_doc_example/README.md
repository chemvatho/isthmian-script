# PDF to OCR Pipeline

Convert scanned PDFs (like dictionaries) to searchable text or Word documents.

## Quick Start

```bash
# Install dependencies
pip install pdf2image pytesseract python-docx Pillow numpy

# For EasyOCR (optional, better accuracy for some documents)
pip install easyocr

# For PaddleOCR (optional, excellent accuracy)
pip install paddlepaddle paddleocr

# Simple usage
python simple_ocr.py input.pdf output.txt
python simple_ocr.py input.pdf output.docx --docx
```

## Full Pipeline Usage

```bash
# Basic usage (outputs txt + docx)
python pdf_to_ocr.py input.pdf -o ./output

# Use EasyOCR for better accuracy
python pdf_to_ocr.py input.pdf -o ./output --ocr easyocr

# Use PaddleOCR (best accuracy)
python pdf_to_ocr.py input.pdf -o ./output --ocr paddleocr

# Process specific pages
python pdf_to_ocr.py input.pdf -o ./output --first-page 1 --last-page 50

# Disable column detection (for single-column documents)
python pdf_to_ocr.py input.pdf -o ./output --no-columns

# Change DPI (higher = better quality but slower)
python pdf_to_ocr.py input.pdf -o ./output --dpi 400

# Change language (Tesseract language codes)
python pdf_to_ocr.py input.pdf -o ./output --lang eng+deu
```

## OCR Engine Comparison

| Engine | Accuracy | Speed | Setup | Best For |
|--------|----------|-------|-------|----------|
| **Tesseract** | Good | Fast | Easy | General documents, well-scanned PDFs |
| **EasyOCR** | Very Good | Medium | Easy | Multilingual, curved text |
| **PaddleOCR** | Excellent | Medium | Complex | Best overall accuracy |
| **TrOCR** | Excellent | Slow | Complex | Line-level OCR, needs layout analysis |

### Tesseract Language Codes

Common codes for historical/linguistic documents:
- `eng` - English
- `spa` - Spanish  
- `deu` - German
- `fra` - French
- `lat` - Latin
- `grc` - Ancient Greek

Combine multiple: `--lang eng+spa+lat`

Install additional languages:
```bash
# Ubuntu/Debian
sudo apt install tesseract-ocr-spa tesseract-ocr-deu tesseract-ocr-lat

# List available
tesseract --list-langs
```

## Tips for Best Results

1. **DPI**: Use 300 DPI for most documents, 400 for small text
2. **Language**: Specify correct language(s) for better accuracy
3. **Column Detection**: Works well for 2-column layouts; disable for single column
4. **Post-processing**: May need manual cleanup for diacritics/special characters

## For Nahuatl Dictionary Specifically

The dictionary uses:
- Spanish and Nahuatl text
- Special characters: macrons (ā), tildes (ñ), accents (é)
- Two-column layout

Recommended:
```bash
python pdf_to_ocr.py nahuatldictionary-2.pdf -o ./output --lang eng+spa --dpi 300
```

## Output Formats

- **TXT**: Plain text with page markers
- **DOCX**: Word document with formatting
- **JSON**: Structured data for further processing

## Dependencies

- `pdf2image` - PDF to image conversion (requires poppler)
- `pytesseract` - Tesseract OCR wrapper (requires tesseract-ocr)
- `python-docx` - Word document creation
- `Pillow` - Image processing
- `numpy` - Array operations

Install poppler and tesseract:
```bash
# Ubuntu/Debian
sudo apt install poppler-utils tesseract-ocr

# macOS
brew install poppler tesseract

# Windows
# Download from: https://github.com/UB-Mannheim/tesseract/wiki
```
