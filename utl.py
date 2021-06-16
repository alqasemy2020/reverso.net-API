from requests import Session
from bs4 import BeautifulSoup


def get_translation(source, lang, word):


    languages_dict = {"ab":"ABKHAZIAN","aa":"AFAR","af":"AFRIKAANS","ak":"AKAN","sq":"ALBANIAN","am":"AMHARIC","ar":"ARABIC","hy":"ARMENIAN","as":"ASSAMESE","ay":"AYMARA","az":"AZERBAIJANI","ba":"BASHKIR","eu":"BASQUE","be":"BELARUSIAN","bn":"BENGALI","bh":"BIHARI","bi":"BISLAMA","bs":"BOSNIAN","br":"BRETON","bg":"BULGARIAN","my":"BURMESE","ca":"CATALAN","ceb":"CEBUANO","chr":"CHEROKEE","ny":"NYANJA","co":"CORSICAN","hr":"CROATIAN","hr":"CROATIAN","cs":"CZECH","zh":"Chinese","zh":"Chinese","zh":"Chinese","zh":"Chinese","zh-Hant":"ChineseT","zh-Hant":"ChineseT","zh-Hant":"ChineseT","zh-Hant":"ChineseT","zh-Hant":"ChineseT","zh-Hant":"ChineseT","da":"DANISH","dv":"DHIVEHI","nl":"DUTCH","dz":"DZONGKHA","en":"ENGLISH","eo":"ESPERANTO","et":"ESTONIAN","ee":"EWE","fo":"FAROESE","fj":"FIJIAN","fi":"FINNISH","fr":"FRENCH","fy":"FRISIAN","gaa":"GA","gl":"GALICIAN","lg":"GANDA","ka":"GEORGIAN","de":"GERMAN","el":"GREEK","kl":"GREENLANDIC","gn":"GUARANI","gu":"GUJARATI","ht":"HAITIAN_CREOLE","ha":"HAUSA","haw":"HAWAIIAN","iw":"HEBREW","iw":"HEBREW","hi":"HINDI","hmn":"HMONG","hu":"HUNGARIAN","is":"ICELANDIC","ig":"IGBO","id":"INDONESIAN","ia":"INTERLINGUA","ie":"INTERLINGUE","iu":"INUKTITUT","ik":"INUPIAK","ga":"IRISH","it":"ITALIAN","xxx":"Ignore","jw":"JAVANESE","jw":"JAVANESE","ja":"Japanese","kn":"KANNADA","ks":"KASHMIRI","kk":"KAZAKH","kha":"KHASI","km":"KHMER","rw":"KINYARWANDA","kri":"KRIO","ku":"KURDISH","ky":"KYRGYZ","ko":"Korean","lo":"LAOTHIAN","la":"LATIN","lv":"LATVIAN","lif":"LIMBU","lif":"LIMBU","lif":"LIMBU","ln":"LINGALA","lt":"LITHUANIAN","loz":"LOZI","lua":"LUBA_LULUA","luo":"LUO_KENYA_AND_TANZANIA","lb":"LUXEMBOURGISH","mk":"MACEDONIAN","mg":"MALAGASY","ms":"MALAY","ml":"MALAYALAM","mt":"MALTESE","gv":"MANX","mi":"MAORI","mr":"MARATHI","mfe":"MAURITIAN_CREOLE","ro":"ROMANIAN","mn":"MONGOLIAN","sr-ME":"MONTENEGRIN","sr-ME":"MONTENEGRIN","sr-ME":"MONTENEGRIN","sr-ME":"MONTENEGRIN","na":"NAURU","nr":"NDEBELE","ne":"NEPALI","new":"NEWARI","no":"NORWEGIAN","no":"NORWEGIAN","nn":"NORWEGIAN_N","ny":"NYANJA","oc":"OCCITAN","or":"ORIYA","om":"OROMO","os":"OSSETIAN","pam":"PAMPANGA","ps":"PASHTO","nso":"PEDI","fa":"PERSIAN","pl":"POLISH","pt":"PORTUGUESE","pa":"PUNJABI","qu":"QUECHUA","raj":"RAJASTHANI","rm":"RHAETO_ROMANCE","ro":"ROMANIAN","rn":"RUNDI","ru":"RUSSIAN","sm":"SAMOAN","sg":"SANGO","sa":"SANSKRIT","sco":"SCOTS","gd":"SCOTS_GAELIC","sr":"SERBIAN","sr":"SERBIAN","crs":"SESELWA","crs":"SESELWA","st":"SESOTHO","sn":"SHONA","sd":"SINDHI","si":"SINHALESE","ss":"SISWANT","sk":"SLOVAK","sl":"SLOVENIAN","so":"SOMALI","es":"SPANISH","su":"SUNDANESE","sw":"SWAHILI","sv":"SWEDISH","syr":"SYRIAC","tl":"TAGALOG","tg":"TAJIK","ta":"TAMIL","tt":"TATAR","te":"TELUGU","th":"THAI","bo":"TIBETAN","ti":"TIGRINYA","to":"TONGA","ts":"TSONGA","tn":"TSWANA","tum":"TUMBUKA","tr":"TURKISH","tk":"TURKMEN","tw":"TWI","ug":"UIGHUR","uk":"UKRAINIAN","ur":"URDU","uz":"UZBEK","ve":"VENDA","vi":"VIETNAMESE","vo":"VOLAPUK","war":"WARAY_PHILIPPINES","cy":"WELSH","wo":"WOLOF","xh":"XHOSA","yi":"YIDDISH","yo":"YORUBA","za":"ZHUANG","zu":"ZULU"}
    headers = {
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Sec-GPC': '1',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Accept-Language': 'en,ar;q=0.9',
    }


    session = Session()

    if len(source) <= 2 or '-' in source:
        source = languages_dict[source].lower()
    if len(lang) <= 2 or '-' in lang:
        lang = languages_dict[lang].lower()

    try:
        url = f'https://context.reverso.net/translation/{source}-{lang}/{word}'
        res = session.get(url, headers=headers).content
        soup = BeautifulSoup(res, 'html.parser')

        data = soup.find('div', {'id':'translations-content'}).find_all('a')

        finall_data = []
        for i in data:
            finall_data.append(u''.join(i.text.strip()))

        return finall_data
    except AttributeError as AErr:
        return 'no results!'
