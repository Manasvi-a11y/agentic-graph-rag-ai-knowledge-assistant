from pathlib import Path
from pypdf import PdfReader

files = list(Path("knowledge_base").rglob("*.pdf"))

print(f"Found {len(files)} PDF files\n")

bad = []

for file in files:
    try:
        reader = PdfReader(str(file))
        pages = len(reader.pages)

        print(f"OK    : {file} ({pages} pages)")

    except Exception as e:
        print(f"ERROR : {file}")
        print(f"        {e}")
        bad.append(file)

print("\n==============================")
print(f"Total PDFs : {len(files)}")
print(f"Bad PDFs   : {len(bad)}")
print("==============================")

for file in bad:
    print("BAD:", file)