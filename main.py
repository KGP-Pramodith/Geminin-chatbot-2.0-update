import tkinter as tk
from tkinter import ttk, scrolledtext
from app import get_gemini_response 
import time 

# --- GUI Function ---
def send_message():
    user_input = entry.get()
    if user_input.strip() == "":
        return
    
    entry.delete(0, tk.END)  # clear entry immediately
    
    # Get response from Gemini first
    response = get_gemini_response(user_input)
    
    # Now display the user input
    chat_area.config(state=tk.NORMAL)
    chat_area.insert(tk.END, f"You: {user_input}\n")
    chat_area.insert(tk.END, "Bot: ")
    chat_area.config(state=tk.DISABLED)
    
    # Type the bot response letter by letter
    type_response(response)
    
def type_response(text):
    """Display text letter by letter in the chat area."""
    chat_area.config(state=tk.NORMAL)
    for char in text:
        chat_area.insert(tk.END, char)
        chat_area.update_idletasks()  # refresh GUI
        time.sleep(0.02)  # adjust typing speed
    chat_area.insert(tk.END, "\n\n")
    chat_area.config(state=tk.DISABLED)
    chat_area.yview(tk.END)

# --- Tkinter GUI ---
def main():
    global entry, chat_area

    root = tk.Tk()
    root.title("Gemini Chatbot")
    root.geometry("500x600")

    # Apply ttk theme
    style = ttk.Style()
    style.theme_use("clam")

    # Chat display area
    chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, state=tk.DISABLED, font=("Segoe UI", 11))
    chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    # Entry + Send button frame
    frame = tk.Frame(root)
    frame.pack(padx=10, pady=10, fill=tk.X)

    entry = tk.Entry(frame, font=("Segoe UI", 11))
    entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
    entry.bind("<Return>", lambda event: send_message())

    send_button = tk.Button(frame, text="Send", command=send_message)
    send_button.pack(side=tk.RIGHT)
    
    exit_button = tk.Button(frame, text="Exit", command=root.destroy)
    exit_button.pack(side=tk.RIGHT, padx=(10, 0))   

    root.mainloop()

if __name__ == "__main__":
    main()