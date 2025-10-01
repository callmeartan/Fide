"""
FIDE Player Data Extractor - GUI Application
A user-friendly graphical interface for extracting FIDE player data
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog, scrolledtext
import threading
import pandas as pd
from datetime import datetime
import json
import csv
from fide_extractor import FIDEDataExtractor


class FIDEExtractorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("FIDE Player Data Extractor")
        self.root.geometry("1000x700")
        self.root.resizable(True, True)
        
        # Initialize extractor
        self.extractor = FIDEDataExtractor()
        self.players_data = []
        
        # Configure style
        self.setup_styles()
        
        # Create GUI components
        self.create_widgets()
        
    def setup_styles(self):
        """Setup custom styles for the GUI"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configure colors
        style.configure('Title.TLabel', font=('Helvetica', 16, 'bold'), foreground='#2c3e50')
        style.configure('Header.TLabel', font=('Helvetica', 10, 'bold'), foreground='#34495e')
        style.configure('Action.TButton', font=('Helvetica', 10), padding=10)
        
    def create_widgets(self):
        """Create all GUI widgets"""
        
        # Title
        title_frame = ttk.Frame(self.root, padding="10")
        title_frame.pack(fill=tk.X)
        
        title_label = ttk.Label(
            title_frame,
            text="♟️ FIDE Player Data Extractor",
            style='Title.TLabel'
        )
        title_label.pack()
        
        # Input Section
        input_frame = ttk.LabelFrame(self.root, text="Input FIDE IDs or Player Names", padding="10")
        input_frame.pack(fill=tk.BOTH, expand=False, padx=10, pady=5)
        
        # Instructions
        instructions = ttk.Label(
            input_frame,
            text="Enter FIDE IDs (numbers) or player names, one per line:",
            style='Header.TLabel'
        )
        instructions.pack(anchor=tk.W, pady=(0, 5))
        
        # Input text area
        self.input_text = scrolledtext.ScrolledText(
            input_frame,
            height=8,
            font=('Courier', 10),
            wrap=tk.WORD
        )
        self.input_text.pack(fill=tk.BOTH, expand=True)
        
        # Add placeholder text
        placeholder = "Example:\n22538496\n12528374\nMagnus Carlsen\nGukesh D"
        self.input_text.insert('1.0', placeholder)
        self.input_text.config(fg='gray')
        
        # Bind events for placeholder
        self.input_text.bind('<FocusIn>', self.on_input_focus_in)
        self.input_text.bind('<FocusOut>', self.on_input_focus_out)
        
        # Buttons Frame
        button_frame = ttk.Frame(self.root, padding="10")
        button_frame.pack(fill=tk.X)
        
        # Extract button
        self.extract_btn = ttk.Button(
            button_frame,
            text="🔍 Extract Data",
            command=self.extract_data,
            style='Action.TButton'
        )
        self.extract_btn.pack(side=tk.LEFT, padx=5)
        
        # Clear button
        self.clear_btn = ttk.Button(
            button_frame,
            text="🗑️ Clear",
            command=self.clear_all,
            style='Action.TButton'
        )
        self.clear_btn.pack(side=tk.LEFT, padx=5)
        
        # Export buttons
        ttk.Label(button_frame, text="Export to:", font=('Helvetica', 10, 'bold')).pack(side=tk.LEFT, padx=(20, 5))
        
        self.export_excel_btn = ttk.Button(
            button_frame,
            text="📊 Excel",
            command=lambda: self.export_data('excel'),
            state=tk.DISABLED
        )
        self.export_excel_btn.pack(side=tk.LEFT, padx=2)
        
        self.export_csv_btn = ttk.Button(
            button_frame,
            text="📄 CSV",
            command=lambda: self.export_data('csv'),
            state=tk.DISABLED
        )
        self.export_csv_btn.pack(side=tk.LEFT, padx=2)
        
        self.export_json_btn = ttk.Button(
            button_frame,
            text="📋 JSON",
            command=lambda: self.export_data('json'),
            state=tk.DISABLED
        )
        self.export_json_btn.pack(side=tk.LEFT, padx=2)
        
        # Progress bar
        self.progress_frame = ttk.Frame(self.root)
        self.progress_frame.pack(fill=tk.X, padx=10, pady=5)
        
        self.progress_label = ttk.Label(self.progress_frame, text="")
        self.progress_label.pack(side=tk.LEFT)
        
        self.progress_bar = ttk.Progressbar(
            self.progress_frame,
            mode='indeterminate',
            length=300
        )
        
        # Results Section
        results_frame = ttk.LabelFrame(self.root, text="Extracted Data", padding="10")
        results_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # Create Treeview for displaying data
        self.create_treeview(results_frame)
        
        # Status bar
        self.status_bar = ttk.Label(
            self.root,
            text="Ready",
            relief=tk.SUNKEN,
            anchor=tk.W,
            padding=(5, 2)
        )
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        
    def create_treeview(self, parent):
        """Create a treeview to display player data"""
        
        # Create frame for treeview and scrollbar
        tree_frame = ttk.Frame(parent)
        tree_frame.pack(fill=tk.BOTH, expand=True)
        
        # Scrollbars
        vsb = ttk.Scrollbar(tree_frame, orient="vertical")
        hsb = ttk.Scrollbar(tree_frame, orient="horizontal")
        
        # Treeview
        self.tree = ttk.Treeview(
            tree_frame,
            columns=('FIDE ID', 'Name', 'Federation', 'Title', 'B-Year', 'Std', 'Rapid', 'Blitz'),
            show='headings',
            yscrollcommand=vsb.set,
            xscrollcommand=hsb.set
        )
        
        vsb.config(command=self.tree.yview)
        hsb.config(command=self.tree.xview)
        
        # Define columns
        columns = {
            'FIDE ID': 80,
            'Name': 180,
            'Federation': 80,
            'Title': 60,
            'B-Year': 70,
            'Std': 70,
            'Rapid': 70,
            'Blitz': 70
        }
        
        for col, width in columns.items():
            self.tree.heading(col, text=col)
            self.tree.column(col, width=width, anchor=tk.CENTER if col != 'Name' else tk.W)
        
        # Pack everything
        self.tree.grid(row=0, column=0, sticky='nsew')
        vsb.grid(row=0, column=1, sticky='ns')
        hsb.grid(row=1, column=0, sticky='ew')
        
        tree_frame.grid_rowconfigure(0, weight=1)
        tree_frame.grid_columnconfigure(0, weight=1)
        
        # Add alternating row colors
        self.tree.tag_configure('oddrow', background='#f9f9f9')
        self.tree.tag_configure('evenrow', background='#ffffff')
        
    def on_input_focus_in(self, event):
        """Remove placeholder text when input is focused"""
        if self.input_text.get('1.0', tk.END).strip().startswith('Example:'):
            self.input_text.delete('1.0', tk.END)
            self.input_text.config(fg='black')
            
    def on_input_focus_out(self, event):
        """Add placeholder text if input is empty"""
        if not self.input_text.get('1.0', tk.END).strip():
            placeholder = "Example:\n22538496\n12528374\nMagnus Carlsen\nGukesh D"
            self.input_text.insert('1.0', placeholder)
            self.input_text.config(fg='gray')
            
    def extract_data(self):
        """Extract FIDE player data"""
        
        # Get input
        input_text = self.input_text.get('1.0', tk.END).strip()
        
        # Check if placeholder
        if input_text.startswith('Example:') or not input_text:
            messagebox.showwarning(
                "No Input",
                "Please enter FIDE IDs or player names!"
            )
            return
        
        # Parse identifiers
        identifiers = [line.strip() for line in input_text.split('\n') if line.strip()]
        
        if not identifiers:
            messagebox.showwarning(
                "No Input",
                "Please enter at least one FIDE ID or player name!"
            )
            return
        
        # Disable buttons
        self.set_buttons_state(tk.DISABLED)
        
        # Show progress
        self.progress_label.config(text=f"Extracting data for {len(identifiers)} player(s)...")
        self.progress_bar.pack(side=tk.LEFT, padx=10)
        self.progress_bar.start(10)
        
        # Run extraction in a separate thread
        thread = threading.Thread(target=self._extract_thread, args=(identifiers,))
        thread.daemon = True
        thread.start()
        
    def _extract_thread(self, identifiers):
        """Thread function for extracting data"""
        try:
            # Extract data
            self.players_data = self.extractor.extract_multiple_players(identifiers)
            
            # Update GUI in main thread
            self.root.after(0, self._update_results)
            
        except Exception as e:
            self.root.after(0, lambda: self._show_error(str(e)))
            
    def _update_results(self):
        """Update the results treeview"""
        
        # Stop progress bar
        self.progress_bar.stop()
        self.progress_bar.pack_forget()
        self.progress_label.config(text="")
        
        # Enable buttons
        self.set_buttons_state(tk.NORMAL)
        
        # Clear existing data
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Check if data was extracted
        if not self.players_data:
            messagebox.showwarning(
                "No Data",
                "Could not extract any player data. Please check the FIDE IDs/names."
            )
            self.status_bar.config(text="No data extracted")
            return
        
        # Add data to treeview
        for idx, player in enumerate(self.players_data):
            tag = 'evenrow' if idx % 2 == 0 else 'oddrow'
            self.tree.insert('', tk.END, values=(
                player.get('FIDE ID', 'N/A'),
                player.get('Name', 'N/A'),
                player.get('Federation', 'N/A'),
                player.get('Title', 'N/A'),
                player.get('B-Year', 'N/A'),
                player.get('Rating std', 'N/A'),
                player.get('Rating rapid', 'N/A'),
                player.get('Rating blitz', 'N/A')
            ), tags=(tag,))
        
        # Enable export buttons
        self.export_excel_btn.config(state=tk.NORMAL)
        self.export_csv_btn.config(state=tk.NORMAL)
        self.export_json_btn.config(state=tk.NORMAL)
        
        # Update status
        self.status_bar.config(text=f"Successfully extracted {len(self.players_data)} player(s)")
        
        messagebox.showinfo(
            "Success",
            f"Successfully extracted data for {len(self.players_data)} player(s)!"
        )
        
    def _show_error(self, error_msg):
        """Show error message"""
        self.progress_bar.stop()
        self.progress_bar.pack_forget()
        self.progress_label.config(text="")
        self.set_buttons_state(tk.NORMAL)
        
        messagebox.showerror("Error", f"An error occurred:\n{error_msg}")
        self.status_bar.config(text="Error occurred")
        
    def export_data(self, format_type):
        """Export data to specified format"""
        
        if not self.players_data:
            messagebox.showwarning("No Data", "No data to export!")
            return
        
        # Create default filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # File dialog based on format
        if format_type == 'excel':
            filename = filedialog.asksaveasfilename(
                defaultextension=".xlsx",
                filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")],
                initialfile=f"fide_players_{timestamp}.xlsx"
            )
            if filename:
                self._export_excel(filename)
                
        elif format_type == 'csv':
            filename = filedialog.asksaveasfilename(
                defaultextension=".csv",
                filetypes=[("CSV files", "*.csv"), ("All files", "*.*")],
                initialfile=f"fide_players_{timestamp}.csv"
            )
            if filename:
                self._export_csv(filename)
                
        elif format_type == 'json':
            filename = filedialog.asksaveasfilename(
                defaultextension=".json",
                filetypes=[("JSON files", "*.json"), ("All files", "*.*")],
                initialfile=f"fide_players_{timestamp}.json"
            )
            if filename:
                self._export_json(filename)
                
    def _export_excel(self, filename):
        """Export to Excel"""
        try:
            df = pd.DataFrame(self.players_data)
            df.to_excel(filename, index=False, engine='openpyxl')
            messagebox.showinfo("Success", f"Data exported to:\n{filename}")
            self.status_bar.config(text=f"Exported to Excel: {filename}")
        except Exception as e:
            messagebox.showerror("Export Error", f"Failed to export to Excel:\n{str(e)}")
            
    def _export_csv(self, filename):
        """Export to CSV"""
        try:
            df = pd.DataFrame(self.players_data)
            df.to_csv(filename, index=False, encoding='utf-8')
            messagebox.showinfo("Success", f"Data exported to:\n{filename}")
            self.status_bar.config(text=f"Exported to CSV: {filename}")
        except Exception as e:
            messagebox.showerror("Export Error", f"Failed to export to CSV:\n{str(e)}")
            
    def _export_json(self, filename):
        """Export to JSON"""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(self.players_data, f, indent=2, ensure_ascii=False)
            messagebox.showinfo("Success", f"Data exported to:\n{filename}")
            self.status_bar.config(text=f"Exported to JSON: {filename}")
        except Exception as e:
            messagebox.showerror("Export Error", f"Failed to export to JSON:\n{str(e)}")
            
    def clear_all(self):
        """Clear all data and reset the interface"""
        
        # Clear input
        self.input_text.delete('1.0', tk.END)
        placeholder = "Example:\n22538496\n12528374\nMagnus Carlsen\nGukesh D"
        self.input_text.insert('1.0', placeholder)
        self.input_text.config(fg='gray')
        
        # Clear treeview
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Clear data
        self.players_data = []
        
        # Disable export buttons
        self.export_excel_btn.config(state=tk.DISABLED)
        self.export_csv_btn.config(state=tk.DISABLED)
        self.export_json_btn.config(state=tk.DISABLED)
        
        # Update status
        self.status_bar.config(text="Ready")
        
    def set_buttons_state(self, state):
        """Enable or disable all buttons"""
        self.extract_btn.config(state=state)
        self.clear_btn.config(state=state)


def main():
    """Main function to run the GUI application"""
    root = tk.Tk()
    app = FIDEExtractorGUI(root)
    
    # Center window on screen
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')
    
    root.mainloop()


if __name__ == "__main__":
    main()


