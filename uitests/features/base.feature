@ui_smoke
Feature: Base functionality

  Scenario: Check if GOOGLE is running
    When I visit GOOGLE
    Then page should have a title "Facebook – log in or sign up"
#  loginbutton
  Scenario: Login to GOOGLE
    When I visit GOOGLE
    And I enter "omerta" for id field "u_0_m"
    And I enter "femina" for id field "u_0_o"
    And I enter "9844198441" for id field "u_0_r"
    And I enter "pass1@1" for id field "u_0_w"
    And I enter "10" text for select "day"
    And I enter "Apr" text for select "month"
    And I enter "1986" text for select "year"
    And I click id named "u_0_6"
    And I click id named "u_0_13"
    Then page should have a title "Facebook"
#    And I click button "u_0_13"
#    And I click "Forgotten password?"
#    And I enter "1234" for field "recovery_code_entry"
#    And I click button named "reset_action"
#    And I click "reset_action"
  Scenario: Login to GOOGLE
    When I visit GOOGLE
    And I login into GOOGLE
    Then page should have a title "Facebook"


#  Scenario: Enter expert mode
#    Given I am logged into GOOGLE
#    When I enter expert mode by id "launch_expert_mode"
#    Then page should have a title "NSO"
