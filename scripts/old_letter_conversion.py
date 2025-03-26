from pathlib import Path
import argparse

lengthmarks_w_z = {
    # "ŗ": "r",
    # "Ŗ": "R",

# Ā
    "ah": "ā",
    "â": "ā",
    "à": "ā",
    "á": "ā",
    "ä": "ā",

# Ē
    "eh": "ē",
    "ê": "ē",
    "è": "ē",
    "é": "ē",
    "ë": "ē",

# Ī
    "ih": "ī",
    "î": "ī",
    "ì": "ī",
    "í": "ī",
    "ï": "ī",

# O
    "ô": "o",
    "ò": "o",
    "ó": "o",
    "ö": "o",
    "oh": "o",

# Ū
    "uh": "ū",
    "û": "ū",
    "ù": "ū",
    "ú": "ū",
    "ü": "ū",

# W, Z
    "w": "v",
    "z": "c",
}

z_cap = {
    "S ": "┌■",
    "S,": "┌²",
    "S.": "┌³",
    "S:": "┌¹",
    "S:": "┌·",
    "S!": "┌°",
    "S?": "┌┘",
    "S*": "┌×",
    "S/": "┌¤",
    "S»": "┌▓",
    'S"': '┌│',
    "S”": "┌┤",
    "S'": "┌┴",
    "S)": "┌├",
    "S-": "┌┬",

    "S": "Z",

    "┌■": "S ",
    "┌²": "S,",
    "┌³": "S.",
    "┌¹": "S:",
    "┌·": "S:",
    "┌°": "S!",
    "┌┘": "S?",
    "┌×": "S*",
    "┌¤": "S/",
    "┌▓": "S»",
    '┌│': 'S"',
    "┌┤": "S”",
    "┌┴": "S'",
    "┌├": "S)",
    "┌┬": "S-",
}

st_tzch_exc = {
    "greezt": "▲¶",
    "īdzt": "▲↨",
    "areizt": "▲↓",
    "lauzt": "▲←",  # Klauztiņš (no Gulbja Pēc 100 g.)

    # atžirgt, grāmatžurnāls/politžurnāls
    "atzchir": "▲▀",
    "tzchurn": "▲▄",
}

s_š_č = {
    "ş": "s",
    "tatsch": "tač",
    "atsch": "atš",
    "tsch": "č",
    "sch": "š",
}

prefixes = {
# UZ
    " us": " uz",
    "/us": "/uz",
    "«us": "«uz",
    '"us': '"uz',
    "„us": "„uz",
    "'us": "'uz",
    "(us": "(uz",
    "-us": "-uz",

# NEUZ
    " neus": " neuz",
    "/neus": "/neuz",
    "«neus": "«neuz",
    '"neus': '"neuz',
    "„neus": "„neuz",
    "'neus": "'neuz",
    "(neus": "(neuz",
    "-neus": "-neuz",

# JĀUZ
    " jāus": " jāuz",
    "/jāus": "/jāuz",
    "«jāus": "«jāuz",
    '"jāus': '"jāuz',
    "„jāus": "„jāuz",
    "'jāus": "'jāuz",
    "(jāus": "(jāuz",
    "-jāus": "-jāuz",

# IZ
    " is": " iz",
    "/is": "/iz",
    "«is": "«iz",
    '"is': '"iz',
    "„is": "„iz",
    "'is": "'iz",
    "(is": "(iz",
    "-is": "-iz",

# NEIZ
    " neis": " neiz",
    "/neis": "/neiz",
    "«neis": "«neiz",
    '"neis': '"neiz',
    "„neis": "„neiz",
    "'neis": "'neiz",
    "(neis": "(neiz",
    "-neis": "-neiz",

# JĀIZ
    " jāis": " jāiz",
    "/jāis": "/jāiz",
    "«jāis": "«jāiz",
    '"jāis': '"jāiz',
    "„jāis": "„jāiz",
    "'jāis": "'jāiz",
    "(jāis": "(jāiz",
    "-jāis": "-jāiz",

# AIZ
    " ais": " aiz",
    "/ais": "/aiz",
    "«ais": "«aiz",
    '"ais': '"aiz',
    "„ais": "„aiz",
    "'ais": "'aiz",
    "(ais": "(aiz",
    "-ais": "-aiz",

# NEAIZ
    " neais": " neaiz",
    "/neais": "/neaiz",
    "«neais": "«neaiz",
    '"neais': '"neaiz',
    "„neais": "„neaiz",
    "'neais": "'neaiz",
    "(neais": "(neaiz",
    "-neais": "-neaiz",

# JĀAIZ
    " jāais": " jāaiz",
    "/jāais": "/jāaiz",
    "«jāais": "«jāaiz",
    '"jāais': '"jāaiz',
    "„jāais": "„jāaiz",
    "'jāais": "'jāaiz",
    "(jāais": "(jāaiz",
    "-jāais": "-jāaiz",


# BEZ
    " bes": " bez",
    "/bes": "/bez",
    "«bes": "«bez",
    '"bes': '"bez',
    "„bes": "„bez",
    "'bes": "'bez",
    "(bes": "(bez",
    "-bes": "-bez",

    "iztab": "istab",
    "aizberg": "aisberg",
}

ee_exc = {
    "neeee!": "☼☺",
    "neee!": "☼☻",
    " nee!": "☼♣",
    "/nee!": "☼♠",
    "«nee!": "☼•",
    '"nee!': "☼◘",
    "„nee!": "☼○",
    "'nee!": "☼◙",
    "(nee!": "☼♂",
    "-nee!": "☼♀",

    "neeeee": "☼♪", # neieie

    "neeee": "☼╬",
    "eeee": "☼═", # ieie

    "neee": "☼╠", # neie
    "iee": "☼╦",

    # neesmu, neej, neefektīvs, neelpo, neecēt
    " nees": "♫♥",
    "/nees": "♫♦",
    "«nees": "♫♣",
    '"nees': "♫♠",
    "„nees": "♫•",
    "'nees": "♫◘",
    "(nees": "♫○",
    "-nees": "♫◙",

    " neej": "►♥",
    "/neej": "►♦",
    "«neej": "►♣",
    '"neej': "►♠",
    "„neej": "►•",
    "'neej": "►◘",
    "(neej": "►○",
    "-neej": "►◙",

    " neef": "◄♥",
    "/neef": "◄♦",
    "«neef": "◄♣",
    '"neef': "◄♠",
    "„neef": "◄•",
    "'neef": "◄◘",
    "(neef": "◄○",
    "-neef": "◄◙",

    " neel": "↕♥",
    "/neel": "↕♦",
    "«neel": "↕♣",
    '"neel': "↕♠",
    "„neel": "↕•",
    "'neel": "↕◘",
    "(neel": "↕○",
    "-neel": "↕◙",

    " neecē": "‼♥",
    "/neecē": "‼♦",
    "«neecē": "‼♣",
    '"neecē': "‼♠",
    "„neecē": "‼•",
    "'neecē": "‼◘",
    "(neecē": "‼○",
    "-neecē": "‼◙",

    # neekranizēts, neekvivalents, neekvadoras/toriāls, neekonomiski, neekoloģiski, neeksistē
    "eekrani": "¶☺",
    "eekviv": "¶☻",
    "eekva": "¶♥",
    "eekono": "¶♦",
    "eekol": "¶♠",
    "eeksis": "¶♣",
}

def transform(text, change_S_to_Z=True, ee_only=False):
    text = " " + text + " "
    # \n, \t
    text = text.replace("\n", " 🤯 ")
    text = text.replace("\t", " 📏 ")


    if ee_only:
            for key, value in ee_exc.items():
                    text = text.replace(key.upper(), value+"§")
                    text = text.replace(key.title(), value+"╩")
                    text = text.replace(key, value+"╔")

            text = text.replace("EE", "IE")
            text = text.replace("Ee", "Ie")
            text = text.replace("ee", "ie")

            for key, value in {"☼♪": "neieie", "☼╬": "neiee", "☼═": "ieie", "☼╠": "neie"}.items():
                    text = text.replace(key+"§", value.upper())
                    text = text.replace(key+"╩", value.title())
                    text = text.replace(key+"╔", value)
            for key, value in ee_exc.items():
                    text = text.replace(value+"§", key.upper())
                    text = text.replace(value+"╩", key.title())
                    text = text.replace(value+"╔", key)

            # \n, \t
            text = text.replace(" 🤯 ", "\n")
            text = text.replace(" 📏 ", "\t")
            return text.strip()


    # Ā, Ē, Ī, Ō, Ū, W, Z
    for key, value in lengthmarks_w_z.items():
            text = text.replace(key.upper(), value.upper())
            if len(key) > 1:
                    text = text.replace(key.title(), value.title())
            text = text.replace(key, value)

    if change_S_to_Z:
        for key, value in z_cap.items():
                text = text.replace(key, value)

    # Z, Ž, Č, ST
    text = text.replace("ſ", "z")
    for key, value in st_tzch_exc.items():
            text = text.replace(key.upper(), value+"▌")
            text = text.replace(key.title(), value+"▐")
            text = text.replace(key, value+"▬")

    for key, value in {"zt": "st", "tatzch": "tač", "atzch": "atš", "tzch": "č", "zch": "ž"}.items():
            text = text.replace(key.upper(), value.upper())
            text = text.replace(key.title(), value.title())
            text = text.replace(key, value)

    for key, value in st_tzch_exc.items():
            text = text.replace(value+"▌", key.upper())
            text = text.replace(value+"▐", key.title())
            text = text.replace(value+"▬", key)
    # atžirgt, grāmatžurnāls/politžurnāls
    for key, value in {"tzchurn": "tžurn", "atzchir": "atžir"}.items():
            text = text.replace(key.upper(), value.upper())
            text = text.replace(key.title(), value.title())
            text = text.replace(key, value)

    # S, Š, Č
    text = text.replace("ẜ", "s")
    text = text.replace("Ꞩ", "S")
    for key, value in s_š_č.items():
            text = text.replace(key.upper(), value.upper())
            if len(key) > 1:
                    text = text.replace(key.title(), value.title())
            text = text.replace(key, value)

    # PREFIXES
    for key, value in prefixes.items():
            text = text.replace(key.upper(), value.upper())
            text = text.replace(key.title(), value.title())
            text = text.replace(key, value)

    # EE
    for key, value in ee_exc.items():
            text = text.replace(key.upper(), value+"§")
            text = text.replace(key.title(), value+"╩")
            text = text.replace(key, value+"╔")

    text = text.replace("EE", "IE")
    text = text.replace("Ee", "Ie")
    text = text.replace("ee", "ie")

    for key, value in {"☼♪": "neieie", "☼╬": "neiee", "☼═": "ieie", "☼╠": "neie"}.items():
            text = text.replace(key+"§", value.upper())
            text = text.replace(key+"╩", value.title())
            text = text.replace(key+"╔", value)
    for key, value in ee_exc.items():
            text = text.replace(value+"§", key.upper())
            text = text.replace(value+"╩", key.title())
            text = text.replace(value+"╔", key)

    # \n, \t
    text = text.replace(" 🤯 ", "\n")
    text = text.replace(" 📏 ", "\t")
    return text.strip()


def transform_files(in_dir, out_dir, ee_only, cap_s):
    for file in Path(in_dir).iterdir():
        text = file.read_text("utf8")
        old_header = text[:text.index("\n\n\n")].strip().splitlines()
        new_header = []
        for i in old_header:
            i = i if not i.startswith("normalization:") else "normalization: Pārveidots mūsdienu ortogrāfijā"
            new_header.append(i)

        text = text[text.find("\n\n"):].strip()
        text = transform(text, cap_s, ee_only) #"Ee" pārveidots par "ie"
        text = "\n".join(new_header) + "\n\n\n\n" + text

        with open(out_dir + "/" + file.name, "w", encoding="utf8") as out_file:
            out_file.write(text)
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Converts old Latvian letters")
    parser.add_argument(
        "-i",
        "--in_dir",
        default="vd_texts",
        type=str,
        help="Folder of files to convert",
    )
    parser.add_argument(
        "-o",
        "--out_dir",
        default="jd_texts",
        type=str,
        help="Folder where files will be saved",
    )
    parser.add_argument(
        "-ee",
        "--ee_only",
        default=False,
        type=bool,
        help="Convert only 'ee' to 'ie' in text",
    )
    parser.add_argument(
        "-s",
        "--cap_s",
        default=True,
        type=bool,
        help="Convert 'S' to 'Z' in text",
    )
    args = parser.parse_args()
    
    Path(args.out_dir).mkdir(exist_ok=True)
    transform_files(args.in_dir, args.out_dir, args.ee_only, args.cap_s)