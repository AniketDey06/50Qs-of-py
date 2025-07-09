import os
import re

README_FILE = "README.md"
SECTION_HEADER = "# 🐍 Python Questions"

def get_question_files_by_folder():
    grouped = {}
    for folder in sorted(os.listdir()):
        if folder.count('-') == 1 and os.path.isdir(folder):  # e.g., '01-10'
            files = sorted([
                f for f in os.listdir(folder) if f.startswith("Q") and f.endswith(".py")
            ])
            if files:
                grouped[folder] = files
    return grouped

def update_readme():
    if os.path.exists(README_FILE):
        with open(README_FILE, "r", encoding="utf-8") as f:
            content = f.read()
    else:
        content = ""

    # Regex to isolate the section between header and the next '---'
    pattern = rf"({re.escape(SECTION_HEADER)}\n)(.*?)(\n---)"
    question_groups = get_question_files_by_folder()

    # Rebuild the section
    questions_section = SECTION_HEADER + "\n\n"
    for folder, files in question_groups.items():
        questions_section += f"### 📁 {folder}\n"
        for file in files:
            questions_section += f"- [{file}]({folder}/{file})\n"
        questions_section += "\n"
    questions_section += "---"

    # Replace or append
    if re.search(pattern, content, flags=re.DOTALL):
        updated_content = re.sub(pattern, rf"\1{questions_section[len(SECTION_HEADER)+1:]}", content, flags=re.DOTALL)
    else:
        updated_content = content.strip() + "\n\n" + questions_section

    with open(README_FILE, "w", encoding="utf-8") as f:
        f.write(updated_content)

    print("✅ 'Python Questions' section updated with folder structure!")

if __name__ == "__main__":
    update_readme()
