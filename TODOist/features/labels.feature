Feature: Labels won't be available for standard, non-premium accounts like the one we have
  If labels service will be called by an standard's account token then status code 403 (Forbidden) should be returned
@smoke @labels
Scenario: CREATE a label
  Given I use "labels" endpoint
  And I perform "UPDATE" method
  And I will send the following data:
    """
    {"name": "My Label"}
    """
  When I send the request
  Then I get status code "403"

@smoke @labels
Scenario:  GET all labels
  Given I use "labels" endpoint
  And I perform "GET" method
  When I send the request
  Then I get status code "403"

@smoke @labels @get_label
Scenario: GET a label
  Given I use "labels" endpoint
  And I perform "GET" method
  And I sent the proper id: "label_id"
  When I send the request
  Then I get status code "403"

@smoke @labels
Scenario: UPDATE a label
  Given I use "labels" endpoint
    And I perform "UPDATE" method
    And I will send the following data:
      """
      {"name": "New Name Label"}
      """
    When I send the request
    Then I get status code "403"

@smoke @labels @delete_label
Scenario: DELETE a label
  Given I use "labels" endpoint
  And I perform "DELETE" method
  And I sent the proper id: "label_id"
  When I send the request
  Then I get status code "403"