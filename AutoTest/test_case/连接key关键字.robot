*** Settings ***
Resource          ../key_words/key.robot

*** Test Cases ***
作文大全接口
    ${return}    nihao    zuowen.api.juhe.cn    04adb605ebad26611e9c20059e900b1b    2
    Should Be Equal    ${return}    success

乘法计算
    chengfa    5    4

传参数1
    ${12}    create list    1    2    3
    hello_1    ${12}

嵌套循环
    FOR    ${i}    IN    2    3    4
    LOG    来自外循环${i}
    Inloop    ${i}
    END
