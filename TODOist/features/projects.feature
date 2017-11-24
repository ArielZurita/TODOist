Feature: Projects

@get_project
Scenario: GET by id
    Given I use "projects" endpoint
      And I perform "GET" method
      And I sent the proper id: "project_id"
    When I send the request
    Then I get status code "200"


@update_project
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
Scenario: DELETE by id
    Given I use "projects" endpoint
      And I perform "DELETE" method
      And I sent the proper id: "project_id"
    When I send the request
    Then I get status code "204"

