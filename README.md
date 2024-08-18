# Random API

The API everyone needs, Serves fun with user friendly environment and makes developers life easy(maybe :D)

<a href="https://random-api-nu.vercel.app">API URL</a>

## API Reference

#### Get Version

Check out when was API's latest version released

```http
  GET /api/version
```

#### Get Quote

```http
  GET /api/quote
```

| Endpoint | Type     | Description                   |
| :------- | :------- | :---------------------------- |
| `quote`  | `string` | Returns a Quote from the API. |

#### Get Roast

```http
  GET /api/roast
```

| Endpoint           | Type     | Description                  |
| :----------------- | :------- | :--------------------------- |
| `roast` | `string` | Returns a Roast from the API. |

#### Get Question

```http
  GET /api/question
```

| Endpoint   | Type     | Description                      |
| :--------- | :------- | :------------------------------- |
| `question` | `string` | Returns a Question from the API. |

#### Get Trivia

```http
  GET /api/trivia
```

| Endpoint | Type     | Description                    |
| :------- | :------- | :----------------------------- |
| `trivia` | `string` | Returns a trivia from the API. |

#### Get Beautified Image

```http
  GET /api/beautify
```

| Endpoint   | Type    | Description                              |
| :--------- | :------ | :--------------------------------------- |
| `beautify` | `image` | Returns a beautified image from the API. |

#### Get Blurred Image

```http
  GET /api/blur
```

| Endpoint | Type    | Description                           |
| :------- | :------ | :------------------------------------ |
| `blur`   | `image` | Returns a blurred image from the API. |

#### Get Greyscaled Image

```http
  GET /api/greyscale
```

| Endpoint    | Type    | Description                              |
| :---------- | :------ | :--------------------------------------- |
| `greyscale` | `image` | Returns a greyscaled image from the API. |

## Usage/Examples

```python
import requests

url = requests.get("https://random-api-nu.vercel.app/api/quote")
result = url.json()
quote = result['quote']
author = result['author']
print(f"{quote}\n{author}")
```

## Output:

```json
The only way to do great work is to love what you do.
Steve Jobs
```

## Links

Need help ? Check out those links\

[Docs](https://github.com/TheRealShreyash/random-api-docs)\
[Discord](https://dsc.gg/vistara-lounge)

## License

[MIT](https://choosealicense.com/licenses/mit/)
