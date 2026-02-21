$shell = New-Object -ComObject WScript.Shell
Get-ChildItem "C:\Users\kkmin\Desktop\ebook\*.lnk" | ForEach-Object {
    $shortcut = $shell.CreateShortcut($_.FullName)
    Write-Output "$($_.Name): $($shortcut.TargetPath)"
}
