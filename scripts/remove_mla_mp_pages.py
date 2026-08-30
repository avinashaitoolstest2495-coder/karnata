import os
import shutil

dirs_to_remove = [
    'mla',
    'mp',
    'namma-karnataka/mla',
    'namma-karnataka/mp'
]

removed_count = 0
for d in dirs_to_remove:
    if os.path.exists(d):
        num_files = len(os.listdir(d))
        shutil.rmtree(d, ignore_errors=True)
        print(f"Removed directory: {d} ({num_files} files)")
        removed_count += num_files

print(f"TOTAL_REMOVED_FILES: {removed_count}")
