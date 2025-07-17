# Hackathon/app_ui.py
import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import pandas as pd # For loading data in UI
from pathlib import Path

# Import clean_data script
from clean_data import clean_and_transform_data

# Import analysis functions from analyze_data folder
# (Ensure these names match the function definitions in the respective files)
from analyze_data.analysis_anc import generate_anc_impact_plot
from analyze_data.analysis_referral import generate_referral_patterns_plot
from analyze_data.analysis_birth_spacing import generate_birth_spacing_impact_plot
from analyze_data.analysis_health_worker import generate_health_worker_impact_plot
from analyze_data.analysis_patient_preference import generate_patient_preference_plot
from analyze_data.analysis_time_of_day_week import generate_time_of_day_week_heatmap


class MaternalDeliveryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Maternal Delivery Analysis") # Updated title
        self.root.geometry("800x600")
        self.root.configure(bg="#FFC0CB") # Light pink background

        # Try to set Algerian font, fallback if not available
        try:
            self.title_font = ("Algerian", 36, "bold")
            self.button_font = ("Algerian", 16)
        except tk.TclError:
            self.title_font = ("Arial", 36, "bold")
            self.button_font = ("Arial", 16)
            print("Warning: Algerian font not found. Falling back to Arial.")

        self.df = None # DataFrame will be loaded here

        self._create_initial_page()

    def _create_initial_page(self):
        # Clear any existing widgets
        for widget in self.root.winfo_children():
            widget.destroy()

        self.root.title("Maternal Delivery Analysis") # Ensure title is set for this page

        title_label = tk.Label(self.root, text="Maternal Delivery Analysis",
                               font=self.title_font, fg="black", bg="#FFC0CB")
        title_label.pack(pady=100)

        enter_button = tk.Button(self.root, text="ENTER",
                                 font=self.button_font, fg="black", bg="#FF69B4", # Dark pink button
                                 command=self._enter_main_menu)
        enter_button.pack(pady=50, ipadx=20, ipady=10)

    def _enter_main_menu(self):
        # Clear initial page widgets
        for widget in self.root.winfo_children():
            widget.destroy()

        self.root.title("Analysis Menu")
        self.root.configure(bg="#FFC0CB") # Light pink background for menu

        # Data Management Frame
        data_frame = ttk.LabelFrame(self.root, text="Data Management", padding="10")
        data_frame.pack(pady=10, padx=10, fill="x")

        ttk.Button(data_frame, text="Clean/Prepare Data", command=self._run_clean_data).pack(side="left", padx=5, pady=5)
        ttk.Button(data_frame, text="Load Clean Data", command=self._load_clean_data).pack(side="left", padx=5, pady=5)
        self.data_status_label = ttk.Label(data_frame, text="Data Status: Not Loaded", background="#FFC0CB", foreground="black") # Use background/foreground
        self.data_status_label.pack(side="left", padx=10)

        # Analysis Buttons Frame
        analysis_buttons_frame = tk.Frame(self.root, bg="#FFC0CB")
        analysis_buttons_frame.pack(pady=20, padx=20, fill="both", expand=True)

        # Define the analysis buttons with their corresponding functions
        # These map directly to the 6 selected analysis types
        self.analysis_map = {
            "ANC Visits & Delivery Type": generate_anc_impact_plot,
            "Referral Patterns & C-section Rates": generate_referral_patterns_plot,
            "Birth Spacing (IDI) Impact": generate_birth_spacing_impact_plot,
            "Health Worker Density Impact": generate_health_worker_impact_plot,
            "Patient Preference & Delivery Type": generate_patient_preference_plot,
            "Time of Day/Week Analysis (Heatmap)": generate_time_of_day_week_heatmap,
        }

        # Create buttons in a grid layout
        row = 0
        col = 0
        for text, func in self.analysis_map.items():
            button = tk.Button(analysis_buttons_frame, text=text,
                               font=self.button_font, fg="black", bg="#FF69B4", # Dark pink boxes
                               width=30, height=5,
                               command=lambda f=func: self._show_plot(f, text)) # Pass text for window title
            button.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")
            col += 1
            if col > 1: # 2 buttons per row
                col = 0
                row += 1
        
        # Make grid cells expand proportionally
        for i in range(2):
            analysis_buttons_frame.grid_columnconfigure(i, weight=1)
        for i in range(row + 1):
            analysis_buttons_frame.grid_rowconfigure(i, weight=1)

        # Initial check for clean data
        self._load_clean_data_on_start()

    def _run_clean_data(self):
        """Runs the clean_data.py script to generate clean_data.csv."""
        self.data_status_label.config(text="Data Status: Cleaning/Preparing data (this may take a moment)...")
        self.root.update_idletasks() # Update GUI to show message
        try:
            df_cleaned = clean_and_transform_data()
            if df_cleaned is not None:
                self.df = df_cleaned
                self.data_status_label.config(text=f"Data Status: Cleaned & Loaded {len(self.df)} records.")
                messagebox.showinfo("Data Prepared", f"Data cleaned and saved to data/clean_data.csv. Loaded {len(self.df)} records.")
            else:
                self.data_status_label.config(text="Data Status: Cleaning failed. Check console for errors.")
        except Exception as e:
            messagebox.showerror("Cleaning Error", f"An error occurred during data cleaning: {e}\nCheck console for details.")
            self.data_status_label.config(text="Data Status: Error cleaning")
            print(f"Error during data cleaning: {e}")

    def _load_clean_data_on_start(self):
        """Attempts to load clean_data.csv when the main menu is entered."""
        self.data_status_label.config(text="Data Status: Attempting to load clean_data.csv...")
        try:
            BASE_DIR = Path(__file__).resolve().parent
            clean_data_path = BASE_DIR / 'data' / 'clean_data.csv'
            self.df = pd.read_csv(clean_data_path)
            self.data_status_label.config(text=f"Data Status: Loaded {len(self.df)} records from clean_data.csv.")
        except FileNotFoundError:
            self.data_status_label.config(text="Data Status: clean_data.csv not found. Please 'Clean/Prepare Data'.")
            messagebox.showwarning("Data Not Found", "clean_data.csv not found. Please click 'Clean/Prepare Data' first.")
        except Exception as e:
            messagebox.showerror("Loading Error", f"An error occurred during data load: {e}\nCheck console for details.")
            self.data_status_label.config(text="Data Status: Error loading")
            print(f"Error loading clean data: {e}")

    def _load_clean_data(self):
        """Button command to explicitly load clean_data.csv."""
        self._load_clean_data_on_start()

    def _show_plot(self, analysis_func, plot_title_text):
        if self.df is None:
            messagebox.showwarning("No Data", "Please load or prepare data first.")
            return

        try:
            # Generate the plot figure
            fig = analysis_func(self.df.copy()) # Pass a copy to analysis functions

            # Create a new top-level window for the plot
            plot_window = tk.Toplevel(self.root)
            plot_window.title(f"Analysis: {plot_title_text}") # Use descriptive title
            plot_window.geometry("1000x800") # Adjust size for plots
            plot_window.configure(bg="#FFC0CB") # Light pink background

            # Embed the matplotlib figure in the Tkinter window
            canvas = FigureCanvasTkAgg(fig, master=plot_window)
            canvas_widget = canvas.get_tk_widget()
            canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

            # Add Matplotlib toolbar
            toolbar = NavigationToolbar2Tk(canvas, plot_window)
            toolbar.update()
            canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

            # Back button
            back_button = tk.Button(plot_window, text="BACK",
                                    font=self.button_font, fg="black", bg="#FF69B4",
                                    command=plot_window.destroy) # Destroys the plot window
            back_button.pack(pady=10)

            plot_window.grab_set() # Make this window modal
            self.root.wait_window(plot_window) # Wait for this window to close
            plt.close(fig) # Close the matplotlib figure to free memory

        except Exception as e:
            messagebox.showerror("Plot Error", f"An error occurred while generating the plot: {e}\nCheck console for details.")
            print(f"Error in {analysis_func.__name__}: {e}")
            plt.close('all') # Close any potentially open matplotlib figures

if __name__ == "__main__":
    root = tk.Tk()
    app = MaternalDeliveryApp(root)
    root.mainloop()