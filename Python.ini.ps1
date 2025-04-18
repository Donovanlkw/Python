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
