*** Settings ***
Library           ../common/zuowenkeyword.py

*** Keywords ***
nihao
    [Arguments]    ${ip_name}    ${key_1}    ${id_1}
    ${return}    zuowen    ${ip_name}    ${key_1}    ${id_1}
    [Return]    ${return}

chengfa
    [Arguments]    ${number_1}    ${number_2}
    ${result}    evaluate    ${number_1}*${number_2}

sey_hello
    [Arguments]    ${bcd}
    log    ${bcd}

hello_1
    [Arguments]    ${parem}
    ${par}    log many    ${parem}[2]
    log    ${par}

Inloop
    [Arguments]    ${times}
    LOG    来自内循环${times}
    FOR    ${j}    IN RANGE    0    ${times}
    log    ${j}
    END
