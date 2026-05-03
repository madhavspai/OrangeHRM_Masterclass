@smoke
Feature: Login Functionality

  @smoke
  @allure.label.owner:Madhav
  @allure.severity.critical
  Scenario: Successful login with valid credentials
    Given I navigate to the OrangeHRM login page
    When I enter valid credentials
    And I click the login button
    Then I should be logged in successfully