*** Settings ***

Library  SeleniumLibrary
Library  BuiltIn

*** Variables ***


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

