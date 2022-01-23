# Introduction
Classroom is a platform to create and join digital classrooms.<br>
The API is based on REST returns JSON-encoded responses, and returns standard HTTP response codes.
* The base url for the API is: `shashankkkkk.pythonanywhere.com/`
<hr>

## Authorization
The project uses **[JWT](https://jwt.io/)** for authorization and authentication. You can obtain the tokens with a registered email and password from Obtain Token endpoint. <br>
**The token claims related to user are the user_id and user_name**.<br>
You must send the unexpired, valid access tokens in the request header `Authorization: Bearer {{token}}`<br>
All the endpoints of the API require authentication so you must send access tokens in each request to the API.<br>
The API endpoints for following **do not** require users to be authenticated i.e. no need to provide tokens.
* User Registration
* Obtain Token
* Token Refresh

If you try to access rest of the views without a valid access token with Authorization header then you will get a `401` Unathorized error.
<hr>

## Functionalities

* [User Registration](#user-registration)
* [Obtain Token](#obtaining-tokens)
* [Token Refresh](#token-refresh)
* [Creating class](#creating-a-class)
* [View created and joined classes](#view-all-the-created-and-joined-classes)
* [Basic info of a class](#view-basic-info-of-a-class)
* [Enroll in a class](#joiningenrolling-in-a-class)
* [Members of a class](#view-classroom-members-or-students)
* [Uenroll from a class](#unenrollleave-a-class)
* [Contents of a class](#contents-of-a-class)

* [API Endpoints](#all-api-endpoints-and-their-allowed-methods)
<hr>

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
* `201` : When user is registered successfullly.
* `400` : When a user with provided email already exists  or a bad request is sent.

**Example Response for 201**<br>
```json
{
    "id": 8,
    "email": "shashanktrp556@gmail.com",
    "first_name": "shashank",
    "last_name": "tripathi",
    "created_at": "2022-01-23T16:01:11.192997+05:30"
}
```
<hr>

## Obtaining Tokens
Obtain jwt Access and Refresh tokens for registered users. Refresh token is valid for 30 days and access token is valid for 5 days.<br>
**Endpoint** `login/`<br>
**HTTP METHOD** `POST`<br>
**Form Fields for POST**
* {"email","password"}

Provide correct combination of email and password to obtain the tokens

**Response**
* `200` : When provided credentials are correct and token is successfully created.
* `401` : When provided credentials do not match or do not exist
* `400` : When a bad request is sent

**Example Response for 200**<br>
```json
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY0NTUyNTkzNSwiaWF0IjoxNjQyOTMzOTM1LCJqdGkiOiI0MTZmYTBiYzhkMWM0YjFkYWE0NTcyYjEzY2RjM2RlMSIsInVzZXJfaWQiOjgsInVzZXJfbmFtZSI6InNoYXNoYW5rIHRyaXBhdGhpIn0.PDqF17MQqZVUzWup6Y2NeQ2YjYYbWfYS3b1Q_cCpCxc",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQzMzY1OTM1LCJpYXQiOjE2NDI5MzM5MzUsImp0aSI6IjJmMmE2MThkN2UwNjQwM2RiMmNjOGU0MjYxNjJmNjA1IiwidXNlcl9pZCI6OCwidXNlcl9uYW1lIjoic2hhc2hhbmsgdHJpcGF0aGkifQ.foQe6Dm4R1LUcc2LIrqDsfwZ8JZqy9lxeFRqYDlgbFQ"
}
```
<hr>

## Token Refresh
Obtain another valid access token by using the refresh token<br>
**Endpoint** `login/refresh/`<br>
**HTTP METHOD** `POST`<br>
**Form Fields for POST**
* {"refresh"}<br><br>
**Fields Description**
* refresh : A valid unexpired refresh token

**Response**
* `200` : When an access token is successfully generated
* `400` : When a bad request is sent

**Example Response for 200**<br>
```json
{
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQzMzY2MDQ4LCJpYXQiOjE2NDI5MzM5MzUsImp0aSI6IjI1NzAwNWNhMGY5MjQ0NWQ4YTE3OTdjMzcxNTBhZjM3IiwidXNlcl9pZCI6OCwidXNlcl9uYW1lIjoic2hhc2hhbmsgdHJpcGF0aGkifQ.lN8bnTbcIe4RaDwcI6AdVwNL6-fKUn3dACJClUMSaG8"
}
```
<hr>

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
* `201` : When a class is successfully created.
* `400` : When a bad request is sent

**Example Response for 201**<br>
```json
{
    "id": 11,
    "code": "irqfaoj",
    "name": "Operating system",
    "description": "This class is for IT 3rd semester students.",
    "created_at": "2022-01-23T15:11:55.799756+05:30"
}
```
<hr>

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

**Example response for url `shashankkkkk.pythonanywhere.com/class?q=created` for some user**
```json
[
    {
        "id": 10,
        "code": "mohhtn",
        "name": "Operating system",
        "description": "test2",
        "created_at": "2022-01-23T14:48:09.909769+05:30"
    },
    {
        "id": 11,
        "code": "irqfaoj",
        "name": "Operating system",
        "description": "This class is for IT 3rd semester students.",
        "created_at": "2022-01-23T15:11:55.799756+05:30"
    }
]
```
**Example response for url `shashankkkkk.pythonanywhere.com/class?q=joined` for some user**
```json
[
    {
        "id": 1,
        "name": "OS",
        "description": "Operating systems are cool",
        "created_at": "2022-01-10T21:12:15.679056+05:30",
        "creater": "someone4 noone4"
    },
    {
        "id": 2,
        "name": "CD",
        "description": "Compiler design is a cool class",
        "created_at": "2022-01-11T15:27:45.774607+05:30",
        "creater": "someone2 noone2"
    }
]
```
If the user has no created or joined classes then the response will be an empty list or array i.e. []
<hr>

## View Basic info of a class
*Requires Authentication and Classroom Membership*<br>
Request basic info like name,description,creater_name of a class<br>
**Endpoint** `class/<integer:classid>/`<br>
**HTTP METHOD** `GET`<br>

**Response**
* `200` : upon sccessful retrieval of class information.
* `403` : When the user is neither the owner nor the member of a class
* `404` : When url is incorrect or provided int is not a PK of any class.


**Example for class with id=2 when it is requested by the owner** url : `base_url/class/2/`
```json
{
    "id": 2,
    "code": "kwargrq",
    "name": "CD",
    "description": "Compiler design is a cool class",
    "created_at": "2022-01-11T15:27:45.774607+05:30"
}
```

**Example for class with id=2 when it is requested by the members or students of a class** url : `base_url/class/2/`
```json
{
    "id": 2,
    "name": "CD",
    "description": "Compiler design is a cool class",
    "created_at": "2022-01-11T15:27:45.774607+05:30",
    "creater": "someone2 noone2"
}
```
<hr>

## Joining/Enrolling in a class
*Requires Authentication*<br>
**Endpoint** `class/join/`<br>
**HTTP METHOD** `POST`<br>
**Form Fields for POST**
* {"code"}<br><br>
**Fields Description**
* code : A class code which is a 6-8 character random string of lowercase ascii characters, unique for particular classroom .

**Response**
* `201` : If the user joins successfully
* `200` : if the user is already a member of the class
* `403` : Forbidden if the creater of a class tries to join its own class.
* `400` : On bad request
* `404` : If code is invalid or url is wrong

When a user joins a class the response is same if a member of student of a class requested the basic info of the class

**Example response for 201 or 200 when a user joins a class with a valid code or is already a member**
```json
{
    "id": 4,
    "name": "ML",
    "description": "Machine Learning",
    "created_at": "2022-01-11T15:29:12.949036+05:30",
    "creater": "someone4 noone4"
}
```
<hr>

## View Classroom Members or Students
*Requires Authentication and Classroom Membership*<br>
See all the members of class<br>
**Endpoint** `class/<integer:classid>/member/`<br>
**HTTP METHOD** `GET`<br>

**Response**
* `200` : upon sccessful retrieval of class members.
* `403` : When the user is neither the owner nor the member of a class
* `404` : When url is incorrect or provided int is not a PK of any class.

**Example for class with id=2 when it is requested by the owner or a member** url : `base_url/class/2/member/`
```json
{

    "creater": "someone2 noone2",
    "students": [
        "someone3 noone3",
        "someone4 noone4"
    ]
}
```
<hr>

## Unenroll/Leave a class
*Requires Authentication and Class Membership*<br>
Member of a class can send a delete request at the url of the classroom<br>
**Endpoint** `class/<integer:classid>/member/`<br>
**HTTP METHOD** `DELETE`<br>

**Response**
* `200` : Upon  succesfully unenrolling from a class
* `404` : If classid is invalid 

*No data is returned upon successful unenrollment*
<hr>

## Contents of a class
*Requires Authentication and Class Membership*<br>
Note that all the contents returned are sorted in descending order of their creation time i.e. most recently created content is at the top. 

### View all content of the class
*Both Owner and member can perform this action*<br>
**Endpoint** `class/<integer:classid>/content/`<br>
**HTTP METHOD** `GET`<br>

**Response**
* `200` : upon sccessful retrieval of class contents.
* `403` : When the user is neither the owner nor the member of a class
* `404` : When url is incorrect or provided int is not a PK of any class.

**Example response for** `base_url/class/2/content/`
```json
[
    {
        "id": 7,
        "msg": "This is your lecutere number 4.",
        "created_at": "2022-01-19T16:57:24.019598+05:30"
    },
    {
        "id": 3,
        "msg": "This is your lecutere number 3",
        "created_at": "2022-01-16T21:18:43.705590+05:30"
    },
    {
        "id": 2,
        "msg": "This is your lecutere number 2.",
        "created_at": "2022-01-15T23:45:59.763466+05:30"
    },
    {
        "id": 1,
        "msg": "Your first lecute is scheduled to on this link: www.somestupidvideostreamingapp.com/sdlfds/",
        "created_at": "2022-01-15T23:45:20.227275+05:30"
    }
]
```
Empty list [] is returned if no content is present.

### Create content of a class
*Only Owner or creater of classroom can perform this action*<br>
**Endpoint** `class/<integer:classid>/content/`<br>
**HTTP METHOD** `POST`<br>
**Form Fields for POST**
* {"msg"}<br><br>
**Fields Description**
* msg : First name of the user , Max-Length = 200 characters

**Response**
* `201` : upon sccessful creation of class content.
* `403` : When the user is neither the owner nor the member of a class
* `404` : When url is incorrect or provided int is not a PK of any class.

**Example response for 201**
```json
{
    "id": 10,
    "msg": "This is your lecture number 4",
    "created_at": "2022-01-23T18:52:20.657353+05:30"
}
```

### Update content of a class
*Only Owner or creater of classroom can perform this action*<br>
**Endpoint** `class/<integer:classid>/content/<integer:contentid>/`<br>
**HTTP METHOD** `PUT`<br>
**Form Fields for PUT**
* {"msg"}<br><br>
**Fields Description**
* msg : First name of the user , Max-Length = 200 characters

**Response**
* `200` : upon sccessful updation of class content.
* `403` : When the user is neither the owner nor the member of a class
* `404` : When url is incorrect or provided int is not a PK of any class or invalid contentid.

**Example response for 200**
```json
{
    "id": 10,
    "msg": "This is your lecture number 5",
    "created_at": "2022-01-23T18:52:20.657353+05:30"
}
```

### Delete content of a class
*Only Owner or creater of classroom can perform this action*<br>
**Endpoint** `class/<integer:classid>/content/<integer:contentid>/`<br>
**HTTP METHOD** `DELETE`<br>

**Response**
* `200` : upon sccessful deletion of class content with given contentid.
* `403` : When the user is neither the owner nor the member of a class
* `404` : When url is incorrect or provided int is not a PK of any class or invalid contentid.

*No data is sent on deletion*


## All API endpoints and their allowed methods

* (POST) `shashankkkkk.pythonanywhere.com/register/`           
* (POST) `shashankkkkk.pythonanywhere.com/login/`
* (POST) `shashankkkkk.pythonanywhere.com/login/refresh/`
* (GET,POST) `shashankkkkk.pythonanywhere.com/class/`
* (GET) `shashankkkkk.pythonanywhere.com/class/<int:classid>/`
* (GET,POST) `shashankkkkk.pythonanywhere.com/class/<int:classid>/content/`
* (DELETE,PUT) `shashankkkkk.pythonanywhere.com/class/<int:classid>/content/<int:contentid>/`
* (GET,DELETE) `shashankkkkk.pythonanywhere.com/class/<int:classid>/member/`
* (POST) `shashankkkkk.pythonanywhere.com/class/join/`

