#https://www.python.org/downloads/windows/

# New path you want to add
$newPath1 = "$env:LOCALAPPDATA\Programs\Python\Python313\"
$newPath2 = "$env:LOCALAPPDATA\Programs\Python\Python313\Scripts\"

# Get current system PATH
$sysPath = [Environment]::GetEnvironmentVariable("PATH", "Machine")

# Set updated system PATH
$newPathValue = "$sysPath;$newPath1;$newPath2"
[Environment]::SetEnvironmentVariable("PATH", $newPathValue, "Machine")


pip --version  
pip install pyautogui
pip install time
pip install selenium
pip install playwright

#python -m playwright install
#python.exe -m pip --version
#python -m pip install -U selenium



Set-Service -Name w32time -StartupType Automatic

# 2. Start the Windows Time service
Start-Service -Name w32time

# 3. Configure the time server (you can change this to any preferred NTP server)
$ntpServer = "time.windows.com,0x1"
w32tm /config /manualpeerlist:$ntpServer /syncfromflags:manual /reliable:yes /update

# 4. Force resync
w32tm /resync

# 5. Show the current configuration
w32tm /query /status
w32tm /query /configuration
