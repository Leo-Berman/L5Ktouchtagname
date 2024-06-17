import subprocess

def main():
    subprocess.call(r"python -m PyInstaller --onefile Main.py")



if __name__ == "__main__":
    main()
