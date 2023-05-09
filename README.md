# Python-MySQL_PasswordManager

A secure password manager that is run within the terminal. It has all the features you need.
It hash encrypts your passwords and they can only be seen when you copy them into your clipboard. 
Also it has the option to generate secure passwords of a desired lenght. Other than that if offers 
the functionality you'd spect from a password manager, see all entries, retrieve a certain entry, add 
and entry, delete and entry, etc.

Guide:

1. First you have to open the 'config.py' file with the terminal with the make option: 'config.py make'
and the database will be created automatically and will ask you to put in a master password (MP) to
handle every command within the program.

2. In the 'how-to.txt' file attached to this repository, and also below here in the README you can find all the commands
needed to add, delete, retrieve and copy entries. 

------------ DATABASE CREATION ------------

config.py make = make new database and pick new mp
config.py delete = delete existing database
config.py remake

------------ COMMANDS ------------

pm.py add -s sitename -u siteurl -e email -l loginname = ADD ENTRY 
pm.py d -s sitename -u siteurl -e email -l loginname = DELETE ENTRY
pm.py e = SHOW ALL ENTRIES
pm.py e -s sitename == SHOW SPECIFIC ENTRY
pmpy e -s sitename --copy = COPY PASSWORD TO CLIPBOARD
pm.py g --lenght = GENERATE PASSWORD
pm.py help = show all commands
