import subprocess

def create_azure_user(username, first_name, last_name, password):
    command = [
        "az", "ad", "user", "create",
        "--display-name", f"{first_name} {last_name}",
        "--user-principal-name", f"{username}@yourdomain.com",
        "--password", password,
        "--force-change-password-next-login", "true"
    ]
    subprocess.run(command)
    print(f"Usuario {username} creado con éxito.")

# Ejemplo de uso
create_azure_user("jdoe", "John", "Doe", "Password123!")
