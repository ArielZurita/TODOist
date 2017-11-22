Feature: Create tasks
#    ## Can be uncomment
#Scenario: POST to crate a new task
#    Given I use "tasks" endpoint
#      And I perform "POST" method
#      And I will send the following data:
#      """
#      {"content": "Testnew1",
#       "due_string": "tomorrow at 12:00",
#       "due_lang": "en",
#       "priority": 4}
#      """
#    When I send the request
#    Then I get status code "200"


    ### Can be see close task in show archived tasks
@insert_tasks

Scenario: CLOSE
    Given I use "tasks" endpoint
      And I perform "CLOSE" method
      And I sent the proper id: "task_id"
    When I send the request
    Then I get status code "204"


    ### Can be uncomment
@insert_tasks

Scenario: UPDATE
    Given I use "tasks" endpoint
      And I perform "UPDATE" method
      And I sent the proper id: "task_id"
      And I will send the following data:
      """
      {"content": "ABCDEFGHIJK",
       "due_string": "tomorrow at 12:00",
       "due_lang": "en",
       "priority": 4}
      """
    When I send the request
    Then I get status code "204"