import os
import subprocess
import random
from datetime import datetime, timedelta

# ========================
# CONFIGURATION
# ========================
REPO_PATH = os.getcwd()  # Your repo path
GITHUB_BRANCH = "main"

# Start + end date for contribution graph
start_date = datetime(2024, 3, 1)
end_date   = datetime(2025, 9, 12)

# Topics + mini projects
topics = [
    "Variables", "Control_Flow", "Loops", "Functions", "Strings",
    "Data_Structures", "OOP", "File_IO", "Modules", "Error_Handling",
    "Decorators", "Generators", "Wrap_Up"
]

projects = ["Project_1_Snake_Water_Gun", "Project_2_Perfect_Guess"]

all_topics = topics + projects

# Languages and extensions
languages = {
    "Python": ".py",
    "Java": ".java",
    "Kotlin": ".kt",
    "JavaScript": ".js",
    "HTML": ".html",
    "CSS": ".css",
    "Julia": ".jl",
    "C": ".c",
    "C++": ".cpp",
    "SQL": ".sql",
    "Rust": ".rs",
    "Bash": ".sh"
}

# Rest days set (randomly chosen to look human)
total_days = (end_date - start_date).days
rest_days = set(random.sample(range(1, total_days), k=int(total_days * 0.15)))  # ~15% rest days

# Max commits per day
MIN_COMMITS = 1
MAX_COMMITS = 5

# ========================
# HELPER FUNCTIONS
# ========================
def run(cmd):
    subprocess.run(cmd, shell=True, check=True)

def random_code_snippet(topic, lang):
    """Generate small functional code snippet per language & topic."""
    if lang == "Python":
        return f"x = 5\nprint('Python {topic}:', x)"
    elif lang == "Java":
        return f"public class {topic} {{\n public static void main(String[] args) {{\n  int x = 5;\n  System.out.println(\"Java {topic}: \" + x);\n }}\n}}"
    elif lang == "Kotlin":
        return f"fun main() {{ val x = 5; println(\"Kotlin {topic}: $x\") }}"
    elif lang == "JavaScript":
        return f"let x = 5;\nconsole.log('JS {topic}:', x);"
    elif lang == "HTML":
        return f"<html><body><p>HTML {topic}: Example</p></body></html>"
    elif lang == "CSS":
        return f"/* CSS {topic} example */\np {{ color: blue; }}"
    elif lang == "Julia":
        return f"x = 5\nprintln(\"Julia {topic}: \", x)"
    elif lang == "C":
        return f"#include <stdio.h>\nint main() {{ int x = 5; printf(\"C {topic}: %d\\n\", x); return 0; }}"
    elif lang == "C++":
        return f"#include <iostream>\nint main() {{ int x=5; std::cout << \"C++ {topic}: \" << x << std::endl; return 0; }}"
    elif lang == "SQL":
        return f"-- SQL {topic} example\nSELECT 5 AS {topic};"
    elif lang == "Rust":
        return f"fn main() {{ let x = 5; println!(\"Rust {topic}: {{}}\", x); }}"
    elif lang == "Bash":
        return f"#!/bin/bash\nx=5\necho \"Bash {topic}: $x\""
    else:
        return f"// {lang} {topic} placeholder"

def create_files(topic):
    folder = f"{topic}"
    os.makedirs(folder, exist_ok=True)
    files_created = []
    # Randomly choose 4–7 languages per topic to mix
    langs_today = random.sample(list(languages.keys()), k=random.randint(4, len(languages)))
    for lang in langs_today:
        file_path = os.path.join(folder, f"{lang}_{topic}{languages[lang]}")
        with open(file_path, "w") as f:
            f.write(random_code_snippet(topic, lang))
        files_created.append(file_path)
    return files_created

def commit_files(files, commit_date):
    for f in files:
        run(f'git add "{f}"')
    msg = f"Add/update code for {os.path.basename(os.path.dirname(files[0]))}"
    date_str = commit_date.strftime("%Y-%m-%d %H:%M:%S")
    run(f'GIT_COMMITTER_DATE="{date_str}" git commit --date="{date_str}" -m "{msg}"')

# ========================
# MAIN SCRIPT
# ========================
if __name__ == "__main__":
    day_counter = 0
    current_date = start_date
    topic_idx = 0

    while current_date <= end_date:
        day_counter += 1
        # Skip rest days for human touch
        if day_counter in rest_days:
            current_date += timedelta(days=1)
            continue

        # Pick topic cyclically
        topic = all_topics[topic_idx % len(all_topics)]
        topic_idx += 1

        # Create/update files for the day
        files_today = create_files(topic)

        # Random commit count for the day
        commits_today = random.randint(MIN_COMMITS, MAX_COMMITS)
        for _ in range(commits_today):
            commit_files(files_today, current_date)

        # Move to next day
        current_date += timedelta(days=1)

    # Force push to GitHub to overwrite remote
    run(f'git push origin {GITHUB_BRANCH} --force') 
