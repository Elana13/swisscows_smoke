# Created by Iveonik08 at 12.05.2021
Feature: Web page scenarios


#  Scenario: "Did you mean" appears
#    Given User is on Web page with "appple" query
#    Then Did you mean appears

  Scenario: Suggest is present
    Given User is on Web page with "any" query
    When User type text into search field
    Then Suggest appears
#
#  Scenario: Search with Suggest
#    Given User is on Homepage
#    When User type text into search field
#    And User select item from Suggest
#    Then User is on Web page
#
#  Scenario: Use paging on web
#    Given User is on Web page with "apple" query
#    When User press second page
#    Then Next 10 results are displayed
