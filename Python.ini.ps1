#https://www.python.org/downloads/windows/
$path = "$env:LOCALAPPDATA\Programs\Python\Python313\Scripts\"
$env:Path += ";$path"
$path1 = "$env:LOCALAPPDATA\Programs\Python\Python313\"
$env:Path += ";$path1"

pip --version  
pip install pyautogui
pip install time
pip install selenium

pip install playwright
python -m playwright install

python.exe -m pip --version
python -m pip install -U selenium
