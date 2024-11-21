import subprocess

def modify_azure_user(username, new_job_title):
    command = [
        "az", "ad", "user", "update",
        "--id", f"{username}@yourdomain.com",
        "--job-title", new_job_title
    ]
    subprocess.run(command)
    print(f"Usuario {username} modificado con éxito.")

# Ejemplo de uso
modify_azure_user("jdoe", "Senior Developer")
