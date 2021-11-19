# RestaurantApp G1

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

Add the following feature to the cash-register page:
* Make an overlay screen with a small spinner to block the view for cash register while the user waits for server to respond. you can activate/deactivate the overlay in `submitOrder` function.
