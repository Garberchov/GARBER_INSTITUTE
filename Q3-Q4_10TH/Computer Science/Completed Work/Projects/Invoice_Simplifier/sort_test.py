from tkinter import *
from tkinter import ttk
from supabase import create_client, Client

supabaseUrl = 'https://mldfcbinlomjgvsanlzs.supabase.co'
supabaseKey = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im1sZGZjYmlubG9tamd2c2FubHpzIiwicm9sZSI6ImFub24iLCJpYXQiOjE2NTEyMzk1NjksImV4cCI6MTk2NjgxNTU2OX0.VeKe2-FCHAk7aAW_bjBHp5kJDHgGvl0yDonvbqEosJI'
supabase: Client = create_client(supabase_url=supabaseUrl, supabase_key=supabaseKey)



def fetch():
	return supabase.table('invoicer').select("*").execute()

data = fetch()
list_data = list(data)
print(list_data)
print("------------")
for x in list_data:
        my_list = list(x)
        for y in my_list:
                try:
                        for z in y:
                                if type(z) is dict:
                                        list_z = list(z)
                                        print(list_z)
                except TypeError:
                        pass