for /f "tokens=*" %%F IN ('DIR .\ /AD /B') do @py manage.py migrate %%F zero
for /f "tokens=*" %%F IN ('DIR .\ /AD /B') do @forfiles -p  %%F\migrations\ -m 00* -c "cmd /c del @file"