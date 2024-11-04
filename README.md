# B2BBroker test task by Dmitry O

This repository is the complete task. Its environment is managed via `poetry`, so if you don't have it, either [install it](https://python-poetry.org/docs/) before running the project or use only the dockerized version.

When you have `poetry` on your system and have initialized the environment (`poetry install`), you can run the tests via `DEBUG=TRUE poetry run pytest` (specifying DEBUG is needed so that the MySQL option is not picked for the database - if you have a configured MySQL that you can provide in the env, please feel free to use that, but I do not think that is necessary for running tests in this project).

## The dockerized version

It is usable via `docker compose up`. When reviewing the `docker-compose.yml` file, please note that the supplied username/password/etc. are test values, and in a real application would be fetched from an `.env` file like this: `${MYSQL_USER_PASSWORD}`.

To access the dockerized version when it is up, go to https://localhost:1337. Please note that DRF does not recognize the port, so you have to add it yourself when using the links provided by the API root. This is a bug that is inherent in DRF and not present when using a proper host name with default port, so I do not consider it as needing a fix.

## Comments

Please note that in certain places, the code is supplied with comments prefixed with `NOTE: `. These comments clarify some of the decisions I made.

Thank you for taking the time to review this task, and please feel free to reach out if any questions arise. Cheers!
