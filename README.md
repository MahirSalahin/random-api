Random API
===========

This API provides a set of endpoints for generating random data.

Endpoints
---------

### `/`
Get a random float between 0 and 1.

* Method: `GET`
* Response: `{"random": float}`

### `/random_in_range/{left}/{right}`
Get a random integer within the specified range.

* Method: `GET`
* Parameters:
	+ `left`: int (default: 0)
	+ `right`: int (default: math.inf)
* Response: `{"random": int}`
* Errors:
	+ 400: Invalid range (left > right)

### `/toss_a_coin`
Simulate a coin toss and get the result.

* Method: `GET`
* Response: `{"result": "Heads" | "Tails"}`

### `/select/{options}`
Select a random option from the given list.

* Method: `GET`
* Parameters:
	+ `options`: JSON-encoded list of options
* Response: `{"selected": string}`
* Errors:
	+ 400: Invalid options (empty list)
