import os
import random
import tkinter as tk
from tkinter import filedialog, messagebox

def delete_half_files(folder_path):
    """Deletes approximately half the files in the given folder."""
    try:
        files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
        num_files_to_delete = len(files) // 2
        files_to_delete = random.sample(files, num_files_to_delete)

        if messagebox.askyesno("Confirmation", f"Are you sure you want to permanently delete approximately {num_files_to_delete} files in {folder_path}?\nThis action cannot be undone."):
            for file_name in files_to_delete:
                file_path = os.path.join(folder_path, file_name)
                os.remove(file_path)

                messagebox.showinfo("Success", f"Successfully deleted approximately {num_files_to_delete} files.")

    except FileNotFoundError:
        messagebox.showerror("Error", "Folder not found.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def browse_folder():
    """Opens a folder selection dialog and deletes half the files."""
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        delete_half_files(folder_selected)

def main():
    """Creates the main application window."""
    root = tk.Tk()
    root.title("Half-File Deleter")

    browse_button = tk.Button(root, text="Select Folder and Delete Half", command=browse_folder)
    browse_button.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()
