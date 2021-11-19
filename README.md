# RestaurantApp
A small app for an imaginary restaurant...

In order to run the app you need to install virtualenv on your machine. Then you can run it like this:

```
cd RestaurantApp
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 main.py
```


# Your Task

Add the following feature to the app:
  * write a new API for the app, which can update the price of the items in the database.
    * investigate how the price of the items are setup in `priceTable` in `main.py`
    * investigate how the APIs work in `main.py`
    * setup your API and test it. 
    * you can use `sqlitebrowser` to look into your databse.
