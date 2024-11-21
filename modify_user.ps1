# modify_user.ps1
param(
    [string]$Username,
    [string]$NewDepartment
)

# Modificar propiedad del usuario
Set-ADUser -Identity $Username -Department $NewDepartment
Write-Host "Usuario $Username modificado con éxito."
