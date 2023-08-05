import os
import shutil
import logging

# Function to shred a file
def shred_file(file_path):
    try:
        with open(file_path, "rb") as f:
            data = f.read()
        # Overwrite the file contents with random data multiple times
        for i in range(10):
            data = os.urandom(len(data))
        with open(file_path, "wb") as f:
            f.write(data)
        # Remove the file after shredding
        os.remove(file_path)
        # Log the deletion of the file
        logging.info(f"Deleted file: {file_path}")
        print("File shredded successfully!")
    except IOError as e:
        # Log and print any error that occurs during file shredding
        logging.error(f"Error shredding file: {str(e)}")
        print(f"Error shredding file: {str(e)}")

# Function to shred a folder
def shred_folder(folder_path):
    try:
        # Delete the folder and its contents recursively
        shutil.rmtree(folder_path)
        # Log the deletion of the folder
        logging.info(f"Deleted folder: {folder_path}")
        print("Folder shredded successfully!")
    except OSError as e:
        # Log and print any error that occurs during folder shredding
        logging.error(f"Error shredding folder: {str(e)}")
        print(f"Error shredding folder: {str(e)}")


def main():
    # Configure logging
    logging.basicConfig(filename='shredder.log', level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')
    print("Welcome to the Secure File Shredder!")
    while True:
        print(
            """
           ................   Enter 1 for shredding a file ..............
           ................   Enter 2 for shredding a folder .............. 
           ................   Enter 3 to exit ..............
              """
        )
        choice = input("==>")
        if choice == "1":
            file_path = input("Enter the path of the file to shred: ")
            shred_file(file_path)
        elif choice == "2":
            folder_path = input("Enter the path of the folder to shred: ")
            shred_folder(folder_path)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
