*** Settings ***
Library           Selenium2Library
Library           ../common/add_1.py

*** Variables ***
@{lise_1}         1    2    3    4
${scalar_1}       12
${number_1}       ${1000}

*** Test Cases ***
234
    ${re}    add    10    15
    log    ${re}

chengfa
    chenfa    22    3

var_log
    log    @{list_1}

*** Keywords ***
chenfa
    [Arguments]    ${number_1}    ${number_2}
    ${sesult}    evaluate    ${number_1}*${number_2}
    log    ${sesult}
