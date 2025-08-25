Feature: Login functionality

  Scenario: Valid user login
    Given I open the browser
    When I navigate to "https://example.com/login"
    And I fill "username" with "testuser"
    And I fill "password" with "secret123"
    And I click "Login"
    Then I should see "Welcome, testuser"