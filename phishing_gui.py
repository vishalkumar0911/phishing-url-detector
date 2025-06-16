import tkinter as tk
from tkinter import messagebox
import joblib
import traceback

try:
    model = joblib.load('ml_model.pkl')
    vectorizer = joblib.load('vectorizer.pkl')
except Exception as e:
    print("❌ Failed to load model/vectorizer.")
    print(traceback.format_exc())
    exit()

def check_url():
    url = url_entry.get().strip()
    if not url:
        messagebox.showwarning("Input Error", "Please enter a URL.")
        return

    try:
        url_vec = vectorizer.transform([url])
        result = model.predict(url_vec)[0]
        if result == 1:
            result_label.config(text="⚠️ Phishing Detected!", fg="red")
        else:
            result_label.config(text="✅ Legitimate URL", fg="green")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred:\n{e}")

# GUI setup
try:
    root = tk.Tk()
    root.title("Phishing URL Detector")
    root.geometry("400x250")
    root.resizable(False, False)

    tk.Label(root, text="Enter a URL to check:", font=("Arial", 14)).pack(pady=10)
    url_entry = tk.Entry(root, font=("Arial", 12), width=40)
    url_entry.pack(pady=5)
    tk.Button(root, text="Check URL", font=("Arial", 12), command=check_url).pack(pady=10)
    result_label = tk.Label(root, text="", font=("Arial", 16))
    result_label.pack(pady=20)

    print("✅ GUI loaded. Waiting for input...")
    root.mainloop()
except Exception as gui_error:
    print("❌ GUI failed to start:")
    print(traceback.format_exc())
