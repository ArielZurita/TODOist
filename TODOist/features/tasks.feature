Feature: In this feature covers the principals API task actions,GET tasks, GET tasks by ID, Create a new task, UPDATE a created task,

@smoke
Scenario: GET all tasks returns status code 200 when entering a valid token
    Given I use "tasks" endpoint
      And I perform "GET" method
    When I send the request
    Then I get status code "200"

@insert_tasks
@delete_tasks
Scenario: GET task by id and returns status code 200 when entering a valid token and a valid id task
    Given I use "tasks" endpoint
      And I perform "GET" method
      And I sent the proper id: "task_id"
    When I send the request
    Then I get status code "200"

@insert_tasks
@delete_tasks
  @functional
Scenario: GET task by id and compare data
    Given I use "tasks" endpoint
      And I perform "GET" method
      And I sent the proper id: "task_id"
    When I send the request
    Then I get status code "200"
      And I compare data

  @functional
Scenario: POST to create a new task
    Given I use "tasks" endpoint
      And I perform "POST" method
      And I will send the following data:
      """
      {"content": "Test123",
       "due_string": "tomorrow at 12:00",
       "due_lang": "en",
       "priority": 4}
      """
    When I send the request
    Then I get status code "200"



@insert_tasks
@delete_tasks
Scenario: UPDATE a created task
    Given I use "tasks" endpoint
      And I perform "UPDATE" method
      And I sent the proper id: "task_id"
      And I will send the following data:
      """
      {"content": "Test12334",
       "due_string": "tomorrow at 12:00",
       "due_lang": "en",
       "priority": 4}
      """
    When I send the request
    Then I get status code "204"

@smoke
@insert_tasks
Scenario: CLOSE an specific task in show archived task
    Given I use "tasks" endpoint
      And I perform "CLOSE" method
      And I sent the proper id: "task_id"
    When I send the request
    Then I get status code "204"

@close_tasks
Scenario: REOPEN a closed task
    Given I use "tasks" endpoint
      And I perform "REOPEN" method
      And I sent the proper id: "task_id"
    When I send the request
    Then I get status code "204"
