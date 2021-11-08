# Chainalysis_project

## Software Engineer, University Grad take home test at Chainalysis

### How to run

First, you will have to make a Shrimpy account and get an API key and Secret. Feel free to email me (pc2858@columbia.edu) if you would prefer to just use mine to test the webpage.

Once you have the Api key and secret you should add them to a secrets.json file in the same directory as app.py. It should look like:

```
{
  "public": "your public key",
  "secret": "your secret key"
}

```

Once you have this file, you can create a virtual environment. For example:

```
python3 -m venv env
```

You can close and open the environment by respectively running:

```
source env/bin/activate
deactivate
```

Once you are in the environment, you can run:

```
pip install -r requirements.txt
```

Which will install the requirements for this project.

Once all is done, you can run:

```
flask run
```

The webpage will be at http://localhost:5000/
If you wish to gracefully terminate the page, go to http://localhost:5000/stopServer
Feel free to explore different routes ;)

### Questions

#### Are there any sub-optimal choices( or short cuts taken due to limited time ) in your implementation?

With more time, I would have spent more time on the front-end. I have not done much front end in the past and I am willing to learn.
Due to issues with validating my French ID, creating accounts with many exchanges, and finding a free API that provides the detailing of the currency prices (buy and sell), I resorted to use the Shrimpy API. I have encounteres moments when it was down, so with more time I would have gotten the data directly from the corresponding excchanges.
I am also currently refreshing the page every 20 seconds with javascript code in my html page. With more time I would want my app to ressemble a single page application, either switching to react or using a library such as Turbo Flask
Improving my error checking and edge cases in my code is essential if I would work on it further.
The only hard coded parts work with this assignment (Exchange and currency names in the html), and I would have removed those completely, especially if I had implemented what I wanted to implement the enhancements I discuss.

#### Is any part of it over-designed? ( It is fine to over-design to showcase your skills as long as you are clear about it)

In the interest of time, I believe I did not overdesign anything and went for the MVP.

#### If you have to scale your solution to 100 users/second traffic what changes would you make, if any?

Sending requests to the API is already sub optimal for one user every 20 seconds, so I would request it once for all my users and store the values for a certain amount of time, that I would then distribute to all my users. I would probably make the refresh manual, in case users stayed on the page.

#### What are some other enhancements you would have made, if you had more time to do this implementation?

With more time, I would have added a way to add/remove currencies and exchanges to the tracker. And using historical API data, would have enjoyed implemented a simple regression to have an additional recommendation on whether or not to buy any currencies.
