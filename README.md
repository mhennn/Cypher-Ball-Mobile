![ui_icon](/src/assets/icon.png)

# CypherBall app

A mobile version of Cypher Ball — ask any random question and receive unexpected, fun answers in return. Inspired by the iconic 90’s Magic 8-Ball, it brings the same nostalgic randomness into a modern interactive experience.

Built as a Flet application, it’s simple, playful, and ready to try anytime you need a quick answer or a bit of digital fate.

### IOS UI Interface
![ios_ui_interface](/src/assets/ios_ui.jpg)

### Application Setup
> Environment
```bash
py -m venv .venv
```

```bash
.venv\Scripts\activate
```

> Requirements Installation
```bash
pip install -r requirements.txt
```

> FastAPI Activation (Root Folder)
```bash
uvicorn src.API.api_get_endpoint:app --reload
```

### Run the application in different platform
Run as a desktop app:
```bash
flet run
```

Run as a web app:
```bash
flet run --web
```

Run as IOS app:
```bash
flet run --ios
```

###### Random Answers can be changed based on developers/user purposes. This is just an example.

> For more details on building Web app, refer to the [Web Packaging Guide](https://flet.dev/docs/publish/web/).
