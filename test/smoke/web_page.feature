# Created by Iveonik08 at 12.05.2021
Feature: Web page scenarios


#  Scenario: "Did you mean" appears
#    Given User is on Web page with "appple" query
#    Then Did you mean appears
#
#  Scenario: Suggest is present
#    Given User is on Web page with "fl" query
#    When User type text "ow" into search field
#    Then Suggest appears

#  Scenario: Search with Suggest
#    Given User is on Web page with "fl" query
#    When User type text "ow" into search field
#    And User select item from Suggest
#    Then Search field contains text
#    Then User is on Web page

  Scenario: Use paging on web
    Given User is on Web page with "apple" query
    When User press second page
    Then Next 10 results are displayed
