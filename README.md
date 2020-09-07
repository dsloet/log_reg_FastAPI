# LOGREG FastAPI
Small API service deployable to Google Cloud Platform's (GCP) Cloud Run service.

```shell
#!/bin/bash
# clone github
$ git clone https://github.com/dsloet/log_reg_FastAPI.git
$ cd log_reg_FastAPI

# create virtual env
$ virtualenv -p /user/bin/python3 venv
$ source venv/bin/activate

```

## Create GCP project

Browse to GCP, create a new project and follow instructions when prompted.

Install the GCP SDK. Using the SDK in CLI you're able to deploy the docker container to the cloud.

## CLI to build and deploy

First initialize your cli in the terminal to point to the right project.

```shell
$ gcloud init
```
Use the instructions to setup everything to point to your GCP project.

Build your image in the cloud:
```shell
$ gcloud builds submit --tag gcr.io/<YOUR ProjectID>/docker-api
```

Deploy your image
```shell
$ gcloud run deploy <name_your_service> --image gcr.io/<Your ProjectID>/docker-api --allow-unauthenticated
```
And follow the instructions. Finally you'll find your image running URL in the terminal.

### Sources
- https://madflex.de/use-google-cloud-run-with-fastapi/
- https://cloud.google.com/run/docs/quickstarts/build-and-deploy?_ga=2.66419182.-1750665002.1597402809&_gac=1.262528638.1597409612.Cj0KCQjw7Nj5BRCZARIsABwxDKLZywTBuDA0cZYApCEEUNHzFUBjKtn1SQbPW81vt0jZSn69JmMkagcaAg0bEALw_wcB#python
- https://cloud.google.com/run/docs/deploying

