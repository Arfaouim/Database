import tkinter as tk

class intro(tk.Frame):
	"""docstring for intro"""
	def __init__(self, master):
		tk.Frame.__init__(self,master)
		self.master = master

def main():
	""" main app """
	root=tk.Tk()
	app=intro(root)
	root.mainloop()		

if __name__ =="__main__":
	main()	