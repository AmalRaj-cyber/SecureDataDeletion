import os
import shutil

def secure_delete(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'rb+') as f:
                # Overwrite the file content with random data
                f.write(os.urandom(os.path.getsize(file_path)))

if __name__ == "__main__":
    folder_path = "/path/to/your/data"  # Replace with the path to your data folder
    secure_delete(folder_path)
    print("Data securely deleted.")
