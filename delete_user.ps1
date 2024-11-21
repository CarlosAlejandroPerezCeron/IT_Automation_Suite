# delete_user.ps1
param(
    [string]$Username
)

# Eliminar usuario
Remove-ADUser -Identity $Username -Confirm:$false
Write-Host "Usuario $Username eliminado con éxito."
