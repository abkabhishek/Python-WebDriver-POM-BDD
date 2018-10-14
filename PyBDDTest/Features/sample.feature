
@homepage
Feature: Verify functional and UI verification of Homepage of Startpage.com

  @regression
  Scenario: Verify the page title on the Home page.

    Given User loads https://quest1:quest123@crucible.startpage.com/en/ in browser
    When User checks title of the page in browser
    Then page title is "Startpage.com - The world's most private search engine"


  @regression
  Scenario: Verify the default selected category on loading Home page.

    Given User loads https://quest1:quest123@crucible.startpage.com/en/ in browser
    When User checks current selected result category at top left of the Home page
    Then Web category appears selected and underlined by default

  @regression
  Scenario Outline: Verify the changing of result category from Home page.

    Given User loads https://quest1:quest123@crucible.startpage.com/en/ in browser
    And Default selected category is "Web"
    When User clicks on "<cat>" category
    Then "<cat>" category gets selected
    And "<cat>" category gets underlined


    Examples: Test data
      | cat     |
      | Images   |
      | Videos   |
      | Web     |

  @regression
  Scenario: Verify the first focus of the page on loading the Home page.

    Given User loads https://quest1:quest123@crucible.startpage.com/en/ in browser
    When User observes current focused element on the Home page
    Then first focus is on Search box on the Home page
    And  cursor starts blinking in the search box

  
  @regression
  Scenario Outline: Verify the functionality of performing Web Search

    Given User loads https://quest1:quest123@crucible.startpage.com/en/ in browser
    When User input '<searchterm>' in the search box
    And User clicks Search button
    Then User navigates to Web result page containing web results of searched term

    Examples:  Test Data
      | searchterm  |
      | paris       |
      | car         |
      | pizza       |
  
  @regression
  Scenario Outline: Verify the functionality of performing Image Search

    Given User loads https://quest1:quest123@crucible.startpage.com/en/ in browser
    When User clicks on "Images" category
    And User input '<searchterm>' in the search box
    And User clicks Search button
    Then User navigates to Image result page containing Image results of searched term

    Examples:  Test Data
      | searchterm  |
      | paris       |
      | car         |
      | pizza       |
  
  @regression
  Scenario Outline: Verify the functionality of performing Video Search

    Given User loads https://quest1:quest123@crucible.startpage.com/en/ in browser
    When User clicks on "Videos" category
    And User input '<searchterm>' in the search box
    And User clicks Search button
    Then User navigates to Video result page containing Video results of searched term

    Examples:  Test Data
      | searchterm  |
      | paris       |
      | car         |
      | pizza       |
  
  @regression
  Scenario Outline: Verify the functionality of performing search by using search button.

    Given User loads https://quest1:quest123@crucible.startpage.com/en/ in browser
    When User input '<searchterm>' in the search box
    And User clicks Search button
    Then User navigates to Web result page containing Web results of searched term

    Examples:  Test Data
      | searchterm  |
      | paris       |
      | car         |
      | pizza       |

  @regression
  Scenario Outline: Verify the functionality of performing search by using enter key.

    Given User loads https://quest1:quest123@crucible.startpage.com/en/ in browser
    When User input '<searchterm>' in the search box
    And User presses 'Enter' key
    Then User navigates to Web result page containing Web results of searched term

    Examples:  Test Data
      | searchterm  |
      | paris       |
      | car         |
      | pizza       |

  @regression @navigation
  Scenario: Verify the navigation to Settings page

    Given User loads https://quest1:quest123@crucible.startpage.com/en/ in browser
    When User clicks on 'Settings' link on the Top right corner
    Then User navigates to Settings page

  @regression @navigation
  Scenario: Verify the navigation to Support site

    Given User loads https://quest1:quest123@crucible.startpage.com/en/ in browser
    When User clicks on 'Support' link on the Top right corner
    Then User navigates to Support site
  
  @regression @navigation
  Scenario: Verify the navigation to Startmail site

    Given User loads https://quest1:quest123@crucible.startpage.com/en/ in browser
    When User clicks on 'Mail' link on the Top right corner
    Then User navigates to our Mail page
  
  @regression @smallscreen
  Scenario Outline: Verify the availability of Hamburger menu in small screen containing Top right navigation links.

    Given User loads https://quest1:quest123@crucible.startpage.com/en/ in browser
    When User changes its browser resolution to '<resolution>'
    Then Visibility of the Hamburger menu is '<visibility>'

    Examples:  Test Data
      | resolution  | visibility  |
      | 1400x800    | False       |
      | 1280x800    | True        |
      | 1024x800    | True        |
      | 800x600     | True        |
      | 400x600     | True        |


	@regression @smallscreen
	Scenario: Verify that the user is able to open Hamburger menu in small screen.

		Given User loads https://quest1:quest123@crucible.startpage.com/en/ in browser
		And User changes its browser resolution to '800x700'
		When User click on the hamburger menu
		Then Hamburger menu will appear on right side


	@regression @navigation @smallscreen
	Scenario Outline: Verify that the User can access links inside Hamburger menu

		Given User loads https://quest1:quest123@crucible.startpage.com/en/ in browser
		And User changes its browser resolution to '800x700'
		And User click on the hamburger menu
		When User click on the <link> from hamburger menu
		Then landed page title is <pageTitle>

		Examples: Test Data
			|	link	|	pageTitle	|
			|	Settings|	undefined	|
			|	Support	|	StartPage Support Center - StartPage Support Center	|
			|	Mail 	| 	StartMail - Private & encrypted email made easy	|



#  @regression @navigation @deferred
#  Scenario: Verify the navigation of User on clicking links available in Extended section
#
#    Given User is on Home page and focus is on extended page section
#    When User click on the '<link>' link text available in the extended page section
#    Then landed page title is '<pageTitle>'
#    | link    | pageTitle 	|
#    | Ab      | undefined	|
#    | Ac      | undefined	|


  @regression @UI @planned
  Scenario Outline: Verify Footer items are appearing correctly

    Given User loads https://quest1:quest123@crucible.startpage.com/en/ in browser
    When User look for <link> in the page footer section
    Then User see their <visibility> correctly

    Examples: Test Data
    | link    		  | visibility 	|
    | Blog    		  | true  	    |
    | Privacy    	  | true  	    |
    | About us   	  | true  	    |
    | Press    		  | true  	    |

  @regression @navigation
  Scenario Outline: Verify navigation on clicking the Footer links

    Given User loads https://quest1:quest123@crucible.startpage.com/en/ in browser
    When User click on the '<link>' from footer bar on Home page
    Then landed page title is '<pageTitle>'

    Examples: Test Data
    | link    		| pageTitle 	|
    | Blog    		| StartPage Blog - StartPage.com Blog  	|
    | Privacy    	| undefined  	                        |
    | About us   	| undefined  	|
    | Press    		| StartPage.com Press - StartPage.com Blog  |



#****************** =============================================================== ************************
#****************** =============================================================== ************************
#    For additional modules in Home page, please prepare second feature file of Home page
#****************** =============================================================== ************************
#****************** =============================================================== ************************