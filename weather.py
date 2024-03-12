import pandas as pd
import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Function to compare cities
def compare_cities():
    city1 = city1_var.get()
    city2 = city2_var.get()

    if not city1 or not city2:
        messagebox.showerror("Error", "Please select two cities to compare.")
        return

    city_mapping = {
        'Bangalore': 'Bangalore',
        'Chennai': 'Chennai',
        'Delhi': 'Delhi',
        'Jaipur': 'Jaipur',
        'Mumbai': 'Mumbai'
    }

    city1_file = f"E:\\dvpproj\\{city_mapping[city1]}.csv"
    city2_file = f"E:\\dvpproj\\{city_mapping[city2]}.csv"

    w1 = pd.read_csv(city1_file)
    w2 = pd.read_csv(city2_file)

    title1 = city1
    title2 = city2

    attribute = attribute_var.get()

    plt.close('all')  # Close any existing plots

    if attribute == "AQI":
        aqicol = ['aqi']
        aqiselected1 = w1[aqicol]
        aqiselected2 = w2[aqicol]

        fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))

        aqiselected1.plot(kind='bar', ax=axes[0], title=f"{title1} AQI", legend=False)
        axes[0].set_ylabel('AQI')
        axes[0].set_xlabel('Date')

        aqiselected2.plot(kind='bar', ax=axes[1], title=f"{title2} AQI", legend=False)
        axes[1].set_ylabel('AQI')
        axes[1].set_xlabel('Date')

        # Add horizontal lines for AQI levels
        for ax in axes:
            ax.axhline(y=1, color='green', linestyle='--', linewidth=2, label='Safe')
            ax.axhline(y=3, color='orange', linestyle='--', linewidth=2, label='Moderate')
            ax.axhline(y=4.5, color='red', linestyle='--', linewidth=2, label='High')
            ax.legend(loc='upper right')

    else:
        fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))

        if attribute == "Temperature Comparison":
            tempcolm = ['tavg', 'tmin', 'tmax']
            selected_columns1 = w1[tempcolm]
            selected_columns2 = w2[tempcolm]

            selected_columns1.plot(ax=axes[0], title=f"{title1} Temperature", grid=True)
            selected_columns2.plot(ax=axes[1], title=f"{title2} Temperature", grid=True)

            for ax in axes:
                ax.set_ylabel('Temperature')
                ax.set_xlabel('Date')

        elif attribute == "PM Index Comparison":
            pmcolm = ['pm2_5', 'pm10']
            pm_columns1 = w1[pmcolm]
            pm_columns2 = w2[pmcolm]

            pm_columns1.plot(ax=axes[0], title=f"{title1} PM Index", grid=True)
            pm_columns2.plot(ax=axes[1], title=f"{title2} PM Index", grid=True)

            for ax in axes:
                ax.set_ylabel('PM Index')
                ax.set_xlabel('Date')

        elif attribute == "Pollutants Comparison":
            polcolm = ['no', 'no2', 'so2']
            polselected1 = w1[polcolm]
            polselected2 = w2[polcolm]

            polselected1.plot(ax=axes[0], title=f"{title1} Pollutants Intensity", grid=True)
            polselected2.plot(ax=axes[1], title=f"{title2} Pollutants Intensity", grid=True)

            for ax in axes:
                ax.set_ylabel('Pollutants Intensity')
                ax.set_xlabel('Date')

    plt.tight_layout()
    plt.show()

# Create GUI
root = tk.Tk()
root.title("Weather Analysis and Comparison")
root.geometry("800x600")  # Set window size to occupy the full screen
root.configure(bg="black")  # Set background color

# Styling
style = ttk.Style()
style.configure("TLabel", foreground="white", font=("Arial", 12))
style.configure("Title.TLabel", foreground="white", font=("Arial", 24, "bold"))

# Project title
project_title = ttk.Label(root, text="Comparative Analysis of Air Quality and Weather Patterns", style="Title.TLabel", background="black")
project_title.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="ew")

# Instructions
instructions = """
Select two cities and an attribute to compare their weather data.
"""
instructions_label = ttk.Label(root, text=instructions, background="black")
instructions_label.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="ew")

# City selection
ttk.Label(root, text="Select City 1:", background="black").grid(row=2, column=0, padx=10, pady=5)
city1_var = tk.StringVar()
city1_dropdown = ttk.Combobox(root, textvariable=city1_var, values=["Bangalore", "Chennai", "Delhi", "Jaipur", "Mumbai"], font=("Arial", 10))
city1_dropdown.grid(row=2, column=1, padx=10, pady=5)

ttk.Label(root, text="Select City 2:", background="black").grid(row=3, column=0, padx=10, pady=5)
city2_var = tk.StringVar()
city2_dropdown = ttk.Combobox(root, textvariable=city2_var, values=["Bangalore", "Chennai", "Delhi", "Jaipur", "Mumbai"], font=("Arial", 10))
city2_dropdown.grid(row=3, column=1, padx=10, pady=5)

# Attribute selection
ttk.Label(root, text="Select Attribute:", background="black").grid(row=4, column=0, padx=10, pady=5)
attribute_var = tk.StringVar()
attribute_var.set("AQI")  # Default selection
attribute_dropdown = ttk.Combobox(root, textvariable=attribute_var, values=["AQI", "Temperature Comparison", "PM Index Comparison", "Pollutants Comparison"], font=("Arial", 10))
attribute_dropdown.grid(row=4, column=1, padx=10, pady=5)

# Compare button
compare_button = ttk.Button(root, text="Compare Cities", command=compare_cities)
compare_button.grid(row=5, column=0, columnspan=3, padx=10, pady=10, sticky="ew")

root.mainloop()
