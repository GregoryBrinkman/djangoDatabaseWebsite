#Database Project
A website for the 'Notown' record company.

Customers can search for musicians, albums and songs by name.

After logging in, Admins can search for, edit, or delete any item or relation in the Notown Catalog.
Admins can also add, edit, or delete users to the Notown Admin Panel

I figured that there should be a phoneNumber for both 'musicians' and 'address'.
I changed the original schema to remove this ambiguity in the database. 

Most of the constraints are not captured in sql, but instead in abstracted python models and views.
These constraints will be clear upon usage of the Notown Admin Panel

I tried to make this as close to a real world project as possible, so I decided to build a website.
It's currently at the deployed at the url below.
gregorybrinkman.pythonanywhere.com

All of the code is located on github at:
https://github.com/GregoryBrinkman/djangoWebsite

To access the database directly, we use the command:

$ python manage.py dbshell
(I will show this more clearly at the meeting)

Happy Testing!
