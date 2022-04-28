# Test Automation
Use “Robot Framework” as test automation framework to automate test without using automation recorders or code generators:
- Go to your favorite e-shop
- navigate to some category
- add two most expensive items to the shopping cart from this category.

Provide code from implementation.

# Result (in python + selenium)
Before run, you have to set CHROME_PATH from vars.py to chromedriver path

# Note
For reasons beyond my control, the site sorts by price incorrectly.
I took the first two most expensive items regardless of this (in order of output)

# Run robot tests
robot -P .\ .\tests\test_ryboedov.robot

# Coding
See file .\coding.py
