# Legal Update™️
## Author

[Team 3 Law Firm ](https://github.com/3xistentialcrisis/LegalUpdate)

# Description
This  is a flask application that enables lawyers to create digital copies of their client files and post status updates on these files.  

## Live Link
[View Site](https://legalupdate.herokuapp.com)

## Screenshots

<img src="https://raw.githubusercontent.com/3xistentialcrisis/LegalUpdate/master/app/static/photos/homepage.png" width="900px" height="440px">
<img src="https://raw.githubusercontent.com/3xistentialcrisis/LegalUpdate/master/app/static/photos/homepage2.png" width="900px" height="440px">
<img src="https://raw.githubusercontent.com/3xistentialcrisis/LegalUpdate/master/app/static/photos/signin.png" width="900px" height="440px">
<img src="https://raw.githubusercontent.com/3xistentialcrisis/LegalUpdate/master/app/static/photos/postcase.png" width="900px" height="440px">
<img src="https://raw.githubusercontent.com/3xistentialcrisis/LegalUpdate/master/app/static/photos/poststatus.png" width="900px" height="440px">


## User Story
A user can:
* Sign in or sign up to the application
* Create a Client File
* Post a File Status Update
* View all Created Files
* View all Created Status Updates


## BDD
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Load the page | **On page load** | Scroll down to Lawyers Portal Sign In 
| Select Sign in| **Email**,**Username**,**Password** | Redirect to login|
| Select Login | **Username** and **password** | Redirect homepage|
| Select Create Client File on Navbar | **Client File** | Form that you input your File |
| Select Update File Status on Navbar | **File Status** | Form that you input your File Status|
| View File  | **File** | View All Files Status on File Page
| View File Status  | **File Status** | View All File Status on File Status Page


## Development Installation
To get the code..

1. Cloning the repository:
  ```bash
  https://github.com/3xistentialcrisis/LegalUpdate.git
  ```
2. Move to the folder and install requirements
  ```bash
  cd legalupdate
  pip install -r requirements.txt
  ```
3. Exporting Configurations
  ```bash
  export SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://{User Name}:{password}@localhost/{database name}
  ```
4. Running the application
  ```bash
  python manage.py server
  ```

Open the application on your browser `127.0.0.1:5000`.


## Technology used

* [Python3.8](https://www.python.org/)
* [Flask](http://flask.pocoo.org/)
* [Heroku](https://heroku.com)


## Known Bugs
* There are no known bugs currently but pull requests are allowed incase you spot a bug

## Contact Information 

If you have any question or contributions, please email me at [team3lawfirm@gmail.com]

# License
[![license](https://img.shields.io/github/license/DAVFoundation/captain-n3m0.svg?style=flat-square)](https://github.com/3xistentialcrisis/legalupdate/blob/master/LICENSE)