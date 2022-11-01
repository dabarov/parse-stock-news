# Stock Market News Parsing Microservice

## Installation

1. Clone this repo
2. Create `.env` file with the following keys:

```
POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=
SECRET_KEY=
FIN_HUB_KEY=
```

Where `POSTGRES_***` is a values for db initialization and connection to it.
`SECRET_KEY` is a django secret key. `FIN_HUB_KEY` is an api key to interact with `Finnhub.io` api.

3. Run the following command to initialize the database via applying migrations.

```shell
docker compose run api python manage.py migrate
```

4. Start the app with the following command:

```shell
docker compose up
```

## Usage

The app has an hourly task to fetch the data from `Finhub.io`.
You can retrieve saved data through the following endpoint:

```shell
http://localhost:8001/news/stock/NFLX
```

Where `NFLX` can be replaced with the ticket of interest.
You can change the port forwarded to your local host in `docker-compose.yml` file.

It is also possible to filter the news by dates with the following usage of query parameters:

```shell
http://localhost:8001/news/stock/NFLX/?date_from=2022-10-31&date_to=2022-10-31
```
