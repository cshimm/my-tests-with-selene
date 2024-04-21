import sys
import os

# Find the absolute path of the directory containing your module
module_dir = os.path.relpath(r'selene')
# Add the absolute path to sys.path
sys.path.append(module_dir)
from selene import browser, by, be, have
browser.open('https://google.com/ncr')
browser.element(by.name('q')).should(be.blank) \
    .type('selenium').press_enter()
browser.all('#rso>div').should(have.size_greater_than(1)) \
    .first.should(have.text('Selenium automates browsers'))