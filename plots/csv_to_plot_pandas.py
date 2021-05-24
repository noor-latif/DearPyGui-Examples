from dearpygui import core as gui
from dearpygui import simple as module
import pandas


def colormap_callback(sender, data):
    value = gui.get_value("Colormaps")
    gui.set_color_map("Plot", value)


def plot_callback(sender, data):
    # create dataframe
    data_frame_to_write = pandas.DataFrame(
        {'time': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
         'data': [1, 2, 6, 15, 4, 10, 6, 20, 4, 5, 3, 1, 2, 10, 20, 1, 6],
         }
    )

    # write to csv file
    data_frame_to_write.to_csv('test_data.csv', index=False)

    # read csv
    data_frame_read = pandas.read_csv('test_data.csv')

    # getting data from data frame
    time = data_frame_read['time']
    data = data_frame_read['data']

    # converting getting it from the pandas series data item to a normal list
    data_x = []
    data_y = []

    for i in range(len(data)):
        data_x.append(time[i])
        data_y.append(data[i])

    # plot dataframe
    gui.clear_plot("Plot")
    gui.add_line_series("Plot", "Data", data_x, data_y)
    gui.add_scatter_series("Plot", "Data", data_x, data_y)


with module.window("Main Window"):
    gui.add_text("Tips")
    gui.add_text("This example requires the pandas python module", bullet=True)
    gui.add_text(
        "This example reads and writes to a csv file with the pandas dataframe object", bullet=True)
    gui.add_text("It also plots the data from the dataframe", bullet=True)
    gui.add_text(
        "Plots in DPG require the data is a float list", bullet=True)
    gui.add_button("Plot data", callback=plot_callback)
    gui.add_listbox("Colormaps", items=["Default", "Dark", "Pastel", "Paired", "Viridis",
                                        "Plasma", "Hot", "Cool", "Pink", "Jet"],
                    width=500, num_items=3, callback=colormap_callback)
    gui.add_plot("Plot", height=-1)
gui.start_dearpygui(primary_window="Main Window")