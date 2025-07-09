import os

README_FILE = "README.md"
SECTION_HEADER = "# 🐍 Python Questions\n"

def get_question_files():
    return sorted([f for f in os.listdir() if f.startswith("Q") and f.endswith(".py")])

def update_readme():
    # Read existing README content
    if os.path.exists(README_FILE):
        with open(README_FILE, "r", encoding="utf-8") as f:
            content = f.read()
    else:
        content = ""

    # Keep only the part before the SECTION_HEADER
    if SECTION_HEADER in content:
        pre_content = content.split(SECTION_HEADER)[0]
    else:
        pre_content = content + "\n"

    # Build new question list
    question_files = get_question_files()
    questions_section = SECTION_HEADER + "\n"
    for file in question_files:
        questions_section += f"- [{file}](./{file})\n"

    # Combine and write back
    with open(README_FILE, "w", encoding="utf-8") as f:
        f.write(pre_content.strip() + "\n\n" + questions_section)

    print("✅ README.md partially updated!")

if __name__ == "__main__":
    update_readme()
