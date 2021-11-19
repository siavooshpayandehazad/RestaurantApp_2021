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
* write a python script that reads if the button is pressed or not every few milliseconds.
* turn on the LED on your button when it is pressed.
* send a request to your server to register a coffee every time the button is pressed. Use a `POST` request to `save_order` API. 
