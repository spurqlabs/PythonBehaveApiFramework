# Created by hp at 31-01-2023
Feature: API Automation

  @api
  Scenario: Verify GET call for single user
    When User sends "GET" call to endpoint "api/users/2"
    Then User verifies the status code is "200"
    And User verifies GET response contains following information
      | First_name | Last_name | Mail-id                |
      | Janet      | Weaver    | janet.weaver@reqres.in |

  @api
  Scenario: Verify POST call for single user
    When User sends "POST" call to endpoint "api/users"
      | Name   | Job  |
      | Yogesh | SDET |
    Then User verifies the status code is "201"
    And User verifies POST response body contains following information
      | Name   | Job  |
      | Yogesh | SDET |

  @api
  Scenario: Verify PUT call for single user
    When User sends "PUT" call to endpoint "api/users/2"
      | Name   | Job  |
      | Yogesh | SDET |
    Then User verifies the status code is "200"
    And User verifies PUT response body contains following information
      | Name   | Job  |
      | Yogesh | SDET |

  @api
  Scenario: Verify DELETE call for single user
    When User sends DELETE call to the endpoint "api/users/2"
    Then User verifies the status code is "200"

