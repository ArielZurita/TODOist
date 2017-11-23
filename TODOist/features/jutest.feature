Feature: Reopen tests
@close_tasks
Scenario: REOPEN a closed task
    Given I use "tasks" endpoint
      And I perform "REOPEN" method
      And I sent the proper id: "task_id"
    When I send the request
    Then I get status code "204"