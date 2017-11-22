Feature: GET tasks
  #https://beta.todoist.com/API/v8/tasks?token=$token

  ### Can be uncomment
#Scenario: GET tasks returns status code 200 when entering a valid token and a valid project identifier
#    Given I use "tasks" endpoint
#      And I perform "GET" method
#    When I send the request
#    Then I get status code "200"

@insert_tasks
  @delete_tasks
Scenario: GET by id
    Given I use "tasks" endpoint
      And I perform "GET" method
      And I sent the proper id: "task_id"
    When I send the request
    Then I get status code "200"

  ### Can be uncomment
#Scenario: POST to crate a new task
#    Given I use "tasks" endpoint
#      And I perform "POST" method
#      And I will send the following data:
#      """
#      {"content": "Test123",
#       "due_string": "tomorrow at 12:00",
#       "due_lang": "en",
#       "priority": 4}
#      """
#    When I send the request
#    Then I get status code "200"
#

  ### Can be uncomment
@insert_tasks
  @delete_tasks
Scenario: UPDATE
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


  ##Not implemented yet to compare data. Don't uncomment

##  Scenario: GET tasks returns status code 200 when entering a valid token and a valid project identifier
##    #Given I have access to API
##    When I perform "GET" request to "tasks" endpoint
##      And to get the " 2407873746" task
##    Then I get status code "200"
###      And the "data" returned should be the same than
###    """
###    {
###
###    "project_id": 2166590740,
###    "content": "Appointment with Maria",
###    "completed": false,
###    "order": 1,
###    "indent": 1,
###    "priority": 4,
###    "comment_count": 0,
###    "due": {
###        "recurring": false,
###        "string": "tomorrow at 12:00",
###        "date": "2017-11-21",
###        "timezone": "UTC-04:00"
###      }
###     }
###    """
#


  ### Can be uncomment
#Scenario: GET projects
#    Given I use "projects" endpoint
#      And I perform "GET" method
#    When I send the request
#    Then I get status code "200"


