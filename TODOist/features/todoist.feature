Feature: Get Project

  Scenario: Get all projects
    Given I ask for the list of projects from host
    When I enter the token
    Then  I get the list of projects

