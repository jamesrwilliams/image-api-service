# Image API Service

[![Project Status: Concept – Minimal or no implementation has been done yet, or the repository is only intended to be a limited example, demo, or proof-of-concept.](https://www.repostatus.org/badges/latest/concept.svg)](https://www.repostatus.org/#concept)

Goal of this is to have an API that responds with an image that is generated from a unique set of data. 
A bit like bespoke repository badges, or dynamic README images that show the status (and simple configuration) of deployed mono-repo apps across a few environments.
Written in Python using [Flask](https://flask.palletsprojects.com/en/2.0.x) and [Pillow](https://pillow.readthedocs.io/).

Example URLs (via Heroku):

- https://image-api-service.herokuapp.com
- https://image-api-service.herokuapp.com/api/demo/text
- https://image-api-service.herokuapp.com/api/status/example

## Getting started

- `pip3 install pipenv` - Setup your virtual env
- `pipenv shell` - Access the python shell
- `pipenv install` - Install our dependencies
- `flask run` - Start the server

## Example

Usage in a README.md file or HTML site. Add the URL as the src and the image will render. See `demo/index.html` for an example working with your local server.

```html
<img alt="Current status of the project" src="https://example.com/api/" />
```

## Uses
