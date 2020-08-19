# Profile Compatibility
-----------------------

### DESCRIPTION
- The focus of this project is to show the current user, the top 5 people he/she is compatible with.
- The percentage of compatibility is calculated using the answers given by the users to the questions available.
- This is Backend Ready and has only limited frontend to allow the users to use the functionalities.


### Getting Started
- To just view the final outcome, you can use test credentials:
    ``` Username: testuser1 ```
    ``` Password: test123456 ```
    Using these credentials you can view how the compatibilities are shown and can also edit the profile.

- To start over and test all features, start by signing up.
- After sign up, you will be prompted to login and upon successful login, you will have to complete your profile by filling all the deatils.
- You then have to answer three randomly generated questions. Answer them carefully because this is what decides your compatibility with your fellow users.
- You can edit your profile only after completing the above step.
- Once all the steps are completed, you now have the 5 users you are the most compatible with!!


### Logic Used for Compatibility

The logic used as of now is that, say you have **x** questions in common with a user **U** and the both of you have same answers for **y** questions, Then, your compatibility with user **U** would be **y/x** percent. Other answers are not being taken into consideration due to obvious reasons of those not being answered by you.


### Technology

This project is currently written using Django 3.1 and Python 3.8.5. Very limited HTML5 and CSS3 have been used yet.

# IN DEVELOPMENT AS OF 19 AUG' 20
