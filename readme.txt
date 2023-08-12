Hello SoftUni,

This is a file with some information regarding my project.

1. Locally, you have to set up postgres database as I did not deploy the project.

2. When creating the superuser, it is not linked to the profile model as it is created via command.
This is probably a mistake on my end as I didn't find how to create the superuser with the profile model.
I only found how to create custom superuser command, which I don't think is what I need.

3. After setting up the database, you have to create a superuser, 1-2 staff users with the Staff Group and
1-2 normal users so that you can test the behaviour of all. After creating the superuser, you have
to manually link it to the profile from the admin panel.

4. You have to create the categories manually as I was unable to populate them on db creation.
   	Example list of categories:
        1	Meat
        2	Vegan
        3	Breakfast
        4	Bread
        5	Soup
        7	Vegetarian
        8	Main Dishes
        9	Desserts
        10	Alaminute

5. Regarding the Security features:
    a/ SQL Injection is automatically implemented if we are using the Django ORM.
    b/ To prevent XSS attacks, Django automatically escapes variables that are rendered in templates
       except we use the |safe filter, which I didn't.
    c/ CSRF - I used the {% csrf_token %} everywhere in my post forms.
    d/ Parameter tampering - I think I did all the needed validations both on server and client side.