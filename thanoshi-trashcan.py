import os
import random
import tkinter as tk
from tkinter import filedialog, messagebox
import send2trash

def move_half_files_to_trash(folder_path):
    """Moves approximately half the files in the given folder to the recycle bin."""
    try:
        files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
        num_files_to_move = len(files) // 2
        files_to_move = random.sample(files, num_files_to_move)

        if messagebox.askyesno("Confirmation", f"Are you sure you want to move approximately {num_files_to_move} files to the recycle bin in {folder_path}?\nThis action can be undone by restoring from the recycle bin."):
            success = True  # Add a flag to track success
            for file_name in files_to_move:
                file_path = os.path.join(folder_path, file_name)
                corrected_path = os.path.abspath(file_path)
                print(f"Attempting to move: {corrected_path}")  # Add print statement
                try:
                    send2trash.send2trash(corrected_path)
                    print(f"Successfully moved: {corrected_path}")  # Add print statement
                except send2trash.TrashPermissionError as e:
                    messagebox.showerror("Error", f"Permission error moving {file_name} to trash: {e}")
                    print(f"Permission error: {e}") #Print error to console.
                    success = False  # Set success to False if an error occurs
                except Exception as e:
                    messagebox.showerror("Error", f"An error occurred moving {file_name} to trash: {e}")
                    print(f"General error: {e}") #print error to console.
                    success = False  # Set success to False if an error occurs
            if success:
                messagebox.showinfo("Success", f"Successfully moved approximately {num_files_to_move} files to the recycle bin.")
            else:
                messagebox.showerror("Error", "One or more files could not be moved. Check the console for details.")
        else:
            messagebox.showinfo("Cancelled", "File movement cancelled.")

    except FileNotFoundError:
        messagebox.showerror("Error", "Folder not found.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def browse_folder():
    """Opens a folder selection dialog and moves half the files to the recycle bin."""
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        move_half_files_to_trash(folder_selected)

def main():
    """Creates the main application window."""
    root = tk.Tk()
    root.title("Half-File Recycler")

    browse_button = tk.Button(root, text="Select Folder and Move Half to Recycle Bin", command=browse_folder)
    browse_button.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()
