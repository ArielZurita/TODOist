Feature: Create Project and Get project
@get_all_projects
Scenario: GET all
    Given I use "projects" endpoint
      And I perform "GET" method
    When I send the request
    Then I get status code "200"
     And I get all projects
Scenario: Create project
  Given I use "projects" endpoint
      And I perform "POST" method
    When I send the request
    Then I get status code "200"
