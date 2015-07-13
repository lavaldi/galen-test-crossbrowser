java -Xrs -jar C:\selenium-grid-node\selenium-server-standalone.jar -role node -host %COMPUTERNAME% -nodeConfig C:\selenium-grid-node\localNodeConfig.json -Dwebdriver.chrome.driver="C:\selenium-grid-node\chromedriver.exe" -Dwebdriver.ie.driver="C:\selenium-grid-node\IEDriver.exe"

rem java -jar C:\selenium-grid-node\selenium-server-standalone-2.46.0.jar -role node -nodeConfig C:\selenium-grid-node\localNodeConfig.json -Dwebdriver.chrome.driver="C:\Program Files\Google\Chrome\Application\chrome.exe" -Dwebdriver.ie.driver="C:\selenium-grid-node\IEDriverServer.exe" -hub http://10.54.12.104:4444/grid/register

rem java -jar C:\selenium-grid-node\selenium-server-standalone-2.46.0.jar -role node -nodeConfig C:\selenium-grid-node\localNodeConfig.json -Dwebdriver.ie.driver="C:\selenium-grid-node\IEDriverServer.exe" -hub http://10.54.12.104:4444/grid/register

rem java -jar /home/claudia/Downloads/selenium-server-standalone-2.46.0.jar -role node -nodeConfig /home/claudia/htdocs/galen-test-crossbrowser/selenium/localNodeConfig.json -Dwebdriver.chrome.driver="/home/claudia/Downloads/chromedriver"