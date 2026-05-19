import requests
import tkinter as tk
from tkinter import ttk

API_KEY = "h465ik027oar"

def birds():
    area = entry.get()
    url = "https://api.ebird.org/v2/data/obs/" + area + "/recent"
    headers = { "X-eBirdApiToken": API_KEY}

    response = requests.get(url, headers=headers)
    data = response.json()
    print(data)
    for row in tree.get_children():
        tree.delete(row)

    for bird in data:
        common = bird.get("comName")
        scientific = bird.get("sciName")
        location = bird.get("locName")
        data = bird.get("obsDt")

        tree.insert(
            "",
            tk.END,
            values=(common, scientific, location, data)
        )

root = tk.Tk()

root.title("Bird Watching Data")
root.geometry("800x500")

title = tk.Label(
    root,
    text="Bird Watching Data",
    font=("Arial", 20)
)

title.pack(pady=10)

label = tk.Label(
    root,
    text="Enter Region/Area name such as US-NY: "
)

label.pack()

entry = tk.Entry(root, width=25)

entry.pack(pady=5)

button = tk.Button(
    root,
    text = "search",
    command = birds
)

button.pack(pady=10)

columns=("Bird", "Scientific Name", "Location", "Date")

tree = ttk.Treeview(
    root,
    columns = columns ,
    show="headings"
)

tree.column("Bird", width=150)
tree.column("Scientific Name", width=200)
tree.column("Location", width=250)
tree.column("Date", width=150)

tree.pack(fill="both", expand=True)

root.mainloop()
