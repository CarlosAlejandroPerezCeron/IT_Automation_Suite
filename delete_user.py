import subprocess

def remove_github_user(username):
    command = [
        "gh", "org", "remove-member",
        username
    ]
    subprocess.run(command)
    print(f"Usuario {username} eliminado del repositorio.")

# Ejemplo de uso
remove_github_user("jdoe")
