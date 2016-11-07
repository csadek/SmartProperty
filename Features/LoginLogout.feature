Feature: Login and Logout
  Scenario: Login with valid credentials
    Given The user is at the Home Page
    When The user Logs In with Valid Credentials
    |UserName               |Password   |
    |csadek@integrant.com|ZAQ!cde3|
    Then The user is logged in successfully
