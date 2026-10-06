*** Settings ***

Library  SeleniumLibrary
Library  BuiltIn
Library  Collections
Library  String




*** Variables ***
${var1}    hello world

@{fruits}    apple  banana  mango  orange   pear   grape
&{person}    name=shashwat  age=25  city=indore
${name}    shashwat



*** Keywords ***

*** Test Cases ***

LoginTest
    Log  "hi"
    Log  "abc"
    Open Browser  https://leetcode.com/accounts/signup/  chrome
    Maximize Browser Window
    sleep  4s
    Input Text  xpath://input[starts-with(@class,input)]  shashwat
    # sleep  4s
    # Close Browser
    #//input[contains(@name,'User')]

Datatypes
    Log  ${var1}
    Log Many  @{fruits}
    Log  ${person['name']}
    Log  ${name}
    Log  ${person['age']}
    Log  ${person['city']}

    FOR    ${user}    IN    Alice    Bob    John
        Log    ${user}
    END
    
    @{users}    Alice    Bob    John

    FOR    ${user}    IN    @{users}
        Log    ${user}
    END

    FOR    ${i}    IN RANGE    1    5
        Log    ${i}
    END