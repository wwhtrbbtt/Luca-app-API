# login/registration

## Registration

POST `https://app.luca-app.de/api/v3/operators`
Format: 
Data: (json)
```
{
   "email": "<email>",
   "firstName": "<first name>",
   "lastName": "<last name>",
   "password": "<password>",
   "agreement": true,
   "avvAccepted" :true,
   "lang": "en"
}
```

### Returns
	204
	No data

This will send a confirmation email

Link format:
	`https://app.luca-app.de/activation/9f5046e5-8e1c-45ec-9916-e756493d52b4`

When you visit the URL, the account will get activated


## Login

POST `https://app.luca-app.de/api/v3/auth/login`
Data: (json)

```
{
	"username": "<email>",
	"password":"<password>"
}
```

On successfull response:
	

### Returns
	200
	Cookie `connect.sid`
	"Ok"

# Manage Locations

## Create location

POST `https://app.luca-app.de/api/v3/locationGroups`
Data (json):

```
{
   "type": "base",
   "name": "<location name>",
   "phone": "<phone number>",
   "streetName": "<street>",
   "streetNr": "<street number>",
   "zipCode": "<zip>",
   "city": "<city>",
   "state": "<state>",
   "lat": <lat>,
   "lng": <long>,
   "radius": 0,
   "areas":[
      
   ],
   "isIndoor": true
}
```

### Returns:
	200
	```
	{
	   "groupId":"<group id>",
	   "name":"<specified name>",
	   "location":{
	      "scannerId":"<scanner id>",
	      "tableCount":null,
	      "locationId":"<location id>"
	   }
	}
	```

## Get all locations

GET `https://app.luca-app.de/api/v3/locationGroups`

### Returns:
	List of same data as response from "Create location"


## Additional data for group or location

Groups:

GET `https://app.luca-app.de/api/v3/locationGroups/additionalDataSchema/<group id>`

Location:

GET `https://app.luca-app.de/api/v3/locations/additionalDataSchema/<location id>`

Returns more data like lat, long, (data specified when created)

## Checked in users for scanner ID

GET `https://app.luca-app.de/api/v3/scanners/<scanner id>/traces/count/current`

### returns:
	interger







