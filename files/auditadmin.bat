echo auditpol /set /subcategory:"logon" /success:enable /failure:enable important
echo auditpol /set /subcategory:"Other Account Logon Events" not important https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/audit-other-account-logon-events
echo auditpol /set /subcategory:"Computer Account Management" - not important
echo auditpol /set /subcategory:"User Account Management" important
echo auditpol /set /subcategory:"Process Creation" - not important
echo auditpol /set /subcategory:"Other Logon/Logoff Events" - important
echo auditpol /set /subcategory:"Application Generated" - not working
echo auditpol /set /subcategory:"Filtering Platform Connection" - not important
echo auditpol /set /subcategory:"Filtering Platform Packet Drop" - not important
echo auditpol /set /subcategory:"Other Object Access Events" - important
echo auditpol /set /subcategory:"MPSSVC Rule-Level Policy Change" - important
echo auditpol /set /subcategory:"Security System Extension" - important
pause
sleep 1 
timeout /t 1
choice
REM auditpol /get /Category:*