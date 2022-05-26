Welcome to my first test project with implemented Page Object Model.

# Python | Selenium | Page Object 

In theory, by applying this design pattern we can gain:
- Reduction of duplicate code
- Easier use of the same code in multiple tests
- Increased test readability
- Easier code maintenance


In `BasePage` you can find all basic operations done on a website. It inherits it's methods for all other Page classes.


To run this program:
1. Run `pytest test_RegistrationPage.py` for account creation on a [seleniumdemo.com](http://seleniumdemo.com/) website. Created account is valid for 24 hours. By that time it's deleted.
2. Run `pytest test_LoginPage.py` for login test 



Thanks for checking it out!
