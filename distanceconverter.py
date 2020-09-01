import tkinter as tk
from tkinter import ttk
#from windows import set_dpi_awareness

#set_dpi_awareness()
try:
	from ctypes import windll
	windll.shcore.SetProcessDpiAwareness(1)
except:
	pass


root = tk.Tk()
root.title('Distance Converter')

meter_value = tk.StringVar()
feet_value = tk.StringVar(value='Feet shown here')


def calculate_feet(*args):
	try:
		meter = float(meter_value.get())
		feet = meter * 3.28084
		feet_value.set(f'{feet:.3f}')
		#print(f'{meter} meters is equal to {feet:.3f} feet.')
	except ValueError:
		pass



root.columnconfigure(0,weight=1)


main = ttk.Frame(root, padding = (30,15))
main.grid()

meter_label = ttk.Label(main,text= 'Meters: ')
meter_input = ttk.Entry(main, width=10,textvariable=meter_value)
feet_label = ttk.Label(main,text='Feet: ')
feet_display = ttk.Label(main,textvariable=feet_value)
calc_button = ttk.Button(main, text='calculate',command=calculate_feet)

meter_label.grid(column=0,row=0,sticky='W',padx=6,pady=6)
meter_input.grid(column=1,row=0,sticky='EW',padx=6,pady=6)
meter_input.focus()

feet_label.grid(column=0,row=1,sticky='W',padx=6,pady=6)
feet_display.grid(column=1,row=1,sticky='EW',padx=6,pady=6)

calc_button.grid(column=0,row=2, columnspan=2,sticky='EW',padx=6,pady=6)

root.bind('<Return>',calculate_feet)
root.bind('<KP_Enter>',calculate_feet)



root.mainloop()