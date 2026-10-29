import os

print("Files in functions/:")
for root, dirs, files in os.walk('functions'):
    for f in files:
        print(os.path.join(root, f))
