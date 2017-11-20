Feature: GET tasks
  #https://beta.todoist.com/API/v8/tasks?token=$token
  Scenario: GET tasks retruns status code 200 when entering a valid token and a valid project identifier
    Given I connect to the 'tasks' service
    When I enter a valid 'token'
    And I enter a valid 'project' identifier
    Then I get status code '200'

