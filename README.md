# flask-react-template
A simple full stack template with a Python + Flask backend, PostgreSQL database and React frontend. Containerized using Docker for easy development and deployment.

## Development
The development build only runs the backend and server containerized. The backend can be started by running the following command:
```sh
$ docker-compose -p projname -f docker-compose.dev.yml up
```

The frontend can then be optionally started by running:
```sh
$ cd frontend && yarn run start
```

## Deployment
A production ready build can be launched by running:
```sh
$ docker-compose -p projname up
```
