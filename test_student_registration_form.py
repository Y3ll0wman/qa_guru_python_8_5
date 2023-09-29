from selene import browser, be


def test_student_registration_form():
    browser.open("https://demoqa.com/automation-practice-form")
    browser.element("#firstName").should(be.visible).type("Vasya")
    browser.element("#lastName").should(be.visible).type("Vasilyev")
    browser.element("#userEmail").should(be.visible).type("example@example.com")
    browser.element(".custom-control.custom-radio.custom-control-inline").should(be.visible).click()
    browser.element("#userNumber").should(be.visible).type("+79999999999")
    browser.element("#dateOfBirthInput").should(be.visible).click()
    browser.element(".react-datepicker__month-select").should(be.visible).click()
    browser.element(".react-datepicker__month-select > option:nth-child(5)").should(be.visible).click()
    browser.element(".react-datepicker__year-select").should(be.visible).click()
    browser.element(".react-datepicker__year-select > option:nth-child(20)").should(be.visible).click()
    browser.element(".react-datepicker__day.react-datepicker__day--012").should(be.visible).click()
