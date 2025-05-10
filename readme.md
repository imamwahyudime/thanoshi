# Half-Files Deleter

This Python script provides a simple GUI application to delete half the files within the selected folder. 

It offers two modes of operation:
1.  **Permanent Deletion:** Permanently deletes about half the files. **⚠️ Use with extreme caution!**
2.  **Move to Recycle Bin:** Moves about half the files to the system's recycle bin (safer).

This single script replaces the previous `thanoshi-permanent.py` and `thanoshi-trashcan.py` variants.

**Tested on Windows 10** 

## Features:

It uses `tkinter` for the GUI, `os` for file system operations, and `random` for selecting files to delete.

* **GUI Interface:** Uses `tkinter` for a user-friendly interface.
* **Folder Selection:** Allows users to select a folder using a system dialog.
* **Dual Operation Modes:**
    * **Permanently Delete:** Option to permanently remove approximately half the files.
    * **Move to Recycle Bin:** Option to send approximately half the files to the recycle bin (requires `send2trash` library).
* **Random File Selection:** Randomly selects which files will be affected to reach approximately half.
* **Confirmation Prompts:** Displays a confirmation dialog before executing any file operation, detailing the action, number of files, and specific warnings (e.g., about permanent deletion or reversibility from trash).
* **Error Handling:** Includes error handling for issues like "folder not found," file operation errors, and permissions, with messages displayed to the user and details in the console.
* **Conditional Recycle Bin Feature:** The "Move to Recycle Bin" functionality is only enabled if the `send2trash` library is installed. The application will indicate if it's missing.

## Prerequisites:

* **Python 3.x**
* **`send2trash` (Python library):**
    * Required **only** for the "Move to Recycle Bin" feature.
    * The application will run without it, but the recycle bin option will be disabled.
    * Install it via pip:
        ```bash
        pip install Send2Trash
        ```
## Usage:

1.  **Save the Script:**
    Save the combined Python code as a `.py` file (e.g., `thanos_file_tool.py`).

2.  **Run the Script:**
    Navigate to the directory containing the script and run it using Python:
    ```bash
    python thanos_file_tool.py
    ```

3.  **Choose an Operation:**
    The application window will open with two main buttons:
    * "Select Folder & Permanently Delete Half"
    * "Select Folder & Move Half to Recycle Bin"

4.  **Select Folder:**
    * Click the button corresponding to your desired action.
    * A folder selection dialog will open. Choose the folder you want to process.

5.  **Confirm Action:**
    * After selecting a folder, a confirmation dialog will appear.
    * It will state the action to be performed (permanent deletion or move to trash), the number of files selected, and the full path to the folder.
    * **Crucially, it will also provide a warning about the irreversibility of permanent deletion or the reversibility of moving to trash.** Review this information very carefully.

6.  **Proceed or Cancel:**
    * Click "Yes" to proceed with the operation.
    * Click "No" to cancel.

7.  **View Outcome:**
    * A message will inform you of the success (e.g., "Successfully deleted X files") or failure of the operation.
    * In case of partial success or errors, you'll be advised to check the console output for more details.

## Important Notes:

* **⚠️ PERMANENT DELETION RISK:** The "Permanently Delete" option erases files for good. Once deleted this way, files **CANNOT** be easily recovered. **Always double-check the folder and ensure you have backups of any important data before using this option.**
* **Recycle Bin for Safety:** The "Move to Recycle Bin" option is significantly safer, as files can typically be restored from your operating system's recycle bin. This is the recommended option for most use cases.
* **Approximation:** The script affects *approximately* half of the files. The exact number is determined by `total_files // 2`. If a folder has 0 or 1 file, no files will be selected for operation.
* **`send2trash` Dependency:** If the `send2trash` library is not installed, the "Move to Recycle Bin" button will be disabled. The script will inform you of this.
* **TEST THOROUGHLY:** It is **highly recommended** to test this script on a sample folder containing non-critical, dummy files first. This will help you understand its behavior and confirm it works as expected in your environment before using it on important data.
* **Console Logs:** The script prints actions and errors to the console, which can be useful for troubleshooting or seeing a detailed log of operations.

## Contributing:

If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.
