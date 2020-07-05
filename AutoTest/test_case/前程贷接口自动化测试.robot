*** Settings ***
Suite Setup       用户登录环境准备
Resource          ../key_words/key.robot
Resource          ../variable.txt

*** Test Cases ***
正常注册-手机号11位，密码16位，0管理员、昵称10位
    ${return}    注册    ${ip}    ${port}    18206264880    houlei5837    1    奈何
    Should Be Equal    ${return}    OK

注册10位手机号
    ${return}    注册    ${ip}    ${port}    1820626488    houlei5837    1    奈何
    Should Be Equal    ${return}    OK

正常登录-手机号11位，密码16位
    ${return}    登录    ${ip}    ${port}    15815541763    lemon12345678912
    Should Be Equal    ${return}["msg"]    OK

正常充值
    ${tokenid}    set variable    ${return_longin_info}["date"]["token_info"]
    ${return}    充值    ${ip}    ${port}    1    100    ${tokenid}
