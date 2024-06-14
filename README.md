Random API
===========
A FastAPI application that provides a variety of randomization endpoints for generating random data, simulating random events, and more.

Features
----------

* Generate random floats, integers and characters
* Simulate coin tosses and random choices
* Generate random users and passwords

Endpoints
-----------

### `/`

* **Method:** GET
* **Description:** Server status
* **Response:** {"message": "Server is running"}


### `/random`

* **Method:** GET
* **Description:** Returns a random float between 0 and 1.
* **Response:** `{"float": <random_float>}`
* **Errors:**
	+ `500 Internal Server Error`: If an error occurs while generating the random float.

### `/random/int`

* **Method:** GET
* **Description:** Returns a random integer.
* **Response:** `{"int": <random_int>}`
* **Errors:**
	+ `500 Internal Server Error`: If an error occurs while generating the random integers.




### `/random/int/{left}/{right}`

* **Method:** GET
* **Description:** Returns a random integer within the specified range.
* **Parameters:**
	+ `left`: The minimum value of the range (inclusive).
	+ `right`: The maximum value of the range (inclusive).
* **Response:** `{"int": <random_int>}`
* **Errors:**
	+ `400 Bad Request`: If `left` is greater than `right`.
	+ `500 Internal Server Error`: If an error occurs while generating the random integer.


### `/random/char`

* **Method:** GET
* **Description:** Returns a random ASCII character.
* **Response:** `{"char": <random_char>}`
* **Errors:**
	+ `500 Internal Server Error`: If an error occurs while generating the random character.


### `/random/coinflip`

* **Method:** GET
* **Description:** Simulates a coin toss and returns the result.
* **Response:** `{"result": "Heads" or "Tails"}`
* **Errors:**
	+ `500 Internal Server Error`: If an error occurs while simulating the coin toss.


### `/random/select/{options}`

* **Method:** GET
* **Description:** Selects a random option from the given list.
* **Parameters:**
	+ `options`: A JSON-encoded list of options.
* **Response:** `{"selected": <random_option>}`
* **Errors:**
	+ `400 Bad Request`: If `options` is an empty list or not a valid JSON-encoded list.
	+ `500 Internal Server Error`: If an error occurs while selecting the random option.


### `/random/color`

* **Method:** GET
* **Description:** Returns a random hex color.
* **Response:** `{"color": <random_color>}`
* **Errors:**
	+ `500 Internal Server Error`: If an error occurs while generating the random color.


### `/random/user`

* **Method:** GET
* **Description:** Generates a random user with name, email, and password.
* **Response:** `{"name": <random_name>, "email": <random_email>, "password": <random_password>}`
* **Errors:**
	+ `500 Internal Server Error`: If an error occurs while generating the random user data.

	
### `/random/password/{length}`

* **Method:** GET
* **Description:** Generates a random password of the specified length.
* **Parameters:**
	+ `length`: The length of the password.
* **Response:** `{"password": <random_password>}`
* **Errors:**
	+ `400 Bad Request`: If `length` is less than 1.
	+ `500 Internal Server Error`: If an error occurs while generating the random password.



Live API
--------

The API is live at: 
* *https://salahin-random-api.hf.space/*
* *https://random-api-dnl4.onrender.com/*

You can test the endpoints using your favorite HTTP client or tool, such as `curl` or `Postman`.

Installation (for Development)
------------

To install the required dependencies for development, run:
```
pip install -r requirements.txt
```

Running the API (for Development)
---------------

To run the API locally for development, execute:
```
uvicorn main:app --reload
```

This will start the API server on `http://localhost:8000`.

License
-------

This API is licensed under the MIT License.

Contributing
------------

Contributions are welcome! If you'd like to add a new endpoint or feature, please submit a pull request.

Acknowledgments
-----------------

Thanks to the FastAPI and Python communities for making this project possible.