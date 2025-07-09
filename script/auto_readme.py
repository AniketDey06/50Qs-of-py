import os
import re

README_FILE = "README.md"
SECTION_HEADER = "# 🐍 Python Questions"

def get_question_files():
    return sorted([f for f in os.listdir() if f.startswith("Q") and f.endswith(".py")])

def update_readme():
    # Read existing README content
    if os.path.exists(README_FILE):
        with open(README_FILE, "r", encoding="utf-8") as f:
            content = f.read()
    else:
        content = ""

    # Regex pattern to capture the Python Questions section
    pattern = rf"({re.escape(SECTION_HEADER)}\n)(.*?)(\n---)"
    question_files = get_question_files()

    # Build updated section
    new_section = SECTION_HEADER + "\n"
    for file in question_files:
        new_section += f"- [{file}](./{file})\n"
    new_section += "\n---"

    # Replace the old section with the new one
    if re.search(pattern, content, flags=re.DOTALL):
        updated_content = re.sub(pattern, rf"\1{new_section[len(SECTION_HEADER)+1:]}", content, flags=re.DOTALL)
    else:
        # If the section doesn't exist, append it at the end
        updated_content = content.strip() + "\n\n" + new_section

    # Write updated content back
    with open(README_FILE, "w", encoding="utf-8") as f:
        f.write(updated_content)

    print("✅ 'Python Questions' section updated in README.md!")

if __name__ == "__main__":
    update_readme()
