
# Cookiecutter Template for HEX DDD

This repository is a Cookiecutter template for generating a Flask project based on Hexagonal Architecture and Domain-Driven Design (DDD) principles.

## Template Overview

This template generates a well-structured Flask application with the following layers:
- **Domain:** Contains entities, aggregates, value objects, and exceptions.
- **Application:** Includes ports, services, and domain events.
- **Infrastructure:** Provides adapters (input via REST API, output for persistence and messaging), configuration, and mappers.
- **Tests:** Supports unit and integration tests.
- Other key files such as `requirements.txt`, `Dockerfile`, and `README.md` are also included.

Additionally, the template leverages pre- and post-generation hooks:
- **Pre-generation Hook:** Validates input parameters before project creation.
- **Post-generation Hook:** Dynamically creates a `.gitignore`, initializes a Git repository, creates a virtual environment, and installs dependencies.

## Prerequisites

Before using this template, make sure you have:
- [Python 3.8+](https://www.python.org/downloads/)
- [Cookiecutter](https://cookiecutter.readthedocs.io/en/latest/installation.html) (`pip install cookiecutter`)
- [Git](https://git-scm.com/downloads)

## How to Use the Template

### Using the GitHub Repository
If your template is hosted on GitHub, you can generate a new project by running:
```sh
cookiecutter gh:your-username/your-template-repo
```

### Using a Local Copy
Alternatively, if you have cloned this repository locally, run:
```sh
cookiecutter /path/to/cookiecutter-hexddd
```

### Follow the Prompts
You will be asked to provide several configuration options, such as:
- `project_name`
- `package_name`
- `author`
- `email`
- `description`
- `use_docker`
- Database selection (sqlite, postgres, mysql)
- Message queue selection (none, rabbitmq, kafka)
- CI/CD selection (none, github_actions, gitlab_ci)
- Testing framework selection (pytest, unittest)

## Post-generation Tasks

After generating your project, the post-generation hook will:
- Dynamically generate a `.gitignore`
- Initialize a Git repository and perform the initial commit
- Create a virtual environment named `venv`
- Install the required dependencies from `requirements.txt`

## Project Structure

The generated project will have a structure similar to the following:
```
{{ cookiecutter.project_name }}/
├── src/
│   ├── domain/
│   │   ├── __init__.py
│   │   ├── model/
│   │   │   └── __init__.py
│   │   ├── value_objects/
│   │   │   └── __init__.py
│   │   └── exceptions/
│   │       └── __init__.py
│   ├── application/
│   │   ├── __init__.py
│   │   ├── ports/
│   │   │   ├── __init__.py
│   │   │   ├── input/
│   │   │   │   └── __init__.py
│   │   │   └── output/
│   │   │       └── __init__.py
│   │   ├── services/
│   │   │   └── __init__.py
│   │   └── events/
│   │       └── __init__.py
│   ├── infrastructure/
│   │   ├── __init__.py
│   │   ├── adapters/
│   │   │   ├── __init__.py
│   │   │   ├── input/
│   │   │   │   ├── __init__.py
│   │   │   │   └── rest/
│   │   │   │       ├── __init__.py
│   │   │   │       ├── app.py
│   │   │   │       ├── blueprints/
│   │   │   │       │   └── __init__.py
│   │   │   │       └── schemas/
│   │   │   │           └── __init__.py
│   │   │   └── output/
│   │   │       └── __init__.py
│   │   │       ├── persistence/
│   │   │       │   ├── __init__.py
│   │   │       │   └── models/
│   │   │       │      └── __init__.py
│   │   │       └── messaging/
│   │   │           └── __init__.py
│   │   ├── config/
│   │   │   ├── __init__.py
│   │   │   ├── settings.py
│   │   │   └── di_container.py
│   │   └── mappers/
│   │       └── __init__.py
│   └── app.py
├── tests/
│   ├── __init__.py
│   ├── unit/
│   │   ├── __init__.py
│   │   ├── domain/
│   │   ├── application/
│   │   └── infrastructure/
│   └── integration/
│       └── __init__.py
├── requirements.txt
├── Dockerfile
└── README.md
```

## Contributing

Contributions to improve this template are welcome. Please feel free to open issues or submit pull requests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
