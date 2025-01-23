# File Organizer

A Python script to organize files in a directory into folders based on their extensions. This script is designed to be simple, efficient, and user-friendly.

---

## Features

- **Organize Files by Extension**: Automatically sorts files into folders named after their extensions (e.g., `.txt` files go into a `txt` folder).
- **Logging**: Logs all actions (e.g., file movements, errors) to a file (`file_organizer.log`) and the console.
- **Command-Line Interface**: Allows users to specify the directory path via command-line arguments.
- **Error Handling**: Gracefully handles errors such as invalid directories, permission issues, and more.


## Installation

1. **Clone the Repository**:
    https://github.com/manoje8/python_projects.git
    cd file-organizer 

2. **Command-Line Arguments**
	Run the script with the following command:
	`python fileOrganizer.py --dir "path/to/your/directory"`

	 `--dir`: Specify the directory to organize. If not provided, the script defaults to the current working directory.
```
	python fileOrganizer.py --dir "C:/Downloads"
```

### Output

The script will:
1. Create folders for each file extension.
2. Move files into their respective folders.
3. Log all actions to `file_organizer.log` and the console.
