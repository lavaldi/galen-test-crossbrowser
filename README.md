# Galen Test Crossbrowser

## 1. Download Selenium Server and IE Server

http://www.seleniumhq.org/download/

## 2. Download Chrome Driver

https://sites.google.com/a/chromium.org/chromedriver/downloads

Choose from windows or linux version

## 3. Set up a hub (hubConfig.json)

The commands for Windows or Linux are in [run_hub.txt](https://github.com/lavaldi/galen-test-crossbrowser/blob/master/selenium/run_hub.txt) file

## 4. Set up a node (localNodeConfig.json)

The commands for Windows or Linux are in [start_local.txt](https://github.com/lavaldi/galen-test-crossbrowser/blob/master/selenium/start_local.txt) file

## 5. Check the Grid console

In `http://localhost:4444/grid/console` or `http://%COMPUTER_IP%:4444/grid/console`

## 6. Run the test

If all it's OK, run the command

```galen test galen-tests/cross-browser.test --htmlreport "reports"```
