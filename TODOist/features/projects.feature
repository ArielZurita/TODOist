Feature: Projects

@get_project
Scenario: GET project returns status code 200 when entering a valid token and a valid project identifier
    Given I use "projects" endpoint
      And I perform "GET" method
      And I sent the proper id: "5"
    When I send the request
    Then I get status code "200"

@update_project
Scenario: POST by id
    Given I use "projects" endpoint
      And I perform "POST" method
      And I sent the proper id: "5"
      And I will send the following data: "{"Movies to watch"}"
    When I send the request
    Then I get status code "204"

@delete_project
Scenario: DELETE by id
    Given I use "projects" endpoint
      And I perform "DELETE" method
      And I sent the proper id: "5"
    When I send the request
    Then I get status code "204"
