from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import re
import utils.template_handler
import data_access_tools.dishes_da as tools_dishes


"""
This module configures the dish creation template by modifying the 
'dynamic_frame'.
It imports libraries such as 'tkinter', 'ttk', 're'(Regular Expression)
for checking specific conditions within text input, the 'dishes_da'
module for calling methods that assist in dish creation and updates,
and the 'template_handler' module for configuring the frame.
"""


dish_name = ''
dish_price = ''
dish_description = ''
dish_availability = ''
OPTIONS = ('Si', 'No')


def warning(dynamic_frame):
    try:
        result = messagebox.askokcancel("Confirmación",
                                        "¿Deseas agregar este plato?")
        if result:
            save_process()
            utils.template_handler.templ_handler('dishes_management',
                                                 dynamic_frame)
    except ValueError:
        messagebox.showerror('Faltan campos', 'Hay algún campo vacío,'
                             'por favor verifica.')
    except Exception:
        messagebox.showerror('No se pudo completar la acción',
                             'No se ha logrado realizar el proceso de '
                             'agregación llama al proveedor para asesoria')


def save_process():
    """
    This function verifies, processes, and saves the new data.

    Raises:
        ValueError: Raised to preemptively handle potential errors
        during execution.
    """
    global dish_name
    global dish_price
    global dish_description
    global dish_availability
    if (dish_name.isspace() or dish_name == '' or
            not dish_price.isnumeric() or
            dish_description.isspace() or dish_description == '' or
            dish_availability not in OPTIONS):
        raise ValueError
    else:
        dish_to_create = [0,
                          dish_name.capitalize(),
                          dish_price,
                          dish_description.capitalize(),
                          dish_availability]
        tools_dishes.add_dish(dish_to_create)
        dish_to_create.clear()
        dish_name = ''
        dish_price = ''
        dish_description = ''
        dish_availability = ''


def catch_dish_name(var):
    """_summary_

    Args:
        var (_type_): _description_

    Returns:
        _type_: _description_
    """
    if len(var) > 25:
        return False
    global dish_name
    dish_name = var
    return True


def catch_dish_price(var):
    pattern = r'\d*'
    if re.fullmatch(pattern, var) is None or len(var) > 6:
        return False
    global dish_price
    dish_price = var
    return True


def catch_dish_description(var):
    if len(var) > 50:
        return False
    global dish_description
    dish_description = var
    return True


def catch_dish_availability(event):
    global dish_availability
    dish_availability = event.widget.get()
    return True


def create_dish_template(dynamic_frame):
    """_summary_

    Args:
        dynamic_frame (_type_): _description_
    """
    global dish_name
    global dish_price
    global dish_description
    global dish_availability
    entry_box_width = 25
    lbl_title = ttk.Label(dynamic_frame,
                          text="Agregar platos",
                          font=("default", 12, "bold"))
    lbl_dish_name = ttk.Label(dynamic_frame,
                              text="Nombre")
    lbl_dish_price = ttk.Label(dynamic_frame,
                               text="Precio")
    lbl_dish_description = ttk.Label(dynamic_frame,
                                     text="Descripción")
    lbl_dish_availability = ttk.Label(dynamic_frame,
                                      text="Disponibilidad")

    dish_name = StringVar()
    dish_price = StringVar()
    dish_description = StringVar()
    dish_availability = StringVar()

    entry_dish_name = ttk.Entry(dynamic_frame,
                                width=entry_box_width,
                                validate="key",
                                validatecommand=(dynamic_frame.register\
                                    (catch_dish_name), '%P'))
    entry_dish_price = ttk.Entry(dynamic_frame,
                                 width=entry_box_width,
                                 validate="key",
                                 validatecommand=(dynamic_frame.register\
                                     (catch_dish_price), '%P'))
    entry_dish_description = ttk.Entry(dynamic_frame,
                                       width=entry_box_width,
                                       validate="key",
                                       validatecommand=(dynamic_frame.register\
                                           (catch_dish_description), '%P'))

    combobox_dish_availability = ttk.Combobox(dynamic_frame,
                                              width=(entry_box_width - 3),
                                              values=OPTIONS)
    combobox_dish_availability.bind("<<ComboboxSelected>>",
                                    catch_dish_availability)

    button_add = ttk.Button(dynamic_frame,
                            text="Agregar",
                            style="Accent.TButton",
                            command=lambda: warning(dynamic_frame))

    button_back = ttk.Button(dynamic_frame,
                             text="Atrás",
                             command=lambda: utils.template_handler.\
                                 templ_handler('dishes_management',
                                               dynamic_frame))

    lbl_title.grid(column=0, row=0, columnspan=2, padx=40, pady=10)
    lbl_dish_name.grid(column=0, row=1, sticky="w", padx=(20, 0), pady=2)
    entry_dish_name.grid(column=0, row=2, padx=(20, 10), pady=2)
    lbl_dish_price.grid(column=1, row=1, sticky="w", padx=(10, 0), pady=2)
    entry_dish_price.grid(column=1, row=2, padx=(10, 20), pady=2)
    lbl_dish_description.grid(column=0, row=3, sticky="w", padx=(20, 0), pady=2)
    entry_dish_description.grid(column=0, row=4, padx=(20, 10), pady=2)
    lbl_dish_availability.grid(column=1, row=3, sticky="w", padx=(10, 0), pady=2)
    combobox_dish_availability.grid(column=1, row=4, padx=(10, 20), pady=2)
    button_back.grid(column=0, row=5, sticky="e", padx=(0, 10), pady=15)
    button_add.grid(column=1, row=5, sticky="w", padx=(10, 0), pady=15)
