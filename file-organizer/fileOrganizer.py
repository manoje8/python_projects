import argparse
import os
import shutil
import logging


DEFAULT_DIRECTORY = os.getcwd()
LOG_FILE = "file_organizer.log"

# Configure logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler(LOG_FILE), logging.StreamHandler()]
)


class FileOrganizer:
    def __init__(self, dir):
        self.dir = os.path.abspath(dir)

    def organizeFile(self):

        if not os.path.exists(self.dir):
            logging.warning(f"The directory {self.dir} doesn't exist")
        else:

            logging.info(f"Organizing files in {self.dir}...")

            fileList = [file for file in os.listdir(self.dir)]

            print(fileList)

            if not fileList:
                logging.warning(f"No file found in {self.dir}")

            for file in fileList:
                try:
                    ext = os.path.splitext(file)[1][1:]
                    if not ext:
                        continue

                    folderPath = os.path.join(self.dir + "/" + ext)

                    if not os.path.exists(folderPath):
                        os.makedirs(folderPath)
                        logging.info(f'Created folder: {folderPath}')

                    shutil.move(
                        os.path.join(self.dir + "/" + file),
                        os.path.join(folderPath + "/" + file)
                    )

                    logging.info(f"Moved {file} to {folderPath}")
                except Exception as e:
                    logging.error(f'Failed to move {file}: {e}')

        logging.info("File organization completed.")


def main():
    parser = argparse.ArgumentParser(description="Organize files into folders by their extensions.")
    parser.add_argument(
        "--dir",
        type=str,
        default=DEFAULT_DIRECTORY,
        help="The directory to organize (default current working directory)."
    )
    args = parser.parse_args()
    organizer = FileOrganizer(args.dir)
    organizer.organizeFile()


if __name__ == "__main__":
    main()
