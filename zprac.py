from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import numpy as np
import matplotlib.pyplot as plt


master = Tk()
master.title("Zprac_krivek")

def graph():
    normal_dist = np.random.normal(200000,25000,5000)
    plt.hist(normal_dist, 20)
    plt.show()

def folder_selection():
    global folder
    folder = filedialog.askdirectory()
    folder_selected.config(text=folder)

# DEF - Set buttons
def def_set():
    global folder_selection, start_date_selection, end_date_selection, folder_selected

    # Set buttons
    #filter section
    filter_frame = LabelFrame(master, text="Select Parameters", padx=10, pady=10)

    select_folder = Label(filter_frame, text="Select folder: ", borderwidth=3, relief="solid")
    folder_selection = Button(filter_frame, text="Open Folder", command=folder_selection, borderwidth=3, relief="solid")
    folder_selected = Label(filter_frame, text=" ")
    select_start_date = Label(filter_frame, text="Select start date: ", borderwidth=3, relief="solid")
    start_date_selection = Entry(filter_frame, bg="cyan", borderwidth=3, relief="solid")
    select_end_date = Label(filter_frame, text="Select end date: ", borderwidth=3, relief="solid")
    end_date_selection = Entry(filter_frame, bg="cyan", borderwidth=3, relief="solid")

    #info section
    info_frame = LabelFrame(master, text="Info", padx=10, pady=10)

    files_in_folder = Label(info_frame, text="Files in folder: ", borderwidth=3, relief="solid")
    files_in_folder_nr = Entry(info_frame, bg="cyan", borderwidth=3, relief="solid")
    files_in_selection = Label(info_frame, text="Files in selection: ", borderwidth=3, relief="solid")
    files_in_selection_nr = Entry(info_frame, bg="cyan", borderwidth=3, relief="solid")
    ok_results = Label(info_frame, text="OK results: ", borderwidth=3, relief="solid")
    ok_results_nr = Entry(info_frame, bg="cyan", borderwidth=3, relief="solid")
    nok_results = Label(info_frame, text="NOK results: ", borderwidth=3, relief="solid")
    nok_results_nr = Entry(info_frame, bg="cyan", borderwidth=3, relief="solid")

    #graf
    graf = Button(master, text="GRAF", command=graph, borderwidth=3, relief="solid")

    #exports
    export_frame = LabelFrame(master, text="Export", padx=10, pady=10)

    export_data = Label(export_frame, text="Export data", borderwidth=3, relief="solid")
    export_data_nr = Entry(export_frame, bg="cyan", borderwidth=3, relief="solid")
    export_plot = Label(export_frame, text="Export plot", borderwidth=3, relief="solid")
    export_plot_nr = Entry(export_frame, bg="cyan", borderwidth=3, relief="solid")

    # Set grid
    #filter section
    filter_frame.grid(row=0, column=0)
    select_folder.grid(row=0, column=0)
    folder_selection.grid(row=0, column=1)
    folder_selected.grid(row=0, column=2)
    select_start_date.grid(row=1, column=0)
    start_date_selection.grid(row=1, column=1)
    select_end_date.grid(row=2, column=0)
    end_date_selection.grid(row=2, column=1)

    #info section
    info_frame.grid(row=0, column=1)
    files_in_folder.grid(row=0, column=0)
    files_in_folder_nr.grid(row=0, column=1)
    files_in_selection.grid(row=1, column=0)
    files_in_selection_nr.grid(row=1, column=1)
    ok_results.grid(row=2, column=0)
    ok_results_nr.grid(row=2, column=1)
    nok_results.grid(row=3, column=0)
    nok_results_nr.grid(row=1, column=1)

    #graf
    graf.grid(row=5, column=0, columnspan=4, rowspan=4, sticky=W+N)

    #exports
    export_frame.grid(row=1, column=2)

    export_data.grid(row=0, column=0)
    export_data_nr.grid(row=1, column=0)
    export_plot.grid(row=2, column=0)
    export_plot_nr.grid(row=3, column=0)

def_set()

master.mainloop()

