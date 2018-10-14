Feature: Validation of Basic Home page features

  Scenario: Verify the performing web search functionality
     Given User loads www.google.com in browser
      When User input search term in search box and submit it
      Then User navigates to Web result page of searched term
       And page title contains search term