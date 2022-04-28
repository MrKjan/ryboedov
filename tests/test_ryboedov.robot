*** Settings ***
Library         SeleniumLibrary
Library         String
Library         Collections
Suite Setup     Go to Ryboedov
Suite teardown  Close All Browsers

*** Variables ***
${Price filter xpath}       //ul[contains(@class, 'sort-by-options')]//a[contains(text(), 'Цене')]
${Fish category xpath}      //span[contains(text(), 'Рыба')]
${Buy button xpath}         //*[contains(@class,"catalog-items")]//*[contains(@class, "catalog-item")]/*[contains(@class,"catalog-item-price-and-buy")]//a[@data-action="add-to-basket"]
${Item name xpath postfix}  /parent::*/parent::*/parent::*/*[contains(@class,"catalog-item-title")]//a
${Close popup xpath}        //*[contains(@class,"fancybox-close")]

*** Test Cases ***
Buy two valuable items
    Click Element           xpath=${Fish category xpath}
    Filter by descending price
    Add to cart  1
    Add to cart  2

*** Keywords ***
Go to Ryboedov
    Open browser    https://ryboedov.ru/     browser=chrome     desired_capabilities=pageLoadStrategy:eager

Filter by descending price
    Wait Until Page Contains Element  xpath=${Price filter xpath}
    ${Price filter status}=  Get Element Attribute  ${Price filter xpath}/parent::*  class
    ${active}=  Get Lines Containing String  ${Price filter status}  active
    IF  "${active}" == "${EMPTY}"
        Click Element    xpath=${Price filter xpath}
        Wait Until Page Contains Element  xpath=${Price filter xpath}
        ${Price filter status}=  Get Element Attribute  ${Price filter xpath}/parent::*  class
    END
    ${descending}=  Get Lines Containing String  ${Price filter status}  desc
    IF  "${descending}" == "${EMPTY}"
        Click Element    xpath=${Price filter xpath}
        Wait Until Page Contains Element  xpath=${Price filter xpath}
        ${Price filter status}=  Get Element Attribute  ${Price filter xpath}/parent::*  class
    END
    ${descending}=  Get Lines Containing String  ${Price filter status}  desc
    Should Not Be Empty  ${descending}

Add to cart
    [Arguments]     ${sequence number}
    Wait Until Page Contains Element    xpath=${Buy button xpath}
    ${Buy button}=  Get WebElement      xpath=(${Buy button xpath})[${sequence number}]
    ${Item name}  Get Text  (${Buy button xpath}${Item name xpath postfix})[${sequence number}]
    Log To Console   Buying: ${Item name}
    Click Element    ${Buy button}
    Wait Until Page Contains Element    xpath=${Close popup xpath}
    Click Element    xpath=${Close popup xpath}


