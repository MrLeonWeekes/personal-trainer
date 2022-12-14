PERSONAL TRAINER APP

This is a simple Personal Trainer app using the Python web framework Flask. The app contains links in the navbar that allows you add personal trainers and clients to the app which will store the information in your mySql database. You can view various lists of data and clients can be updated and deleted.

![Home Page](https://user-images.githubusercontent.com/48031756/183020266-0e92a4e3-aac8-496c-a411-fe3d0ec83054.png)

GET STARTED

The app uses many great dependencies to be able to run and I have listed them all in the requirements.txt file on the application. 

flask
flask_sqlalchemy
pymysql
flask_wtf
wtforms
pytest
pytest-cov
flask_testing

Please see installation instructions below:

- In a virtual environment, run pip3 install -r requirements.txt to install the necessary dependencies.
- Run python3 create.py to create the database
- Run python3 app.py to launch the application

USE THE PROJECT

You can use this app to add personal trainers and clients to a database

![Add Trainer](https://user-images.githubusercontent.com/48031756/183021006-a74ea22c-15c0-48de-885a-fd182edbc7ef.png)

![MySQL Database](https://user-images.githubusercontent.com/48031756/183020799-ffede03a-f0b2-4e24-b2a7-0eb7450bfd83.png)

![personal-trainer-erd drawio](https://user-images.githubusercontent.com/48031756/183021137-face2022-e572-45eb-be22-5d1ff286b037.png)

TESTING

The app has been 88% unit tested using PyTest & TestCase. This will ensure the app run

![Test Coverage](https://user-images.githubusercontent.com/48031756/183021493-2c6db148-457b-422f-a7ef-0d79df8f8684.png)

CONTRIBUTING

This project is open source. Pull requests are welcome. 
