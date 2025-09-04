# Test
Chalo ajj kuch naya sikhte h 


import os, random, subprocess
from datetime import datetime, timedelta

# ========================
# CONFIGURATION
# ========================
REPO_PATH = os.getcwd()     # Current repo path (Codespace/Termux me chalega)
BRANCH = "main"

# Start 1.5 years ago
start_date = datetime.now() - timedelta(days=550)
end_date   = datetime.now()

# File topics by language
topics = {
    "Python": ["chapter01", "chapter02", "loops", "functions", "oop", "project_calc"],
    "Java": ["HelloWorld", "Calculator", "Student", "Sorting"],
    "Kotlin": ["MainActivity", "Utils", "Coroutines", "DataClass"],
    "Web": ["index", "style", "script", "todo_app"],
    "Julia": ["matrix_ops", "linear_regression", "plotting"],
    "Docs": ["README", "notes", "changelog", ".gitignore"]
}

extensions = {
    "Python": ".py",
    "Java": ".java",
    "Kotlin": ".kt",
    "Web_html": ".html",
    "Web_css": ".css",
    "Web_js": ".js",
    "Julia": ".jl",
    "Docs_md": ".md",
    "Docs_ignore": ""
}

# Commit message templates
messages = [
    "feat: Added {topic}",
    "fix: Resolved bug in {topic}",
    "docs: Updated {topic} documentation",
    "refactor: Improved {topic} structure",
    "test: Added tests for {topic}",
    "chore: Minor update in {topic}"
]

def run(cmd):
    subprocess.run(cmd, shell=True, check=True)

def create_file(lang, topic, commit_date):
    folder = lang
    os.makedirs(folder, exist_ok=True)

    # Extension choose
    if lang == "Web":
        ext = random.choice(["_html", "_css", "_js"])
    elif lang == "Docs":
        ext = random.choice(["_md", "_ignore"])
    else:
        ext = ""

    extension = extensions[lang + ext] if ext else extensions.get(lang, ".txt")

    filename = f"{topic}{extension}"
    filepath = os.path.join(folder, filename)

    # Content
    with open(filepath, "w") as f:
        f.write(f"// Auto-generated {lang} file\n")
        f.write(f"// Work on {topic} at {commit_date}\n")
        if lang == "Python":
            f.write(f"print('Working on {topic}')\n")
        elif lang == "Java":
            f.write(f"public class {topic} "+"{\n public static void main(String[] a) { System.out.println(\"{topic}\"); } }")
        elif lang == "Kotlin":
            f.write(f"fun main() "+"{ println(\"{topic}\") }")
        elif lang == "Web":
            if extension == ".html":
                f.write(f"<html><body><h1>{topic}</h1></body></html>")
            elif extension == ".css":
                f.write(f"body {{ background-color: #{random.randint(100000,999999)}; }}")
            elif extension == ".js":
                f.write(f"console.log('{topic}');")
        elif lang == "Julia":
            f.write(f"println(\"Working on {topic}\")")
        else:  # Docs
            f.write(f"# Notes about {topic}\nUpdated on {commit_date}\n")

    return filepath

def make_commits():
    current = start_date
    while current <= end_date:
        commits_today = random.choice([0,0,1,1,1,2,2,3])  # realistic pattern
        for _ in range(commits_today):
            lang = random.choice(list(topics.keys()))
            topic = random.choice(topics[lang])
            commit_date = current.strftime("%Y-%m-%d %H:%M:%S")

            filepath = create_file(lang, topic, commit_date)
            run(f"git add {filepath}")

            msg_template = random.choice(messages)
            commit_msg = msg_template.format(topic=topic)

            run(f'GIT_COMMITTER_DATE="{commit_date}" git commit --date="{commit_date}" -m "{commit_msg}"')

        current += timedelta(days=1)

    run(f"git push origin {BRANCH}")

if __name__ == "__main__":
    make_commits()
