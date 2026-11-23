import os

SETUP = """My agent delegates to a subagent, which delegates to a subagent, """
PUNCH = """and now three of us are billing you for one typo."""


def assemble_text():
    return SETUP + PUNCH


os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(assemble_text())
