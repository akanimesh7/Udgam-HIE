Online Ehopping portal for art and crafts of North East India made using Django and python.
The site is running on ashish2011.pythonanywhere.com

To see the codebase or run the server locally perform the following steps:
1.Clone or Download the project in your PC using user interface or command line.
2.Extract the downloaded file.
3.Go to ekraft/ekraft/settings.py and edit settings.py file.
4. Edit the Allowed_hosts and clear the entry of the list in it.
5. Enter these commands in terminal after changing the directory to ekraft folder.
  python manage.py makemigrations
  python manage.py migrate
5. Run the server locally using pyhton manage.py runserver command.
6. Open the browser and open the url 127.0.0.1:8000/
