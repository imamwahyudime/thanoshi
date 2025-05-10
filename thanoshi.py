import os
import random
import tkinter as tk
from tkinter import filedialog, messagebox

try:
    import send2trash
    SEND2TRASH_AVAILABLE = True
except ImportError:
    SEND2TRASH_AVAILABLE = False

def operate_on_half_files(folder_path, operation_mode):
    """
    Performs an operation (delete or move to trash) on approximately half the files
    in the given folder.
    """
    try:
        files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
        if not files:
            messagebox.showinfo("Info", "No files found in the selected folder.")
            return

        # Determine the number of files to select (approximately half)
        num_files_to_select = len(files) // 2

        if num_files_to_select == 0:
            messagebox.showinfo("Info", "Not enough files to select half (e.g., folder contains 0 or 1 file). No action taken.")
            return

        files_to_operate_on = random.sample(files, num_files_to_select)
        actual_num_to_operate = len(files_to_operate_on) # Should be same as num_files_to_select

        # Define action-specific terms
        if operation_mode == "delete":
            action_verb_present = "permanently delete"
            action_verb_past = "permanently deleted"
            action_description_for_cancel = "permanent deletion"
            undo_message = "This action CANNOT be undone."
        elif operation_mode == "trash":
            action_verb_present = "move to the recycle bin"
            action_verb_past = "moved to the recycle bin"
            action_description_for_cancel = "move to recycle bin"
            undo_message = "This action can be undone by restoring from the recycle bin."
        else:
            # This case should not be reached with the current button setup
            messagebox.showerror("Internal Error", "Invalid operation mode specified.")
            return

        confirmation_message = (
            f"Are you sure you want to {action_verb_present} {actual_num_to_operate} file(s) "
            f"in the folder:\n{folder_path}\n\n{undo_message}"
        )

        if messagebox.askyesno("Confirmation", confirmation_message):
            processed_count = 0
            errors_occurred = False
            
            print(f"Attempting to {action_verb_present} {actual_num_to_operate} file(s):")
            for file_name in files_to_operate_on:
                file_path_full = os.path.join(folder_path, file_name)
                try:
                    if operation_mode == "delete":
                        os.remove(file_path_full)
                        print(f"  Deleted: {file_path_full}")
                    elif operation_mode == "trash":
                        # send2trash requires absolute paths for reliability
                        send2trash.send2trash(os.path.abspath(file_path_full))
                        print(f"  Moved to trash: {file_path_full}")
                    processed_count += 1
                except send2trash.TrashPermissionError as e:
                    error_detail = f"Permission error while trying to {action_verb_present} '{file_name}':\n{e}"
                    messagebox.showerror("Permission Error", error_detail)
                    errors_occurred = True
                    print(f"  ERROR (Permission): {file_path_full} - {e}")
                except Exception as e:
                    error_detail = f"An error occurred while trying to {action_verb_present} '{file_name}':\n{e}"
                    messagebox.showerror("File Operation Error", error_detail)
                    errors_occurred = True
                    print(f"  ERROR (General): {file_path_full} - {e}")
            
            # Report final outcome
            if errors_occurred:
                if processed_count > 0:
                    messagebox.showwarning("Partial Success",
                                           f"Successfully {action_verb_past} {processed_count} of {actual_num_to_operate} selected file(s).\n"
                                           f"{actual_num_to_operate - processed_count} file(s) could not be processed. Check the console for error details.")
                else: # processed_count == 0
                    messagebox.showerror("Operation Failed",
                                         f"Failed to {action_verb_present} any of the {actual_num_to_operate} selected file(s).\n"
                                         f"Check the console for error details.")
            else: # No errors occurred during processing loop
                if processed_count > 0 : # Implies processed_count == actual_num_to_operate
                    messagebox.showinfo("Success",
                                        f"Successfully {action_verb_past} all {processed_count} selected file(s).")
                elif actual_num_to_operate > 0 and processed_count == 0:
                    # This state is highly unlikely if no errors were reported
                    messagebox.showwarning("No Action Taken",
                                           "Although files were selected and confirmed, none were processed, and no errors were reported. This is unexpected.")
                # If actual_num_to_operate was 0, it's handled before confirmation.
        else: # User clicked "No" on the confirmation dialog
            messagebox.showinfo("Cancelled", f"File {action_description_for_cancel} operation cancelled by user.")

    except FileNotFoundError:
        messagebox.showerror("Error", "The selected folder was not found.")
    except ValueError as ve: 
        # Handles errors from random.sample if num_files_to_select is invalid
        # (though current logic should prevent this by checking num_files_to_select first)
        messagebox.showerror("Selection Error", f"Error selecting files: {ve}")
    except Exception as e:
        messagebox.showerror("Unexpected Error", f"An unexpected error occurred: {e}")
        print(f"Unexpected error in operate_on_half_files: {e}")


def browse_and_process(operation_mode):
    """Opens a folder selection dialog and then calls operate_on_half_files."""
    if operation_mode == "trash" and not SEND2TRASH_AVAILABLE:
        messagebox.showerror("Missing Dependency", 
                             "The 'send2trash' library is not installed, which is required for moving files to the recycle bin. "
                             "This feature is currently unavailable.\n\nPlease install it by running: pip install Send2Trash")
        return

    folder_selected = filedialog.askdirectory()
    if folder_selected: # Proceed if a folder was selected
        operate_on_half_files(folder_selected, operation_mode)

def main():
    """Creates and runs the main application window."""
    root = tk.Tk()
    root.title("File Half-Operator")
    root.geometry("400x180") # Adjusted size for better layout

    main_frame = tk.Frame(root, padx=15, pady=15)
    main_frame.pack(expand=True, fill=tk.BOTH)

    delete_button = tk.Button(main_frame, text="Select Folder & Permanently Delete Half",
                              command=lambda: browse_and_process("delete"),
                              height=2) # Make buttons a bit taller
    delete_button.pack(pady=7, fill=tk.X)

    # Determine state of the trash button based on send2trash availability
    trash_button_state = tk.NORMAL if SEND2TRASH_AVAILABLE else tk.DISABLED
    trash_button = tk.Button(main_frame, text="Select Folder & Move Half to Recycle Bin",
                             command=lambda: browse_and_process("trash"),
                             state=trash_button_state,
                             height=2) # Make buttons a bit taller
    trash_button.pack(pady=7, fill=tk.X)

    if not SEND2TRASH_AVAILABLE:
        warning_label = tk.Label(main_frame, 
                                 text="Recycle Bin feature disabled: 'send2trash' not found.\nInstall with: pip install Send2Trash",
                                 fg="red", justify=tk.CENTER, wraplength=380)
        warning_label.pack(pady=(10,0))

    root.mainloop()

if __name__ == "__main__":
    main()