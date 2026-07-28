import shutil
from pathlib import Path
from datetime import datetime


def create_backup():
    print("Python Backup Automation")
    print("------------------------")

    source_folder = Path(
        input("Enter the source folder path: ").strip()
    ).expanduser()

    backup_folder = Path(
        input("Enter the backup folder path: ").strip()
    ).expanduser()

    if not source_folder.exists():
        print("Error: The source folder does not exist.")
        return

    if not source_folder.is_dir():
        print("Error: The source path is not a folder.")
        return

    backup_folder.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    destination = backup_folder / f"backup_{timestamp}"

    try:
        shutil.copytree(source_folder, destination)

        file_count = sum(
            1 for item in destination.rglob("*")
            if item.is_file()
        )

        print()
        print("Backup completed successfully.")
        print(f"Files copied: {file_count}")
        print(f"Backup location: {destination}")

    except PermissionError:
        print("Error: Permission denied while copying files.")

    except OSError as error:
        print(f"Backup failed: {error}")


create_backup()