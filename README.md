# Luca-app-API
A small library for the private API of the german "Luca app".
This library is far from finished - only some methods work right now. Feel free to add anything you find! 
There are no library docs yet.


#### All Luca API docs I wrote for this are in the `docs.md` file.
#### The python3 library sits in the luca.py file. Some things don't yet.


## Example:

Lists all of the created locations.
```
l = Luca()
l.login(email, password)

groups = l.getAllLocations()
for count, location in enumerate(groups):
	print(f"Location {count +1}: {location['name']}")
```
