# User Login API with Email and OTP Authentication Using Django

## Features

- **User Registration**: Register users with email addresses.
- **OTP Generation and Sending**: Generate and send OTPs to user email addresses.
- **OTP Verification**: Verify OTPs and authenticate users.
- **Session Management**: Manage user sessions using JWT.
- **Security Measures**: Rate limiting for OTP requests and secure OTP algorithms.

## API Endpoints

1. **User Registration**:
   - **Method**: `POST`
   - **Endpoint**: `/api/register`


2. **Request OTP**:
   - **Method**: `POST`
   - **Endpoint**: `/api/request-otp`
 

3. **Verify OTP**:
   - **Method**: `POST`
   - **Endpoint**: `/api/verify-otp`
  

## Installation and Setup


### Prerequisites

- Docker
- Docker Compose

   
### Setup Your Environment

```bash
SECRET_KEY=your_secret_key
DEBUG=True
EMAIL_HOST_USER=your_gmail_id
EMAIL_HOST_PASSWORD=add_your_email_password


## Build and Run Containers

To build and run your Docker containers, execute:

```bash
docker-compose up --build
docker-compose run web python manage.py migrate


  




