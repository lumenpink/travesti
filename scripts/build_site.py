#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gerador de Páginas Estáticas Anti-Design para travesti.2lp.in
Utiliza a biblioteca oficial Python Markdown com extensões completas
para garantir a renderização impecável de todos os elementos.
"""

import os
import re
from datetime import datetime, timezone
import markdown

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SITE_DIR = os.path.join(BASE_DIR, "site")
ASSETS_DIR = os.path.join(SITE_DIR, "assets")
OBSIDIAN_MD = "/home/lumen/obsidian/97_floranda/jardins/Travesti.md"

# Carrega versão e data/hora de montagem/compilação ISO UTC conforme Perfil Lumen
VERSION_FILE = os.path.join(BASE_DIR, "VERSION")
with open(VERSION_FILE, "r", encoding="utf-8") as vf:
    APP_VERSION = vf.read().strip()
BUILD_TIMESTAMP = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
BUILD_ID = int(datetime.now(timezone.utc).timestamp())

LANGS = [
    {"code": "pt", "name": "Português", "dir": "ltr", "country": "Brasil 🇧🇷", "flag_text": "travesti latina"},
    {"code": "en", "name": "English", "dir": "ltr", "country": "Brazil 🇧🇷", "flag_text": "Latin American travesti"},
    {"code": "es", "name": "Español", "dir": "ltr", "country": "Brasil 🇧🇷", "flag_text": "travesti latinoamericana"},
    {"code": "fr", "name": "Français", "dir": "ltr", "country": "Brésil 🇧🇷", "flag_text": "travesti latino-américaine"},
    {"code": "de", "name": "Deutsch", "dir": "ltr", "country": "Brasilien 🇧🇷", "flag_text": "lateinamerikanischen Travesti"},
    {"code": "it", "name": "Italiano", "dir": "ltr", "country": "Brasile 🇧🇷", "flag_text": "travesti latinoamericana"},
    {"code": "ru", "name": "Русский", "dir": "ltr", "country": "Бразилия 🇧🇷", "flag_text": "латиноамериканской travesti"},
    {"code": "zh", "name": "中文", "dir": "ltr", "country": "巴西 🇧🇷", "flag_text": "拉美 travesti"},
    {"code": "ja", "name": "日本語", "dir": "ltr", "country": "ブラジル 🇧🇷", "flag_text": "ラテンアメリカの travesti"},
    {"code": "ar", "name": "العربية", "dir": "rtl", "country": "البرازيل 🇧🇷", "flag_text": "travesti أمريكية لاتينية"}
]

I18N = {
    "pt": {
        "title": "Travesti (identidade de gênero e política)",
        "brand_badge": "🏳️‍⚧️ AUTODETERMINAÇÃO",
        "hero_tape": "TRAVESTI VIVE // AUTODETERMINAÇÃO // NÃO SOMOS DISFARCE // SUBSTANTIVO POLÍTICO",
        "hero_tag": "MANIFESTO & HISTORIOGRAFIA POLÍTICA",
        "hero_sub": "Identidade de gênero e política de matriz estritamente latino-americana, marcada pela autodeterminação, pela história de luta nas ruas e pela intraduzibilidade semântica.",
        "stamp": "SUBSTANTIVO POLÍTICO • INTRADUZÍVEL • NÃO SOMOS DISFARCE",
        "footer_l1": "Orgulhosamente produzido por uma <a href=\"https://travesti.2lp.in/pt/\">travesti latina</a> 🏳️‍⚧️ :)",
        "footer_l2": f"Travesti v{APP_VERSION} • por <a href=\"https://lumen.pink\">Lumen Pink</a> • {BUILD_TIMESTAMP} • Brasil 🇧🇷 • <a href=\"https://creativecommons.org/licenses/by-sa/4.0\">CC-BY-SA-4.0</a>",
        "meta_desc": "História, etimologia, teoria dissidente, neurobiologia e lutas políticas da travestilidade no Brasil e na América Latina.",
        "lang_switch_label": "IDIOMA / LÍNGUA:"
    },
    "en": {
        "title": "Travesti (gender identity and politics)",
        "brand_badge": "🏳️‍⚧️ SELF-DETERMINATION",
        "hero_tape": "TRAVESTI LIVES // SELF-DETERMINATION // NOT A DISGUISE // POLITICAL NOUN",
        "hero_tag": "POLITICAL MANIFESTO & HISTORIOGRAPHY",
        "hero_sub": "A Latin American gender and political identity marked by self-determination, street resistance, and radical semantic untranslatability.",
        "stamp": "POLITICAL NOUN • UNTRANSLATABLE • NOT A DISGUISE",
        "footer_l1": "Proudly produced by a <a href=\"https://travesti.2lp.in/en/\">Latin American travesti</a> 🏳️‍⚧️ :)",
        "footer_l2": f"Travesti v{APP_VERSION} • by <a href=\"https://lumen.pink\">Lumen Pink</a> • {BUILD_TIMESTAMP} • Brazil 🇧🇷 • <a href=\"https://creativecommons.org/licenses/by-sa/4.0\">CC-BY-SA-4.0</a>",
        "meta_desc": "History, etymology, dissident theory, neurobiology, and political struggles of travestilidade in Brazil and Latin America.",
        "lang_switch_label": "LANGUAGE:"
    },
    "es": {
        "title": "Travesti (identidad de género y política)",
        "brand_badge": "🏳️‍⚧️ AUTODETERMINACIÓN",
        "hero_tape": "TRAVESTI VIVE // AUTODETERMINACIÓN // NO SOMOS DISFRAZ // SUSTANTIVO POLÍTICO",
        "hero_tag": "MANIFIESTO E HISTORIOGRAFÍA POLÍTICA",
        "hero_sub": "Identidad de género y política estrictamente latinoamericana, marcada por la autodeterminación, la lucha en las calles y la intraducibilidad semántica.",
        "stamp": "SUSTANTIVO POLÍTICO • INTRADUCIBLE • NO SOMOS DISFRAZ",
        "footer_l1": "Orgullosamente produzido por una <a href=\"https://travesti.2lp.in/es/\">travesti latinoamericana</a> 🏳️‍⚧️ :)",
        "footer_l2": f"Travesti v{APP_VERSION} • por <a href=\"https://lumen.pink\">Lumen Pink</a> • {BUILD_TIMESTAMP} • Brasil 🇧🇷 • <a href=\"https://creativecommons.org/licenses/by-sa/4.0\">CC-BY-SA-4.0</a>",
        "meta_desc": "Historia, etimología, teoría disidente, neurobiología y luchas políticas de la travestilidad en Brasil y América Latina.",
        "lang_switch_label": "IDIOMA:"
    },
    "fr": {
        "title": "Travesti (identité de genre et politique)",
        "brand_badge": "🏳️‍⚧️ AUTODÉTERMINATION",
        "hero_tape": "TRAVESTI VIT // AUTODÉTERMINATION // PAS UN DÉGUISEMENT // SUBSTANTIF POLITIQUE",
        "hero_tag": "MANIFESTE ET HISTORIOGRAPHIE POLITIQUE",
        "hero_sub": "Une identité de genre et politique strictement latino-américaine, caractérisée par l'autodétermination, la lutte dans la rue et l'intraduisibilité sémantique.",
        "stamp": "SUBSTANTIF POLITIQUE • INTRADUISIBLE • PAS UN DÉGUISEMENT",
        "footer_l1": "Fièrement produit par une <a href=\"https://travesti.2lp.in/fr/\">travesti latino-américaine</a> 🏳️‍⚧️ :)",
        "footer_l2": f"Travesti v{APP_VERSION} • par <a href=\"https://lumen.pink\">Lumen Pink</a> • {BUILD_TIMESTAMP} • Brésil 🇧🇷 • <a href=\"https://creativecommons.org/licenses/by-sa/4.0\">CC-BY-SA-4.0</a>",
        "meta_desc": "Histoire, étymologie, théorie dissidente, neurobiologie et luttes politiques de la travestilité au Brésil et en Amérique latine.",
        "lang_switch_label": "LANGUE :"
    },
    "de": {
        "title": "Travesti (Geschlechtsidentität und Politik)",
        "brand_badge": "🏳️‍⚧️ SELBSTBESTIMMUNG",
        "hero_tape": "TRAVESTI LEBT // SELBSTBESTIMMUNG // KEINE VERKLEIDUNG // POLITISCHES SUBSTANTIV",
        "hero_tag": "POLITISCHES MANIFEST & HISTORIOGRAPHIE",
        "hero_sub": "Eine lateinamerikanische Geschlechts- und politische Identität, geprägt von Selbstbestimmung, Straßenwiderstand und semantischer Unübersetzbarkeit.",
        "stamp": "POLITISCHES SUBSTANTIV • UNÜBERSETZBAR • KEINE VERKLEIDUNG",
        "footer_l1": "Mit Stolz entwickelt von einer <a href=\"https://travesti.2lp.in/de/\">lateinamerikanischen Travesti</a> 🏳️‍⚧️ :)",
        "footer_l2": f"Travesti v{APP_VERSION} • von <a href=\"https://lumen.pink\">Lumen Pink</a> • {BUILD_TIMESTAMP} • Brasilien 🇧🇷 • <a href=\"https://creativecommons.org/licenses/by-sa/4.0\">CC-BY-SA-4.0</a>",
        "meta_desc": "Geschichte, Etymologie, dissidente Theorie, Neurobiologie und politische Kämpfe der Travestilität in Brasilien und Lateinamerika.",
        "lang_switch_label": "SPRACHE:"
    },
    "it": {
        "title": "Travesti (identità di genere e politica)",
        "brand_badge": "🏳️‍⚧️ AUTODETERMINAZIONE",
        "hero_tape": "TRAVESTI VIVE // AUTODETERMINAZIONE // NON UN TRAVESTIMENTO // SOSTANTIVO POLITICO",
        "hero_tag": "MANIFESTO E STORIOGRAFIA POLITICA",
        "hero_sub": "Un'identità di genere e politica strettamente latinoamericana, segnata dall'autodeterminazione, dalla resistenza nelle strade e dall'intraducibilità semantica.",
        "stamp": "SOSTANTIVO POLITICO • INTRADUCIBILE • NON UN TRAVESTIMENTO",
        "footer_l1": "Orgogliosamente prodotto da uma <a href=\"https://travesti.2lp.in/it/\">travesti latinoamericana</a> 🏳️‍⚧️ :)",
        "footer_l2": f"Travesti v{APP_VERSION} • da <a href=\"https://lumen.pink\">Lumen Pink</a> • {BUILD_TIMESTAMP} • Brasile 🇧🇷 • <a href=\"https://creativecommons.org/licenses/by-sa/4.0\">CC-BY-SA-4.0</a>",
        "meta_desc": "Storia, etimologia, teoria dissidente, neurobiologia e lotte politiche della travestilità in Brasile e America Latina.",
        "lang_switch_label": "LINGUA:"
    },
    "ru": {
        "title": "Травести / Travesti (гендерная и политическая идентичность)",
        "brand_badge": "🏳️‍⚧️ САМООПРЕДЕЛЕНИЕ",
        "hero_tape": "TRAVESTI ЖИВЁТ // САМООПРЕДЕЛЕНИЕ // НЕ МАСКАРАД // ПОЛИТИЧЕСКОЕ СУЩЕСТВИТЕЛЬНОЕ",
        "hero_tag": "ПОЛИТИЧЕСКИЙ МАНИФЕСТ И ИСТОРИОГРАФИЯ",
        "hero_sub": "Латиноамериканская гендерная и политическая идентичность, отмеченная самоопределением, уличным сопротивлением и непереводимостью.",
        "stamp": "ПОЛИТИЧЕСКОЕ СУЩЕСТВИТЕЛЬНОЕ • НЕПЕРЕВОДИМО • НЕ МАСКАРАД",
        "footer_l1": "С гордостью создано <a href=\"https://travesti.2lp.in/ru/\">латиноамериканской travesti</a> 🏳️‍⚧️ :)",
        "footer_l2": f"Travesti v{APP_VERSION} • от <a href=\"https://lumen.pink\">Lumen Pink</a> • {BUILD_TIMESTAMP} • Бразилия 🇧🇷 • <a href=\"https://creativecommons.org/licenses/by-sa/4.0\">CC-BY-SA-4.0</a>",
        "meta_desc": "История, этимология, диссидентская теория, нейробиология и политическая борьба травести в Бразилии и Латинской Америке.",
        "lang_switch_label": "ЯЗЫК:"
    },
    "zh": {
        "title": "Travesti (性别认同与政治身份)",
        "brand_badge": "🏳️‍⚧️ 身体自主",
        "hero_tape": "TRAVESTI 存在 // 身体自主 // 绝非伪装 // 政治名词",
        "hero_tag": "政治宣言与历史档案",
        "hero_sub": "拉丁美洲特有的性别与政治身份，以身体自主、街头抗争与不可直接翻译的文化特异性为标志。",
        "stamp": "政治名词 • 无法翻译 • 绝非变装游戏",
        "footer_l1": "由一位<a href=\"https://travesti.2lp.in/zh/\">拉美 travesti</a> 自豪制作 🏳️‍⚧️ :)",
        "footer_l2": f"Travesti v{APP_VERSION} • 来自 <a href=\"https://lumen.pink\">Lumen Pink</a> • {BUILD_TIMESTAMP} • 巴西 🇧🇷 • <a href=\"https://creativecommons.org/licenses/by-sa/4.0\">CC-BY-SA-4.0</a>",
        "meta_desc": "巴西与拉丁美洲 travesti 的历史斗争、词源考证、身体理论、神经生物学及反殖民抗争。",
        "lang_switch_label": "语言 / LANGUAGE:"
    },
    "ja": {
        "title": "Travesti / トラヴェスティ (ジェンダーと政治のアイデンティティ)",
        "brand_badge": "🏳️‍⚧️ 自己決定",
        "hero_tape": "TRAVESTI は生きている // 自己決定 // 単なる変装ではない // 政治的名詞",
        "hero_tag": "政治宣言と歴史記録",
        "hero_sub": "ラテンアメリカ独自のジェンダー・政治アイデンティティ。自己決定、路上での抵抗、他言語への安易な翻訳を拒絶する自律的な概念。",
        "stamp": "政治的名詞 • 翻訳不可能 • 単なる変装ではない",
        "footer_l1": "<a href=\"https://travesti.2lp.in/ja/\">ラテンアメリカの travesti</a> によって誇りを持って制作されました 🏳️‍⚧️ :)",
        "footer_l2": f"Travesti v{APP_VERSION} • 制作: <a href=\"https://lumen.pink\">Lumen Pink</a> • {BUILD_TIMESTAMP} • ブラジル 🇧🇷 • <a href=\"https://creativecommons.org/licenses/by-sa/4.0\">CC-BY-SA-4.0</a>",
        "meta_desc": "ブラジルおよびラテンアメリカにおける travesti の歴史、語源、異見理論、神经生物学、路上闘争の記録。",
        "lang_switch_label": "言語 / LANGUAGE:"
    },
    "ar": {
        "title": "ترافيستي / Travesti (الهوية الجندرية والسياسية)",
        "brand_badge": "🏳️‍⚧️ تقرير المصير",
        "hero_tape": "TRAVESTI تحيا // تقرير المصير // لسنا تنكراً // اسم سياسي",
        "hero_tag": "بيان سياسي وتأريخ نضالي",
        "hero_sub": "هوية جندرية وسياسية لاتينية أصيلة تتسم بتقرير المصير، ومقاومة الشوارع، وعدم قابليتها للترجمة الحرفية للغات الاستعمارية.",
        "stamp": "اسم سياسي • غير قابل للترجمة • لسنا تنكراً",
        "footer_l1": "صُنع بكل فخر بواسطة <a href=\"https://travesti.2lp.in/ar/\">travesti أمريكية لاتينية</a> 🏳️‍⚧️ :)",
        "footer_l2": f"Travesti v{APP_VERSION} • بواسطة <a href=\"https://lumen.pink\">Lumen Pink</a> • {BUILD_TIMESTAMP} • البرازيل 🇧🇷 • <a href=\"https://creativecommons.org/licenses/by-sa/4.0\">CC-BY-SA-4.0</a>",
        "meta_desc": "تاريخ وهوية ونضال travesti في البرازيل وأمريكا اللاتينية، من علم الأعصاب إلى نظرية الجندر المقاومة للاستعمار.",
        "lang_switch_label": "اللغة:"
    }
}

PHOTOS = {
    "Orgulho_Trans_Travesti_Congresso_Nacional.jpg": {
        "caption_pt": "Projeção mapeada no Congresso Nacional em Brasília em alusão ao Dia Nacional do Orgulho Trans e Travesti. (Foto: Agência Senado / Flickr, 15/05/2024. Licença: CC BY-SA 4.0)",
        "caption_en": "Projection mapped onto the National Congress in Brasília for National Trans and Travesti Pride Day. (Photo: Agência Senado / Flickr, May 15, 2024. License: CC BY-SA 4.0)",
        "caption_es": "Proyección cartográfica en el Congreso Nacional en Brasilia por el Día Nacional del Orgullo Trans y Travesti. (Foto: Agência Senado / Flickr, 15/05/2024. Licencia: CC BY-SA 4.0)",
        "caption_fr": "Projection sur le Congrès national à Brasilia pour la Journée nationale de la fierté trans et travesti. (Photo: Agência Senado, 2024. CC BY-SA 4.0)",
        "caption_de": "Lichtprojektion am Nationalkongress in Brasília anlässlich des Trans- und Travesti-Stolztages. (Foto: Agência Senado, 2024. CC BY-SA 4.0)",
        "caption_it": "Proiezione sul Congresso Nazionale a Brasilia in occasione della Giornata Nazionale dell'Orgoglio Trans e Travesti. (Foto: Agência Senado, 2024. CC BY-SA 4.0)",
        "caption_ru": "Проекция на здание Национального конгресса в Бразилиа в честь Дня гордости транс- и travesti-людей. (Фото: Agência Senado, 2024. CC BY-SA 4.0)",
        "caption_zh": "巴西利亚国家国会大厦建筑投影，纪念全国跨性别者与 Travesti 骄傲日。(摄影: Agência Senado, 2024. 授权: CC BY-SA 4.0)",
        "caption_ja": "ブラジリアの連邦議会議事堂に投影された「トランス＆トラヴェスティ・プライド・デー」の光のメッセージ。(写真: 上院通信社, 2024. CC BY-SA 4.0)",
        "caption_ar": "إضاءة مبنى الكونغرس الوطني في برازيليا بمناسبة اليوم الوطني للفخر بالهوية العابرة وTravesti. (تصوير: وكالة مجلس الشيوخ، 2024. ترخيص: CC BY-SA 4.0)"
    },
    "Angela_Davis_2019.jpg": {
        "caption_pt": "Angela Davis em conferência sobre abolicionismo penal, direitos humanos e libertação travesti e trans. (Foto: Oregon State University / Flickr, 01/04/2019. CC BY-SA 2.0)",
        "caption_en": "Angela Davis speaking on prison abolition, human rights, and solidarity with trans and travesti liberation. (Photo: Oregon State University, 2019. CC BY-SA 2.0)",
        "caption_es": "Angela Davis disertando sobre abolicionismo penal, derechos humanos y liberación travesti y trans. (Foto: Oregon State University, 2019. CC BY-SA 2.0)",
        "caption_fr": "Angela Davis s'exprimant sur l'abolitionnisme carcéral et la libération travesti et trans. (Photo: Oregon State University, 2019. CC BY-SA 2.0)",
        "caption_de": "Angela Davis bei einem Vortrag über Gefängnisabschaffung und die Befreiung von Trans- und Travesti-Menschen. (Foto: Oregon State University, 2019. CC BY-SA 2.0)",
        "caption_it": "Angela Davis parla di abolizionismo carcerario e liberazione travesti e trans. (Foto: Oregon State University, 2019. CC BY-SA 2.0)",
        "caption_ru": "Анджела Дэвис выступает с речью об аболиционизме пенитенциарной системы и освобождении travesti и транс-людей. (Фото: Oregon State Univ, 2019. CC BY-SA 2.0)",
        "caption_zh": "安吉拉·戴维斯就废除监狱制度、人权以及声援跨性别与 travesti 解放运动发表演讲。(摄影: 俄勒冈州立大学, 2019. CC BY-SA 2.0)",
        "caption_ja": "アンジェラ・デイヴィス：刑務所廃止論、人権、そしてトラヴェスティとトランスの解放への連帯を語る。(写真: オレゴン州立大学, 2019. CC BY-SA 2.0)",
        "caption_ar": "أنجيلا ديفيس تتحدث عن إلغاء السجون وحقوق الإنسان والتضامن مع تحرير travesti والعابرات. (تصوير: جامعة ولاية أوريغون، 2019. ترخيص: CC BY-SA 2.0)"
    },
    "IV_ENTLAIDS_1996_Katia_Tapety.jpg": {
        "caption_pt": "Kátia Tapety (ao centro) e lideranças travestis durante o IV ENTLAIDS em Curitiba (1996) — gênese da ANTRA. (Acervo Keila Simpson / SciELO)",
        "caption_en": "Kátia Tapety (center) and travesti leaders during IV ENTLAIDS in Curitiba (1996) — founding moment of ANTRA. (Keila Simpson Collection / SciELO)",
        "caption_es": "Kátia Tapety (centro) y líderes travestis en el IV ENTLAIDS en Curitiba (1996) — génesis de ANTRA. (Archivo Keila Simpson / SciELO)",
        "caption_fr": "Kátia Tapety (au centre) et les leaders travestis lors du IVe ENTLAIDS à Curitiba (1996) — fondation de l'ANTRA. (Coll. Keila Simpson)",
        "caption_de": "Kátia Tapety (Mitte) und Travesti-Aktivistinnen beim IV. ENTLAIDS in Curitiba (1996) — Gründung von ANTRA. (Sammlung Keila Simpson)",
        "caption_it": "Kátia Tapety (al centro) e le leader travesti al IV ENTLAIDS a Curitiba (1996) — nascita di ANTRA. (Archivio Keila Simpson)",
        "caption_ru": "Катия Тапети (в центре) и лидеры travesti во время IV ENTLAIDS в Куритибе (1996) — создание ANTRA. (Архив Keila Simpson)",
        "caption_zh": "卡蒂亚·塔佩蒂 (中) 与多位 travesti 运动领袖于 1996 年库里蒂巴第四届 ENTLAIDS 会议 — ANTRA 诞生之基石。(收藏: Keila Simpson)",
        "caption_ja": "カティア・タペティ（中央）とトラヴェスティの指導者たち（1996年クリチバ、第4回ENTLAIDS）— ANTRA創設の瞬間。(ケイラ・シンプソン所蔵)",
        "caption_ar": "كاتيا تابيتي (في الوسط) وقائدات travesti خلال المؤتمر الوطني الرابع في كوريتيبا (1996) — تأسيس رابطة ANTRA. (أرشيف كيلا سيمبسون)"
    },
    "Erika_Hilton_Camara_2024.jpg": {
        "caption_pt": "A deputada federal Erika Hilton em pronunciamento na Câmara dos Deputados em Brasília. (Foto: Zeca Ribeiro / Câmara dos Deputados, 2024. CC BY 3.0)",
        "caption_en": "Federal Deputy Erika Hilton speaking at the Chamber of Deputies in Brasília. (Photo: Zeca Ribeiro / Chamber of Deputies, 2024. CC BY 3.0)",
        "caption_es": "La diputada federal Erika Hilton en un discurso en la Cámara de Diputados en Brasilia. (Foto: Zeca Ribeiro, 2024. CC BY 3.0)",
        "caption_fr": "La députée fédérale Erika Hilton s'exprimant à la Chambre des députés à Brasilia. (Photo: Zeca Ribeiro, 2024. CC BY 3.0)",
        "caption_de": "Die Bundesabgeordnete Erika Hilton spricht in der Abgeordnetenkammer in Brasília. (Foto: Zeca Ribeiro, 2024. CC BY 3.0)",
        "caption_it": "La deputata federale Erika Hilton parla alla Camera dei Deputati a Brasilia. (Foto: Zeca Ribeiro, 2024. CC BY 3.0)",
        "caption_ru": "Федеральный депутат Эрика Хилтон выступает в Палате депутатов в Бразилиа. (Фото: Zeca Ribeiro, 2024. CC BY 3.0)",
        "caption_zh": "联邦众议员埃丽卡·希尔顿在巴西利亚众议院发表讲话。(摄影: Zeca Ribeiro, 2024. 授权: CC BY 3.0)",
        "caption_ja": "ブラジリアの下院本会議で発言する連邦下院議員エリカ・ヒルトン。(写真: ゼカ・リベイロ, 2024. CC BY 3.0)",
        "caption_ar": "النائبة الفيدرالية إريكا هيلتون تلقي كلمة في مجلس النواب في برازيليا. (تصوير: زيكا ريبيرو، 2024. ترخيص: CC BY 3.0)"
    },
    "Lohana_Berkins_e_Maria_Belen_Correa.jpg": {
        "caption_pt": "Lohana Berkins e María Belén Correa marchando pelos direitos civis travestis e revogação dos éditos policiais em Buenos Aires. (Arquivo Histórico Travesti)",
        "caption_en": "Lohana Berkins and María Belén Correa marching for travesti civil rights and against police edicts in Buenos Aires. (Travesti Historical Archive)",
        "caption_es": "Lohana Berkins y María Belén Correa marchando por los derechos civiles travestis y derogación de los edictos policiales en Buenos Aires. (Archivo Histórico Travesti)",
        "caption_fr": "Lohana Berkins et María Belén Correa manifestant pour les droits civils travestis à Buenos Aires. (Archives Historiques Travesti)",
        "caption_de": "Lohana Berkins und María Belén Correa bei einer Demonstration für Travesti-Bürgerrechte in Buenos Aires. (Travesti-Geschichtsarchiv)",
        "caption_it": "Lohana Berkins e María Belén Correa manifestano per i diritti civili travesti a Buenos Aires. (Archivio Storico Travesti)",
        "caption_ru": "Лохана Беркинс и Мария Белен Корреа на марше за гражданские права travesti в Буэнос-Айресе. (Исторический архив Travesti)",
        "caption_zh": "洛哈娜·贝尔金斯与玛丽亚·贝伦·科雷亚在布宜诺斯艾利斯街头游行，争取 travesti 公民权利并废除警方治安法令。(历史档案)",
        "caption_ja": "ブエノスアイレスで警察令の撤廃とトラヴェスティの権利を求めて行進するロハナ・ベルキンスとマリア・ベレン・コレア。(トラヴェスティ歴史資料館)",
        "caption_ar": "لوهانا بيركينز وماريا بيلين كوريا تتظاهران في بوينس آيرس للمطالبة بحقوق travesti المدنية وإلغاء المراسيم البوليسية. (الأرشيف التاريخي)"
    },
    "Susy_Shock.jpg": {
        "caption_pt": "Susy Shock, poeta e performer argentina: 'Reivindico meu direito de ser um monstro'. (Foto: Divulgação Cultural)",
        "caption_en": "Susy Shock, Argentine poet and performer: 'I claim my right to be a monster'. (Cultural Archive)",
        "caption_es": "Susy Shock, poeta y performer argentina: 'Reivindico mi derecho a ser un monstruo'. (Archivo Cultural)",
        "caption_fr": "Susy Shock, poète et performeuse argentine: 'Je revendique mon droit d'être un monstre'. (Archives Culturelles)",
        "caption_de": "Susy Shock, argentinische Dichterin und Performerin: 'Ich fordere mein Recht, ein Monster zu sein'. (Kulturarchiv)",
        "caption_it": "Susy Shock, poetessa e performer argentina: 'Rivendico il mio diritto di essere un mostro'. (Archivio Culturale)",
        "caption_ru": "Суси Шок, аргентинская поэтесса и перформер: 'Я требую свое право быть монстром'. (Культурный архив)",
        "caption_zh": "苏西·肖克，阿根廷诗人与行为艺术家：“我捍卫我成为怪物的权利”。(文化档案)",
        "caption_ja": "スージー・ショック（アルゼンチンの詩人・パフォーマー）：「私はモンスターである権利を主張する」。(文化資料)",
        "caption_ar": "سوزي شوك، الشاعرة والمؤدية الأرجنتينية: 'أطالب بحقي في أن أكون وحشاً'. (الأرشيف الثقافي)"
    }
}

def convert_markdown_body(raw_md, lang_code, is_root=False):
    # 1. Remove metadados YAML do Obsidian
    text = re.sub(r'^---[\s\S]*?---\s*', '', raw_md)

    # 2. Remove o H1 inicial (já exibido no Hero)
    text = re.sub(r'^#\s+Travesti[^\n]*\n+', '', text)

    # 3. TRATA AS IMAGENS DO OBSIDIAN PRIMEIRO (Evita que o regex de links destrua ![[img]])
    # Absorve também as linhas de legenda em itálico que sucedem imediatamente a imagem
    asset_prefix = "assets/" if is_root else "../assets/"
    for photo_name, photo_data in PHOTOS.items():
        caption = photo_data.get(f"caption_{lang_code}", photo_data["caption_pt"])
        pattern = rf'!\[\[{re.escape(photo_name)}(?:\|\d+)?\]\](?:\s*\n\*[^\n]+\*)*'
        replacement = f'''
<div class="photo-street-frame">
    <img src="{asset_prefix}{photo_name}" alt="{caption}" class="photo-street-img" loading="lazy">
    <div class="photo-street-caption">
        <strong>{caption.split('(')[0].strip()}</strong><br>
        <span>{'(' + caption.split('(')[1] if '(' in caption else ''}</span>
    </div>
</div>
'''
        text = re.sub(pattern, replacement, text)

    # 4. Trata links internos do Obsidian [[Link|Texto]] e [[Link]]
    text = re.sub(r'\[\[([^|\]]+)\|([^\]]+)\]\]', r'\2', text)
    text = re.sub(r'\[\[([^\]]+)\]\]', r'\1', text)

    # 5. Converte Callouts do Obsidian (> [!info] ...) com markdown interno limpo
    def render_callout(m):
        header_text = m.group(1).replace('*', '').strip()
        body_lines = [re.sub(r'^>\s?', '', l) for l in m.group(2).strip().split('\n')]
        body_md = '\n'.join(body_lines)
        body_conv = markdown.markdown(body_md, extensions=['extra', 'sane_lists'])
        return f'\n<div class="tarja-choque-preta">\n<strong>★ {header_text}</strong>\n{body_conv}\n</div>\n'

    text = re.sub(r'>\s*\[!info\]\s*([^\n]+)\n((?:>[^\n]*\n?)*)', render_callout, text)

    # 6. Processa através da biblioteca oficial Python Markdown
    md_parser = markdown.Markdown(extensions=[
        'extra',
        'sane_lists',
        'tables',
        'smarty'
    ])
    html = md_parser.convert(text)

    # 7. Pós-processa o HTML para adicionar as classes de Anti-Design e Papel Rasgado
    # Divide pelas tags <h2> e embrulha cada seção em <section class="paper-section...">
    parts = re.split(r'(<h2>.*?</h2>)', html)
    
    out_html = []
    current_sec = []
    sec_idx = 0
    
    # Processa introdução (antes do primeiro <h2>)
    if parts and not parts[0].strip().startswith('<h2'):
        intro_html = parts.pop(0)
        out_html.append(f'<section class="paper-section">{intro_html}</section>')
    
    i = 0
    while i < len(parts):
        h2_tag = parts[i]
        sec_body = parts[i+1] if i+1 < len(parts) else ""
        sec_idx += 1
        is_torn = (sec_idx % 2 == 1)
        sec_class = "paper-section torn-paper" if is_torn else "paper-section"
        out_html.append(f'<section class="{sec_class}">\n{h2_tag}\n{sec_body}\n</section>')
        i += 2

    return '\n'.join(out_html)

def build_language_page(lang_code, raw_md, is_root=False):
    lang_info = next(l for l in LANGS if l["code"] == lang_code)
    i18n = I18N[lang_code]
    direction = lang_info["dir"]

    # Constrói a fita de idiomas
    lang_items_html = []
    rotations = [-2, 1, -1, 3, -2, 2, -1, 1, -3, 2]
    for idx, l in enumerate(LANGS):
        active_cls = "active" if l["code"] == lang_code else ""
        href = f"../{l['code']}/" if not is_root else f"{l['code']}/"
        lang_items_html.append(f'<a href="{href}" class="lang-tape-item {active_cls}" style="--rot:{rotations[idx]};">{l["code"].upper()}</a>')

    langs_bar_html = '\n'.join(lang_items_html)

    # Converte o conteúdo do artigo
    body_content = convert_markdown_body(raw_md, lang_code, is_root=is_root)

    # Nota de tradução para outras línguas
    note_intl = ""
    if lang_code != "pt":
        note_intl = f'''
        <div class="tarja-choque-preta" style="border-left-color: var(--cor-amarelo-manifesto); margin-bottom: 30px;">
            <strong>★ TRANSLATION &amp; CONTEXTUAL NOTE ({lang_info["name"].upper()}):</strong><br>
            The term <em>travesti</em> is a South American gender, political and cultural identity with deep roots in street resistance, transfeminism and anti-colonial history. It cannot be reduced to Western or Anglo-Saxon categories such as "trans woman" or "crossdresser". In this edition, <em>travesti</em> remains in its authentic original spelling as an act of political self-determination.
        </div>
        '''

    asset_css = "assets/style.css" if is_root else "../assets/style.css"

    page_html = f'''<!DOCTYPE html>
<html lang="{lang_code}" dir="{direction}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{i18n["title"]} — travesti.2lp.in</title>
    <meta name="description" content="{i18n["meta_desc"]}">
    
    <!-- Open Graph & Twitter Cards -->
    <meta property="og:title" content="{i18n["title"]}">
    <meta property="og:description" content="{i18n["meta_desc"]}">
    <meta property="og:image" content="https://travesti.2lp.in/assets/Orgulho_Trans_Travesti_Congresso_Nacional.jpg">
    <meta property="og:type" content="article">
    <meta property="og:url" content="https://travesti.2lp.in/{lang_code}/">
    <meta name="twitter:card" content="summary_large_image">
    
    <!-- Links Canônicos Multilíngues (Norma GOST) -->
    <link rel="canonical" href="https://travesti.2lp.in/{lang_code}/">
    {' '.join([f'<link rel="alternate" hreflang="{l["code"]}" href="https://travesti.2lp.in/{l["code"]}/">' for l in LANGS])}
    <link rel="alternate" hreflang="x-default" href="https://travesti.2lp.in/">

    <link rel="stylesheet" href="{asset_css}?v={BUILD_ID}">
</head>
<body>
    <!-- Barra Superior de Fita Adesiva -->
    <nav class="top-tape-bar" aria-label="Seletor de Idiomas">
        <div class="tape-brand">
            <span>TRAVESTI.2LP.IN</span>
            <span class="badge-trans">{i18n["brand_badge"]}</span>
        </div>
        <div class="lang-selector-tape">
            <span style="font-family: 'Space Mono', monospace; font-size: 11px; color: #aaa; align-self: center; margin-right: 6px;">{i18n["lang_switch_label"]}</span>
            {langs_bar_html}
        </div>
    </nav>

    <!-- Conteúdo Zine Anti-Design -->
    <main class="zine-container">
        <!-- Capa / Manchete de Choque com Duct Tape Além da Borda -->
        <div class="hero-wrapper">
            <div class="duct-tape">{i18n["hero_tape"]}</div>
            <header class="hero-zine-cover">
                <div class="zine-tag-insurgente">{i18n["hero_tag"]}</div>
                <h1 class="hero-title-glitch">TRAVESTI</h1>
                <div class="hero-subtitle-manifesto">{i18n["hero_sub"]}</div>
                <div class="stamp-box">{i18n["stamp"]}</div>
            </header>
        </div>

        {note_intl}

        <!-- Corpo do Ensaio com Rasgos e Intervenções -->
        <article class="article-zine-body">
            {body_content}
        </article>
    </main>

    <!-- Rodapé Canônico em 2 Linhas (Perfil Lumen // Norma GOST) -->
    <footer class="lumen-footer-canonical">
        <div class="footer-line-1">
            {i18n["footer_l1"]}
        </div>
        <div class="footer-line-2">
            {i18n["footer_l2"]}
        </div>
    </footer>
</body>
</html>
'''
    return page_html

def main():
    print(f"Lendo artigo de {OBSIDIAN_MD}...")
    with open(OBSIDIAN_MD, 'r', encoding='utf-8') as f:
        raw_md = f.read()

    # Gera cada pasta de língua: site/<lang>/index.html
    for lang in LANGS:
        code = lang["code"]
        lang_dir = os.path.join(SITE_DIR, code)
        os.makedirs(lang_dir, exist_ok=True)
        html = build_language_page(code, raw_md, is_root=False)
        out_path = os.path.join(lang_dir, "index.html")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"✓ Gerada página para '{code}': site/{code}/index.html")

    # Gera a raiz site/index.html como roteador cliente e fallback para pt
    root_html = build_language_page("pt", raw_md, is_root=True)
    router_script = """
    <script>
        // Roteamento inteligente de idioma (Norma GOST)
        (function() {
            var saved = localStorage.getItem('travesti_lang');
            if (saved && saved !== 'pt') {
                window.location.replace('/' + saved + '/');
                return;
            }
            if (!saved) {
                var navLang = (navigator.language || navigator.userLanguage || '').toLowerCase();
                var supported = ['pt', 'en', 'es', 'fr', 'de', 'it', 'ru', 'zh', 'ja', 'ar'];
                for (var i = 0; i < supported.length; i++) {
                    if (navLang.indexOf(supported[i]) === 0 && supported[i] !== 'pt') {
                        window.location.replace('/' + supported[i] + '/');
                        return;
                    }
                }
            }
        })();
    </script>
    """
    root_html = root_html.replace('</head>', router_script + '\n</head>')
    
    with open(os.path.join(SITE_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(root_html)
    print("✓ Gerada raiz inteligente: site/index.html")

if __name__ == "__main__":
    main()
