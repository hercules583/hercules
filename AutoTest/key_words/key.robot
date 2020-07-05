*** Settings ***
Library           Selenium2Library
Library           ../common/zuowenkeyword.py

*** Keywords ***
作文
    [Arguments]    ${zuowen_ip}    ${key}    ${id}
    ${return}    zuowen    ${zuowen_ip}    ${key}    ${id}
    [Return]    ${return}

乘法
    [Arguments]    ${number_1}    ${number_2}
    ${result}    evaluate    ${number_1}*${number_2}

接收参数
    [Arguments]    ${parem}
    ${par}    log many    ${parem}[2]
    log    ${par}

Inloop
    [Arguments]    ${times}
    LOG    来自内循环${times}
    FOR    ${j}    IN RANGE    0    ${times}
        log    ${j}
    END

打开浏览器
    [Arguments]    ${browser_url}    ${browser_name}
    open browser    ${browser_url}    ${browser_name}

打开浏览器1
    [Arguments]    ${browser_url}
    OB    ${browser_url}

注册
    [Arguments]    ${ip}    ${port}    ${mobile_phone}    ${pwd}    ${type}    ${reg_name}
    ${return}    register    ${ip}    ${port}    ${mobile_phone}    ${pwd}    ${type}    ${reg_name}
    [Return]    ${return}

登录
    [Arguments]    ${ip}    ${port}    ${moblie_phone}    ${pwd}
    ${return}    login    ${ip}    ${port}    ${moblie_phone}    ${pwd}
    [Return]    ${return}

充值
    [Arguments]    ${ip}    ${port}    ${member_id}    ${amount}    ${token_id}
    ${return}    recharge    ${ip}    ${port}    ${member_id}    ${amount}    ${token_id}
    [Return]    ${return}

用户登录环境准备
    [Arguments]    ${ip}    ${port}    ${moblie_phone}    ${pwd}
    ${return_longin_info}    login    ${ip}    ${port}    18206264880    houlei5837
    set global variable    ${return_longin_info}
