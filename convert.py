import sys
from tables import qtd, dtq

if len(sys.argv) > 1:
    text: str = " ".join(sys.argv[2:]) if sys.argv[1] == "-dtq" else " ".join(sys.argv[2:]) if sys.argv[1] == "-qtd" else " ".join(sys.argv[1:])
    layout = qtd if sys.argv[1] == "-qtd" else dtq
    text = "".join(layout.get(c, c) for c in text)
else:
    text = "usage: convert.py [-qtd|-dtq] <text>"

print(text)