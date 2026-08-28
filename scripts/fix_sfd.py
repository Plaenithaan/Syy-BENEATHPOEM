import sys
import os

def destroy_glifname(sfd_path):
    # Validate input path
    if not sfd_path.endswith(".sfd") or not os.path.isfile(sfd_path):
        print(f"Error: Invalid SFD file: {sfd_path}")
        return

    # Read and filter lines
    with open(sfd_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    filtered_lines = [line for line in lines if not line.strip().startswith("GlifName:")]

    # Write back to file
    with open(sfd_path, 'w', encoding='utf-8') as f:
        f.writelines(filtered_lines)

    print(f"✅ GlifName lines removed from {sfd_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python fix_sfd.py sources/SyyUDT-Regular.sfd")
    else:
        destroy_glifname(sys.argv[1])
