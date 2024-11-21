# create_user.ps1
param(
    [string]$FirstName,
    [string]$LastName,
    [string]$Username,
    [string]$Password
)

# Importar módulo ActiveDirectory
Import-Module ActiveDirectory

# Crear usuario
New-ADUser `
    -Name "$FirstName $LastName" `
    -GivenName $FirstName `
    -Surname $LastName `
    -SamAccountName $Username `
    -UserPrincipalName "$Username@domain.com" `
    -AccountPassword (ConvertTo-SecureString $Password -AsPlainText -Force) `
    -Enabled $true

Write-Host "Usuario $Username creado con éxito."
