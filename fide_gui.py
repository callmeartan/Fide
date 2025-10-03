"""
FIDE Player Data Extractor - Modern GUI Application
Professional interface for extracting FIDE player data
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog, scrolledtext
import threading
import pandas as pd
from datetime import datetime
import json
from fide_extractor import FIDEDataExtractor


class ModernButton(tk.Canvas):
    """Custom modern button with hover effects"""
    def __init__(self, parent, text, command, bg_color, hover_color, text_color="white", width=120, height=40):
        super().__init__(parent, width=width, height=height, bg=parent['bg'], highlightthickness=0)
        
        self.bg_color = bg_color
        self.hover_color = hover_color
        self.text_color = text_color
        self.command = command
        self.is_enabled = True
        
        # Draw button
        self.rect = self.create_rectangle(0, 0, width, height, fill=bg_color, outline="", width=0)
        self.text_id = self.create_text(width/2, height/2, text=text, fill=text_color, 
                                       font=('SF Pro Display', 11, 'bold'))
        
        # Bind events
        self.bind('<Button-1>', self._on_click)
        self.bind('<Enter>', self._on_enter)
        self.bind('<Leave>', self._on_leave)
        
    def _on_enter(self, event):
        if self.is_enabled:
            self.itemconfig(self.rect, fill=self.hover_color)
            
    def _on_leave(self, event):
        if self.is_enabled:
            self.itemconfig(self.rect, fill=self.bg_color)
            
    def _on_click(self, event):
        if self.is_enabled and self.command:
            self.command()
    
    def set_enabled(self, enabled):
        self.is_enabled = enabled
        if enabled:
            self.itemconfig(self.rect, fill=self.bg_color)
            self.itemconfig(self.text_id, fill=self.text_color)
        else:
            self.itemconfig(self.rect, fill='#CCCCCC')
            self.itemconfig(self.text_id, fill='#888888')


class FIDEExtractorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("FIDE Player Data Extractor")
        self.root.geometry("1100x750")
        self.root.resizable(True, True)
        
        # Color scheme - Modern professional
        self.colors = {
            'bg': '#F5F7FA',
            'primary': '#2563EB',      # Blue
            'primary_hover': '#1D4ED8',
            'success': '#10B981',       # Green
            'success_hover': '#059669',
            'danger': '#EF4444',        # Red
            'danger_hover': '#DC2626',
            'secondary': '#6B7280',     # Gray
            'secondary_hover': '#4B5563',
            'card': '#FFFFFF',
            'border': '#E5E7EB',
            'text': '#1F2937',
            'text_secondary': '#6B7280',
            'input_bg': '#F9FAFB',
        }
        
        self.root.configure(bg=self.colors['bg'])
        
        # Initialize extractor
        self.extractor = FIDEDataExtractor()
        self.players_data = []
        
        # Placeholder state
        self.placeholder_text = "22538496\n12528374\nMagnus Carlsen\nGukesh D"
        self.is_placeholder = True
        
        # Create GUI components
        self.create_widgets()
        
    def create_widgets(self):
        """Create all GUI widgets with modern design"""
        
        # Main container with padding
        main_container = tk.Frame(self.root, bg=self.colors['bg'])
        main_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Header
        self.create_header(main_container)
        
        # Content area
        content = tk.Frame(main_container, bg=self.colors['bg'])
        content.pack(fill=tk.BOTH, expand=True, pady=(15, 0))
        
        # Input card
        self.create_input_section(content)
        
        # Action buttons
        self.create_action_buttons(content)
        
        # Results section
        self.create_results_section(content)
        
        # Footer status
        self.create_footer(main_container)
        
    def create_header(self, parent):
        """Create modern header"""
        header = tk.Frame(parent, bg=self.colors['card'], height=80)
        header.pack(fill=tk.X, pady=(0, 15))
        header.pack_propagate(False)
        
        # Add subtle shadow effect
        shadow = tk.Frame(parent, bg='#E5E7EB', height=1)
        shadow.place(in_=header, relx=0, rely=1, relwidth=1)
        
        header_content = tk.Frame(header, bg=self.colors['card'])
        header_content.pack(expand=True, fill=tk.BOTH, padx=25, pady=15)
        
        # Title
        title = tk.Label(
            header_content,
            text="♟ FIDE Player Data Extractor",
            font=('SF Pro Display', 24, 'bold'),
            bg=self.colors['card'],
            fg=self.colors['text']
        )
        title.pack(side=tk.LEFT)
        
        # Subtitle
        subtitle = tk.Label(
            header_content,
            text="Extract chess player data from FIDE database",
            font=('SF Pro Display', 11),
            bg=self.colors['card'],
            fg=self.colors['text_secondary']
        )
        subtitle.pack(side=tk.LEFT, padx=(15, 0))
        
    def create_input_section(self, parent):
        """Create input card"""
        # Card frame
        card = tk.Frame(parent, bg=self.colors['card'], relief=tk.FLAT)
        card.pack(fill=tk.BOTH, expand=False, pady=(0, 15))
        
        # Card header
        card_header = tk.Frame(card, bg=self.colors['card'])
        card_header.pack(fill=tk.X, padx=25, pady=(20, 10))
        
        tk.Label(
            card_header,
            text="Input",
            font=('SF Pro Display', 14, 'bold'),
            bg=self.colors['card'],
            fg=self.colors['text']
        ).pack(side=tk.LEFT)
        
        tk.Label(
            card_header,
            text="Enter FIDE IDs or player names, one per line",
            font=('SF Pro Display', 10),
            bg=self.colors['card'],
            fg=self.colors['text_secondary']
        ).pack(side=tk.LEFT, padx=(10, 0))
        
        # Input frame
        input_frame = tk.Frame(card, bg=self.colors['card'])
        input_frame.pack(fill=tk.BOTH, expand=False, padx=25, pady=(0, 20))
        
        # Custom text widget with modern styling
        text_frame = tk.Frame(input_frame, bg=self.colors['border'], relief=tk.FLAT)
        text_frame.pack(fill=tk.BOTH, expand=False)
        
        self.input_text = tk.Text(
            text_frame,
            height=6,
            font=('SF Mono', 11),
            bg=self.colors['input_bg'],
            fg=self.colors['text'],
            relief=tk.FLAT,
            borderwidth=0,
            padx=15,
            pady=12,
            insertbackground=self.colors['primary'],
            selectbackground=self.colors['primary'],
            selectforeground='white'
        )
        self.input_text.pack(fill=tk.BOTH, expand=True, padx=1, pady=1)
        
        # Placeholder
        self.input_text.insert('1.0', self.placeholder_text)
        self.input_text.config(fg=self.colors['text_secondary'])
        self.is_placeholder = True
        
        # Placeholder events
        self.input_text.bind('<FocusIn>', self.on_input_focus_in)
        self.input_text.bind('<FocusOut>', self.on_input_focus_out)
        
    def create_action_buttons(self, parent):
        """Create modern action buttons"""
        button_frame = tk.Frame(parent, bg=self.colors['bg'])
        button_frame.pack(fill=tk.X, pady=(0, 15))
        
        # Left side - main actions
        left_buttons = tk.Frame(button_frame, bg=self.colors['bg'])
        left_buttons.pack(side=tk.LEFT)
        
        # Extract button (primary)
        self.extract_btn = ModernButton(
            left_buttons,
            text="Extract Data",
            command=self.extract_data,
            bg_color=self.colors['primary'],
            hover_color=self.colors['primary_hover'],
            width=140,
            height=42
        )
        self.extract_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        # Clear button (secondary)
        self.clear_btn = ModernButton(
            left_buttons,
            text="Clear",
            command=self.clear_all,
            bg_color=self.colors['secondary'],
            hover_color=self.colors['secondary_hover'],
            width=100,
            height=42
        )
        self.clear_btn.pack(side=tk.LEFT)
        
        # Right side - export buttons
        right_buttons = tk.Frame(button_frame, bg=self.colors['bg'])
        right_buttons.pack(side=tk.RIGHT)
        
        tk.Label(
            right_buttons,
            text="Export:",
            font=('SF Pro Display', 11, 'bold'),
            bg=self.colors['bg'],
            fg=self.colors['text']
        ).pack(side=tk.LEFT, padx=(0, 10))
        
        # Export buttons
        self.export_excel_btn = ModernButton(
            right_buttons,
            text="Excel",
            command=lambda: self.export_data('excel'),
            bg_color=self.colors['success'],
            hover_color=self.colors['success_hover'],
            width=90,
            height=42
        )
        self.export_excel_btn.pack(side=tk.LEFT, padx=(0, 8))
        self.export_excel_btn.set_enabled(False)
        
        self.export_csv_btn = ModernButton(
            right_buttons,
            text="CSV",
            command=lambda: self.export_data('csv'),
            bg_color=self.colors['success'],
            hover_color=self.colors['success_hover'],
            width=90,
            height=42
        )
        self.export_csv_btn.pack(side=tk.LEFT, padx=(0, 8))
        self.export_csv_btn.set_enabled(False)
        
        self.export_json_btn = ModernButton(
            right_buttons,
            text="JSON",
            command=lambda: self.export_data('json'),
            bg_color=self.colors['success'],
            hover_color=self.colors['success_hover'],
            width=90,
            height=42
        )
        self.export_json_btn.pack(side=tk.LEFT)
        self.export_json_btn.set_enabled(False)
        
        # Progress section
        self.progress_frame = tk.Frame(parent, bg=self.colors['bg'])
        self.progress_frame.pack(fill=tk.X, pady=(0, 15))
        
        self.progress_label = tk.Label(
            self.progress_frame,
            text="",
            font=('SF Pro Display', 10),
            bg=self.colors['bg'],
            fg=self.colors['text_secondary']
        )
        self.progress_label.pack(side=tk.LEFT)
        
        style = ttk.Style()
        style.theme_use('clam')
        style.configure(
            "Custom.Horizontal.TProgressbar",
            troughcolor=self.colors['border'],
            background=self.colors['primary'],
            borderwidth=0,
            thickness=4
        )
        
        self.progress_bar = ttk.Progressbar(
            self.progress_frame,
            mode='indeterminate',
            length=300,
            style="Custom.Horizontal.TProgressbar"
        )
        
    def create_results_section(self, parent):
        """Create results table section"""
        # Results card
        results_card = tk.Frame(parent, bg=self.colors['card'])
        results_card.pack(fill=tk.BOTH, expand=True)
        
        # Card header
        results_header = tk.Frame(results_card, bg=self.colors['card'])
        results_header.pack(fill=tk.X, padx=25, pady=(20, 15))
        
        tk.Label(
            results_header,
            text="Results",
            font=('SF Pro Display', 14, 'bold'),
            bg=self.colors['card'],
            fg=self.colors['text']
        ).pack(side=tk.LEFT)
        
        self.results_count = tk.Label(
            results_header,
            text="0 players",
            font=('SF Pro Display', 10),
            bg=self.colors['card'],
            fg=self.colors['text_secondary']
        )
        self.results_count.pack(side=tk.LEFT, padx=(10, 0))
        
        # Table container
        table_container = tk.Frame(results_card, bg=self.colors['card'])
        table_container.pack(fill=tk.BOTH, expand=True, padx=25, pady=(0, 20))
        
        # Create Treeview with custom style
        self.create_treeview(table_container)
        
    def create_treeview(self, parent):
        """Create modern styled treeview"""
        # Style configuration
        style = ttk.Style()
        
        # Treeview style
        style.configure(
            "Custom.Treeview",
            background=self.colors['card'],
            foreground=self.colors['text'],
            fieldbackground=self.colors['card'],
            borderwidth=0,
            font=('SF Pro Display', 10)
        )
        
        style.configure(
            "Custom.Treeview.Heading",
            background=self.colors['input_bg'],
            foreground=self.colors['text'],
            borderwidth=0,
            font=('SF Pro Display', 10, 'bold')
        )
        
        style.map('Custom.Treeview',
                 background=[('selected', self.colors['primary'])],
                 foreground=[('selected', 'white')])
        
        # Frame for tree and scrollbars
        tree_frame = tk.Frame(parent, bg=self.colors['border'])
        tree_frame.pack(fill=tk.BOTH, expand=True)
        
        # Scrollbars
        vsb = ttk.Scrollbar(tree_frame, orient="vertical")
        hsb = ttk.Scrollbar(tree_frame, orient="horizontal")
        
        # Treeview
        columns = ('FIDE ID', 'Name', 'Federation', 'Title', 'B-Year', 'Age', 'Std', 'Rapid', 'Blitz')
        self.tree = ttk.Treeview(
            tree_frame,
            columns=columns,
            show='headings',
            yscrollcommand=vsb.set,
            xscrollcommand=hsb.set,
            style="Custom.Treeview",
            height=15
        )
        
        vsb.config(command=self.tree.yview)
        hsb.config(command=self.tree.xview)
        
        # Column configuration
        column_widths = {
            'FIDE ID': 90,
            'Name': 200,
            'Federation': 90,
            'Title': 60,
            'B-Year': 70,
            'Age': 50,
            'Std': 70,
            'Rapid': 70,
            'Blitz': 70
        }
        
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=column_widths[col], anchor='center' if col != 'Name' else 'w')
        
        # Grid layout
        self.tree.grid(row=0, column=0, sticky='nsew', padx=1, pady=1)
        vsb.grid(row=0, column=1, sticky='ns')
        hsb.grid(row=1, column=0, sticky='ew')
        
        tree_frame.grid_rowconfigure(0, weight=1)
        tree_frame.grid_columnconfigure(0, weight=1)
        
        # Row colors
        self.tree.tag_configure('evenrow', background='#F9FAFB')
        self.tree.tag_configure('oddrow', background=self.colors['card'])
        
    def create_footer(self, parent):
        """Create footer status bar"""
        footer = tk.Frame(parent, bg=self.colors['card'], height=45)
        footer.pack(fill=tk.X, pady=(15, 0))
        footer.pack_propagate(False)
        
        # Top border
        border = tk.Frame(footer, bg=self.colors['border'], height=1)
        border.pack(fill=tk.X)
        
        # Status content
        status_content = tk.Frame(footer, bg=self.colors['card'])
        status_content.pack(fill=tk.BOTH, expand=True, padx=25)
        
        self.status_bar = tk.Label(
            status_content,
            text="Ready to extract player data",
            font=('SF Pro Display', 10),
            bg=self.colors['card'],
            fg=self.colors['text_secondary'],
            anchor=tk.W
        )
        self.status_bar.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, pady=12)
        
    def on_input_focus_in(self, event):
        """Remove placeholder on focus"""
        if self.is_placeholder:
            self.input_text.delete('1.0', tk.END)
            self.input_text.config(fg=self.colors['text'])
            self.is_placeholder = False
            
    def on_input_focus_out(self, event):
        """Add placeholder if empty"""
        if not self.input_text.get('1.0', tk.END).strip():
            self.input_text.insert('1.0', self.placeholder_text)
            self.input_text.config(fg=self.colors['text_secondary'])
            self.is_placeholder = True
            
    def extract_data(self):
        """Extract FIDE player data"""
        # Check if placeholder is still showing
        if self.is_placeholder:
            messagebox.showwarning("No Input", "Please enter FIDE IDs or player names!")
            return
        
        input_text = self.input_text.get('1.0', tk.END).strip()
        
        if not input_text:
            messagebox.showwarning("No Input", "Please enter FIDE IDs or player names!")
            return
        
        identifiers = [line.strip() for line in input_text.split('\n') if line.strip()]
        
        if not identifiers:
            messagebox.showwarning("No Input", "Please enter at least one FIDE ID or player name!")
            return
        
        # Disable buttons
        self.set_buttons_state(False)
        
        # Show progress
        self.progress_label.config(text=f"Extracting data for {len(identifiers)} player(s)...")
        self.progress_bar.pack(side=tk.LEFT, padx=(10, 0))
        self.progress_bar.start(10)
        
        # Run extraction in thread
        thread = threading.Thread(target=self._extract_thread, args=(identifiers,))
        thread.daemon = True
        thread.start()
        
    def _extract_thread(self, identifiers):
        """Thread function for extracting data"""
        try:
            self.players_data = self.extractor.extract_multiple_players(identifiers)
            self.root.after(0, self._update_results)
        except Exception as e:
            self.root.after(0, lambda: self._show_error(str(e)))
            
    def _update_results(self):
        """Update results table"""
        self.progress_bar.stop()
        self.progress_bar.pack_forget()
        self.progress_label.config(text="")
        
        self.set_buttons_state(True)
        
        # Clear existing
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        if not self.players_data:
            messagebox.showwarning("No Data", "Could not extract any player data. Please check the FIDE IDs/names.")
            self.status_bar.config(text="No data extracted")
            self.results_count.config(text="0 players")
            return
        
        # Add data
        for idx, player in enumerate(self.players_data):
            tag = 'evenrow' if idx % 2 == 0 else 'oddrow'
            # Replace N/A with empty string for display
            self.tree.insert('', tk.END, values=(
                player.get('FIDE ID', ''),
                player.get('Name', ''),
                player.get('Federation', ''),
                player.get('Title', ''),
                player.get('B-Year', ''),
                player.get('Age', ''),
                player.get('Rating std', ''),
                player.get('Rating rapid', ''),
                player.get('Rating blitz', '')
            ), tags=(tag,))
        
        # Enable export
        self.export_excel_btn.set_enabled(True)
        self.export_csv_btn.set_enabled(True)
        self.export_json_btn.set_enabled(True)
        
        # Update status
        count = len(self.players_data)
        self.status_bar.config(text=f"✓ Successfully extracted {count} player(s)")
        self.results_count.config(text=f"{count} player{'s' if count != 1 else ''}")
        
        messagebox.showinfo("Success", f"Successfully extracted data for {count} player(s)!")
        
    def _show_error(self, error_msg):
        """Show error message"""
        self.progress_bar.stop()
        self.progress_bar.pack_forget()
        self.progress_label.config(text="")
        self.set_buttons_state(True)
        
        messagebox.showerror("Error", f"An error occurred:\n{error_msg}")
        self.status_bar.config(text="Error occurred")
        
    def export_data(self, format_type):
        """Export data to specified format"""
        if not self.players_data:
            messagebox.showwarning("No Data", "No data to export!")
            return
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
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
            # Replace N/A with empty strings
            df = df.replace('N/A', '')
            df.to_excel(filename, index=False, engine='openpyxl')
            messagebox.showinfo("Success", f"Data exported to:\n{filename}")
            self.status_bar.config(text=f"✓ Exported to Excel: {filename}")
        except Exception as e:
            messagebox.showerror("Export Error", f"Failed to export to Excel:\n{str(e)}")
            
    def _export_csv(self, filename):
        """Export to CSV"""
        try:
            df = pd.DataFrame(self.players_data)
            # Replace N/A with empty strings
            df = df.replace('N/A', '')
            df.to_csv(filename, index=False, encoding='utf-8')
            messagebox.showinfo("Success", f"Data exported to:\n{filename}")
            self.status_bar.config(text=f"✓ Exported to CSV: {filename}")
        except Exception as e:
            messagebox.showerror("Export Error", f"Failed to export to CSV:\n{str(e)}")
            
    def _export_json(self, filename):
        """Export to JSON"""
        try:
            # Replace N/A with empty strings
            clean_data = []
            for player in self.players_data:
                clean_player = {k: ('' if v == 'N/A' else v) for k, v in player.items()}
                clean_data.append(clean_player)
            
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(clean_data, f, indent=2, ensure_ascii=False)
            messagebox.showinfo("Success", f"Data exported to:\n{filename}")
            self.status_bar.config(text=f"✓ Exported to JSON: {filename}")
        except Exception as e:
            messagebox.showerror("Export Error", f"Failed to export to JSON:\n{str(e)}")
            
    def clear_all(self):
        """Clear all data"""
        self.input_text.delete('1.0', tk.END)
        self.input_text.insert('1.0', self.placeholder_text)
        self.input_text.config(fg=self.colors['text_secondary'])
        self.is_placeholder = True
        
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        self.players_data = []
        
        self.export_excel_btn.set_enabled(False)
        self.export_csv_btn.set_enabled(False)
        self.export_json_btn.set_enabled(False)
        
        self.status_bar.config(text="Ready to extract player data")
        self.results_count.config(text="0 players")
        
    def set_buttons_state(self, enabled):
        """Enable or disable buttons"""
        self.extract_btn.set_enabled(enabled)
        self.clear_btn.set_enabled(enabled)


def main():
    """Main function to run the GUI application"""
    root = tk.Tk()
    app = FIDEExtractorGUI(root)
    
    # Center window
    root.update_idletasks()
    width = 1100
    height = 750
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')
    
    # Set minimum size
    root.minsize(900, 600)
    
    root.mainloop()


if __name__ == "__main__":
    main()
