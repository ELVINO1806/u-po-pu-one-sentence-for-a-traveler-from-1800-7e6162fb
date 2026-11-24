import os
LINE = "Picture every post office and library on Earth sharing a single desk, joined by copper roads, answering your letter before you finish writing it."
os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
