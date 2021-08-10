# How to run

### Requisites

- docker & docker-compose ([click here](https://docs.docker.com/get-docker/))
- poetry (use `pip`)
- postgresql, libpq-dev (use `apt-install`)

### Serve both databases:

```console
$ docker run -d -p 27017:27017 --name mongodb mongo
$ docker-compose up -d
```

<details>
  <summary>auxiliary cmds for db</summary>
  
<blockquote>


- mongo

```console
$ docker exec -it mongodb bash
```

- postgres

```console
$ docker-compose down && docker-compose up -d --force-recreate
```

</blockquote>


</details>

### Populate with postgres:

```console
poetry run import_postgres
```

### Populate with csv:

```console
poetry run import_csv
```

### Run sample queries:

```console
poetry run example_queries
```
