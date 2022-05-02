from tkinter import *
from tkinter import ttk
from supabase import create_client, Client

# Global VARS
company_name = 'Argyle Marketplace'
supabaseUrl = 'https://mldfcbinlomjgvsanlzs.supabase.co'
supabaseKey = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im1sZGZjYmlubG9tamd2c2FubHpzIiwicm9sZSI6ImFub24iLCJpYXQiOjE2NTEyMzk1NjksImV4cCI6MTk2NjgxNTU2OX0.VeKe2-FCHAk7aAW_bjBHp5kJDHgGvl0yDonvbqEosJI'
supabase: Client = create_client(supabase_url=supabaseUrl, supabase_key=supabaseKey)
# Code

window = Tk()
window.title(f'Invoice Simplifier {company_name}')
window.geometry("720x480")

canvas = Canvas(window, width=720, height=480)


def get_value(): 
        temp_list = []
        customer_name = name_input.get()
        # don't delete customer name as it would have to be retyped for every item

        customer_contact = contact_input.get()
        # don't delete customer contact as it would have to be retyped for every item

        customer_day = day_input.get()
        # don't delete customer day as it would have to be retyped for every item

        item = item_input.get()
        item_input.delete(0, END)
        item_price = price_input.get()
        price_input.delete(0, END)
        
        temp_list.append(customer_name)
        temp_list.append(customer_contact)
        temp_list.append(customer_day)
        temp_list.append(item)
        temp_list.append(float(item_price))

        print(temp_list)
        final_item_dict = {'cust_name': customer_name, 'cust_contact': customer_contact, 'cust_day': customer_day, 'item_name': item, 'item_price': item_price}
        supabase.table('invoicer').insert(final_item_dict).execute()

#heading
label1 = Label(window, text="Invoice Simplifier", font=('Helvetica', 18, 'bold'))
label1.pack()


#Customer Name Input
name_label = Label(window, text="Customer Name")
name_label.pack()

name_input = Entry(window)
name_input.pack()


#Customer Contact

contact_label = Label(window, text="Customer Contact Information")
contact_label.pack()

contact_input = Entry(window)
contact_input.pack()
#Day
day_label = Label(window, text="Day")
day_label.pack()

day_input = Entry(window)
day_input.pack()

#Item Name
item_label = Label(window, text="Item Name")
item_label.pack()

item_input = Entry(window)
item_input.pack()


# Price
price_label = Label(window, text="Item Price")
price_label.pack()

price_input = Entry(window)
price_input.pack()

#Submit Item

submit_btn = ttk.Button(window, text="Submit Item", command=get_value)
submit_btn.pack()

window.mainloop()

