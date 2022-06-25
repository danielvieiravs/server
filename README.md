
# Manage Packages

## Compile requirements
[`pip-tools`](https://github.com/jazzband/pip-tools) is used to manage the project
Python packages. It must be installed separately by running:

```shell
pip install pip-tools
```

It simplifies the dependency monitoring and packages upgrade process.

It has two commands:
 - [`pip-compile`](https://github.com/jazzband/pip-tools#example-usage-for-pip-compile)
 Add / upgrade the Python package entry in `requirements.txt` files.
 - [`pip-sync`](https://github.com/jazzband/pip-tools#example-usage-for-pip-sync)
 Install / sync the Python packages


### How to add new package
> Remember to add new package without specifying the version in the `.in` file.
Package version is pinned automatically in the automatically generated `txt` file.

If the package is used for production purposes, add it to the `requirements.in` and
then compile requirements by:

```shell
pip-compile --output-file requirements.txt requirements.in && \
pip-compile --output-file requirements_dev.txt requirements_dev.in
```

> Note: both, production and development requirements must be compiled at the same time.
This is because we always want to have the same version of the package in the
production and dev requirements.

If this is package used only for development, add it to the `requirements_dev.in`
and then compile the requirements by:

```shell
pip-compile --output-file requirements_dev.txt requirements_dev.in
```

### How to upgrade package

To upgrade package from production requirements run:

1st:
```shell
pip install pip-tools
```

```shell
pip-compile --upgrade-package <package_name> --output-file requirements.txt requirements.in && \
pip-compile --upgrade-package <package_name> --output-file requirements_dev.txt requirements_dev.in
```

> Note: compile production and dev requirements to keep the packages versions in sync.

To upgrade the package from development requirements, run:

```shell
pip-compile --upgrade-package <package_name> --output-file requirements_dev.txt requirements_dev.in
```

### How to install / sync the packages

[`pip-sync`](https://github.com/jazzband/pip-tools#example-usage-for-pip-sync) is used in this case.

For production setup, run:

```shell
pip-sync requirements.txt
```

For development setup, run:

```shell
pip-sync requirements_dev.txt
```

# Pre-commit

If not already installed, please install pre-commit hooks
```shell
pip install pre-commit
```

After every ".pre-commit-config.yaml" file change, or for the first time, do:
```shell
$ pre-commit install
```

# Docker

## Build && Run
```shell
$ docker-compose up -d --build
```

## Down
```shell
$ docker-compose -f docker-compose.prod.yml down -v
```

## Container logs
```shell
$ docker-compose -f docker-compose.prod.yml logs -f
```

## Remove all data from the database
```shell
$ docker-compose exec web python manage.py flush --no-input
```

## Run the migrations
```shell
$ docker-compose exec web python manage.py migrate --noinput
```

## Access postgres container
```shell
$ docker-compose exec db psql --username= --dbname=
```
