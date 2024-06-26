import asyncj


async def load_texts(language: str = "ru") -> dict:
    js = asyncj.AsyncJson("texts.json")
    data: dict[str, dict] = await js.read()
    return data.get(language, "en")


async def write_texts(key: str, arg: str, language: str = "ru"):
    js = asyncj.AsyncJson("texts.json")
    texts: dict[str, dict] = await js.read()
    texts[language][key] = arg
    return await js.write(texts)
