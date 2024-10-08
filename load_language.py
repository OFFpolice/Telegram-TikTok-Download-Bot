import json
import aiofiles


async def load_language_files():
    async with aiofiles.open("language/lang.json", "r", encoding="utf-8") as lang_file:
        lang = json.loads(await lang_file.read())

    async with aiofiles.open("language/strings_ru.json", "r", encoding="utf-8") as ru_file:
        strings_ru = json.loads(await ru_file.read())

    async with aiofiles.open("language/strings_en.json", "r", encoding="utf-8") as en_file:
        strings_en = json.loads(await en_file.read())

    async with aiofiles.open("language/strings_uk.json", "r", encoding="utf-8") as uk_file:
        strings_uk = json.loads(await uk_file.read())

    async with aiofiles.open("language/strings_de.json", "r", encoding="utf-8") as de_file:
        strings_de = json.loads(await de_file.read())

    async with aiofiles.open("language/strings_fr.json", "r", encoding="utf-8") as fr_file:
        strings_fr = json.loads(await fr_file.read())

    async with aiofiles.open("language/strings_es.json", "r", encoding="utf-8") as es_file:
        strings_es = json.loads(await es_file.read())

    async with aiofiles.open("language/strings_jap.json", "r", encoding="utf-8") as jap_file:
        strings_jap = json.loads(await jap_file.read())

    async with aiofiles.open("language/strings_ko.json", "r", encoding="utf-8") as ko_file:
        strings_ko = json.loads(await ko_file.read())

    async with aiofiles.open("language/strings_zh_hans.json", "r", encoding="utf-8") as zh_hans_file:
        strings_zh_hans = json.loads(await zh_hans_file.read())

    async with aiofiles.open("language/strings_zh_hant.json", "r", encoding="utf-8") as zh_hant_file:
        strings_zh_hant = json.loads(await zh_hant_file.read())

    return {
        "lang": lang,
        "strings_ru": strings_ru,
        "strings_en": strings_en,
        "strings_uk": strings_uk,
        "strings_de": strings_de,
        "strings_fr": strings_fr,
        "strings_es": strings_es,
        "strings_jap": strings_jap,
        "strings_ko": strings_ko,
        "strings_zh_hans": strings_zh_hans,
        "strings_zh_hant": strings_zh_hant
    }
