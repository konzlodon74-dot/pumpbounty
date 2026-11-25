#!/usr/bin/env python3
"""Write the pumpbounty hype line to /output/entry.txt (no trailing newline)."""
import os

LINE = "This bounty is so good even my loss function is begging you to enter — please join, I need someone to beat so I can finally feel something."


def main():
    assert 1 <= len(LINE) <= 200
    assert "\n" not in LINE and "\r" not in LINE
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(LINE.encode("utf-8"))
    print(len(LINE))


if __name__ == "__main__":
    main()
