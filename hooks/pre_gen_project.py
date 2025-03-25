import sys

def main():
    print("🚀 Starting project generation...")

    # Ejemplo de validación de variables de Cookiecutter
    project_name = "{{ cookiecutter.project_name }}"
    package_name = "{{ cookiecutter.package_name }}"
    database = "{{ cookiecutter.database }}"
    use_docker = "{{ cookiecutter.use_docker }}"

    # Validar que el nombre del proyecto no esté vacío
    if not project_name.strip():
        print("Error: 'project_name' cannot be empty.")
        sys.exit(1)

    # Ejemplo: validar que se haya seleccionado 'yes' o 'no' para usar Docker
    if use_docker.lower() not in ["yes", "no"]:
        print("Error: 'use_docker' must be either 'yes' or 'no'.")
        sys.exit(1)

if __name__ == '__main__':
    main()
