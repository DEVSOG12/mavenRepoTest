# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['langcodes', 'langcodes.tests']

package_data = \
{'': ['*'], 'langcodes': ['data/*']}

extras_require = \
{'data': ['language-data>=1.1,<2.0']}

setup_kwargs = {
    'name': 'langcodes',
    'version': '3.3.0',
    'description': 'Tools for labeling human languages with IETF language tags',
    'long_description': '# Langcodes: a library for language codes\n\n**langcodes** knows what languages are. It knows the standardized codes that\nrefer to them, such as `en` for English, `es` for Spanish and `hi` for Hindi.\n\nThese are [IETF language tags][]. You may know them by their old name, ISO 639\nlanguage codes. IETF has done some important things for backward compatibility\nand supporting language variations that you won\'t find in the ISO standard.\n\n[IETF language tags]: https://www.w3.org/International/articles/language-tags/\n\nIt may sound to you like langcodes solves a pretty boring problem. At one\nlevel, that\'s right. Sometimes you have a boring problem, and it\'s great when a\nlibrary solves it for you.\n\nBut there\'s an interesting problem hiding in here. How do you work with\nlanguage codes? How do you know when two different codes represent the same\nthing? How should your code represent relationships between codes, like the\nfollowing?\n\n* `eng` is equivalent to `en`.\n* `fra` and `fre` are both equivalent to `fr`.\n* `en-GB` might be written as `en-gb` or `en_GB`. Or as \'en-UK\', which is\n  erroneous, but should be treated as the same.\n* `en-CA` is not exactly equivalent to `en-US`, but it\'s really, really close.\n* `en-Latn-US` is equivalent to `en-US`, because written English must be written\n  in the Latin alphabet to be understood.\n* The difference between `ar` and `arb` is the difference between "Arabic" and\n  "Modern Standard Arabic", a difference that may not be relevant to you.\n* You\'ll find Mandarin Chinese tagged as `cmn` on Wiktionary, but many other\n  resources would call the same language `zh`.\n* Chinese is written in different scripts in different territories. Some\n  software distinguishes the script. Other software distinguishes the territory.\n  The result is that `zh-CN` and `zh-Hans` are used interchangeably, as are\n  `zh-TW` and `zh-Hant`, even though occasionally you\'ll need something\n  different such as `zh-HK` or `zh-Latn-pinyin`.\n* The Indonesian (`id`) and Malaysian (`ms` or `zsm`) languages are mutually\n  intelligible.\n* `jp` is not a language code. (The language code for Japanese is `ja`, but\n  people confuse it with the country code for Japan.)\n\nOne way to know is to read IETF standards and Unicode technical reports.\nAnother way is to use a library that implements those standards and guidelines\nfor you, which langcodes does.\n\nWhen you\'re working with these short language codes, you may want to see the\nname that the language is called _in_ a language: `fr` is called "French" in\nEnglish. That language doesn\'t have to be English: `fr` is called "français" in\nFrench. A supplement to langcodes, [`language_data`][language-data], provides\nthis information.\n\n[language-data]: https://github.com/rspeer/language_data\n\nlangcodes is maintained by Elia Robyn Lake a.k.a. Robyn Speer, and is released\nas free software under the MIT license.\n\n\n## Standards implemented\n\nAlthough this is not the only reason to use it, langcodes will make you more\nacronym-compliant.\n\nlangcodes implements [BCP 47](http://tools.ietf.org/html/bcp47), the IETF Best\nCurrent Practices on Tags for Identifying Languages. BCP 47 is also known as\nRFC 5646. It subsumes ISO 639 and is backward compatible with it, and it also\nimplements recommendations from the [Unicode CLDR](http://cldr.unicode.org).\n\nlangcodes can also refer to a database of language properties and names, built\nfrom Unicode CLDR and the IANA subtag registry, if you install `language_data`.\n\nIn summary, langcodes takes language codes and does the Right Thing with them,\nand if you want to know exactly what the Right Thing is, there are some\ndocuments you can go read.\n\n\n# Documentation\n\n## Standardizing language tags\n\nThis function standardizes tags, as strings, in several ways.\n\nIt replaces overlong tags with their shortest version, and also formats them\naccording to the conventions of BCP 47:\n\n    >>> from langcodes import *\n    >>> standardize_tag(\'eng_US\')\n    \'en-US\'\n\nIt removes script subtags that are redundant with the language:\n\n    >>> standardize_tag(\'en-Latn\')\n    \'en\'\n\nIt replaces deprecated values with their correct versions, if possible:\n\n    >>> standardize_tag(\'en-uk\')\n    \'en-GB\'\n\nSometimes this involves complex substitutions, such as replacing Serbo-Croatian\n(`sh`) with Serbian in Latin script (`sr-Latn`), or the entire tag `sgn-US`\nwith `ase` (American Sign Language).\n\n    >>> standardize_tag(\'sh-QU\')\n    \'sr-Latn-EU\'\n\n    >>> standardize_tag(\'sgn-US\')\n    \'ase\'\n\nIf *macro* is True, it uses macrolanguage codes as a replacement for the most\ncommon standardized language within that macrolanguage.\n\n    >>> standardize_tag(\'arb-Arab\', macro=True)\n    \'ar\'\n\nEven when *macro* is False, it shortens tags that contain both the\nmacrolanguage and the language:\n\n    >>> standardize_tag(\'zh-cmn-hans-cn\')\n    \'zh-Hans-CN\'\n\nIf the tag can\'t be parsed according to BCP 47, this will raise a\nLanguageTagError (a subclass of ValueError):\n\n    >>> standardize_tag(\'spa-latn-mx\')\n    \'es-MX\'\n\n    >>> standardize_tag(\'spa-mx-latn\')\n    Traceback (most recent call last):\n        ...\n    langcodes.tag_parser.LanguageTagError: This script subtag, \'latn\', is out of place. Expected variant, extension, or end of string.\n\n\n## Language objects\n\nThis package defines one class, named Language, which contains the results\nof parsing a language tag. Language objects have the following fields,\nany of which may be unspecified:\n\n- *language*: the code for the language itself.\n- *script*: the 4-letter code for the writing system being used.\n- *territory*: the 2-letter or 3-digit code for the country or similar region\n  whose usage of the language appears in this text.\n- *extlangs*: a list of more specific language codes that follow the language\n  code. (This is allowed by the language code syntax, but deprecated.)\n- *variants*: codes for specific variations of language usage that aren\'t\n  covered by the *script* or *territory* codes.\n- *extensions*: information that\'s attached to the language code for use in\n  some specific system, such as Unicode collation orders.\n- *private*: a code starting with `x-` that has no defined meaning.\n\nThe `Language.get` method converts a string to a Language instance, and the\n`Language.make` method makes a Language instance from its fields.  These values\nare cached so that calling `Language.get` or `Language.make` again with the\nsame values returns the same object, for efficiency.\n\nBy default, it will replace non-standard and overlong tags as it interprets\nthem. To disable this feature and get the codes that literally appear in the\nlanguage tag, use the *normalize=False* option.\n\n    >>> Language.get(\'en-Latn-US\')\n    Language.make(language=\'en\', script=\'Latn\', territory=\'US\')\n\n    >>> Language.get(\'sgn-US\', normalize=False)\n    Language.make(language=\'sgn\', territory=\'US\')\n\n    >>> Language.get(\'und\')\n    Language.make()\n\nHere are some examples of replacing non-standard tags:\n\n    >>> Language.get(\'sh-QU\')\n    Language.make(language=\'sr\', script=\'Latn\', territory=\'EU\')\n\n    >>> Language.get(\'sgn-US\')\n    Language.make(language=\'ase\')\n\n    >>> Language.get(\'zh-cmn-Hant\')\n    Language.make(language=\'zh\', script=\'Hant\')\n\nUse the `str()` function on a Language object to convert it back to its\nstandard string form:\n\n    >>> str(Language.get(\'sh-QU\'))\n    \'sr-Latn-EU\'\n\n    >>> str(Language.make(territory=\'IN\'))\n    \'und-IN\'\n\n\n### Checking validity\n\nA language code is _valid_ when every part of it is assigned a meaning by IANA.\nThat meaning could be "private use".\n\nIn langcodes, we check the language subtag, script, territory, and variants for\nvalidity. We don\'t check other parts such as extlangs or Unicode extensions.\n\nFor example, `ja` is a valid language code, and `jp` is not:\n\n    >>> Language.get(\'ja\').is_valid()\n    True\n\n    >>> Language.get(\'jp\').is_valid()\n    False\n\nThe top-level function `tag_is_valid(tag)` is possibly more convenient to use,\nbecause it can return False even for tags that don\'t parse:\n\n    >>> tag_is_valid(\'C\')\n    False\n\nIf one subtag is invalid, the entire code is invalid:\n\n    >>> tag_is_valid(\'en-000\')\n    False\n\n`iw` is valid, though it\'s a deprecated alias for `he`:\n\n    >>> tag_is_valid(\'iw\')\n    True\n\nThe empty language tag (`und`) is valid:\n\n    >>> tag_is_valid(\'und\')\n    True\n\nPrivate use codes are valid:\n\n    >>> tag_is_valid(\'x-other\')\n    True\n\n    >>> tag_is_valid(\'qaa-Qaai-AA-x-what-even-is-this\')\n    True\n\nLanguage tags that are very unlikely are still valid:\n\n    >>> tag_is_valid(\'fr-Cyrl\')\n    True\n\nTags with non-ASCII characters are invalid, because they don\'t parse:\n\n   >>> tag_is_valid(\'zh-普通话\')\n   False\n\n\n### Getting alpha3 codes\n\nBefore there was BCP 47, there was ISO 639-2. The ISO tried to make room for the\nvariety of human languages by assigning every language a 3-letter code,\nincluding the ones that already had 2-letter codes.\n\nUnfortunately, this just led to more confusion. Some languages ended up with two\ndifferent 3-letter codes for legacy reasons, such as French, which is `fra` as a\n"terminology" code, and `fre` as a "biblographic" code. And meanwhile, `fr` was\nstill a code that you\'d be using if you followed ISO 639-1.\n\nIn BCP 47, you should use 2-letter codes whenever they\'re available, and that\'s\nwhat langcodes does. Fortunately, all the languages that have two different\n3-letter codes also have a 2-letter code, so if you prefer the 2-letter code,\nyou don\'t have to worry about the distinction.\n\nBut some applications want the 3-letter code in particular, so langcodes\nprovides a method for getting those, `Language.to_alpha3()`. It returns the\n\'terminology\' code by default, and passing `variant=\'B\'` returns the\nbibliographic code.\n\nWhen this method returns, it always returns a 3-letter string.\n\n    >>> Language.get(\'fr\').to_alpha3()\n    \'fra\'\n    >>> Language.get(\'fr-CA\').to_alpha3()\n    \'fra\'\n    >>> Language.get(\'fr-CA\').to_alpha3(variant=\'B\')\n    \'fre\'\n    >>> Language.get(\'de\').to_alpha3()\n    \'deu\'\n    >>> Language.get(\'no\').to_alpha3()\n    \'nor\'\n    >>> Language.get(\'un\').to_alpha3()\n    Traceback (most recent call last):\n        ...\n    LookupError: \'un\' is not a known language code, and has no alpha3 code.\n\nFor many languages, the terminology and bibliographic alpha3 codes are the same.\n\n    >>> Language.get(\'en\').to_alpha3(variant=\'T\')\n    \'eng\'\n    >>> Language.get(\'en\').to_alpha3(variant=\'B\')\n    \'eng\'\n\nWhen you use any of these "overlong" alpha3 codes in langcodes, they normalize\nback to the alpha2 code:\n\n    >>> Language.get(\'zho\')\n    Language.make(language=\'zh\')\n\n\n## Working with language names\n\nThe methods in this section require an optional package called `language_data`.\nYou can install it with `pip install language_data`, or request the optional\n"data" feature of langcodes with `pip install langcodes[data]`.\n\nThe dependency that you put in setup.py should be `langcodes[data]`.\n\n### Describing Language objects in natural language\n\nIt\'s often helpful to be able to describe a language code in a way that a user\n(or you) can understand, instead of in inscrutable short codes. The\n`display_name` method lets you describe a Language object *in a language*.\n\nThe `.display_name(language, min_score)` method will look up the name of the\nlanguage. The names come from the IANA language tag registry, which is only in\nEnglish, plus CLDR, which names languages in many commonly-used languages.\n\nThe default language for naming things is English:\n\n    >>> Language.make(language=\'fr\').display_name()\n    \'French\'\n\n    >>> Language.make().display_name()\n    \'Unknown language\'\n\n    >>> Language.get(\'zh-Hans\').display_name()\n    \'Chinese (Simplified)\'\n\n    >>> Language.get(\'en-US\').display_name()\n    \'English (United States)\'\n\nBut you can ask for language names in numerous other languages:\n\n    >>> Language.get(\'fr\').display_name(\'fr\')\n    \'français\'\n\n    >>> Language.get(\'fr\').display_name(\'es\')\n    \'francés\'\n\n    >>> Language.make().display_name(\'es\')\n    \'lengua desconocida\'\n\n    >>> Language.get(\'zh-Hans\').display_name(\'de\')\n    \'Chinesisch (Vereinfacht)\'\n\n    >>> Language.get(\'en-US\').display_name(\'zh-Hans\')\n    \'英语（美国）\'\n\nWhy does everyone get Slovak and Slovenian confused? Let\'s ask them.\n\n    >>> Language.get(\'sl\').display_name(\'sl\')\n    \'slovenščina\'\n    >>> Language.get(\'sk\').display_name(\'sk\')\n    \'slovenčina\'\n    >>> Language.get(\'sl\').display_name(\'sk\')\n    \'slovinčina\'\n    >>> Language.get(\'sk\').display_name(\'sl\')\n    \'slovaščina\'\n\nIf the language has a script or territory code attached to it, these will be\ndescribed in parentheses:\n\n    >>> Language.get(\'en-US\').display_name()\n    \'English (United States)\'\n\nSometimes these can be the result of tag normalization, such as in this case\nwhere the legacy tag \'sh\' becomes \'sr-Latn\':\n\n    >>> Language.get(\'sh\').display_name()\n    \'Serbian (Latin)\'\n\n    >>> Language.get(\'sh\', normalize=False).display_name()\n    \'Serbo-Croatian\'\n\nNaming a language in itself is sometimes a useful thing to do, so the\n`.autonym()` method makes this easy, providing the display name of a language\nin the language itself:\n\n    >>> Language.get(\'fr\').autonym()\n    \'français\'\n    >>> Language.get(\'es\').autonym()\n    \'español\'\n    >>> Language.get(\'ja\').autonym()\n    \'日本語\'\n    >>> Language.get(\'en-AU\').autonym()\n    \'English (Australia)\'\n    >>> Language.get(\'sr-Latn\').autonym()\n    \'srpski (latinica)\'\n    >>> Language.get(\'sr-Cyrl\').autonym()\n    \'српски (ћирилица)\'\n\nThe names come from the Unicode CLDR data files, and in English they can\nalso come from the IANA language subtag registry. Together, they can give\nyou language names in the 196 languages that CLDR supports.\n\n\n### Describing components of language codes\n\nYou can get the parts of the name separately with the methods `.language_name()`,\n`.script_name()`, and `.territory_name()`, or get a dictionary of all the parts\nthat are present using the `.describe()` method. These methods also accept a\nlanguage code for what language they should be described in.\n\n    >>> shaw = Language.get(\'en-Shaw-GB\')\n    >>> shaw.describe(\'en\')\n    {\'language\': \'English\', \'script\': \'Shavian\', \'territory\': \'United Kingdom\'}\n\n    >>> shaw.describe(\'es\')\n    {\'language\': \'inglés\', \'script\': \'shaviano\', \'territory\': \'Reino Unido\'}\n\n\n### Recognizing language names in natural language\n\nAs the reverse of the above operations, you may want to look up a language by\nits name, converting a natural language name such as "French" to a code such as\n\'fr\'.\n\nThe name can be in any language that CLDR supports (see "Ambiguity" below).\n\n    >>> import langcodes\n    >>> langcodes.find(\'french\')\n    Language.make(language=\'fr\')\n\n    >>> langcodes.find(\'francés\')\n    Language.make(language=\'fr\')\n\nHowever, this method currently ignores the parenthetical expressions that come from\n`.display_name()`:\n\n    >>> langcodes.find(\'English (Canada)\')\n    Language.make(language=\'en\')\n\nThere is still room to improve the way that language names are matched, because\nsome languages are not consistently named the same way. The method currently\nworks with hundreds of language names that are used on Wiktionary.\n\n#### Ambiguity\n\nFor the sake of usability, `langcodes.find()` doesn\'t require you to specify what\nlanguage you\'re looking up a language in by name. This could potentially lead to\na conflict: what if name "X" is language A\'s name for language B, and language C\'s\nname for language D?\n\nWe can collect the language codes from CLDR and see how many times this\nhappens. In the majority of cases like that, B and D are codes whose names are\nalso overlapping in the _same_ language and can be resolved by some general\nprinciple.\n\nFor example, no matter whether you decide "Tagalog" refers to the language code\n`tl` or the largely overlapping code `fil`, that distinction doesn\'t depend on\nthe language you\'re saying "Tagalog" in. We can just return `tl` consistently.\n\n    >>> langcodes.find(\'tagalog\')\n    Language.make(language=\'tl\')\n\nIn the few cases of actual interlingual ambiguity, langcodes won\'t match a result.\nYou can pass in a `language=` parameter to say what language the name is in.\n\nFor example, there are two distinct languages called "Tonga" in various languages.\nThey are `to`, the language of Tonga which is called "Tongan" in English; and `tog`,\na language of Malawi that can be called "Nyasa Tonga" in English.\n\n    >>> langcodes.find(\'tongan\')\n    Language.make(language=\'to\')\n\n    >>> langcodes.find(\'nyasa tonga\')\n    Language.make(language=\'tog\')\n\n    >>> langcodes.find(\'tonga\')\n    Traceback (most recent call last):\n    ...\n    LookupError: Can\'t find any language named \'tonga\'\n\n    >>> langcodes.find(\'tonga\', language=\'id\')\n    Language.make(language=\'to\')\n\n    >>> langcodes.find(\'tonga\', language=\'ca\')\n    Language.make(language=\'tog\')\n\nOther ambiguous names written in Latin letters are "Kiga", "Mbundu", "Roman", and "Ruanda".\n\n\n## Demographic language data\n\nThe `Language.speaking_population()` and `Language.writing_population()`\nmethods get Unicode\'s estimates of how many people in the world use a\nlanguage.\n\nAs with the language name data, this requires the optional `language_data`\npackage to be installed.\n\n`.speaking_population()` estimates how many people speak a language. It can\nbe limited to a particular territory with a territory code (such as a country\ncode).\n\n    >>> Language.get(\'es\').speaking_population()\n    487664083\n\n    >>> Language.get(\'pt\').speaking_population()\n    237135429\n\n    >>> Language.get(\'es-BR\').speaking_population()\n    76218\n\n    >>> Language.get(\'pt-BR\').speaking_population()\n    192661560\n\n    >>> Language.get(\'vo\').speaking_population()\n    0\n\nScript codes will be ignored, because the script is not involved in speaking:\n\n    >>> Language.get(\'es-Hant\').speaking_population() ==\\\n    ... Language.get(\'es\').speaking_population()\n    True\n\n`.writing_population()` estimates how many people write a language.\n        \n    >>> all = Language.get(\'zh\').writing_population()\n    >>> all\n    1240326057\n\n    >>> traditional = Language.get(\'zh-Hant\').writing_population()\n    >>> traditional\n    37019589\n\n    >>> simplified = Language.get(\'zh-Hans\').writing_population()\n    >>> all == traditional + simplified\n    True\n\nThe estimates for "writing population" are often overestimates, as described\nin the [CLDR documentation on territory data][overestimates]. In most cases,\nthey are derived from published data about literacy rates in the places where\nthose languages are spoken. This doesn\'t take into account that many literate\npeople around the world speak a language that isn\'t typically written, and\nwrite in a _different_ language.\n\n[overestimates]: https://unicode-org.github.io/cldr-staging/charts/39/supplemental/territory_language_information.html\n\nLike `.speaking_population()`, this can be limited to a particular territory:\n\n    >>> Language.get(\'zh-Hant-HK\').writing_population()\n    6439733\n    >>> Language.get(\'zh-Hans-HK\').writing_population()\n    338933\n\n\n## Comparing and matching languages\n\nThe `tag_distance` function returns a number from 0 to 134 indicating the\ndistance between the language the user desires and a supported language.\n\nThe distance data comes from CLDR v38.1 and involves a lot of judgment calls\nmade by the Unicode consortium.\n\n\n### Distance values\n\nThis table summarizes the language distance values:\n\n| Value | Meaning                                                                                                       | Example\n| ----: | :------                                                                                                       | :------\n|     0 | These codes represent the same language, possibly after filling in values and normalizing.                    | Norwegian Bokmål → Norwegian\n|   1-3 | These codes indicate a minor regional difference.                                                             | Australian English → British English\n|   4-9 | These codes indicate a significant but unproblematic regional difference.                                     | American English → British English\n| 10-24 | A gray area that depends on your use case. There may be problems with understanding or usability.             | Afrikaans → Dutch, Wu Chinese → Mandarin Chinese\n| 25-50 | These languages aren\'t similar, but there are demographic reasons to expect some intelligibility.             | Tamil → English, Marathi → Hindi\n| 51-79 | There are large barriers to understanding.                                                                    | Japanese → Japanese in Hepburn romanization\n| 80-99 | These are different languages written in the same script.                                                     | English → French, Arabic → Urdu\n|  100+ | These languages have nothing particularly in common.                                                          | English → Japanese, English → Tamil\n\nSee the docstring of `tag_distance` for more explanation and examples.\n\n\n### Finding the best matching language\n\nSuppose you have software that supports any of the `supported_languages`. The\nuser wants to use `desired_language`.\n\nThe function `closest_supported_match(desired_language, supported_languages)`\nlets you choose the right language, even if there isn\'t an exact match.\nIt returns the language tag of the best-supported language, even if there\nisn\'t an exact match.\n\nThe `max_distance` parameter lets you set a cutoff on what counts as language\nsupport. It has a default of 25, a value that is probably okay for simple\ncases of i18n, but you might want to set it lower to require more precision.\n\n    >>> closest_supported_match(\'fr\', [\'de\', \'en\', \'fr\'])\n    \'fr\'\n\n    >>> closest_supported_match(\'pt\', [\'pt-BR\', \'pt-PT\'])\n    \'pt-BR\'\n\n    >>> closest_supported_match(\'en-AU\', [\'en-GB\', \'en-US\'])\n    \'en-GB\'\n\n    >>> closest_supported_match(\'af\', [\'en\', \'nl\', \'zu\'])\n    \'nl\'\n\n    >>> closest_supported_match(\'und\', [\'en\', \'und\'])\n    \'und\'\n\n    >>> print(closest_supported_match(\'af\', [\'en\', \'nl\', \'zu\'], max_distance=10))\n    None\n\nA similar function is `closest_match(desired_language, supported_language)`,\nwhich returns both the best matching language tag and the distance. If there is\nno match, it returns (\'und\', 1000).\n\n    >>> closest_match(\'fr\', [\'de\', \'en\', \'fr\'])\n    (\'fr\', 0)\n\n    >>> closest_match(\'sh\', [\'hr\', \'bs\', \'sr-Latn\', \'sr-Cyrl\'])\n    (\'sr-Latn\', 0)\n\n    >>> closest_match(\'id\', [\'zsm\', \'mhp\'])\n    (\'zsm\', 14)\n\n    >>> closest_match(\'ja\', [\'ja-Latn-hepburn\', \'en\'])\n    (\'und\', 1000)\n\n    >>> closest_match(\'ja\', [\'ja-Latn-hepburn\', \'en\'], max_distance=60)\n    (\'ja-Latn-hepburn\', 50)\n\n## Further API documentation\n\nThere are many more methods for manipulating and comparing language codes,\nand you will find them documented thoroughly in [the code itself][code].\n\nThe interesting functions all live in this one file, with extensive docstrings\nand annotations. Making a separate Sphinx page out of the docstrings would be\nthe traditional thing to do, but here it just seems redundant. You can go read\nthe docstrings in context, in their native habitat, and they\'ll always be up to\ndate.\n\n[Code with documentation][code]\n\n[code]: https://github.com/rspeer/langcodes/blob/master/langcodes/__init__.py\n\n# Changelog\n\n## Version 3.3 (November 2021)\n\n- Updated to CLDR v40.\n\n- Updated the IANA subtag registry to version 2021-08-06.\n\n- Bug fix: recognize script codes that appear in the IANA registry even if\n  they\'re missing from CLDR for some reason. \'cu-Cyrs\' is valid, for example.\n\n- Switched the build system from `setuptools` to `poetry`.\n\nTo install the package in editable mode before PEP 660 is better supported, use\n`poetry install` instead of `pip install -e .`.\n\n## Version 3.2 (October 2021)\n\n- Supports Python 3.6 through 3.10.\n\n- Added the top-level function `tag_is_valid(tag)`, for determining if a string\n  is a valid language tag without having to parse it first.\n\n- Added the top-level function `closest_supported_match(desired, supported)`,\n  which is similar to `closest_match` but with a simpler return value. It\n  returns the language tag of the closest match, or None if no match is close\n  enough.\n\n- Bug fix: a lot of well-formed but invalid language codes appeared to be\n  valid, such as \'aaj\' or \'en-Latnx\', because the regex could match a prefix of\n  a subtag. The validity regex is now required to match completely.\n\n- Bug fixes that address some edge cases of validity:\n\n  - A language tag that is entirely private use, like \'x-private\', is valid\n  - A language tag that uses the same extension twice, like \'en-a-bbb-a-ccc\',\n    is invalid\n  - A language tag that uses the same variant twice, like \'de-1901-1901\', is\n    invalid\n  - A language tag with two extlangs, like \'sgn-ase-bfi\', is invalid\n\n- Updated dependencies so they are compatible with Python 3.10, including\n  switching back from `marisa-trie-m` to `marisa-trie` in `language_data`.\n\n- In bugfix release 3.2.1, corrected cases where the parser accepted\n  ill-formed language tags:\n\n  - All subtags must be made of between 1 and 8 alphanumeric ASCII characters\n  - Tags with two extension \'singletons\' in a row (`en-a-b-ccc`) should be\n    rejected\n\n## Version 3.1 (February 2021)\n\n- Added the `Language.to_alpha3()` method, for getting a three-letter code for a\n  language according to ISO 639-2.\n\n- Updated the type annotations from obiwan-style to mypy-style.\n\n\n## Version 3.0 (February 2021)\n\n- Moved bulky data, particularly language names, into a separate\n  `language_data` package. In situations where the data isn\'t needed,\n  `langcodes` becomes a smaller, pure-Python package with no dependencies.\n\n- Language codes where the language segment is more than 4 letters no longer\n  parse: Language.get(\'nonsense\') now returns an error.\n\n  (This is technically stricter than the parse rules of BCP 47, but there are\n  no valid language codes of this form and there should never be any. An\n  attempt to parse a language code with 5-8 letters is most likely a mistake or\n  an attempt to make up a code.)\n\n- Added a method for checking the validity of a language code.\n\n- Added methods for estimating language population.\n\n- Updated to CLDR 38.1, which includes differences in language matching.\n\n- Tested on Python 3.6 through 3.9; no longer tested on Python 3.5.\n\n\n## Version 2.2 (February 2021)\n\n- Replaced `marisa-trie` dependency with `marisa-trie-m`, to achieve\n  compatibility with Python 3.9.\n\n\n## Version 2.1 (June 2020)\n\n- Added the `display_name` method to be a more intuitive way to get a string\n  describing a language code, and made the `autonym` method use it instead of\n  `language_name`.\n\n- Updated to CLDR v37.\n\n- Previously, some attempts to get the name of a language would return its\n  language code instead, perhaps because the name was being requested in a\n  language for which CLDR doesn\'t have name data. This is unfortunate because\n  names and codes should not be interchangeable.\n\n  Now we fall back on English names instead, which exists for all IANA codes.\n  If the code is unknown, we return a string such as "Unknown language [xx]".\n\n\n## Version 2.0 (April 2020)\n\nVersion 2.0 involves some significant changes that may break compatibility with 1.4,\nin addition to updating to version 36.1 of the Unicode CLDR data and the April 2020\nversion of the IANA subtag registry.\n\nThis version requires Python 3.5 or later.\n\n### Match scores replaced with distances\n\nOriginally, the goodness of a match between two different language codes was defined\nin terms of a "match score" with a maximum of 100. Around 2016, Unicode started\nreplacing this with a different measure, the "match distance", which was defined\nmuch more clearly, but we had to keep using the "match score".\n\nAs of langcodes version 2.0, the "score" functions (such as\n`Language.match_score`, `tag_match_score`, and `best_match`) are deprecated.\nThey\'ll keep using the deprecated language match tables from around CLDR 27.\n\nFor a better measure of the closeness of two language codes, use `Language.distance`,\n`tag_distance`, and `closest_match`.\n\n### \'region\' renamed to \'territory\'\n\nWe were always out of step with CLDR here. Following the example of the IANA\ndatabase, we referred to things like the \'US\' in \'en-US\' as a "region code",\nbut the Unicode standards consistently call it a "territory code".\n\nIn langcodes 2.0, parameters, dictionary keys, and attributes named `region`\nhave been renamed to `territory`.  We try to support a few common cases with\ndeprecation warnings, such as looking up the `region` property of a Language\nobject.\n\nA nice benefit of this is that when a dictionary is displayed with \'language\',\n\'script\', and \'territory\' keys in alphabetical order, they are in the same\norder as they are in a language code.\n\n',
    'author': 'Elia Robyn Speer',
    'author_email': 'rspeer@arborelia.net',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/rspeer/langcodes',
    'packages': packages,
    'package_data': package_data,
    'extras_require': extras_require,
    'python_requires': '>=3.6',
}


setup(**setup_kwargs)
