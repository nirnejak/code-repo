# Heroku Deployment Process for Flask App
Execute these tasks in your project directory After managing dependencies with **pipenv**.


## Create Procfile
```js
web: gunicorn <yourAppFilename>:<yourappname>
```

## Execute these commands
```sh
$ heroku create
$ git add .
$ git commit -m "Commit Message"
$ git push heroku master
$ heroku open
```