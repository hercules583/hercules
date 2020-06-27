*** Test Cases ***
forzip
    ${Number}    set variable    1    2    3
    ${Name}    set variable    one    two    three
    FOR    ${number}    ${name}    IN ZIP    ${Number}    ${Name}
        log    ${number}
        log    ${name}
    END

exitfor
    FOR    ${i}    IN RANGE    0    10
    run keyword if    ${i}==5    exit for loop
        LOG    ${i}
    END

continueloop
    FOR    ${i}    IN RANGE    0    10
    run keyword if    ${i}==5    continue for loop
        LOG    ${i}
    END

example_for
    ${sum}    set variable    0
    FOR    ${i}    IN RANGE    1    101
    ${resuite}    evaluate    ${i}%2
    run keyword if    ${resuite}==0    continue for loop
        ${sum}    evaluate    ${sum}+${i}
        LOG    ${sum}
    END
