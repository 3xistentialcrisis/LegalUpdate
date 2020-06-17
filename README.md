# Legal_Update App

## Developers.
 legal_update law firm

## Description.
The legal_update was created whereby clients can view their files cases which have been posted by the lawyers.For this to be done the client needs to be have an account and also the lawyer.The lawyer will uploading the files and the client will be getting the update immediately.Clients have the chance to make comments about the files which are being worked everytime.The cases are in only three categories:
    1.Criminal Cases
    2.Civil Cases
    3.Family Cases
The Client chooses which case he/she wants judgement to be done.


## BDD(Behaviour Driven Development)

| Behavior            | Input                         | Output                        | 
| ------------------- | ----------------------------- | ----------------------------- |
|Sign up either the client side or lawyer|Filling in the form | Redirects you to the login page|
| Sign in | Filling in the form at the signing page | Redirects you to the home page |
| Posting a casepitch | In the home page, enter your case in text, select a category in the drop down menu and submit! | Reloads the page with the case picked as the new case  |
| Leaving feedback your feedback | Type the feedback on the text area field in the case page, and submit | Reloads the page and posts the feedback. The comments will be shown from the most recent |
| Editing the bio | Click on the ```edit bio``` button and enter your bio  | Redirects the page back to the profile page with an updated bio |


## Creating a Virtual Environment
Run the following commands in the same terminal:
  $ sudo apt-get install python3.6-ven`
  $ python3.6 -m venv virtual
  $ source virtual/bin/activate

## Run Database Migrations:

   $ python manage.py db init
   $ python manage.py db migrate -m "initial migration"
   $ python manage.py db upgrade
   
## Running the app in development
In the same terminal type:
   $ python3 manage.py server

## Technologies used
    - Python 3.6
    - HTML
    - Bootstrap 4
    - Animate CSS
    - Heroku
    - Postgresql


## Support and contact details:
        ~Incase of any issues or clarification email us at:3xistentialcrisislawfirm5@gmail.com
        ~Call us : 0110443278

## License
  Powered by eRegulations ©, a content management system developed byUNCTAD's Business Facilitation Programand licensed underCreative Commons License.
                  # legal_update law firmcopyright(c)2020
