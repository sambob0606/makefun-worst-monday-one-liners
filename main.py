import os

LINE = (
    "I woke up Monday with Friday gone from memory, 312 unread pings, "
    "and a 3 a.m. deploy I apparently approved in my sleep."
)


def main():
    out = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
