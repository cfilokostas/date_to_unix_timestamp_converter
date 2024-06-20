import tkinter as tk
from tkcalendar import DateEntry
from datetime import datetime

def get_date_time():
    start_date = start_date_entry.get_date()
    start_hour = int(start_hour_spinbox.get())
    start_minute = int(start_minute_spinbox.get())
    start_second = int(start_second_spinbox.get())
    
    end_date = end_date_entry.get_date()
    end_hour = int(end_hour_spinbox.get())
    end_minute = int(end_minute_spinbox.get())
    end_second = int(end_second_spinbox.get())
    
    # Combine date and time
    start_datetime = datetime.combine(start_date, datetime.min.time()).replace(hour=start_hour, minute=start_minute, second=start_second)
    end_datetime = datetime.combine(end_date, datetime.min.time()).replace(hour=end_hour, minute=end_minute, second=end_second)
    
    # Convert to Unix timestamps
    start_unix = int(start_datetime.timestamp())
    end_unix = int(end_datetime.timestamp())
    
    print(f"Start Date and Time: {start_datetime} -> Unix Timestamp: {start_unix}")
    print(f"End Date and Time: {end_datetime} -> Unix Timestamp: {end_unix}")

def center_window(root, width, height):
    # Get the screen dimensions
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculate the position of the window
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)

    # Set the position of the window
    root.geometry(f'{width}x{height}+{x}+{y}')

# Create the main window
root = tk.Tk()
root.title("Date and Time Picker")

# Set the window size
window_width = 400
window_height = 500

# Center the window
center_window(root, window_width, window_height)

# Create labels and widgets for start date and time
start_date_label = tk.Label(root, text="Please select a start date:")
start_date_label.pack(pady=5)
start_date_entry = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2, year=2023)
start_date_entry.pack(pady=5)

start_time_label = tk.Label(root, text="Please select a start time:")
start_time_label.pack(pady=5)

start_time_frame = tk.Frame(root)
start_time_frame.pack(pady=5)

start_hour_label = tk.Label(start_time_frame, text="Hours:")
start_hour_label.grid(row=0, column=0, padx=5)
start_hour_spinbox = tk.Spinbox(start_time_frame, from_=0, to=23, wrap=True, width=5, state="readonly", justify=tk.CENTER)
start_hour_spinbox.grid(row=0, column=1, padx=5)

start_minute_label = tk.Label(start_time_frame, text="Minutes:")
start_minute_label.grid(row=0, column=2, padx=5)
start_minute_spinbox = tk.Spinbox(start_time_frame, from_=0, to=59, wrap=True, width=5, state="readonly", justify=tk.CENTER)
start_minute_spinbox.grid(row=0, column=3, padx=5)

start_second_label = tk.Label(start_time_frame, text="Seconds:")
start_second_label.grid(row=0, column=4, padx=5)
start_second_spinbox = tk.Spinbox(start_time_frame, from_=0, to=59, wrap=True, width=5, state="readonly", justify=tk.CENTER)
start_second_spinbox.grid(row=0, column=5, padx=5)

# Create labels and widgets for end date and time
end_date_label = tk.Label(root, text="Please select an end date:")
end_date_label.pack(pady=5)
end_date_entry = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2, year=2023)
end_date_entry.pack(pady=5)

end_time_label = tk.Label(root, text="Please select an end time:")
end_time_label.pack(pady=5)

end_time_frame = tk.Frame(root)
end_time_frame.pack(pady=5)

end_hour_label = tk.Label(end_time_frame, text="Hours:")
end_hour_label.grid(row=0, column=0, padx=5)
end_hour_spinbox = tk.Spinbox(end_time_frame, from_=0, to=23, wrap=True, width=5, state="readonly", justify=tk.CENTER)
end_hour_spinbox.grid(row=0, column=1, padx=5)

end_minute_label = tk.Label(end_time_frame, text="Minutes:")
end_minute_label.grid(row=0, column=2, padx=5)
end_minute_spinbox = tk.Spinbox(end_time_frame, from_=0, to=59, wrap=True, width=5, state="readonly", justify=tk.CENTER)
end_minute_spinbox.grid(row=0, column=3, padx=5)

end_second_label = tk.Label(end_time_frame, text="Seconds:")
end_second_label.grid(row=0, column=4, padx=5)
end_second_spinbox = tk.Spinbox(end_time_frame, from_=0, to=59, wrap=True, width=5, state="readonly", justify=tk.CENTER)
end_second_spinbox.grid(row=0, column=5, padx=5)

# Add a button to get the selected start and end date and time
button = tk.Button(root, text="Get Date and Time", command=get_date_time)
button.pack(pady=20)

# Run the main loop
root.mainloop()
