# Agile Web Development - CITS 5505 Project-2

![image info](./app/static/Image/swift_icoon.png)
## Students:
- Liangbo Jin  23078811
- Kebing Zhao  22863702

## 1.Purpose of the Web Application
- The purpose of this <b>Web Application</b> is to provide fundentmental concept and small test of the <b>Swift</b> programming 
language, and offer feedback for each test. 
- This Web Application comes with <b>educational style</b>, and provides basic Swift concepts for learning, including: Syntax, Grammar, Function, and more.   

### Context & Assessment mechanism
1. Context mechanism
   - The first page that all visiters can see is the home page, they can choose which articles they want to learn
   - For the context, we created several tutorial pages for users ( logined / annonymous) to visit and learn. However, only the logined user can visit the 'Test' page and attempt the test. 
   - The logined user can visit his profile once he finished at least one test. In the profile page, he can see his history attempts ( Finish time, Mark, and personalized feedback), as well as other user's results. What's more, he can also see his average mark.

2. Login mechanism
   - The user can login at any time, and can register an account at any time in the login page. 
   - The 'Test' , 'Profile' & 'Admin' page requires login to visit, and only the admin account can visit the 'Admin' page
3. Admin account mechanism
   - The admin account is used for adding and deleting user's data, including their account and test's result. Only the admin user can visit the admin page, and perform editing. Other's will be redirected to the main page.

4. Assessment mechanism
   - We provide 10 questions that related to the tutorial materials. For each question, if user gives the right answer, the temperory <b>int CurrentResult</b> will add 10 mark. Otherwise, if user gives the wrong answer, the temperory <b>string feedback</b> will add the feedback for the current question.
   - The user's choice will be stored during the whole session, for example, if they refreash the page or leave the current Test page, their answer is preserved. 
   - Once they submit their assessment or logout, their answer will be removed
   - User must enter a verification code to make the submittion. If the verification code is not correct, they cannot make submission
   - User can view their history attempts in the 'Profile' page, last visit time, as well as his average mark. What's more, this page also contains the aggregate results from all user's attempts. Also, the user can edit their personalized message in the 'Profile' page.

<hr>

## 2.Architecture of the Web Application
The whole Architecture of this Web Application is represented below
<pre>
AgileWeb Project 2
|--  README.md
|--  app.db
|--  log.txt
|--  config.py
|--  start.py
|--  testBot.py
|--  requirements.txt
|--  app
    |--  static
        |--  Image
            |--  images...
        |--  Javascript_file.js
        |--  nav_css.css
    |--  templates
        |--  404.html
        |--  500.html
        |--  base.html
        |--  class.html
        |--  condition.html
        |--  edit_profile.html
        |--  function.html
        |--  generic.html
        |--  grammar.html
        |--  home.html
        |--  login.html
        |--  inher.html
        |--  login.html
        |--  loginbase.html
        |--  math.html
        |--  register.html
        |--  Set_Up.html
        |--  Testbase.html
        |--  user.html
    |--  __init__.py
    |--  errors.py
    |--  forms.py
    |--  models.py
    |--  routes.py
</pre>

<hr>

## 3.How to Launch the Application
1. Open the terminal under the file directorym, and run the following commands in terminal
2. Using the <b>pip</b> to install all the packages in the '<b>requirements.txt</b>
<pre>pip install -r requirements.txt</pre>
3. Run the Application
<pre> flask run </pre>
You will see the followings
<pre> 
 * Serving Flask app "start.py"
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)</pre>

If the Web Application cannot run, check the environmental variable <pre>FLASK_APP=start.py</pre>
And store it as environmental variable

<hr>

## 4.About Test
About the test, we use the selenium package to set up a webbot, which includes two tests (registration test and tutorial coverage test), so that we can test most of contents on our webpage and app without human effort. Additionally, we also made a unit test for the login function.

For the running process of the test:
1. Open the terminal, Run the command and keep the local server on.
<pre>flask run</pre>
2. Open another terminal, Run the python file and wait for the test finish.
<pre>python testBot.py / python3 testBot.py</pre>
3. Once you see the test's status: Test # finished, the tests are finished. ( As show below)
<pre>
Process finished with exit code 0
PASSED                                        [33%]Register Here ! 
Test1 finished!

PASSED                                        [66%]Congratulation!!! 
Test2 finished!

PASSED
Test3 finished                                [100%]User password test is done!

Ran 3 tests in 36.566s

OK

Process finished with exit code 0
</pre>

<hr>

## 5. About the Database
The Web Application comes with a existing database named '<b>app.db</b>, it contains several user accounts and one <b>admin</b> account

However, if you want to <b>delete</b> the existing database, and create it on your own, please apply the following commands:
1. delete the file '<b>app.db</b>'
2. <pre>flask db init</pre>
3. <pre>flask db migrate -m "users table"</pre>
4. <pre>flask db upgrade</pre>
5. <pre>flask db migrate -m "posts table"</pre>
6. <pre>flask db upgrade</pre>
<b style="color:red">Important</b>, once you create a new database, to access the admin features, you need to create an account named '<b style="color:red">admin</b>'. The Web application only recoginze the Admin account with name '<b style="color:red">admin</b>'.
<hr>

## 6.Commit log
The log file is named as  '<b> log.txt</b>', and all commit logs are stored inside the file.

### Contributions
We divided our work equally, and the evidences can be found in the log.txt
