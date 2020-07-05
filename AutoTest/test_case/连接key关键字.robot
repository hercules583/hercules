*** Settings ***
Resource          ../key_words/key.robot
Library           Selenium2Library
Resource          ../variable.txt

*** Test Cases ***
作文大全接口
    ${return}    作文    ${zuowen_ip}    04adb605ebad26611e9c20059e900b1b    2
    Should Be Equal    ${return}    success

乘法计算
    乘法    5    4

传参数
    ${12}    create list    1    2    3
    接收参数    ${12}

嵌套循环
    FOR    ${i}    IN    2    3    4
        LOG    来自外循环${i}
        Inloop    ${i}
    END

百度搜索
    ${return}    打开浏览器    http://www.baidu.com/    chrome
    Maximize Browser Window
    input text    id=kw    zhongguo
    click element    id=su
    sleep    3
    [Teardown]    close all browsers
