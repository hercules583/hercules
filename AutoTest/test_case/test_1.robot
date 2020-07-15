*** Settings ***
Suite Setup
Resource          ../key_words/key.robot
Library           RequestsLibrary
Library           SeleniumLibrary

*** Test Cases ***
global_1
    set global variable    ${g_var}    hello,world
    log    ${g_var}

if_1
    ${if_1}    set variable    hello
    run keyword if    "${if_1}"=="hello"    run keywords    log    相等
    ...    AND    log    abc
    ...    ELSE    run keywords    log    不相等
    ...    AND    log    123

forinrange
    ${sum}    set variable    0
    FOR    ${i}    IN RANGE    1    101
        ${sum}    evaluate    ${sum}+${i}
        LOG    ${sum}
    END

forin
    FOR    ${i}    ${j}    IN    1    2    3    4
        LOG    ${i}
        LOG    ${j}
    END

byid
    open browser    http://www.baidu.com/    Chrome
    input text    id=kw    RF 自动化
    click element    id=su
    sleep    3
    [Teardown]    Close All Browsers

bylog
    open browser    http://www.baidu.com/    Chrome
    Maximize Browser Window
    @{list_2}    get webelements    tag=input
    input text    @{list_2}[7]    RF 自动化
    click element    id=su
    sleep    10
    [Teardown]    close all browsers

bylink
    open browser    http://www.baidu.com/    Chrome
    Maximize Browser Window
    click element    link=新闻
    sleep    10
    [Teardown]    Close All Browsers

byname
    open browser    http://www.baidu.com/    Chrome
    Maximize Browser Window
    input text    name=wd    RF自动化
    click element    id=su
    sleep    3
    [Teardown]    close all browsers

byclass
    open browser    http://www.baidu.com/    Chrome
    Maximize Browser Window
    input text    class=s_ipt    RF自动化
    click element    class=s_btn
    sleep    3
    [Teardown]    close all browsers

by pratial link
    open browser    http://www.baidu.com/    Chrome
    Maximize Browser Window
    click element    partial link=闻
    sleep    10
    [Teardown]    close all browsers

byxpath
    open browser    http://www.baidu.com/    Chrome
    Maximize Browser Window
    input text    xpath=/html/body/div[1]/div[1]/div[5]/div/div/form/span[1]/input    RF自动化
    click element    id=su
    sleep    10
    [Teardown]    close all browsers

bycss
    open browser    http://www.baidu.com/    Chrome
    Maximize Browser Window
    input text    css=#kw    RF自动化
    click element    id=su
    sleep    10
    [Teardown]    close all browsers

打开百度新闻1
    打开浏览器1    http://www.baidu.com/
    input text    id=kw    zhongguo
    click element    id=su
    sleep    3

post请求
    Create Session    register    http://120.78.128.25:8766
    ${url}    set variable    /futureloan/member/register
    ${weiba}    evaluate    random.randint(1000,9999)    random
    ${date}    create dictionary    mobile_phone=1820626${weiba}    pwd=12345678
    ${headers}    create dictionary    X-Lemonban-Media-Type=lemonban.v2    Content-Type=application/json
    ${resp}    post Request    register    ${url}    ${date}    headers=${headers}
    log    ${resp.status_code}
    log    ${resp.json()}
