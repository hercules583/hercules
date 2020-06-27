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
