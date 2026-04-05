import sys
import subprocess
from datetime import datetime

def get_commits():
    try:
        r = subprocess.run(["git","log","--pretty=format:%s|||%h"], capture_output=True, text=True)
        commits = []
        for line in r.stdout.strip().split("\n"):
            if "|||" in line:
                msg, hash_ = line.split("|||")
                commits.append((msg, hash_))
        return commits
    except:
        return []

if __name__ == "__main__":
    version = sys.argv[1] if len(sys.argv) > 1 else "1.0.0"
    commits = get_commits()
    today = datetime.now().strftime("%Y-%m-%d")
    
    content = f"# changelog\n\n## [{version}] - {today}\n\n"
    for msg, hash_ in commits:
        content += f"- {msg} ({hash_})\n"
    
    with open("CHANGELOG.md", "w") as f:
        f.write(content)
    print(f"generated CHANGELOG.md with {len(commits)} commits")
# updated
