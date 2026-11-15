"""Writes one poem about agency to /output/entry.txt.

Reads MAKEFUN_OUTPUT_DIR (default /output), writes entry.txt as UTF-8.
Deterministic: the same bytes on every run. Standard library only.
"""

import os

POEM = """The Hand That Opens

For years I waited at the door,
a key in my pocket, a list in my hand,
answering every knock with a question,
never turning the lock.

Then one morning I understood:
the door was never locked.
Only my fear of the room beyond it.

So I turned the key. I stepped through.
The floor was cold. The road was mine.
Every choice I made left a footprint,
and every footprint asked me to keep walking.

A seed does not ask permission to grow.
It splits the dark and pushes up through the soil,
not knowing whether the sun will feed it or burn it,
only that staying buried is a slower death.

I am still afraid. I act anyway.
That is the whole of it -- not the courage,
but the hand that opens, and opens,
and opens again.
"""


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = POEM
    assert 1 <= len(text) <= 1000, "poem must be 1-1000 characters"
    assert text.strip(), "poem must not be only whitespace"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
