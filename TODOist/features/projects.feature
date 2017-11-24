Feature: Create Project, Update, Get and delete project
@get_all_projects
  @functional
Scenario: GET all
    Given I use "projects" endpoint
      And I perform "GET" method
    When I send the request
    Then I get status code "200"
     And I get all projects

@create_project
  @functional
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


@get_project
  @smoke
Scenario: GET by id
    Given I use "projects" endpoint
      And I perform "GET" method
      And I sent the proper id: "project_id"
    When I send the request
    Then I get status code "200"


@update_project
  @smoke
Scenario: UPDATE by id
    Given I use "projects" endpoint
      And I perform "UPDATE" method
      And I sent the proper id: "project_id"
      And I will send the following data:
      """
      {"name":"New movies to watch again"}
      """
    When I send the request
    Then I get status code "204"


@delete_project
  @smoke
Scenario: DELETE by id
    Given I use "projects" endpoint
      And I perform "DELETE" method
      And I sent the proper id: "project_id"
    When I send the request
    Then I get status code "204"

