# Modules
from tkinter import filedialog
import re
import os
from datetime import datetime
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# GUI Initialization
root = tk.Tk()
root.title("Non Ascii Remover")
root.geometry("400x400")

# Path Selection
selected_path = tk.StringVar()


def select_path():
    init_dir = os.getcwd() if selected_path.get() == '' else selected_path.get()
    path = filedialog.askdirectory(initialdir=init_dir, title="Select Initial Path")
    selected_path.set(path)


path_label = tk.Label(root, text="Select Initial Path: ")
path_label.pack()
path_entry = tk.Entry(root, textvariable=selected_path, width=50)
path_entry.pack()
path_button = tk.Button(root, text="Browse", command=select_path)
path_button.pack()

# Year Selection
start_year = tk.StringVar()
end_year = tk.StringVar()


def validate_start_year():
    if start_year_entry.get():
        try:
            year = int(start_year.get())
            current_year = datetime.today().year
            if 2015 <= year <= current_year:
                return True
            else:
                messagebox.showerror("Invalid Year", "Please enter a valid start year.")
                return False
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a numeric start year.")
            return False
    else:
        messagebox.showerror("Invalid Input", "Please enter a start year.")
        return False


def validate_end_year():
    if end_year_entry.get():
        try:
            year = int(end_year.get())
            current_year = datetime.today().year
            start = int(start_year.get())
            if start <= year <= current_year:
                return True
            else:
                messagebox.showerror("Invalid Year", "Please enter a valid end year.")
                return False
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a numeric end year.")
            return False
    else:
        messagebox.showerror("Invalid Input", "Please enter an end year.")
        return False


def validate_months():
    month_list_str = month_entry.get()
    month_list = month_list_str.split(",")
    for month in month_list:
        if not re.match(r'^\d{2}$', month) or int(month) > 13:
            messagebox.showerror("Invalid Month", f"Please enter valid months between 00 and 13.")
            return False
    return True


start_year_label = tk.Label(root, text="Start Year:")
start_year_label.pack()
start_year_entry = tk.Entry(root, textvariable=start_year)
start_year_entry.pack()

end_year_label = tk.Label(root, text="End Year:")
end_year_label.pack()
end_year_entry = tk.Entry(root, textvariable=end_year)
end_year_entry.pack()

month_label = tk.Label(root, text="Enter months (comma-separated):")
month_label.pack()
month_entry = tk.Entry(root)
month_entry.pack()

# Log Messages
log_messages = tk.Text(root, height=5, width=40)
log_messages.pack()

# Progress Bar
progress = ttk.Progressbar(root, orient=tk.HORIZONTAL, length=200, mode='determinate')
progress.pack()


def log_message(message):
    log_messages.insert(tk.END, message + "\n")
    log_messages.see(tk.END)


def update_progress(value):
    progress['value'] = value
    root.update_idletasks()


def remove_non_ascii(text):
    fix_text = re.sub(r'[^\x00-\x7F]+', ' ', text)
    return fix_text


def cleaning_process(file_path):
    new_rows = []
    with open(file_path, 'r', encoding='utf-8') as file:
        total_rows = sum(1 for _ in file)

    with open(file_path, 'r', encoding='utf-8') as file:
        current_row = 0
        for row in file:
            new_row = remove_non_ascii(row)
            new_rows.append(new_row)
            current_row += 1
            progress_value = (current_row / total_rows) * 100
            update_progress(progress_value)

    log_message(os.path.basename(file_path) + ' opened')

    fixed_path = os.path.join(os.path.dirname(file_path), "fixed", os.path.basename(file_path))
    os.makedirs(os.path.dirname(fixed_path), exist_ok=True)

    with open(fixed_path, 'w', encoding='utf-8') as output:
        for row in new_rows:
            output.write(row)
    log_message('fixed/' + os.path.basename(file_path) + ' created')


def start_cleaning():
    if not validate_start_year() or not validate_end_year() or not validate_months():
        return

    root_path = selected_path.get()
    start_year_val = int(start_year.get())
    end_year_val = int(end_year.get()) + 1
    month_list_str = month_entry.get()
    month_list = month_list_str.split(",")

    for year in range(start_year_val, end_year_val):
        for month in month_list:
            path = os.path.join(root_path, str(year), month)
            if not os.path.exists(path):
                continue

            for filetxt in os.listdir(path):
                if filetxt.lower().endswith(".txt"):
                    file_path = os.path.join(path, filetxt)
                    cleaning_process(file_path)

    messagebox.showinfo("Process Completed", "Removing Non-ASCII Process Completed!")


clean_button = tk.Button(root, text="Start Cleaning", command=start_cleaning)
clean_button.pack()

root.mainloop()
