# Introduction
Classroom is a platform to create and join digital classrooms.<br>
The API is based on REST returns JSON-encoded responses, and returns standard HTTP response codes.
* The base url for the API is: `shashankkkkk.pythonanywhere.com/`

## Authorization
The project uses **[JWT](https://jwt.io/)** for authorization and authentication. You can obtain the tokens with a registered email and password from Obtain Token endpoint. The only token claims related to user is the user id.<br>
You must send the unexpired, valid access tokens in the request header `Authorization: Bearer {{token}}`<br>
All the endpoints of the API require authentication so you must send access tokens in each request to the API.<br>
The API endpoints for following **do not** require users to be authenticated i.e. no need to provide tokens.
* User Registration
* Obtain Token
* Token Refresh

## Functionalities

* [User Registration]()
* [Obtain Token]()
* [Token Refresh]()
* [Creating class]()
* [Enroll in a class]()
* [Uenroll from a class]()
* [Basic info of a class]()
* [Contents of a class]()
* [Members of a class]()

* [API Endpoints]()

## User Registration
Users can register with a unique email address
### Endpoint
* `register/`
### Methods Required
* POST 
### Form Fields for POST
* {"first_name","last_name","email","password"}*
#### Fields Description
* first_name : First name of the user , Max-Length = 40 characters
* last_namee : Last name of the user, Max-Length = 40 characters
* email : A valid , unique email address.
* password : Rember your password as it will be used in token generation
### Response


## Obtaining Tokens
Obtain jwt Access and Refresh tokens for registered users. Refresh token is valid for 30 days and access token is valid for 5 days..
### Endpoint
* `login/`
### Methods Required
* POST
### Form Fields for POST
* {"email","password"}
Provide correct combination of email and password to obtain the tokens
### Response

## Token Refresh
Obtain another valid access token by using the refresh token
### Endpoint
* `login/refresh/`
### Methods Required
* POST
### Form Fields for POST
* {"refresh"}
#### Fields Description
* refresh : A valid unexpired refresh token
### Response

## Creating a class
*Requires Authentication*<br>
You can create a class by providing name and description of a class.
### Endpoint
* `class/`
### Methods Required
* POST
### Form Fields for POST
* {"refresh"}
#### Fields Description
* refresh : A valid unexpired refresh token
### Response
