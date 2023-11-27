from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

import utils.template_handler

def menu_tables_template(dynamic_frame):

        lbl_title = ttk.Label(dynamic_frame,
                        text="Gestion de Mesas")
        button_add_table = ttk.Button(dynamic_frame, text="Add Tables",
                                command = lambda \
                        frame=dynamic_frame: utils.template_handler.\
                                templ_handler('add_table', frame))
        button_del_table = ttk.Button(dynamic_frame, text="Delete Tables",
                                command = lambda \
                        frame=dynamic_frame: utils.template_handler.\
                                templ_handler('del_table', frame))
        button_upd_table = ttk.Button(dynamic_frame, text="Update Tables", command = lambda \
                        frame=dynamic_frame: utils.template_handler.\
                                templ_handler('upd_table', frame))
        button_return = ttk.Button(dynamic_frame, text = "BACK", command = lambda \
                        frame=dynamic_frame: utils.template_handler.\
                                templ_handler('main_menu', frame))

        lbl_title.grid(column=0, row=0, pady=10)
        button_add_table.grid(column=0, row=1, pady=10)
        button_del_table.grid(column=0, row=2, pady=10)
        button_upd_table.grid(column=0, row=3, pady=10)
        button_return.grid(column=0, row=4, pady=10)
