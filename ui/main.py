import tkinter as tk
from tkinter import ttk, StringVar
from main_logic import *
from tkinter import Text
from constants import search_options

def clear_frame(frame: ttk.Frame):
    for widget in frame.winfo_children():
        widget.destroy()

window = tk.Tk()
window.title('My reagents')
window.geometry('800x700')
window.state('zoomed')

frame_search_header = tk.Frame(window, width=500, height=500, bg='grey')
frame_search_form = tk.Frame(window, width=500, height=500, bg='grey')
frame_tittle_form_delete = tk.Frame(window, width=500, height=500, bg='grey')
frame_title_change_mass = tk.Frame(window, width=500, height=500, bg='grey')
frame_title_add_form = tk.Frame(window, width=500, height=500, bg='grey')
frame_add_form = tk.Frame(window, width=500, height=500, bg='grey')
frame_change_mass = tk.Frame(window, width=500, height=500, bg='grey')
frame_delete_compound = tk.Frame(window, width=500, height=500, bg='grey')
frame_title_info = tk.Frame(window, width=500, height=500, bg='grey')
frame_info_box = tk.Frame(window, width=500, height=500, bg='grey')
frame_table = tk.Frame(window, width=500, height=500, bg='white')


frame_search_header.place(relx=0, rely=0, relwidth=0.2, relheight=0.1)
frame_search_form.place(relx=0, rely=0.1, relwidth=0.2, relheight=0.1)
frame_tittle_form_delete.place(relx=0, rely=0.2, relwidth=0.2, relheight=0.05)
frame_delete_compound.place(relx=0, rely=0.25, relwidth=0.2, relheight=0.1)
frame_title_change_mass.place(relx=0, rely=0.35, relwidth=0.2, relheight=0.05)
frame_change_mass.place(relx=0, rely=0.4, relwidth=0.2, relheight=0.2)
frame_title_add_form.place(relx=0.2, rely=0, relwidth=0.5, relheight=0.05)
frame_add_form.place(relx=0.2, rely=0.05, relwidth=0.5, relheight=0.55)
frame_title_info.place(relx=0.7, rely=0, relwidth=0.3, relheight=0.05)
frame_info_box.place(relx=0.7, rely=0.05, relwidth=0.3, relheight=0.55)


frame_table.place(relx=0, rely=0.6, relwidth=1, relheight=0.4)


# table_data
table_columns = ['cas_no', 'name_substance', 'total_g', 'class_substance', 'location', 'descrip', 'molecular_weight', 'molecular_formula']
table = ttk.Treeview(frame_table, columns=table_columns, show='headings')

table.column('cas_no', width=80, anchor='center')
table.column('name_substance', width=150, anchor='center')
table.column('total_g', width=80, anchor='center')
table.column('class_substance', width=100, anchor='center')
table.column('location', width=150, anchor='center')
table.column('descrip', width=150, anchor='center')
table.column('molecular_weight', width=100, anchor='center')
table.column('molecular_formula', width=100, anchor='center')

# Расширение строк и столбцов, чтобы таблица занимала всю площадь блока
frame_table.rowconfigure(0, weight=1)
frame_table.columnconfigure(0, weight=1)

def populate_table(table_data):
    # очистить таблицу
    table.delete(*table.get_children())

    for item in table_data:
        table.insert("", "end", values=item)

# SEARCH
search_by = ttk.Label(frame_search_header, text='Search by')
dropdown_search = ttk.Combobox(frame_search_header, values=list(map(lambda option: option[0], search_options)))
dropdown_search.set(search_options[0][0])

search_by.grid(row=0, column=0, sticky='s', padx=15, pady=20)
dropdown_search.grid(row=0, column=1, sticky='s', padx=15, pady=20)

search_value = StringVar()

# Search button
def search():
    table_data = search_request(dropdown_search.get(), search_value.get())
    populate_table(table_data)

def render_form(search_choice):
    search_value.set('')
    clear_frame(frame_search_form)
    # кнопка поиска
    search_button = ttk.Button(frame_search_form, text='Search', command=search)
    search_button.grid(row=1, column=1, padx=15, pady=5)

    if search_choice == search_options[0][0]:
        # search by cas
        l_search_cas = ttk.Label(frame_search_form, text='Input CAS Number')
        e_search_cas = ttk.Entry(frame_search_form, textvariable=search_value)
        l_search_cas.grid(row=0, column=0, sticky='s', padx=10, pady=10)
        e_search_cas.grid(row=0, column=1, sticky='s', padx=10, pady=10)
    
    elif search_choice == search_options[2][0]:
        # search by name
        l_search_name = ttk.Label(frame_search_form, text='Input name substance')
        e_search_name = ttk.Entry(frame_search_form, textvariable=search_value)
        l_search_name.grid(row=0, column=0, sticky='s', padx=10, pady=10)
        e_search_name.grid(row=0, column=1, sticky='s', padx=10, pady=10)

    elif search_choice == search_options[1][0]:
        # search by class
        l_class_search = ttk.Label(frame_search_form, text='Add class of substance')
        options_class_search = ['alkane', 'alkene', 'alkyne', 'arene', 'acid', 'alcohol', 'amine', 'halogen derivat.', 'ester', 'inorganic', 'aldehyde', 'ketone', 'phenol']
        dropdown_class_search = ttk.Combobox(frame_search_form, values=options_class_search, textvariable=search_value)
        l_class_search.grid(row=0, column=0, sticky='s', padx=10, pady=10)
        dropdown_class_search.grid(row=0, column=1, sticky='s', padx=10, pady=10)

def on_search_choice_changed(event):
    render_form(dropdown_search.get())

dropdown_search.bind("<<ComboboxSelected>>", on_search_choice_changed)

render_form(dropdown_search.get())

# Table
for column in table_columns:
    table.heading(column, text=column)

table.grid(sticky="nsew")

# ОКНО ДЛЯ ВВОДА ДАННЫХ
l_title_ad = ttk.Label(frame_title_add_form, text='Add compound to data base', font=('TkDefaultFont', 12, 'bold'))
l_title_ad.grid(row=0, column=0, sticky='s', padx=250, pady=10)
# Labels and Entry Fields for Add Form
l_choose_cas = ttk.Label(frame_add_form, text='Add CAS Number')
e_choose_cas = ttk.Entry(frame_add_form)
l_choose_cas.grid(row=1, column=0, sticky='n', padx=30, pady=30)
e_choose_cas.grid(row=1, column=1, sticky='n', padx=30, pady=30)

l_choose_name = ttk.Label(frame_add_form, text='Add name')
e_choose_name = ttk.Entry(frame_add_form)
l_choose_name.grid(row=2, column=0, sticky='n', padx=30, pady=30)
e_choose_name.grid(row=2, column=1, sticky='n', padx=30, pady=30)

l_mass = ttk.Label(frame_add_form, text='Add mass, g')
e_mass = ttk.Entry(frame_add_form)
l_mass.grid(row=3, column=0, sticky='n', padx=30, pady=30)
e_mass.grid(row=3, column=1, sticky='n', padx=30, pady=30)

l_class = ttk.Label(frame_add_form, text='Add class of substance')
options_class = ['alkane', 'alkene', 'alkyne', 'arene', 'acid', 'alcohol', 'amine', 'halogen derivat.', 'ester', 'inorganic', 'aldehyde', 'ketone', 'phenol']
dropdown_class = ttk.Combobox(frame_add_form, values=options_class)
l_class.grid(row=4, column=0, sticky='n', padx=30, pady=30)
dropdown_class.grid(row=4, column=1, sticky='n', padx=30, pady=30)

l_location = ttk.Label(frame_add_form, text='Add location')
e_location = ttk.Entry(frame_add_form)
l_location.grid(row=1, column=2, sticky='n', padx=30, pady=30)
e_location.grid(row=1, column=3, sticky='n', padx=30, pady=30)

l_description = ttk.Label(frame_add_form, text='Add description of substance')
e_description = ttk.Entry(frame_add_form)
l_description.grid(row=2, column=2, sticky='n', padx=30, pady=30)
e_description.grid(row=2, column=3, sticky='n', padx=30, pady=30)


l_weigt = ttk.Label(frame_add_form, text='Add molecular weight')
e_weight = ttk.Entry(frame_add_form)
l_weigt.grid(row=3, column=2, sticky='n', padx=30, pady=30)
e_weight.grid(row=3, column=3, sticky='n', padx=30, pady=30)

l_molecular_formula = ttk.Label(frame_add_form, text='Add molecular formula')
e_molecular_formula = ttk.Entry(frame_add_form)
l_molecular_formula.grid(row=4, column=2, sticky='n', padx=30, pady=30)
e_molecular_formula.grid(row=4, column=3, sticky='n', padx=30, pady=30)


# Создание виджета Text для вывода информации
title_info = ttk.Label(frame_title_info,text='Information', font=('TkDefaultFont', 12, 'bold'))
title_info.grid(row=0, column=0, sticky='s', padx=200, pady=10)
output_text_widget = Text(frame_info_box, width=40, height=20)  # Increase the width and height values
output_text_widget.grid(row=5, columnspan=3, padx=70, pady=10, sticky="w")
output_text_widget.configure(width=40, height=20)

def submit():
    output_text_widget.delete(1.0, tk.END)
    try:
        compound = Compound(
            e_choose_cas.get(),
            e_choose_name.get(),
            float(e_mass.get()),
            dropdown_class.get(),
            e_location.get(),
            e_description.get(),
            float(e_weight.get()),
            e_molecular_formula.get()
        )
        if upload_class_to_api(compound):
            output_text_widget.insert(tk.END, 'Данные успешно загружены')
        else:
            output_text_widget.insert(tk.END, 'Ошибка загрузки данных')
    except Exception as e:
        output_text_widget.insert(tk.END, f'Ошибка ввода данных: {e}')


# Add button add
add_button = ttk.Button(frame_add_form, text='Submit', command=submit)
add_button.grid(row=5, column=0, padx=10, pady=10)

# CLEAR ENTRY FIELD

def clear_fields():
    e_choose_cas.delete(0, 'end')
    e_choose_name.delete(0, 'end')
    e_mass.delete(0, 'end')
    e_weight.delete(0, 'end')
    e_location.delete(0, 'end')
    dropdown_class.set('')
    e_description.delete(0, 'end')
    e_molecular_formula.delete(0, 'end')
    dropdown_change.set('')
    e_entry_cas.delete(0, 'end')
    e_entry_mass.delete(0, 'end')
    e_delete_cas.delete(0, 'end')
    dropdown_search.set('')


# Add button clear
btn_clear_fields = ttk.Button(frame_add_form, text='Clear fields', command=clear_fields)
btn_clear_fields.grid(row=5, column=3, padx=10, pady=10)



# CHANGE MASS
def update_mass():
    output_text_widget.delete(1.0, tk.END)
    try:
        choice = dropdown_change.get()
        cas_no = e_entry_cas.get()
        mass = 0
        if choice == 'incoming':
            mass = float(e_entry_mass.get())
        elif choice == 'expenditure':
            mass = -float(e_entry_mass.get())
        else:
            output_text_widget.insert(tk.END, 'Wrong choice value')

        if mass != 0:
            if upload_mass_to_api(cas_no, mass):
                output_text_widget.insert(tk.END, 'Mass successfully changed')
            else:
                output_text_widget.insert(tk.END, 'Error deleting data')
    except Exception as e:
        output_text_widget.insert(tk.END, f'Input data error: {e}')

l_change_mass = ttk.Label(frame_title_change_mass, text='Сhange mass of substance', font=('TkDefaultFont', 9, 'bold'))
l_change_mass.grid(row=0, column=0, sticky='s', padx=50, pady=10)


# drop_down 
l_choose_cat = ttk.Label(frame_change_mass, text='Select type')
options_change = ['incoming', 'expenditure']
dropdown_change = ttk.Combobox(frame_change_mass, values=options_change)

# entry cas_no
l_entry_cas = ttk.Label(frame_change_mass, text='Entry Cas No')
e_entry_cas = ttk.Entry(frame_change_mass)

# mass
l_entry_mass = ttk.Label(frame_change_mass, text='Entry mass, g')
e_entry_mass = ttk.Entry(frame_change_mass)

# Add button update
add_button = ttk.Button(frame_change_mass, text='Update', command=update_mass)

# position 


l_choose_cat.grid(row=1, column=0, sticky='n', padx=10, pady=10)
dropdown_change.grid(row=1, column=1, sticky='n', padx=10, pady=10)

l_entry_cas.grid(row=2, column=0, sticky='n', padx=10, pady=10)
e_entry_cas.grid(row=2, column=1, sticky='n', padx=10, pady=10)

l_entry_mass.grid(row=3, column=0, sticky='n', padx=10, pady=10)
e_entry_mass.grid(row=3, column=1, sticky='n', padx=10, pady=10)

add_button.grid(row=4, column=1, padx=10, pady=5)

# info_box

# DELTE
l_delete_comp = ttk.Label(frame_tittle_form_delete, text='Remove substance from database', font=('TkDefaultFont', 9, 'bold'))
l_delete_comp.grid(row=0, column=0, sticky='s', padx=50, pady=10)

l_delete_cas = ttk.Label(frame_delete_compound, text='Cas No:')
l_delete_cas.grid(row=1, column=0, sticky='s', padx=5, pady=30)

e_delete_cas = ttk.Entry(frame_delete_compound)
e_delete_cas.grid(row=1, column=1, sticky='s', padx=5, pady=30)

def delete_compound():
    output_text_widget.delete(1.0, tk.END)
    try:
        cas_no = e_delete_cas.get()
        if delete_to_api(cas_no):
            output_text_widget.insert(tk.END, 'Data successfully deleted')
        else:
            output_text_widget.insert(tk.END, 'Error deleting data')
    except Exception as e:
        output_text_widget.insert(tk.END, f'Input data error: {e}')

delete_button = ttk.Button(frame_delete_compound, text='Delete', command=delete_compound)
delete_button.grid(row=1, column=2, padx=5, pady=5)

window.mainloop()