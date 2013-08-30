# appfog-mongo-example

(Nearly) minimal working example of using MongoDB and a Python Bottle app with Appfog.

## Installation

appfog will run something like `pip install -r requirements.txt` in this directory, so you can require other python packages from PyPI (the central python packaging repository) by adding them to [`requirements.txt`](requirements.txt), each on a new line.

## Deployment

1. Create an account on [appfog](https://www.appfog.com/).
2. Install the command line interface (CLI) to appfog: `gem install af` (you may need to `sudo ...`)
3. Configure the CLI tool: `af login`
4. Get this package: `git clone https://github.com/chbrown/appfog-mongo-bottle.git`
5. Make package root your current working directory: `cd appfog-mongo-bottle`
6. Deploy with a simple `af push`

## Options

You'll be asked several questions, here's what I put:

* Would you like to deploy from the current directory? [Yn]: **y**
* Application Name: **appfog-mongo-bottle**
* Detected a Python WSGI Application, is this correct? [Yn]: **y**
    + 1: AWS US East - Virginia
    + 2: AWS EU West - Ireland
    + 3: AWS Asia SE - Singapore
    + 4: HP AZ 2 - Las Vegas
* Select Infrastructure: **1**
* Application Deployed URL [appfog-mongo-bottle.aws.af.cm]: **_return_**
* Memory reservation (128M, 256M, 512M, 1G, 2G) [64M]: **128M**
* How many instances? [1]: **1**
* Bind existing services to 'appfog-mongo-bottle'? [yN]: **n**
* Create services to bind to 'appfog-mongo-bottle'? [yN]: **y**
    + 1: mongodb
    + 2: mysql
    + 3: postgresql
    + 4: rabbitmq
    + 5: redis
* What kind of service?: **1**
* Specify the name of the service [mongodb-434c7]: **_return_**
* Create another? [yN]: **n**
* Would you like to save this configuration? [yN]: **y**

Saying **y** to the final question will create a file [`manifest.yml`](manifest.example) which will be used the next time you run `af push` (for example, after making a change to the code).

Now you can go to [appfog-mongo-bottle.aws.af.cm](http://appfog-mongo-bottle.aws.af.cm/) to see the app in action!

## License

[WTFPL](http://www.wtfpl.net/txt/copying/) licensed.
