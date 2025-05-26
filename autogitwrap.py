import subprocess
import sys

def run_command(command):
    try:
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        sys.exit(1)

def has_staged_changes():
    result = run_command(["git", "status", "--porcelain"])
    return bool(result.strip())

def git_add_commit_push():
  print("Running git add, commit, and push...")
  run_command(["git", "add", "content/reading.md"])

  categories = ["Books", "Programming", "AI", "Tech", "Math", "Education"]
  commit_category = input("Enter the category for this commit (Books, Programming, AI, Tech, Math, Education): ").strip()
  commit_message=f"Add link(s) to {commit_category} section in reading.md"
  if commit_category not in categories:
      print("Invalid commit category. Exiting.")
      sys.exit(1)

  if not has_staged_changes():
    print("No changes to commit. Exiting.")
    sys.exit(0)

  print("Committing changes...")
  run_command(["git", "commit", "-m", commit_message])
  print("Changes committed successfully.")

  print("Pushing changes...")
  run_command(["git", "push", "origin", "main"])
  print("Changes pushed successfully.")

  return commit_message

def main():
  print("Running AutoGitWrap.py...")
  git_add_commit_push()
  print("Success!")

if __name__ == "__main__":
  main()
