# Half-Files Deleter

This Python script provides a simple GUI application to delete approximately half of the files within a selected folder. 

I have two varian for now : 
- **thanoshi-permanent.py :** **⚠️ Warning:** This script permanently deletes files. Use with caution!
- **thanoshi-trashcan.py :** This script moved files to trash folder. Which is more safer than permanent.py

**Tested on Windows 10**

## Features

It uses `tkinter` for the GUI, `os` for file system operations, and `random` for selecting files to delete.

-   **GUI Interface:** Uses `tkinter` for a user-friendly interface.
-   **Folder Selection:** Allows users to select a folder using a file dialog.
-   **Random File Deletion:** Deletes approximately half of the files in the selected folder randomly.
-   **Confirmation Prompt:** Asks for confirmation before deleting files to prevent accidental data loss.
-   **Error Handling:** Handles `FileNotFoundError` and other exceptions, displaying error messages to the user.

## Prerequisites

-   Python 3.x
-   thanoshi-trashcan.py: send2trash (necessary library)
-   thanoshi-permanent.py : No external libraries required

## Usage

1.  **Run the Script:**
    Navigate to the directory containing the script and run it using Python:

    ```bash
    python your_script_name.py
    ```

2.  **Select Folder:**
    Click the "Select Folder and Delete Half" button.

3.  **Choose Folder:**
    A file dialog will open, allowing you to select the folder containing the files you want to process.

4.  **Confirm Deletion:**
    A confirmation dialog will appear, displaying the number of files to be deleted and the folder path. Review this information carefully.

5.  **Confirm or Cancel:**
    -   Click "Yes" to proceed with the deletion.
    -   Click "No" to cancel the operation.

6.  **Success or Error Message:**
    -   If the deletion is successful, a success message will be displayed.
    -   If an error occurs (e.g., folder not found), an error message will be displayed.

## Important Notes

-   **Data Loss:** The permanent script variant permanently deletes files. Ensure you have backups of important data before using it.
-   **Approximation:** The script deletes *approximately* half of the files. The exact number may vary slightly.
-   **No Undo:** There is no undo functionality. Once files are deleted, they cannot be recovered using this script.
-   **Testing:** It is highly recommended to test this script on a test folder with non-critical files before using it on important data.

## Contributing

If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.
