# Url-Short

A very simple url shortening example.

Linux, more specifically Ubuntu 20, is assumed for all commands.

__Duration: 2 hours__

## Requirements
* `docker`
* `docker-compose`

## Run
* To run the example solution please execute `docker-compose up --build` in the terminal in the project root.

## Test
* To create a new hash make a request to `http://localhost:3000/n?url={url}` where `{url}` is replaced with the URL in need of shortening.
* Copy the response from the previous request and make a request to the copied URL.

## Stop
* To stop the docker-compose services run `docker-compose stop` in the terminal from the project root.

## Gaps
* Testing and benchmarking
* Scaling would be ideal
* Better configuration with expirations for example
* User based routes would be cool
* Security, it is pretty open right now
* Terraform to configure an AWS deployment
