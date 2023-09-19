import database

#database.add_person("Ciccio", "Bello", "ciccio@com")
p_list = [('Beta', 'Betowski', 'b@betowski.com'),
('Omega', 'O', 'omega@O')]
#database.add_persons(p_list)

database.email_lookup('omega@O')
#database.show_people()
#database.del_person('5')  # has to be string even if rowid is an int!

