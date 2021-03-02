# flash-some-card-knowledge

Demonstrating a spaced repetition learning algorithm... with flashcards! And a focus on APIs and UI/UX!

# See it Online

Coming soon! (No, really, I spun this up on a Digital Ocean droplet and this is one of the last steps)

-----
# Run It Locally

The app consists of a Django backend (to make the API bits) and a React frontend (to make the UI/UX bits), and you'll need to spin up the backend, then the frontend. Yes, you'll need two terminal windows.

## Spin up the Backend server

Requires Python 3.6 (or better), Django, and `pipenv`.

In the terminal window with the backend folder: 

1. `pipenv shell` to spin up a virtualization to run the python scripts. 
2. `pipenv install django` if you don't have it already.
3. `python manage.py migrate` so everything in the django database works like it needs to,
4. `python manage.py createsuperuser` to make your own admin account (don't forget to write down your password somewhere)
5. `python manage.py runserver 0.0.0.0:48000` to spin up the server. (yes, it needs that port in order to talk to the frontend.)
6. Log in as the account you made in Step 4 and make some Flashcards! For best results, make a few questions of different difficulty levels (I recommend 1-5) so the spaced repetition algorithm can have some fun. 

## Spin up the Frontend server 

In the terminal window with the frontend folder: 

1. `npm install` to grab some missing dependencies
2. `npm start` to spin up the frontend on `localhost:3000`

Assuming everything works correctly, you'll see a (weighted) random question pop up! Click one of the answers and you'll be greeted with another question!
