from tkinter import messagebox
import data_access_tools.user_auth as tools_users
from templates.main_templates.initial_template import initial_template
from templates.main_templates.login_template import login_template
from templates.main_templates.signin_template import signin_template
from templates.main_templates.main_menu_template import main_menu_template
from templates.dish_templates.dishes_management_template import dishes_management_template
from templates.dish_templates.create_dish_template import create_dish_template
from templates.dish_templates.delete_dish_template import delete_dish_template
from templates.dish_templates.update_dish_template import update_dish_template


normal_access_templ_dic = {'initial': initial_template,
                           'login': login_template,
                           'signin': signin_template}

templ_dic = {'main_menu': main_menu_template,
             'dishes_management': dishes_management_template,
             'create_dish': create_dish_template,
             'delete_dish': delete_dish_template,
             'update_dish': update_dish_template,
             }


def grid_rows_columns_config(dynamic_frame, ratio):
    columns, rows = dynamic_frame.grid_size()
    for i in range(rows):
        dynamic_frame.grid_rowconfigure(i, weight=ratio)
    for j in range(columns):
        dynamic_frame.grid_columnconfigure(j, weight=ratio)


def destroy_widgets(dynamic_frame):
    for widget in dynamic_frame.winfo_children():
        widget.destroy()


def templ_handler(choice, dynamic_frame):

    destroy_widgets(dynamic_frame)
    grid_rows_columns_config(dynamic_frame, 0)

    if choice in templ_dic:
        if tools_users.token:
            temp_chosen = templ_dic[choice]
            temp_chosen(dynamic_frame)
        else:
            messagebox.showerror('Faltan permisos', 'No tiene autorización para realizar esta acción,'
                                                    ' autentiquese primero.')
            temp_chosen = normal_access_templ_dic['initial']
            temp_chosen(dynamic_frame)
    else:
        temp_chosen = normal_access_templ_dic[choice]
        temp_chosen(dynamic_frame)

    grid_rows_columns_config(dynamic_frame, 1)

