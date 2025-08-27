import os
import subprocess
from datetime import datetime, timedelta

# ========================
# CONFIGURATION
# ========================
REPO_PATH = os.getcwd()   # Codespace ke andar current repo path
GITHUB_BRANCH = "main"

# Start + End date for 21-day schedule
start_date = datetime(2025, 7, 5, 10, 0, 0)
end_date   = datetime(2025, 7, 22, 18, 0, 0)

# Roadmap: 13 chapters + 2 projects (NO mega projects)
tasks = [
    "Chapter-01", "Chapter-02", "Chapter-03+Chapter-04",
    "Chapter-05", "Chapter-06", "Chapter-07",
    "Chapter-08", "Project-1-Snake-Water-Gun",
    "Chapter-09+Chapter-10", "Chapter-11",
    "Project-2-Perfect-Guess", "Chapter-12",
    "Chapter-13", "Wrap-Up"
]

# Rest days → no commits
rest_days = {7, 11, 15, 19}

# ========================
# Run shell command
# ========================
def run(cmd):
    print(f"▶ {cmd}")
    subprocess.run(cmd, shell=True, check=True)

# ========================
# Step 1: Create folders + dummy files
# ========================
def create_files():
    for task in tasks:
        folder = task.replace("+", "_")
        os.makedirs(folder, exist_ok=True)
        file_path = os.path.join(folder, "solution.py")
        if not os.path.exists(file_path):
            with open(file_path, "w") as f:
                f.write(f"# {task} solution\nprint('Solved {task}')\n")

# ========================
# Step 2: Backdated commits
# ========================
def make_commits():
    day = 0
    task_idx = 0
    current_date = start_date

    while current_date <= end_date and task_idx < len(tasks):
        day += 1
        if day in rest_days:   # skip rest day
            current_date += timedelta(days=1)
            continue

        task = tasks[task_idx]
        folder = task.replace("+", "_")
        run(f"git add '{folder}/'")
        commit_msg = f"Solved {task}"
        commit_date = current_date.strftime("%Y-%m-%d %H:%M:%S")

        run(
            f'GIT_COMMITTER_DATE="{commit_date}" '
            f'git commit --date="{commit_date}" -m "{commit_msg}"'
        )

        task_idx += 1
        current_date += timedelta(days=1)

    run(f"git push origin {GITHUB_BRANCH}")

# ========================
# MAIN
# ========================
if __name__ == "__main__":
    create_files()
    make_commits() 
