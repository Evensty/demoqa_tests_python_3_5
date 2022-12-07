from selene.support.shared import browser
from selene import have, be
import os


current_dir = os.path.dirname(os.path.abspath(__file__))
res_dir = os.path.join(current_dir, 'Resources')
test_file = os.path.join(res_dir, 'test_image.png')


def test_fill_practice_form(window_size):
    browser.open('https://demoqa.com/automation-practice-form')
    browser.element('#firstName').should(be.blank).type('Ivan')
    browser.element('#lastName').should(be.blank).type('Petrov')
    browser.element('#userEmail').should(be.blank).type('test_practice_form@mail.ru')
    browser.element('[for="gender-radio-1"]').click()
    browser.element('#userNumber[placeholder="Mobile Number"]').should(be.blank).type('89995771202')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('.react-datepicker__month-select [value="8"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('.react-datepicker__year-select [value="1920"]').click()
    browser.element('.react-datepicker__day--021').click()
    browser.element('#subjectsInput').type('Maths').press_enter()
    browser.element('.custom-control-label[for="hobbies-checkbox-2"]').click()
    browser.element('#uploadPicture').send_keys(test_file)
    browser.element('#currentAddress[placeholder="Current Address"]').should(be.blank).type('Starokolpaksky alley')
    browser.element('#react-select-3-input').type('Rajasthan').press_enter()
    browser.element('#react-select-4-input').type('Jaiselmer').press_enter().submit()


def test_should_be_correct_result_form_():
    browser.all('.table tr td ~td').should(have.texts(
        'Ivan Petrov', 'test_practice_form@mail.ru', 'Male', '899957712', '21 September,1920', 'Maths', 'Reading',
        'test_image.png', 'Starokolpaksky alley', 'Rajasthan Jaiselmer'))

