notitas
=======

This is a prototype project with basic logic in Django. Requires installing requirements.

Steps to initialize the project:

1) create a virtual environment, virtualenv notitas.
2) install the requirements with pip using the list of packages in requirements.txt
3) the db is already in the repository, so you should run the server without problems:
    >>> python manage.py runserver
4) load the browswer in 8000 defualt port, or in a different port if passed as argument to the command in 3)


BackEnd:
The application is simple. Note model, that store the notes in a text field. Every time a new note is created,
the hashes (#) are extracted, and for every hash that doesn't exist as a Tag instance, it is created as a new
Tag. The Tags are represented as a text field, and a counter that keeps track of how many times it has been mentioned
in a Note.

An admin is provided, but it doesn't give much advantage here. The user:password is luchux:luchux
Be careful if adding notes from the admin, because you should define the M2M relation to the tags by hand,
as it is expected in the admin with an inlineForm. (if the note is add from front end, all is safe).

The Database is configured as a sqlite3. There is no heavy data load on this app.

FrontEnd:
The Front End uses Django Template in some parts, to show the use of for example ModelForms (NoteForm).
Other parts use AJAX, with JQuery, specially for retrieve the list of notes in the url /notes/ and the
call send data {tags:[array of tags]}, that the logic in the backend uses for selecting only those notes
that contains that tags. If there are no tags, then the whole list of notes is returned to the front end.

The styles are provided by Twitter Bootstrap lib, stored in the static/ folder.
[IMPORTANT] JQuery libs are loaded online, so you should have internet access to make the app work well.

Code:
The comments and the code style doesn't follow any standard, more than PEP and some Google Python Style Programming.
Other programming conventions can be defined, to make the code looks standarized with some base code.
