Feature: Create Project and Get project
@get_all_projects
Scenario: GET all
    Given I use "projects" endpoint
      And I perform "GET" method
    When I send the request
    Then I get status code "200"
     And I get all projects

@create_project
Scenario: Create project
  Given I use "projects" endpoint
      And I perform "POST" method
      And I will send the following data:
      """
      {"name": "test12345679"}
      """
    When I send the request
    Then I get status code "200"
     And I get response with name entered
