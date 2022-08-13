# T5-base API

## Running the App

### Requirements

#### Models

Given the sizes of the model files needed to run the app, they are not included in the repo,
they have to be downloaded separated.

Head [here](https://huggingface.co/t5-base/tree/main) and download the following files into the `t5_models/` directory

- `pytorch_model.bin`
- `tokenizer.json`
- `config.json`
- `spiece.model`

For more info on the model, [check it out here](https://huggingface.co/t5-base).

#### Docker

Docker is required to run the app. If docker is not installed, go the
[official docker page](https://docs.docker.com/engine/install/) to install.

### Running

In the root folder run

    docker-compose up -d

The API should be accessible on `http://localhost:8088`

### Type-check Code

Execute the following command to appy `mypy` type-checking

    docker-compose run --rm web make type_check

### Format Code

Execute the following command to apply `isort` and `black` formatting:

    docker-compose run --rm web make format

### Tests

Run test with `pytest` with the following:

    docker-compose run --rm web make test

## Endpoints

### Translate

    POST http://localhost:8088/api/v1/translate/

This endpoint translates an `input_text` from a `source_language` to a `destination_language`

```json
{
  "source_language": "en",
  "destination_language": "ro",
  "input_text": "How about you?"
}
```

The language choices are

    "en" - English
    "fr" - French
    "ro" - Romanian
    "de" - German


