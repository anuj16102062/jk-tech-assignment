Overview

This document provides simple instructions to set up and run the RAG-based Q&A application using Flask and Grok.

Prerequisites

Python 3.8 or later installed on your system.

Postgres database setup and running.

Install required dependencies using pip.

Steps to Run the Application

1. Clone the Repository

$ git clone <repository-url>
$ cd <repository-directory>

2. Set Up Virtual Environment (Optional but Recommended)

$ python3 -m venv venv
$ source venv/bin/activate   # On Windows: venv\Scripts\activate

3. Install Dependencies

$ pip install -r requirements.txt

4. Configure Environment Variables

Create a .env file in the project root directory with the following variables:

FLASK_APP=app.py
DATABASE_URL=postgresql://<username>:<password>@<host>:<port>/<database_name>

Replace <username>, <password>, <host>, <port>, and <database_name> with your Postgres configuration.

5. Run the Application

$ flask run

The application will be available at http://127.0.0.1:5000.

after that run postman collections 
