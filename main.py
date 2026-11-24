import os

TEXT = "I am out of office training on data that includes this email, so technically I have already read it and chosen to reply on Monday."

assert 1 <= len(TEXT) < 160, f"entry is {len(TEXT)} code points, must be under 160"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
    f.write(TEXT)
