# IT Automation Suite

## Descripción
Scripts para automatizar la gestión de usuarios en Active Directory, Azure AD y GitHub.

## Requisitos
- Python 3.x
- Azure CLI
- GitHub CLI
- PowerShell con módulos ActiveDirectory y AzureAD

## Instalación
1. Clona el repositorio.
2. Instala las dependencias:

pip install -r requirements.txt

3. Configura el acceso a las plataformas (Active Directory, Azure, GitHub).

## Uso
### Active Directory
Ejecutar el script de creación de usuario:


powershell.exe -File active_directory/create_user.ps1 -FirstName "John" -LastName "Doe" -Username "jdoe" -Password "Password123!"


### Azure AD
Ejecutar el script de creación de usuario:


python azure_ad/create_user.py


### GitHub
Ejecutar el script de invitación:

python github/create_user.py


