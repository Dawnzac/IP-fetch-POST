Add-Type -AssemblyName System.Windows.Forms
$ip=get-WmiObject Win32_NetworkAdapterConfiguration|Where {$_.Ipaddress.length -gt 1} 
$ipaddress = $ip.ipaddress[0]
$pcname = [System.Net.Dns]::GetHostName()
[System.Windows.Forms.MessageBox]::Show("My PC name - $pcname `n`nMy IP address - $ipaddress",'About my PC','OK','Information')