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
* [View created and joined classes]()
* [Enroll in a class]()
* [Uenroll from a class]()
* [Basic info of a class]()
* [Contents of a class]()
* [Members of a class]()

* [API Endpoints]()

## User Registration
Users can register with a unique email address<br>
**Endpoint** `register/`<br>
**HTTP METHOD** `POST`<br>
**Form Fields for POST**
* {"first_name","last_name","email","password"}<br><br>
**Fields Description**
* first_name : First name of the user , Max-Length = 40 characters
* last_namee : Last name of the user, Max-Length = 40 characters
* email : A valid , unique email address.
* password : Rember your password as it will be used in token generation

**Response**


## Obtaining Tokens
Obtain jwt Access and Refresh tokens for registered users. Refresh token is valid for 30 days and access token is valid for 5 days.<br>
**Endpoint** `login/`<br>
**HTTP METHOD** `POST`<br>
**Form Fields for POST**
* {"email","password"}

Provide correct combination of email and password to obtain the tokens

**Response**

## Token Refresh
Obtain another valid access token by using the refresh token<br>
**Endpoint** `login/refresh/`<br>
**HTTP METHOD** `POST`<br>
**Form Fields for POST**
* {"refresh"}<br><br>
**Fields Description**
* refresh : A valid unexpired refresh token

**Response**

## Creating a class
*Requires Authentication*<br>
You can create a class by providing name and description of a class.<br>
**Endpoint** `class/`<br>
**HTTP METHOD** `POST`<br>
**Form Fields for POST**
* {"name","description"}<br><br>
**Fields Description**
* name : Name of your classroom, Max-Length = 30 characters
* description : Description of a classroom, Max-Length = 60 characters

**Response**

## View all the created and joined classes
*Requires Authentication*<br>
Users can view all their created class and joined classes.<br>
**Endpoint** `class/`<br>
**HTTP METHOD** `GET`<br>
**Query for GET**
* {q=created,q=joined}<br><br>
**Query Description**
* q=created : Returns a list of json objects of all the classes crated by the user
* q=joined : Returns a list of json objects of all the classes joined by the user

**Response**

## Joining/Enrolling in a class
*Requires Authentication*<br>
**Endpoint** `class/join/`<br>
**Methods Required** `POST`<br>
**Form Fields for POST**
* {"code"}<br><br>
**Fields Description**
* code : A class code which is a 6-8 character random string of lowercase ascii characters, unique for particular classroom .

**Response**

## Unenroll/Leave a class
*Requires Authentication*<br>
Member of a class can send a delete request at the url of the classroom<br>
**Endpoint** `class/<integer:classid>/member/`<br>
**HTTP METHOD** `DELETE`<br>

**Response**
* `200` Upon  succesfully unenrolling from a class


