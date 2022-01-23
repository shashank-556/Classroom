# Introduction
Classroom is a platform to create and join digital classrooms.<br>
The API is based on REST returns JSON-encoded responses, and returns standard HTTP response codes.
* The base url for the API is: `shashankkkkk.pythonanywhere.com/`

## Authorization
The project uses **[JWT](https://jwt.io/)** for authorization and authentication. You can obtain the tokens with a registered email and password from Obtain Token endpoint. <br>
**The token claims related to user are the user_id and user_name**.<br>
You must send the unexpired, valid access tokens in the request header `Authorization: Bearer {{token}}`<br>
All the endpoints of the API require authentication so you must send access tokens in each request to the API.<br>
The API endpoints for following **do not** require users to be authenticated i.e. no need to provide tokens.
* User Registration
* Obtain Token
* Token Refresh

## Functionalities

* [User Registration](#reg)
* [Obtain Token](##obtain-token)
* [Token Refresh]()
* [Creating class]()
* [View created and joined classes]()
* [Basic info of a class]()
* [Enroll in a class]()
* [Uenroll from a class]()
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

## View Basic info of a class
*Requires Authentication and Class Membership*<br>
Request basic info like name,description,creater_name of a class<br>
**Endpoint** `class/<integer:classid>/`<br>
**HTTP METHOD** `GET`<br>

**Response**

<a name="reg"></a>

## Joining/Enrolling in a class
*Requires Authentication*<br>
**Endpoint** `class/join/`<br>
**HTTP METHOD** `POST`<br>
**Form Fields for POST**
* {"code"}<br><br>
**Fields Description**
* code : A class code which is a 6-8 character random string of lowercase ascii characters, unique for particular classroom .

**Response**

## Unenroll/Leave a class
*Requires Authentication and Class Membership*<br>
Member of a class can send a delete request at the url of the classroom<br>
**Endpoint** `class/<integer:classid>/member/`<br>
**HTTP METHOD** `DELETE`<br>

**Response**
* `200` Upon  succesfully unenrolling from a class



