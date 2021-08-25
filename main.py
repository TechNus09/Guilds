import os
import discord as d
import random
from datetime import date
from urllib.request import Request, urlopen
import json

skill = ['','-mining', '-smithing', '-woodcutting', '-crafting', '-fishing', '-cooking']
skills = ['combat','mining', 'smithing', 'woodcutting', 'crafting', 'fishing', 'cooking']

guilds_combat = {}
guilds_mining = {}
guilds_smithing = {}
guilds_woodcutting = {}
guilds_crafting = {}
guilds_fishing = {}
guilds_cooking = {}

guilds_counter  = {'IMMORTAL': 0, 'OWO': 0, 'EXP': 0, 'BRX': 0, 'RNG': 0, 'LAT': 0, 'KRG': 0, 'GGWP': 0, 'PVM': 0, 'DTF': 0, 'HSR': 0, 'FG': 0, 
                    'NS': 0, 'AOE': 0, 'NSFW': 0, 'DMG': 0, 'AXIAL': 0, 'PAK': 0, 'T62': 0, 'VLR': 0, 'RYU': 0, 'TI': 0, 'NSL': 0, '1HB': 0, 'FFA': 0,
                    'OG': 0, 'ORAZE': 0, 'BLITZ': 0, 'DTS': 0, 'SOLO': 0, 'BIG': 0, 'TRG': 0, 'CCCP': 0, 'TNT': 0, 'SOW': 0, 'PAPA': 0, 'TH': 0,
                    'EXC': 0, 'PHG': 0, 'SHORN': 0, 'TT': 0, 'UMBRA': 0, 'AK7': 0, 'GG': 0, 'LNH': 0, 'SLP': 0, 'DEAD': 0, 'TCK': 0, 'XP': 0, 
                    'VN': 0, 'XNW': 0, 'DARK': 0, 'FW': 0, 'DAVY': 0, 'DK': 0, 'II': 0, 'RW': 0, 'WG': 0, 'OL': 0, 'GOD': 0, 'YOUNG': 0, 'MAD': 0,
                    'ORDO': 0, 'LGN': 0, 'STEVE': 0, 'LOST': 0, 'LI': 0, 'GO': 0, 'LOLI': 0, 'PKMN': 0, 'GUN': 0, 'TAZ': 0, 'BH': 0, 'YT': 0,
                    'SYN': 0, 'NINJA': 0, 'ESP': 0, 'DR': 0, 'PK': 0, 'CW': 0, 'XD': 0, 'RS': 0, 'GOLEM': 0, 'IIAMA': 0, 'IL': 0, 'HANSA': 0, 'YAO': 
                    0, 'ST': 0, 'FLO': 0, 'SORRY': 0, 'AEVN': 0, 'MSA': 0, 'TROLL': 0, 'GW': 0, 'AROS': 0, 'GOKU': 0, 'YUZU': 0, 'GEAR': 0, 'IE': 0,
                    'WTH': 0, 'ACE': 0, 'RDS': 0, 'ROYAL': 0, 'KH': 0, 'FT': 0, 'TMG': 0, 'IY': 0, 'W3': 0, 'NEW': 0, 'TTT': 0, 'LT': 0, 'PW': 0,
                    'PAPPY': 0, '403': 0, 'KING': 0, 'FOX': 0, 'YSD': 0, 'NN': 0, 'MARIA': 0, 'OLD': 0, 'ROSE': 0, 'JESSA': 0, 'DAZZ': 0, 'SIR': 0,
                    'RP': 0, 'RSM': 0, '  ILY': 0, 'PWN': 0, 'IV': 0, 'VX': 0, 'ROBBY': 0, 'REN': 0, 'SNAKE': 0, 'GOUL': 0, 'FLOS': 0, 'LBX': 0,
                    'DN': 0, 'SG': 0, 'CUTE': 0, 'SUPER': 0, 'ETN': 0, 'BREAD': 0, 'YAMI': 0, 'GREEN': 0, 'VLOK': 0, 'CASH': 0, 'KAYN': 0, 'SV': 0,
                    'SIAPA': 0, 'KXNG': 0, 'ZERO': 0, 'DIMAS': 0, 'WHO': 0, 'TCM': 0, 'GLOW': 0, 'LDK': 0, 'LX': 0, 'KELLY': 0, 'JANG': 0, 'OLAZ': 0,
                    'THE': 0, 'DIPS': 0, 'GXB': 0, 'TITIT': 0, 'SMOL': 0, 'NEAL': 0, 'SOS': 0, 'FS': 0, 'R13': 0, 'WC2': 0, 'KENJI': 0, 
                    'AG': 0, 'ZIGG': 0, 'MFJ': 0, 'BLUE': 0, 'YAH': 0, 'BILL': 0, 'VAN': 0, 'SOY': 0, 'WAX': 0, 'FBI': 0, 'DUKE': 0, 'APEX': 0,
                    'OOPSY': 0, 'MEYO': 0, '666': 0, 'DADDY': 0, 'MINER': 0, 'NACHT': 0, 'EISA': 0, 'FRTK': 0, 'RRR': 0, 'FAJNA': 0, 'T2': 0,
                    'CFR': 0, 'ION': 0, 'MINI': 0, 'CAKE': 0, 'RANDO': 0, 'OLGA': 0, 'CAP': 0, 'CYCLO': 0, 'LE': 0, 'WAN': 0, 'LV': 0, 'YAN': 0,
                    'CP': 0, 'HMG': 0, 'RED': 0, 'BUZZ': 0, 'GR0': 0, 'A51': 0, 'ISMA': 0, 'THC': 0, 'C137': 0, 'LIAN': 0, 'RON': 0, 'NUB': 0, 'TNS': 0, 
                    'LUCKY': 0, 'SD': 0, 'QL': 0, 'EL': 0, 'DGG': 0, 'DEATH': 0, 'MELEE': 0, 'LQM': 0, 'RIVER': 0, 'KDA': 0, 'GODLY': 0, 'IG': 0, 
                    'AZURE': 0, 'ADNX': 0, 'AK47': 0, 'TETRA': 0, 'KVN': 0, 'BUD': 0, 'FAST': 0, 'CC': 0, 'HONEY': 0, 'YDS': 0, '63': 0, 'OMED': 0,
                    'PIXYZ': 0, 'KOA': 0, 'FROOT': 0, 'ANTI': 0, 'STILL': 0, 'YSO': 0, 'XPLOI': 0, 'BI': 0, 'MC': 0, 'IM': 0, 'LEMON': 0, 'MAOKI': 0,
                    'LEVEL': 0, 'MR': 0, 'THL': 0, 'SAD': 0, '1337': 0, 'ITCHY': 0, 'THOR': 0, 'ROTI': 0, 'WASON': 0, 'FLXW': 0, 'IT': 0, 'RAFA': 0,
                    'MAOU': 0, 'TEXAN': 0, 'HEDGE': 0, 'MLG': 0, 'ISC': 0, 'YOUR': 0, 'GOAT': 0, 'EA': 0, 'PRX': 0, 'OLY': 0, 'BLECK': 0, 'ADAM': 0,
                    'ERBO': 0, 'SZEPT': 0, 'BTW': 0, 'ENZA': 0, 'BL4CK': 0, 'GRB': 0, 'KYOU': 0, 'WORLD': 0, 'XDARK': 0, 'BR': 0, 'LUCAS': 0, 'XZ': 0,
                    'LIL': 0, 'ILI': 0, 'AI': 0, 'TOM': 0, 'CAPT': 0, 'MS': 0, 'LO': 0, 'BD': 0, 'FLOOR': 0, 'LOYAL': 0, 'TRULY': 0, 'AKUTO': 0,
                    'AKT': 0, 'TIGER': 0, 'VND': 0, 'SR': 0, 'GA': 0, 'DMN': 0, 'MANG': 0, 'GM': 0, 'WILL': 0, 'GOLD': 0, 'GK': 0, '808': 0,
                    'RICK': 0, 'ULTR': 0, 'KAMI': 0, 'QUAN': 0, 'FORST': 0, 'DWIKI': 0, 'LBCL': 0, 'EML': 0, 'HUONG': 0, 'AFK': 0, 'NO': 0,
                    'DUCKS': 0, 'XERRA': 0, 'THAT': 0, 'DJ': 0, 'TWO': 0}

guilds_counter_total  = {'IMMORTAL': 0, 'OWO': 0, 'EXP': 0, 'BRX': 0, 'RNG': 0, 'LAT': 0, 'KRG': 0, 'GGWP': 0, 'PVM': 0, 'DTF': 0, 'HSR': 0, 'FG': 0, 
                        'NS': 0, 'AOE': 0, 'NSFW': 0, 'DMG': 0, 'AXIAL': 0, 'PAK': 0, 'T62': 0, 'VLR': 0, 'RYU': 0, 'TI': 0, 'NSL': 0, '1HB': 0, 'FFA': 0,
                        'OG': 0, 'ORAZE': 0, 'BLITZ': 0, 'DTS': 0, 'SOLO': 0, 'BIG': 0, 'TRG': 0, 'CCCP': 0, 'TNT': 0, 'SOW': 0, 'PAPA': 0, 'TH': 0,
                        'EXC': 0, 'PHG': 0, 'SHORN': 0, 'TT': 0, 'UMBRA': 0, 'AK7': 0, 'GG': 0, 'LNH': 0, 'SLP': 0, 'DEAD': 0, 'TCK': 0, 'XP': 0, 
                        'VN': 0, 'XNW': 0, 'DARK': 0, 'FW': 0, 'DAVY': 0, 'DK': 0, 'II': 0, 'RW': 0, 'WG': 0, 'OL': 0, 'GOD': 0, 'YOUNG': 0, 'MAD': 0,
                        'ORDO': 0, 'LGN': 0, 'STEVE': 0, 'LOST': 0, 'LI': 0, 'GO': 0, 'LOLI': 0, 'PKMN': 0, 'GUN': 0, 'TAZ': 0, 'BH': 0, 'YT': 0,
                        'SYN': 0, 'NINJA': 0, 'ESP': 0, 'DR': 0, 'PK': 0, 'CW': 0, 'XD': 0, 'RS': 0, 'GOLEM': 0, 'IIAMA': 0, 'IL': 0, 'HANSA': 0, 'YAO': 
                        0, 'ST': 0, 'FLO': 0, 'SORRY': 0, 'AEVN': 0, 'MSA': 0, 'TROLL': 0, 'GW': 0, 'AROS': 0, 'GOKU': 0, 'YUZU': 0, 'GEAR': 0, 'IE': 0,
                        'WTH': 0, 'ACE': 0, 'RDS': 0, 'ROYAL': 0, 'KH': 0, 'FT': 0, 'TMG': 0, 'IY': 0, 'W3': 0, 'NEW': 0, 'TTT': 0, 'LT': 0, 'PW': 0,
                        'PAPPY': 0, '403': 0, 'KING': 0, 'FOX': 0, 'YSD': 0, 'NN': 0, 'MARIA': 0, 'OLD': 0, 'ROSE': 0, 'JESSA': 0, 'DAZZ': 0, 'SIR': 0,
                        'RP': 0, 'RSM': 0, '  ILY': 0, 'PWN': 0, 'IV': 0, 'VX': 0, 'ROBBY': 0, 'REN': 0, 'SNAKE': 0, 'GOUL': 0, 'FLOS': 0, 'LBX': 0,
                        'DN': 0, 'SG': 0, 'CUTE': 0, 'SUPER': 0, 'ETN': 0, 'BREAD': 0, 'YAMI': 0, 'GREEN': 0, 'VLOK': 0, 'CASH': 0, 'KAYN': 0, 'SV': 0,
                        'SIAPA': 0, 'KXNG': 0, 'ZERO': 0, 'DIMAS': 0, 'WHO': 0, 'TCM': 0, 'GLOW': 0, 'LDK': 0, 'LX': 0, 'KELLY': 0, 'JANG': 0, 'OLAZ': 0,
                        'THE': 0, 'DIPS': 0, 'GXB': 0, 'TITIT': 0, 'SMOL': 0, 'NEAL': 0, 'SOS': 0, 'FS': 0, 'R13': 0, 'WC2': 0, 'KENJI': 0, 
                        'AG': 0, 'ZIGG': 0, 'MFJ': 0, 'BLUE': 0, 'YAH': 0, 'BILL': 0, 'VAN': 0, 'SOY': 0, 'WAX': 0, 'FBI': 0, 'DUKE': 0, 'APEX': 0,
                        'OOPSY': 0, 'MEYO': 0, '666': 0, 'DADDY': 0, 'MINER': 0, 'NACHT': 0, 'EISA': 0, 'FRTK': 0, 'RRR': 0, 'FAJNA': 0, 'T2': 0,
                        'CFR': 0, 'ION': 0, 'MINI': 0, 'CAKE': 0, 'RANDO': 0, 'OLGA': 0, 'CAP': 0, 'CYCLO': 0, 'LE': 0, 'WAN': 0, 'LV': 0, 'YAN': 0,
                        'CP': 0, 'HMG': 0, 'RED': 0, 'BUZZ': 0, 'GR0': 0, 'A51': 0, 'ISMA': 0, 'THC': 0, 'C137': 0, 'LIAN': 0, 'RON': 0, 'NUB': 0, 'TNS': 0, 
                        'LUCKY': 0, 'SD': 0, 'QL': 0, 'EL': 0, 'DGG': 0, 'DEATH': 0, 'MELEE': 0, 'LQM': 0, 'RIVER': 0, 'KDA': 0, 'GODLY': 0, 'IG': 0, 
                        'AZURE': 0, 'ADNX': 0, 'AK47': 0, 'TETRA': 0, 'KVN': 0, 'BUD': 0, 'FAST': 0, 'CC': 0, 'HONEY': 0, 'YDS': 0, '63': 0, 'OMED': 0,
                        'PIXYZ': 0, 'KOA': 0, 'FROOT': 0, 'ANTI': 0, 'STILL': 0, 'YSO': 0, 'XPLOI': 0, 'BI': 0, 'MC': 0, 'IM': 0, 'LEMON': 0, 'MAOKI': 0,
                        'LEVEL': 0, 'MR': 0, 'THL': 0, 'SAD': 0, '1337': 0, 'ITCHY': 0, 'THOR': 0, 'ROTI': 0, 'WASON': 0, 'FLXW': 0, 'IT': 0, 'RAFA': 0,
                        'MAOU': 0, 'TEXAN': 0, 'HEDGE': 0, 'MLG': 0, 'ISC': 0, 'YOUR': 0, 'GOAT': 0, 'EA': 0, 'PRX': 0, 'OLY': 0, 'BLECK': 0, 'ADAM': 0,
                        'ERBO': 0, 'SZEPT': 0, 'BTW': 0, 'ENZA': 0, 'BL4CK': 0, 'GRB': 0, 'KYOU': 0, 'WORLD': 0, 'XDARK': 0, 'BR': 0, 'LUCAS': 0, 'XZ': 0,
                        'LIL': 0, 'ILI': 0, 'AI': 0, 'TOM': 0, 'CAPT': 0, 'MS': 0, 'LO': 0, 'BD': 0, 'FLOOR': 0, 'LOYAL': 0, 'TRULY': 0, 'AKUTO': 0,
                        'AKT': 0, 'TIGER': 0, 'VND': 0, 'SR': 0, 'GA': 0, 'DMN': 0, 'MANG': 0, 'GM': 0, 'WILL': 0, 'GOLD': 0, 'GK': 0, '808': 0,
                        'RICK': 0, 'ULTR': 0, 'KAMI': 0, 'QUAN': 0, 'FORST': 0, 'DWIKI': 0, 'LBCL': 0, 'EML': 0, 'HUONG': 0, 'AFK': 0, 'NO': 0,
                        'DUCKS': 0, 'XERRA': 0, 'THAT': 0, 'DJ': 0, 'TWO': 0}

guilds_counter_int  = {'IMMORTAL': 0, 'OWO': 0, 'EXP': 0, 'BRX': 0, 'RNG': 0, 'LAT': 0, 'KRG': 0, 'GGWP': 0, 'PVM': 0, 'DTF': 0, 'HSR': 0, 'FG': 0, 
                        'NS': 0, 'AOE': 0, 'NSFW': 0, 'DMG': 0, 'AXIAL': 0, 'PAK': 0, 'T62': 0, 'VLR': 0, 'RYU': 0, 'TI': 0, 'NSL': 0, '1HB': 0, 'FFA': 0,
                        'OG': 0, 'ORAZE': 0, 'BLITZ': 0, 'DTS': 0, 'SOLO': 0, 'BIG': 0, 'TRG': 0, 'CCCP': 0, 'TNT': 0, 'SOW': 0, 'PAPA': 0, 'TH': 0,
                        'EXC': 0, 'PHG': 0, 'SHORN': 0, 'TT': 0, 'UMBRA': 0, 'AK7': 0, 'GG': 0, 'LNH': 0, 'SLP': 0, 'DEAD': 0, 'TCK': 0, 'XP': 0, 
                        'VN': 0, 'XNW': 0, 'DARK': 0, 'FW': 0, 'DAVY': 0, 'DK': 0, 'II': 0, 'RW': 0, 'WG': 0, 'OL': 0, 'GOD': 0, 'YOUNG': 0, 'MAD': 0,
                        'ORDO': 0, 'LGN': 0, 'STEVE': 0, 'LOST': 0, 'LI': 0, 'GO': 0, 'LOLI': 0, 'PKMN': 0, 'GUN': 0, 'TAZ': 0, 'BH': 0, 'YT': 0,
                        'SYN': 0, 'NINJA': 0, 'ESP': 0, 'DR': 0, 'PK': 0, 'CW': 0, 'XD': 0, 'RS': 0, 'GOLEM': 0, 'IIAMA': 0, 'IL': 0, 'HANSA': 0, 'YAO': 
                        0, 'ST': 0, 'FLO': 0, 'SORRY': 0, 'AEVN': 0, 'MSA': 0, 'TROLL': 0, 'GW': 0, 'AROS': 0, 'GOKU': 0, 'YUZU': 0, 'GEAR': 0, 'IE': 0,
                        'WTH': 0, 'ACE': 0, 'RDS': 0, 'ROYAL': 0, 'KH': 0, 'FT': 0, 'TMG': 0, 'IY': 0, 'W3': 0, 'NEW': 0, 'TTT': 0, 'LT': 0, 'PW': 0,
                        'PAPPY': 0, '403': 0, 'KING': 0, 'FOX': 0, 'YSD': 0, 'NN': 0, 'MARIA': 0, 'OLD': 0, 'ROSE': 0, 'JESSA': 0, 'DAZZ': 0, 'SIR': 0,
                        'RP': 0, 'RSM': 0, '  ILY': 0, 'PWN': 0, 'IV': 0, 'VX': 0, 'ROBBY': 0, 'REN': 0, 'SNAKE': 0, 'GOUL': 0, 'FLOS': 0, 'LBX': 0,
                        'DN': 0, 'SG': 0, 'CUTE': 0, 'SUPER': 0, 'ETN': 0, 'BREAD': 0, 'YAMI': 0, 'GREEN': 0, 'VLOK': 0, 'CASH': 0, 'KAYN': 0, 'SV': 0,
                        'SIAPA': 0, 'KXNG': 0, 'ZERO': 0, 'DIMAS': 0, 'WHO': 0, 'TCM': 0, 'GLOW': 0, 'LDK': 0, 'LX': 0, 'KELLY': 0, 'JANG': 0, 'OLAZ': 0,
                        'THE': 0, 'DIPS': 0, 'GXB': 0, 'TITIT': 0, 'SMOL': 0, 'NEAL': 0, 'SOS': 0, 'FS': 0, 'R13': 0, 'WC2': 0, 'KENJI': 0, 
                        'AG': 0, 'ZIGG': 0, 'MFJ': 0, 'BLUE': 0, 'YAH': 0, 'BILL': 0, 'VAN': 0, 'SOY': 0, 'WAX': 0, 'FBI': 0, 'DUKE': 0, 'APEX': 0,
                        'OOPSY': 0, 'MEYO': 0, '666': 0, 'DADDY': 0, 'MINER': 0, 'NACHT': 0, 'EISA': 0, 'FRTK': 0, 'RRR': 0, 'FAJNA': 0, 'T2': 0,
                        'CFR': 0, 'ION': 0, 'MINI': 0, 'CAKE': 0, 'RANDO': 0, 'OLGA': 0, 'CAP': 0, 'CYCLO': 0, 'LE': 0, 'WAN': 0, 'LV': 0, 'YAN': 0,
                        'CP': 0, 'HMG': 0, 'RED': 0, 'BUZZ': 0, 'GR0': 0, 'A51': 0, 'ISMA': 0, 'THC': 0, 'C137': 0, 'LIAN': 0, 'RON': 0, 'NUB': 0, 'TNS': 0, 
                        'LUCKY': 0, 'SD': 0, 'QL': 0, 'EL': 0, 'DGG': 0, 'DEATH': 0, 'MELEE': 0, 'LQM': 0, 'RIVER': 0, 'KDA': 0, 'GODLY': 0, 'IG': 0, 
                        'AZURE': 0, 'ADNX': 0, 'AK47': 0, 'TETRA': 0, 'KVN': 0, 'BUD': 0, 'FAST': 0, 'CC': 0, 'HONEY': 0, 'YDS': 0, '63': 0, 'OMED': 0,
                        'PIXYZ': 0, 'KOA': 0, 'FROOT': 0, 'ANTI': 0, 'STILL': 0, 'YSO': 0, 'XPLOI': 0, 'BI': 0, 'MC': 0, 'IM': 0, 'LEMON': 0, 'MAOKI': 0,
                        'LEVEL': 0, 'MR': 0, 'THL': 0, 'SAD': 0, '1337': 0, 'ITCHY': 0, 'THOR': 0, 'ROTI': 0, 'WASON': 0, 'FLXW': 0, 'IT': 0, 'RAFA': 0,
                        'MAOU': 0, 'TEXAN': 0, 'HEDGE': 0, 'MLG': 0, 'ISC': 0, 'YOUR': 0, 'GOAT': 0, 'EA': 0, 'PRX': 0, 'OLY': 0, 'BLECK': 0, 'ADAM': 0,
                        'ERBO': 0, 'SZEPT': 0, 'BTW': 0, 'ENZA': 0, 'BL4CK': 0, 'GRB': 0, 'KYOU': 0, 'WORLD': 0, 'XDARK': 0, 'BR': 0, 'LUCAS': 0, 'XZ': 0,
                        'LIL': 0, 'ILI': 0, 'AI': 0, 'TOM': 0, 'CAPT': 0, 'MS': 0, 'LO': 0, 'BD': 0, 'FLOOR': 0, 'LOYAL': 0, 'TRULY': 0, 'AKUTO': 0,
                        'AKT': 0, 'TIGER': 0, 'VND': 0, 'SR': 0, 'GA': 0, 'DMN': 0, 'MANG': 0, 'GM': 0, 'WILL': 0, 'GOLD': 0, 'GK': 0, '808': 0,
                        'RICK': 0, 'ULTR': 0, 'KAMI': 0, 'QUAN': 0, 'FORST': 0, 'DWIKI': 0, 'LBCL': 0, 'EML': 0, 'HUONG': 0, 'AFK': 0, 'NO': 0,
                        'DUCKS': 0, 'XERRA': 0, 'THAT': 0, 'DJ': 0, 'TWO': 0}

def DictToList (dictio,listo):
    for key, value in dictio.items():
        test = key + " -- " + "{:,}".format(value)
        listo.append(test)

def ResetDict(diction):
    diction = diction.fromkeys(diction, 0)
    return diction

def search(skill_name):
    list_guilds_stred = []
    
    d_test = ResetDict(guilds_counter_int)
    for k in range(0,49):  
        url='https://www.curseofaros.com/highscores'
        headers = {'User-Agent': 'Mozilla/5.0'}        
        request = Request(url+skill_name+'.json?p='+str(k), headers=headers)
        html = urlopen(request).read()       
        data = html.decode("utf-8")        
        fdata = json.loads(data)
        for i in range(0,20): 
            #check names get rank
            player_name = fdata[i]["name"]
            xp = fdata[i]["xp"]
            tag = player_name.split()[0]
            tag = tag.upper()

            if tag in d_test :
                d_test[tag] += xp
            elif "Immortal" in player_name :
                d_test["IMMORTAL"] += xp
            else :                
                continue
        
    temp_guilds = {k: v for k, v in sorted(d_test.items(), key=lambda item: item[1],reverse=True)}

    DictToList(temp_guilds,list_guilds_stred)
    
    mini_list = []
    for i in range(5):
        mini_list.append(list_guilds_stred[i])
    list_guilds_stred.clear()
    temp_guilds = ResetDict(guilds_counter_int)
    return mini_list

def searchTotal():
    list_guilds_total_stred = []
    dd_test = ResetDict(guilds_counter_int)
    for m in range(0,7):
        for k in range(0,49):  
            url='https://www.curseofaros.com/highscores'
            headers = {'User-Agent': 'Mozilla/5.0'}        
            request = Request(url+skill[m]+'.json?p='+str(k), headers=headers)
            html = urlopen(request).read()       
            data = html.decode("utf-8")        
            fdata = json.loads(data)
            for i in range(0,20): 
                #check names get rank
                player_name = fdata[i]["name"]
                xp = fdata[i]["xp"]
                tag = player_name.split()[0]
                tag = tag.upper()

                if tag in dd_test :
                    dd_test[tag] += xp
                elif "Immortal" in player_name :
                    dd_test["IMMORTAL"] += xp
                else :                
                    continue
            
    temp_guilds = {k: v for k, v in sorted(dd_test.items(), key=lambda item: item[1],reverse=True)}

    DictToList(temp_guilds,list_guilds_total_stred)
        
    mini_list = []
    for i in range(5):
            mini_list.append(list_guilds_total_stred[i])
    list_guilds_total_stred.clear()
    temp_guilds = ResetDict(guilds_counter_int)
    return mini_list

############################################################################################################
  
client = d.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=d.Activity(type=d.ActivityType.watching, name="LeaderBoard"))

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return

    if message.channel.name == 'testing' :
        if user_message.lower() == '!hello':
            await message.channel.send(f'Hello {username}!')

        elif user_message.lower() == '!bye':
            await message.channel.send(f'See you later {username}!')
      
        elif user_message.lower() == '!wussup':
            await message.channel.send(f'Nothing much, hbu {username} ?') 

        elif user_message.lower() == '!bestguild':
            await message.channel.send(f'OwO Numba Wan !') 

        elif user_message.lower() == '!random':
            response = f'random number between (0 ; 1,000,000): {random.randrange(1000000)}'
            await message.channel.send(response)

        elif user_message.lower() == ('!dc' or '!disconnect') :
            await client.logout()

    
        elif user_message.lower() == ('!gcombat') :
            await message.channel.send("Fetching Combat Data")
            test_list_1 = search("")
            embedVar1 = d.Embed(title="Top Guilds: Combat", color=0x669999)
            embedVar1.add_field(name="rank#1", value= test_list_1[0] , inline=False)
            embedVar1.add_field(name="rank#2", value= test_list_1[1] , inline=False)
            embedVar1.add_field(name="rank#3", value= test_list_1[2] , inline=False)
            embedVar1.add_field(name="rank#4", value= test_list_1[3] , inline=False)
            embedVar1.add_field(name="rank#5", value= test_list_1[4] , inline=False)
            await message.channel.send(embed=embedVar1)
            test_list_1.clear()
        
        elif user_message.lower() == ('!gtest') :
            embedVar1 = d.Embed(title="Top Guilds", color=0x669999)
            #######################################
            embedVar1.add_field(name=":pick: Mining", value="Test Test" , inline=True)
            embedVar1.add_field(name=" :axe: Woodcutting", value="Test Test" , inline=True)
            embedVar1.add_field(name=" :fishing_pole_and_fish: Fishing", value="Test Test" , inline=True)
            #######################################
            embedVar1.add_field(name="Smithing", value="Test Test" , inline=True)
            embedVar1.add_field(name="Crafting", value="Test Test" , inline=True)
            embedVar1.add_field(name="Cooking", value="Test Test" , inline=True)
            #######################################
            embedVar1.add_field(name="Combat", value="Test Test" , inline=True)
            embedVar1.add_field(name="Total XP", value="Test Test" , inline=True)
            await message.channel.send(embed=embedVar1)
                               
        elif user_message.lower() == ('!gmining') :
            await message.channel.send("Fetching Mining Data ... ")
            test_list_2 = search("-mining")
            embedVar2 = d.Embed(title="Top Guilds: Mining", color=0x333300)
            embedVar2.add_field(name="rank#1", value= test_list_2[0] , inline=False)
            embedVar2.add_field(name="rank#2", value= test_list_2[1] , inline=False)
            embedVar2.add_field(name="rank#3", value= test_list_2[2] , inline=False)
            embedVar2.add_field(name="rank#4", value= test_list_2[3] , inline=False)
            embedVar2.add_field(name="rank#5", value= test_list_2[4] , inline=False)
            await message.channel.send(embed=embedVar2)
            test_list_2.clear()

        elif user_message.lower() == ('!gsmithing') :
            await message.channel.send("Fetching Smithing Data ... ")
            test_list_3 = search("-smithing")
            embedVar3 = d.Embed(title="Top Guilds: Smithing", color=0xff0000)
            embedVar3.add_field(name="rank#1", value= test_list_3[0] , inline=False)
            embedVar3.add_field(name="rank#2", value= test_list_3[1] , inline=False)
            embedVar3.add_field(name="rank#3", value= test_list_3[2] , inline=False)
            embedVar3.add_field(name="rank#4", value= test_list_3[3] , inline=False)
            embedVar3.add_field(name="rank#5", value= test_list_3[4] , inline=False)
            await message.channel.send(embed=embedVar3)
            test_list_3.clear()

        elif user_message.lower() == ('!gwc') :
            await message.channel.send("Fetching Woodcutting Data ... ")
            test_list_4 = search("-woodcutting")
            embedVar4 = d.Embed(title="Top Guilds: Woodcutting", color=0x00cc00)
            embedVar4.add_field(name="rank#1", value= test_list_4[0] , inline=False)
            embedVar4.add_field(name="rank#2", value= test_list_4[1] , inline=False)
            embedVar4.add_field(name="rank#3", value= test_list_4[2] , inline=False)
            embedVar4.add_field(name="rank#4", value= test_list_4[3] , inline=False)
            embedVar4.add_field(name="rank#5", value= test_list_4[4] , inline=False)
            await message.channel.send(embed=embedVar4)
            test_list_4.clear()

        elif user_message.lower() == ('!gcrafting') :
            await message.channel.send("Fetching Crafting Data ... ")
            test_list_5 = search("-crafting")
            embedVar5 = d.Embed(title="Top Guilds: Crafting", color=0x996633)
            embedVar5.add_field(name="rank#1", value= test_list_5[0] , inline=False)
            embedVar5.add_field(name="rank#2", value= test_list_5[1] , inline=False)
            embedVar5.add_field(name="rank#3", value= test_list_5[2] , inline=False)
            embedVar5.add_field(name="rank#4", value= test_list_5[3] , inline=False)
            embedVar5.add_field(name="rank#5", value= test_list_5[4] , inline=False)
            await message.channel.send(embed=embedVar5)
            test_list_5.clear()

        elif user_message.lower() == ('!gfishing') :
            await message.channel.send("Fetching Fishimg Data ... ")
            test_list_6 = search("-fishing")
            embedVar6 = d.Embed(title="Top Guilds: Fishing", color=0x0066ff)
            embedVar6.add_field(name="rank#1", value= test_list_6[0] , inline=False)
            embedVar6.add_field(name="rank#2", value= test_list_6[1] , inline=False)
            embedVar6.add_field(name="rank#3", value= test_list_6[2] , inline=False)
            embedVar6.add_field(name="rank#4", value= test_list_6[3] , inline=False)
            embedVar6.add_field(name="rank#5", value= test_list_6[4] , inline=False)
            await message.channel.send(embed=embedVar6)
            test_list_6.clear()

        elif user_message.lower() == ('!gcooking') :
            await message.channel.send("Fetching Cooking Data ... ")
            test_list_7 = search("-cooking")
            embedVar7 = d.Embed(title="Top Guilds: Cooking", color=0x800000)
            embedVar7.add_field(name="rank#1", value= test_list_7[0] , inline=False)
            embedVar7.add_field(name="rank#2", value= test_list_7[1] , inline=False)
            embedVar7.add_field(name="rank#3", value= test_list_7[2] , inline=False)
            embedVar7.add_field(name="rank#4", value= test_list_7[3] , inline=False)
            embedVar7.add_field(name="rank#5", value= test_list_7[4] , inline=False)
            await message.channel.send(embed=embedVar7)
            test_list_7.clear()

        elif user_message.lower() == ('!gtotal') :
            await message.channel.send("Fetching Data ... ")
            test_list_0 = searchTotal()
        
            embedVar0 = d.Embed(title="Top Guilds: Total XP", color=0x6600ff)
            embedVar0.add_field(name="rank#1", value= test_list_0[0] , inline=False)
            embedVar0.add_field(name="rank#2", value= test_list_0[1] , inline=False)
            embedVar0.add_field(name="rank#3", value= test_list_0[2] , inline=False)
            embedVar0.add_field(name="rank#4", value= test_list_0[3] , inline=False)
            embedVar0.add_field(name="rank#5", value= test_list_0[4] , inline=False)
            await message.channel.send(embed=embedVar0)
            test_list_0.clear()

        elif user_message.lower() == '!date':
            today = date.today()
            d1 = today.strftime("%d/%m/%Y")
            response = f'Today is : {d1}'
            await message.channel.send(response)
        
        elif user_message.lower() == ('!ghelp') :
            embedVar8 = d.Embed(title="Guilds Commands", color=0x669999)
            embedVar8.add_field(name="!gcombat", value= "Show Top 5 Guilds in Combat" , inline=False)
            embedVar8.add_field(name="!gmining", value= "Show Top 5 Guilds in Mining" , inline=False)
            embedVar8.add_field(name="!gsmithing", value= "Show Top 5 Guilds in Smithing" , inline=False)
            embedVar8.add_field(name="!gwc", value= "Show Top 5 Guilds in Woodcutting" , inline=False)
            embedVar8.add_field(name="!gcrafting", value= "Show Top 5 Guilds in Crafting" , inline=False)
            embedVar8.add_field(name="!gfishing", value= "Show Top 5 Guilds in Fishing" , inline=False)
            embedVar8.add_field(name="!gcooking", value= "Show Top 5 Guilds in Cooking" , inline=False)
            embedVar8.add_field(name="!gtotal", value= "Show Top 5 Guilds in Total XP" , inline=False)
            embedVar8.add_field(name="!bestguild", value= "Show The Current Best Guild" , inline=False)
            embedVar8.add_field(name="!random", value= "Random Number (0;1,000,000)" , inline=False)
            embedVar8.add_field(name="!date", value= "Show Today Date" , inline=False)
            embedVar8.add_field(name="!dc or !disconnect", value= "Disconnect The Bot For a While To Reset Himself" , inline=False)
            embedVar8.add_field(name="!hello , !wussup , !bye", value= "Interract With The Bot" , inline=False)
            await message.channel.send(embed=embedVar8)

            return

    elif message.channel.name != 'testing' :
        if user_message.lower() == '!anywhere':
            await message.channel.send('please head to #testing to use me')
            return
          
client.run(os.getenv('TOKEN'))
