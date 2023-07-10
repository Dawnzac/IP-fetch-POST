$ie = New-Object -ComObject 'internetExplorer.Application'
$ie.Visible= $true # Make it visible

$username="#"

$password="#"

$ie.Navigate("http://#/index.php")

While ($ie.Busy -eq $true) {Start-Sleep -Seconds 3;}

$usernamefield = $ie.document.getElementsByTagName("input") | where-object {$_.type -eq "text"}
$usernamefield.value = "$username"

$passwordfield = $ie.document.getElementsByTagName("input") | where-object {$_.type -eq "password"}
$passwordfield.value = "$password"

$Link=$ie.document.getElementsByTagName("button") | where-object {$_.type -eq "submit"}
$Link.click();

# $ie.Quit()
