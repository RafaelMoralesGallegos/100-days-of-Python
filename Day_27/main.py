from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)
# window.grid_columnconfigure(0, weight=1)


def button_clicked(miles):
    km = str(round(int(miles) * 1.609, 2))
    total_km.config(text=km)


# *Row 0
mile_entry = Entry(window, width=10)
mile_entry.grid(column=1, row=0)

miles_label = Label(window, text="Miles")
miles_label.grid(column=2, row=0, sticky="nsew")

# *Row 1
equal_label = Label(window, text="is equal to")
equal_label.grid(column=0, row=1, sticky="nsew")

total_km = Label(window, text=0, width=10)
total_km.config(justify="center")
total_km.grid(column=1, row=1)

km_label = Label(window, text="Km")
km_label.grid(column=2, row=1, sticky="nsew")

# *Row 2
mile_km_button = Button(
    window, text="Calculate", command=lambda: button_clicked(mile_entry.get())
)
mile_km_button.grid(column=1, row=2, sticky="nsew")

window.mainloop()
