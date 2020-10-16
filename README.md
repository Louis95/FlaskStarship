FlaskStarship
----------

###
FlaskStarWar is an application that displaces the list of all starships from star war movies sorted by their hyperdrive


### Main Files: Project Structure

  ```
  ├─- README.md
  ├── app.py *** the main driver of the app.
                    "python app.py" to run after installing dependences
  ├── requirements.txt *** The dependencies we need to install with "pip3 install -r requirements.txt"
 
  ```

### Development Setup

First, [install Flask](http://flask.pocoo.org/docs/1.0/installation/#install-flask) if you haven't already.

  ```
  $ cd ~
  $ sudo pip3 install Flask
  ```

To start and run the local development server,

1. Initialize and activate a virtualenv:
  ```
  $ cd YOUR_PROJECT_DIRECTORY_PATH/
  $ virtualenv --no-site-packages env
  $ source env/bin/activate
  ```

2. Install the dependencies:
  ```
  $ pip install -r requirements.txt
  ```

3. Run the development server:
  ```
  $ export FLASK_APP=myapp
  $ export FLASK_ENV=development # enables debug mode
  $ flask run
  ```

### Endpoints

https://flaskstarship.herokuapp.com/ | https://git.heroku.com/flaskstarship.git

GET '/'
- welcome note

GET '/starships'
- Fetches starships from https://swapi.dev/api/starships/ groupded
-  Returns:A JSON object with the following structure 
   - starships = A list of starships(names and hyperdrive rating) that have hyperdrive rating. Sorted by hyperdrive rating in ascending order.
   - starships_unknown_hyperdrive = A list of starships(just the names) that the hyperdrive rating is unknown.

### Deployment

This guide assumes that you already had gone through the process of installing and authenticating the Heroku Toolbelt.

I'm assumming that you already have heroku installed. If you haven't installed heroku, please check the [installation guide](https://devcenter.heroku.com/articles/heroku-cli)

`web: gunicorn <filename>:<app_name>`

#### Create Your Heroku App
You can also leave your_app_name empty if you want Heroku to create a randomized name.

