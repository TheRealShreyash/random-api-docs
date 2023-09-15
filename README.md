# Random API Docs

## Useful Links

- The Official documentation for the [Random API](https://random-api-nu.vercel.app)
- List of endpoints we provide -> [Endpoints](https://random-api-nu.vercel.app/endpoints)
- Python Examples -> [Py Reference](https://github.com/TheRealShreyash/random-api-docs/examples/Python)
- Javascript Examples -> [Js Reference]()
- Support at -> [Discord](https://dsc.gg/vistara-lounge)

## API Reference

#### Get the version

```http
  GET /api/version
```

#### Get Quote

```http
  GET /api/quote
```

| Endpoint | Response Type | Description                   |
| :------- | :------------ | :---------------------------- |
| `quote`  | `JSON`        | Returns a Quote from the API. |

Also serves the author of the quote in the response.

#### Get Roast

```http
  GET /api/roast
```

| Endpoint | Response Type | Description                   |
| :------- | :------------ | :---------------------------- |
| `roast`  | `JSON`        | Returns a Roast from the API. |

Also serves the id of the roast so you can report something related to that roast to the [Developer](https://github.com/TheRealShreyash) by posting issues on this repo.

#### Get Question

```http
  GET /api/question
```

| Endpoint   | Response Type | Description                      |
| :--------- | :------------ | :------------------------------- |
| `question` | `JSON`        | Returns a Question from the API. |

Also serves the id of the question so you can report something related to that question to the [Developer](https://github.com/TheRealShreyash) by posting issues on this repo.

#### Get Trivia

```http
  GET /api/trivia
```

| Endpoint | Response Type | Description                    |
| :------- | :------------ | :----------------------------- |
| `trivia` | `JSON`        | Returns a trivia from the API. |

#### Get Token

```http
  GET /api/token
```

| Endpoint | Response Type | Description                       |
| :------- | :------------ | :-------------------------------- |
| `token`  | `JSON`        | Returns a 100% safe to use token. |

#### Get Naruto Quiz

```http
  GET /api/naruto
```

| Endpoint | Response Type | Description                                                                |
| :------- | :------------ | :------------------------------------------------------------------------- |
| `naruto` | `JSON`        | Returns a question with 3 options and correct option which is one of them. |

#### Get Beautified Image

```http
  GET /api/beautify
```

| Endpoint   | Response Type | Description                              |
| :--------- | :------------ | :--------------------------------------- |
| `beautify` | `IMAGE`       | Returns a beautified image from the API. |

#### Get Blurred Image

```http
  GET /api/blur
```

| Endpoint | Response Type | Description                           |
| :------- | :------------ | :------------------------------------ |
| `blur`   | `IMAGE`       | Returns a blurred image from the API. |

#### Get Greyscaled Image

```http
  GET /api/greyscale
```

| Endpoint    | Response Type | Description                              |
| :---------- | :------------ | :--------------------------------------- |
| `greyscale` | `IMAGE`       | Returns a greyscaled image from the API. |

## Author

- [TheRealShreyash](https://therealshreyash.github.io)

## Others

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![](https://img.shields.io/badge/Thanks%20for%20reading!-8A2BE2)]()
