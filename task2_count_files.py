import os

# Get all items in the current directory
items = os.listdir('.')

# Keep only files (not folders)
files = [f for f in items if os.path.isfile(f)]

print("Number of files in current directory:", len(files))