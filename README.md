# Non-ASCII Text File Remover

## Overview

The Non-ASCII Text File Remover is a Python program with a graphical user interface (GUI) that allows you to clean non-ASCII characters from text files within a specified directory structure. It provides options to select the initial directory, specify the range of years and months, and then processes the text files accordingly.

## Features

- **Directory Selection**: You can select the initial directory where the program will search for text files to clean.

- **Year and Month Filtering**: Specify the range of years and months to filter the text files you want to process.

- **Progress Tracking**: The program displays a progress bar to track the cleaning process.

- **Logging**: Log messages are provided to keep you informed about the status of file processing.

## Usage

1. Launch the program by running the Python script.

2. Select the initial directory by clicking the "Browse" button and choosing the desired folder.

3. Specify the start and end years, as well as the months (comma-separated) for filtering the files.

4. Click the "Start Cleaning" button to begin the cleaning process.

5. The program will process the selected text files, clean them by removing non-ASCII characters, and save the cleaned files in a "fixed" subdirectory within their respective locations.

6. Progress will be displayed in the GUI, and log messages will inform you of the status of each file processing.

7. Once the process is complete, a message box will indicate that the removal of non-ASCII characters has been completed.

## Requirements

- Python 3.10 or above
- Run the script in an environment with file read and write permissions.
- See [requirements.txt](requirements.txt) for required libraries. 

## Notes

- Your original files will not be overwritten by this program. The cleaned versions will be saved in a "fixed" subdirectory within their respective locations. However, it's always a good practice to maintain backups of your data before making any significant changes.

- Only files with a ".txt" extension will be processed.

## Author

Cansu ZOHRE

## License

This program is open-source and available under the MIT License. See the [LICENSE](LICENSE) file for details.

