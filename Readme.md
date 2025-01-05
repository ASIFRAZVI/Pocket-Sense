# Introduction
Pocket Sense application usefull for tracking and managing student expense. 

# Getting Started:

1. git clone https://github.com/pocketsense/pocketsense.git
2. Software dependencies : Django, Python, Django REST framework, PostgreSQL, Swager .
3. Latest releases : v1
4. API references : http://{host}:{port}/v1/api/schema/swagger-ui/

#setup environment:
1. signiture
DJANGO_SECRET_KEY="Your secrate KeY"
2. debug 
DJANGO_DEBUG=True

3. application version and base configuration
APP_VERSION=v1
4. Application configuration
URLBASE=api

5. jwt 
JWT_SECRET= your jwt secret

6. DB configuration
POSTGRES_DB= your db name
POSTGRES_USER= your db user name
POSTGRES_PASSWORD= db password
POSTGRES_HOST=host
POSTGRES_PORT=port

7. timezone
time_zone= "UTC"

8. email 
EMAIL_HOST_USER= your smtp mail
EMAIL_HOST_PASSWORD= smtp password

# Build and Test
1. cmd: python -m venv venv 
2. cmd: source venv/bin/activate
3. cmd: pip install -r requirements.txt
4. cmd: python manage.py migrate
5. cmd: start.bat

#API guide

# API endpoints
1. Student registration api which is responsible for creating new student and verifiying collage email. and after creation of Student it will send the signal for otp model creation then otp model trigger signal to send otp to mail.

- Endpoint : POST /v1/api/auth/signup/
request body
{
  "name": "string",
  "email": "user@example.com",
  "password": "string",
  "phone_number": 9353580260,
  "roll_number": "string",
  "semister": "string",
  "section": "string",
  "college": "string",
  "default_payment_method": "upi"
}

response:
 ohoo! student registered! code: 201

error :
400 bad request and error message

2. login user
the login endpoint responsible for log in student by comparing hashed password and generation and storing jwt aceess, refresh token in cookies.

- enpoint: POST /v1/api/auth/signin/

body:
{
    "email": "user@example.com",
    "password": "string"
}

response:
200 ok and access and refresh token in cookies.

error:
400 bad request and error message
400 user not activated

3. logout Student

this endpoint will log out student by removing access and refresh token from cookies.

- endpoint: POST /v1/api/auth/signout/

response:
200 Student logged out

error:
400 bad request and error message

4. resend otp to mail
this endpoint will resend otp to student's registered mail.

endpoint : POST v1/api/auth/resend-otp/

body:
{
    "email": "user@example.com"
}

response:
200 otp resent to mail

error:
400 bad request and error message

5. verify otp

this endpoint will verify otp sent to student's registered mail and mark student as active user .

- endpoint : POST v1/api/auth/verify-otp/

validity : 10 mins
body:
{
    "email": "user@example.com"
    "otp": 253427
}

response:
200 Student verified

error:
400 bad request and error message

6. add expense
this end point responsible for creation student expense based on catogary.

endpoint : POST /v1/api/expense-tracker/expense/

body:
{
  "expense_catogary": "food",
  "amount": 0,
  "description": "string",
  "is_paid": true,
  "payment_method": "upi"
}

response:
201 expense created

error:
400 bad request and error message

7. get all expenses

this end point responsible for getting all student expenses.

endpoint : GET /v1/api/expense-tracker/expense/

response:
200 list of all expenses

error:
400 error and error message

8. get expense by id

this end point responsible for getting student expense by expense uuid.

endpoint : GET /v1/api/expense-tracker/expense/{expense-uuid}/

response:
200 expense by id obj

error:
400 error message

9. update expense

this end point responsible for updating student expense by expense uuid.

endpoint : PATCH /v1/api/expense-tracker/expense/{expense-uuid}/

body:
{
  "expense_catogary": "food",
  "amount": 50,
  "description": "updated food expense",
  "is_paid": true,
  "payment_method": "upi"
}

response:
200 expense updated

error:
400 error message

10. delete expense

this end point responsible for deleting student expense by expense uuid.

endpoint : DELETE /v1/api/expense-tracker/expense/{expense-uuid}/

response:
204 expense deleted

error:
400 error message

11. get all expense catogaries

this end point responsible for getting all student expense catogaries.

endpoint : GET /v1/api/expense-tracker/expense/catogaries/

response:
200 list of all expense catogaries

error:
400 error and error message

12. get total expenses with respect to Student(logged in user)
this end point responsible for getting total expenses with respect to student(logged in user)

endpoint: Post /v1/api/expense-tracker/expense/total/

response:
200 total expenses

error:
400 error and error message

13. get total expenses with respect to catogary
this end point responsible for getting total expenses with respect to student(logged in user) and provided catogary

endpoint : POST /v1/api/expense-tracker/expense/total/catogary/

response:
200 total expenses based on catogary

error:
400 error and error message


# Future Improvements (need to be implemented)
1. Add pagination to get all expenses and other endpoints.
2. Implement rate limiting to prevent abuse. (Throttling)
3. Implement password reset and forgot password feature.
4. caching techniques to improve performance.
5. query optimization for better performance.

Portfolio- https://asifrazvi.netlify.app/
resume- https://drive.google.com/file/d/1fdW8IvyfWc6tEKrbZiEtUV6zolV5Hihu/view?usp=drivesdk

email- masifraza.asif@gmail.com
ph- 9353580260

Thankyou!

