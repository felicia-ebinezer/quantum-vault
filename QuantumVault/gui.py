import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import threading
from Main import generate_rsa_key, secure_transfer, secure_receive
import platform

is_mac = platform.system() == "Darwin"

# Modern color scheme
BG_COLOR = "#0F1419"  # Deep dark background
CARD_BG = "#1A1F2E"  # Card background
ACCENT_COLOR = "#00D9FF"  # Cyan accent
ACCENT_HOVER = "#00B8D4"  # Darker cyan
SUCCESS_COLOR = "#00E676"  # Green
ERROR_COLOR = "#FF5252"  # Red
TEXT_PRIMARY = "#FFFFFF"
TEXT_SECONDARY = "#94A3B8"
INPUT_BG = "#2D3748"
INPUT_BORDER = "#4A5568"

class ModernButton(tk.Canvas):
    """Custom modern button with gradient effect and smooth animations"""
    def __init__(self, parent, text, command, **kwargs):
        super().__init__(parent, height=50, bg=CARD_BG, highlightthickness=0, cursor="hand2")
        self.command = command
        self.text = text
        self.is_hovered = False
        
        self.bind("<Button-1>", lambda e: self.command())
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)
        
        self.draw_button()
    
    def draw_button(self):
        self.delete("all")
        color = ACCENT_HOVER if self.is_hovered else ACCENT_COLOR
        
        # Draw rounded rectangle
        self.create_rounded_rect(5, 5, self.winfo_reqwidth()-5 or 345, 45, 25, fill=color, outline="")
        
        # Draw text
        self.create_text(175, 25, text=self.text, fill=TEXT_PRIMARY, 
                        font=("Segoe UI", 12, "bold" if not is_mac else "normal"))
    
    def create_rounded_rect(self, x1, y1, x2, y2, radius, **kwargs):
        points = [x1+radius, y1,
                  x1+radius, y1,
                  x2-radius, y1,
                  x2-radius, y1,
                  x2, y1,
                  x2, y1+radius,
                  x2, y1+radius,
                  x2, y2-radius,
                  x2, y2-radius,
                  x2, y2,
                  x2-radius, y2,
                  x2-radius, y2,
                  x1+radius, y2,
                  x1+radius, y2,
                  x1, y2,
                  x1, y2-radius,
                  x1, y2-radius,
                  x1, y1+radius,
                  x1, y1+radius,
                  x1, y1]
        return self.create_polygon(points, smooth=True, **kwargs)
    def on_enter(self, e):
        self.is_hovered = True
        self.draw_button()
    def on_leave(self, e):
        self.is_hovered = False
        self.draw_button()
class ModernEntry(tk.Frame):
    def __init__(self, parent, label_text, **kwargs):
        super().__init__(parent, bg=CARD_BG)
        tk.Label(self, text=label_text, bg=CARD_BG, fg=TEXT_SECONDARY, 
                font=("Segoe UI", 10)).pack(anchor="w", pady=(0, 5))
        self.entry = tk.Entry(self, bg=INPUT_BG, fg=TEXT_PRIMARY, 
                             insertbackground=ACCENT_COLOR, relief="flat",
                             font=("Segoe UI", 11), bd=0)
        self.entry.pack(fill="x", ipady=10, ipadx=10)
        border_frame = tk.Frame(self, bg=INPUT_BORDER, height=2)
        border_frame.pack(fill="x")
    def get(self):
        return self.entry.get()
root = tk.Tk()
root.title("QuantumVault - Secure File Transfer")
root.geometry("500x650")
root.configure(bg=BG_COLOR)
root.resizable(False, False)
def clear_window():
    """Clears the current window contents."""
    for widget in root.winfo_children():
        widget.destroy()
def create_header(title, subtitle=""):
    """Creates a modern header with title and subtitle"""
    header_frame = tk.Frame(root, bg=BG_COLOR)
    header_frame.pack(pady=(30, 10))
    icon_label = tk.Label(header_frame, text="🔐", font=("Arial", 40), bg=BG_COLOR)
    icon_label.pack()
    tk.Label(header_frame, text=title, font=("Segoe UI", 24, "bold"), 
            bg=BG_COLOR, fg=TEXT_PRIMARY).pack()
    if subtitle:
        tk.Label(header_frame, text=subtitle, font=("Segoe UI", 11), 
                bg=BG_COLOR, fg=TEXT_SECONDARY).pack(pady=(5, 0))
def create_card():
    """Creates a card-like container"""
    card = tk.Frame(root, bg=CARD_BG, padx=30, pady=25)
    card.pack(padx=40, pady=20, fill="both", expand=True)
    return card
def show_main_menu():
    """Displays the main menu with available options."""
    clear_window()
    create_header("QuantumVault", "End-to-End Encrypted File Transfer")
    card = create_card()
    tk.Label(card, text="Choose an action", font=("Segoe UI", 14, "bold"), 
            bg=CARD_BG, fg=TEXT_PRIMARY).pack(pady=(0, 25))
    send_btn = ModernButton(card, "📤  Send File", send_file_ui)
    send_btn.pack(pady=10, fill="x")
    receive_btn = ModernButton(card, "📥  Receive File & Generate Keys", receive_file_ui)
    receive_btn.pack(pady=10, fill="x")
    
    # Divider
    tk.Frame(card, bg=INPUT_BORDER, height=1).pack(fill="x", pady=20)
    
    # Exit Button (secondary style)
    exit_canvas = tk.Canvas(card, height=50, bg=CARD_BG, highlightthickness=0, cursor="hand2")
    exit_canvas.pack(pady=10, fill="x")
    exit_canvas.create_rounded_rect = ModernButton.create_rounded_rect.__get__(exit_canvas, tk.Canvas)
    exit_canvas.create_rounded_rect(5, 5, 345, 45, 25, fill=INPUT_BG, outline="")
    exit_canvas.create_text(175, 25, text="Exit", fill=TEXT_SECONDARY, font=("Segoe UI", 11))
    exit_canvas.bind("<Button-1>", lambda e: root.quit())

def send_file_ui():
    """UI for sending a secure file."""
    clear_window()
    
    create_header("Send File", "Transfer files securely to another device")
    
    card = create_card()
    
    server_ip_entry = ModernEntry(card, "Server IP Address")
    server_ip_entry.pack(fill="x", pady=(0, 15))
    
    server_port_entry = ModernEntry(card, "Server Port")
    server_port_entry.pack(fill="x", pady=(0, 25))
    
    def select_file():
        """Allows user to select a file and starts sending it in a new thread."""
        file_path = filedialog.askopenfilename()
        if file_path:
            # Show file selected
            file_name = file_path.split("/")[-1]
            messagebox.showinfo("File Selected", f"Preparing to send: {file_name}")
            threading.Thread(target=send_file, args=(server_ip_entry.get(), 
                           server_port_entry.get(), file_path), daemon=True).start()
    
    send_btn = ModernButton(card, "📁  Choose File & Send", select_file)
    send_btn.pack(pady=10, fill="x")
    
    back_btn = ModernButton(card, "← Back", show_main_menu)
    back_btn.pack(pady=10, fill="x")

def send_file(server_ip, server_port, file_path):
    """Handles file sending and auto-returns to the main menu."""
    if not server_ip or not server_port:
        messagebox.showerror("Error", "Please enter server IP and port!")
        return
    try:
        secure_transfer(server_ip, int(server_port), file_path)
        messagebox.showinfo("Success", "✓ File sent successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"❌ {str(e)}")
    root.after(1000, show_main_menu)

def receive_file_ui():
    """UI for receiving a secure file & generating keys."""
    clear_window()
    
    create_header("Receive File", "Generate keys and receive encrypted files")
    
    card = create_card()
    
    # Status indicator
    status_label = tk.Label(card, text="Ready to receive", bg=CARD_BG, 
                           fg=TEXT_SECONDARY, font=("Segoe UI", 10))
    status_label.pack(pady=(0, 20))
    
    def generate_keys():
        """Generates RSA keys."""
        try:
            generate_rsa_key("keys")
            messagebox.showinfo("Success", "✓ RSA Keys Generated Successfully!")
            status_label.config(text="✓ Keys generated", fg=SUCCESS_COLOR)
        except Exception as e:
            messagebox.showerror("Error", f"❌ {str(e)}")
    
    keys_btn = ModernButton(card, "🔑  Generate RSA Keys", generate_keys)
    keys_btn.pack(pady=10, fill="x")
    
    tk.Frame(card, bg=INPUT_BORDER, height=1).pack(fill="x", pady=20)
    
    server_port_entry = ModernEntry(card, "Listening Port")
    server_port_entry.pack(fill="x", pady=(0, 20))
    
    def start_receiving():
        """Starts file receiving in a new thread."""
        port = server_port_entry.get()
        if not port:
            messagebox.showerror("Error", "Please enter a port!")
            return
        status_label.config(text="⏳ Waiting for connection...", fg=ACCENT_COLOR)
        threading.Thread(target=receive_file, args=(int(port), status_label), daemon=True).start()
    
    receive_btn = ModernButton(card, "🎧  Start Receiving", start_receiving)
    receive_btn.pack(pady=10, fill="x")
    
    back_btn = ModernButton(card, "← Back", show_main_menu)
    back_btn.pack(pady=10, fill="x")

def receive_file(port, status_label=None):
    """Handles file receiving and auto-returns to the main menu."""
    try:
        secure_receive(port, "keys")
        messagebox.showinfo("Success", "✓ File received successfully!")
        if status_label:
            status_label.config(text="✓ File received", fg=SUCCESS_COLOR)
    except Exception as e:
        messagebox.showerror("Error", f"❌ {str(e)}")
        if status_label:
            status_label.config(text="❌ Error occurred", fg=ERROR_COLOR)
    root.after(1000, show_main_menu)

# Start the GUI
def runner():
    show_main_menu()
    root.mainloop()

if __name__ == "__main__":
    runner()