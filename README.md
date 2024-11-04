# B2BBroker test task by Dmitry O

This repository is the complete task. Its environment is managed via `poetry`, so if you don't have it, either [install it](https://python-poetry.org/docs/) before running the project or use only the dockerized version.

When you have `poetry` on your system and have initialized the environment (`poetry install`), you can run the tests via `poetry run pytest`.

The dockerized version is usable via `docker compose up`. When reviewing the `docker-compose.yml` file, please note that the supplied username/password/etc. are test values, and in a real application would be fetched from an `.env` file like this: `${MYSQL_USER_PASSWORD}`.

Please note that in certain places, the code is supplied with comments prefixed with `NOTE: `. These comments clarify some of the decisions I made.

Thank you for taking the time to review this task, and please feel free to reach out if any questions arise. Cheers!
