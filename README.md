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

Add the following feature to the cash-register page:
* Once the user selects a food option, send a request to the server, asking for the price of the order.
  * Use a `POST` request to the API `/get_price` with data format: `{"item": <item name>}`.
  * The answer will be in format: `{"item": <item name>, "price": <item price>}`.
  * update the price in the order list
  * subtract the value from the item once the cross button is pressed using `onclick` function for the element.
