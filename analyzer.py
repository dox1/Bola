import random

TEAMS_DB = {
    # ═══════════════════════════════════════
    #         الأندية الأوروبية الكبرى
    # ═══════════════════════════════════════
    "real madrid": {"rating": 95, "attack": 94, "defense": 90, "form": "WWWDW"},
    "barcelona": {"rating": 90, "attack": 92, "defense": 85, "form": "WWDWL"},
    "manchester city": {"rating": 93, "attack": 92, "defense": 89, "form": "WWWWW"},
    "manchester united": {"rating": 78, "attack": 75, "defense": 72, "form": "WDLWL"},
    "liverpool": {"rating": 88, "attack": 89, "defense": 84, "form": "WWDWW"},
    "chelsea": {"rating": 80, "attack": 78, "defense": 76, "form": "DWWLD"},
    "arsenal": {"rating": 85, "attack": 86, "defense": 82, "form": "WWWDW"},
    "tottenham": {"rating": 77, "attack": 78, "defense": 73, "form": "LDWWL"},
    "psg": {"rating": 89, "attack": 91, "defense": 84, "form": "WWWLW"},
    "paris saint germain": {"rating": 89, "attack": 91, "defense": 84, "form": "WWWLW"},
    "bayern munich": {"rating": 92, "attack": 93, "defense": 88, "form": "WWWWL"},
    "borussia dortmund": {"rating": 82, "attack": 84, "defense": 78, "form": "WDWLW"},
    "juventus": {"rating": 80, "attack": 78, "defense": 82, "form": "DWWDL"},
    "ac milan": {"rating": 81, "attack": 80, "defense": 81, "form": "WDWWD"},
    "inter milan": {"rating": 85, "attack": 83, "defense": 86, "form": "WWDWW"},
    "atletico madrid": {"rating": 84, "attack": 79, "defense": 88, "form": "WDWDW"},
    "napoli": {"rating": 82, "attack": 83, "defense": 79, "form": "WWLWW"},
    "roma": {"rating": 78, "attack": 77, "defense": 76, "form": "DWWLD"},
    "ajax": {"rating": 79, "attack": 81, "defense": 75, "form": "WWWDL"},
    "porto": {"rating": 78, "attack": 77, "defense": 77, "form": "WWDWL"},
    "benfica": {"rating": 79, "attack": 80, "defense": 76, "form": "WWWLD"},
    "sevilla": {"rating": 76, "attack": 74, "defense": 77, "form": "DWLDW"},
    "valencia": {"rating": 74, "attack": 73, "defense": 74, "form": "LDWWL"},
    "villarreal": {"rating": 75, "attack": 76, "defense": 73, "form": "WDWLD"},
    "celtic": {"rating": 74, "attack": 75, "defense": 72, "form": "WWWDW"},
    "rangers": {"rating": 72, "attack": 71, "defense": 72, "form": "WWDLW"},
    "psv": {"rating": 77, "attack": 79, "defense": 74, "form": "WWWWD"},
    "feyenoord": {"rating": 76, "attack": 77, "defense": 74, "form": "WDWWL"},
    "monaco": {"rating": 75, "attack": 76, "defense": 73, "form": "WWDLW"},
    "lyon": {"rating": 74, "attack": 75, "defense": 72, "form": "DWWLD"},
    "marseille": {"rating": 76, "attack": 77, "defense": 74, "form": "WWLWW"},
    "lazio": {"rating": 76, "attack": 77, "defense": 74, "form": "WDWLW"},
    "fiorentina": {"rating": 74, "attack": 75, "defense": 72, "form": "WWDLW"},
    "atalanta": {"rating": 80, "attack": 83, "defense": 76, "form": "WWWLW"},
    "rb leipzig": {"rating": 79, "attack": 80, "defense": 77, "form": "WWDWL"},
    "bayer leverkusen": {"rating": 83, "attack": 85, "defense": 80, "form": "WWWWL"},

    # ═══════════════════════════════════════
    #         الأندية العربية
    # ═══════════════════════════════════════
    "الهلال": {"rating": 84, "attack": 83, "defense": 82, "form": "WWWWW"},
    "النصر": {"rating": 85, "attack": 87, "defense": 79, "form": "WWDWW"},
    "الأهلي": {"rating": 80, "attack": 79, "defense": 79, "form": "WWWDL"},
    "الاتحاد": {"rating": 76, "attack": 75, "defense": 75, "form": "WDWLW"},
    "الزمالك": {"rating": 75, "attack": 74, "defense": 74, "form": "DWWDW"},
    "الترجي": {"rating": 77, "attack": 76, "defense": 76, "form": "WWWLD"},
    "وداد": {"rating": 74, "attack": 73, "defense": 73, "form": "WDWWL"},
    "الرجاء": {"rating": 72, "attack": 71, "defense": 72, "form": "DWLWW"},
    "الوداد": {"rating": 74, "attack": 73, "defense": 73, "form": "WDWWL"},
    "شباب بلوزداد": {"rating": 70, "attack": 69, "defense": 69, "form": "WWDLW"},
    "مولودية الجزائر": {"rating": 69, "attack": 68, "defense": 68, "form": "DWWLD"},
    "اتحاد العاصمة": {"rating": 68, "attack": 67, "defense": 68, "form": "WDLWW"},
    "الاتفاق": {"rating": 73, "attack": 74, "defense": 71, "form": "WDWLW"},
    "الشباب": {"rating": 72, "attack": 71, "defense": 71, "form": "WWLWL"},
    "الوحدة": {"rating": 70, "attack": 69, "defense": 70, "form": "DWWDL"},
    "العين": {"rating": 74, "attack": 73, "defense": 73, "form": "WWWLD"},
    "الجزيرة": {"rating": 71, "attack": 70, "defense": 70, "form": "WDWWL"},
    "الأهلي طرابلس": {"rating": 67, "attack": 66, "defense": 66, "form": "WDLWW"},

    # ═══════════════════════════════════════
    #    منتخبات أوروبا (55 منتخب)
    # ═══════════════════════════════════════
    "france": {"rating": 91, "attack": 92, "defense": 88, "form": "WWWDW"},
    "فرنسا": {"rating": 91, "attack": 92, "defense": 88, "form": "WWWDW"},
    "spain": {"rating": 88, "attack": 87, "defense": 87, "form": "WWWWD"},
    "اسبانيا": {"rating": 88, "attack": 87, "defense": 87, "form": "WWWWD"},
    "إسبانيا": {"rating": 88, "attack": 87, "defense": 87, "form": "WWWWD"},
    "germany": {"rating": 86, "attack": 85, "defense": 85, "form": "WWDWL"},
    "المانيا": {"rating": 86, "attack": 85, "defense": 85, "form": "WWDWL"},
    "ألمانيا": {"rating": 86, "attack": 85, "defense": 85, "form": "WWDWL"},
    "england": {"rating": 87, "attack": 87, "defense": 85, "form": "WWWDL"},
    "انجلترا": {"rating": 87, "attack": 87, "defense": 85, "form": "WWWDL"},
    "إنجلترا": {"rating": 87, "attack": 87, "defense": 85, "form": "WWWDL"},
    "portugal": {"rating": 88, "attack": 89, "defense": 83, "form": "WWWDW"},
    "البرتغال": {"rating": 88, "attack": 89, "defense": 83, "form": "WWWDW"},
    "netherlands": {"rating": 85, "attack": 85, "defense": 82, "form": "WWWLD"},
    "هولندا": {"rating": 85, "attack": 85, "defense": 82, "form": "WWWLD"},
    "italy": {"rating": 84, "attack": 81, "defense": 87, "form": "WDWDW"},
    "ايطاليا": {"rating": 84, "attack": 81, "defense": 87, "form": "WDWDW"},
    "إيطاليا": {"rating": 84, "attack": 81, "defense": 87, "form": "WDWDW"},
    "belgium": {"rating": 83, "attack": 84, "defense": 80, "form": "WWDLW"},
    "بلجيكا": {"rating": 83, "attack": 84, "defense": 80, "form": "WWDLW"},
    "croatia": {"rating": 81, "attack": 80, "defense": 80, "form": "WDWWL"},
    "كرواتيا": {"rating": 81, "attack": 80, "defense": 80, "form": "WDWWL"},
    "switzerland": {"rating": 79, "attack": 77, "defense": 80, "form": "WWDLW"},
    "سويسرا": {"rating": 79, "attack": 77, "defense": 80, "form": "WWDLW"},
    "denmark": {"rating": 80, "attack": 79, "defense": 80, "form": "WWWLD"},
    "الدنمارك": {"rating": 80, "attack": 79, "defense": 80, "form": "WWWLD"},
    "austria": {"rating": 77, "attack": 77, "defense": 76, "form": "WWDWL"},
    "النمسا": {"rating": 77, "attack": 77, "defense": 76, "form": "WWDWL"},
    "sweden": {"rating": 76, "attack": 74, "defense": 77, "form": "WDWLW"},
    "السويد": {"rating": 76, "attack": 74, "defense": 77, "form": "WDWLW"},
    "ukraine": {"rating": 75, "attack": 74, "defense": 74, "form": "WDLWW"},
    "اوكرانيا": {"rating": 75, "attack": 74, "defense": 74, "form": "WDLWW"},
    "أوكرانيا": {"rating": 75, "attack": 74, "defense": 74, "form": "WDLWW"},
    "poland": {"rating": 76, "attack": 76, "defense": 74, "form": "WDWLW"},
    "بولندا": {"rating": 76, "attack": 76, "defense": 74, "form": "WDWLW"},
    "turkey": {"rating": 76, "attack": 76, "defense": 74, "form": "WWDLW"},
    "تركيا": {"rating": 76, "attack": 76, "defense": 74, "form": "WWDLW"},
    "czech republic": {"rating": 74, "attack": 73, "defense": 74, "form": "DWWLD"},
    "التشيك": {"rating": 74, "attack": 73, "defense": 74, "form": "DWWLD"},
    "hungary": {"rating": 72, "attack": 70, "defense": 73, "form": "WDLWL"},
    "المجر": {"rating": 72, "attack": 70, "defense": 73, "form": "WDLWL"},
    "serbia": {"rating": 74, "attack": 74, "defense": 73, "form": "WWDLW"},
    "صربيا": {"rating": 74, "attack": 74, "defense": 73, "form": "WWDLW"},
    "slovakia": {"rating": 71, "attack": 69, "defense": 72, "form": "WDLWW"},
    "سلوفاكيا": {"rating": 71, "attack": 69, "defense": 72, "form": "WDLWW"},
    "romania": {"rating": 70, "attack": 68, "defense": 71, "form": "DWWLD"},
    "رومانيا": {"rating": 70, "attack": 68, "defense": 71, "form": "DWWLD"},
    "greece": {"rating": 69, "attack": 67, "defense": 71, "form": "WDLWL"},
    "اليونان": {"rating": 69, "attack": 67, "defense": 71, "form": "WDLWL"},
    "scotland": {"rating": 70, "attack": 69, "defense": 70, "form": "WWDLW"},
    "اسكتلندا": {"rating": 70, "attack": 69, "defense": 70, "form": "WWDLW"},
    "wales": {"rating": 69, "attack": 68, "defense": 69, "form": "DWLWL"},
    "ويلز": {"rating": 69, "attack": 68, "defense": 69, "form": "DWLWL"},
    "norway": {"rating": 74, "attack": 76, "defense": 71, "form": "WWWLD"},
    "النرويج": {"rating": 74, "attack": 76, "defense": 71, "form": "WWWLD"},
    "russia": {"rating": 70, "attack": 68, "defense": 71, "form": "WDWLW"},
    "روسيا": {"rating": 70, "attack": 68, "defense": 71, "form": "WDWLW"},
    "albania": {"rating": 66, "attack": 64, "defense": 67, "form": "WDLWL"},
    "ألبانيا": {"rating": 66, "attack": 64, "defense": 67, "form": "WDLWL"},
    "georgia": {"rating": 67, "attack": 65, "defense": 68, "form": "WWDLL"},
    "جورجيا": {"rating": 67, "attack": 65, "defense": 68, "form": "WWDLL"},
    "slovenia": {"rating": 68, "attack": 66, "defense": 69, "form": "WDWLD"},
    "سلوفينيا": {"rating": 68, "attack": 66, "defense": 69, "form": "WDWLD"},
    "finland": {"rating": 67, "attack": 65, "defense": 68, "form": "WDLWL"},
    "فنلندا": {"rating": 67, "attack": 65, "defense": 68, "form": "WDLWL"},
    "iceland": {"rating": 67, "attack": 65, "defense": 68, "form": "DWLWL"},
    "ايسلندا": {"rating": 67, "attack": 65, "defense": 68, "form": "DWLWL"},
    "إيسلندا": {"rating": 67, "attack": 65, "defense": 68, "form": "DWLWL"},
    "ireland": {"rating": 67, "attack": 65, "defense": 68, "form": "WDWLL"},
    "ايرلندا": {"rating": 67, "attack": 65, "defense": 68, "form": "WDWLL"},
    "إيرلندا": {"rating": 67, "attack": 65, "defense": 68, "form": "WDWLL"},
    "north macedonia": {"rating": 65, "attack": 63, "defense": 66, "form": "DWLWL"},
    "مقدونيا": {"rating": 65, "attack": 63, "defense": 66, "form": "DWLWL"},
    "bosnia": {"rating": 67, "attack": 66, "defense": 66, "form": "WDLWL"},
    "البوسنة": {"rating": 67, "attack": 66, "defense": 66, "form": "WDLWL"},
    "montenegro": {"rating": 63, "attack": 62, "defense": 63, "form": "LDWWL"},
    "الجبل الأسود": {"rating": 63, "attack": 62, "defense": 63, "form": "LDWWL"},
    "luxembourg": {"rating": 60, "attack": 58, "defense": 61, "form": "DWLLL"},
    "لوكسمبورغ": {"rating": 60, "attack": 58, "defense": 61, "form": "DWLLL"},
    "israel": {"rating": 68, "attack": 67, "defense": 67, "form": "WDWLW"},
    "اسرائيل": {"rating": 68, "attack": 67, "defense": 67, "form": "WDWLW"},
    "إسرائيل": {"rating": 68, "attack": 67, "defense": 67, "form": "WDWLW"},

    # ═══════════════════════════════════════
    #    منتخبات أفريقيا (54 منتخب)
    # ═══════════════════════════════════════
    "morocco": {"rating": 81, "attack": 78, "defense": 84, "form": "WWDWL"},
    "المغرب": {"rating": 81, "attack": 78, "defense": 84, "form": "WWDWL"},
    "algeria": {"rating": 77, "attack": 76, "defense": 76, "form": "WDWWL"},
    "الجزائر": {"rating": 77, "attack": 76, "defense": 76, "form": "WDWWL"},
    "senegal": {"rating": 79, "attack": 78, "defense": 78, "form": "WWLWW"},
    "السنغال": {"rating": 79, "attack": 78, "defense": 78, "form": "WWLWW"},
    "nigeria": {"rating": 78, "attack": 79, "defense": 74, "form": "WWDLW"},
    "نيجيريا": {"rating": 78, "attack": 79, "defense": 74, "form": "WWDLW"},
    "egypt": {"rating": 76, "attack": 76, "defense": 75, "form": "WWWDL"},
    "مصر": {"rating": 76, "attack": 76, "defense": 75, "form": "WWWDL"},
    "cameroon": {"rating": 74, "attack": 74, "defense": 72, "form": "WDWLW"},
    "الكاميرون": {"rating": 74, "attack": 74, "defense": 72, "form": "WDWLW"},
    "ghana": {"rating": 72, "attack": 72, "defense": 70, "form": "WDLWW"},
    "غانا": {"rating": 72, "attack": 72, "defense": 70, "form": "WDLWW"},
    "ivory coast": {"rating": 75, "attack": 75, "defense": 73, "form": "WWDWL"},
    "ساحل العاج": {"rating": 75, "attack": 75, "defense": 73, "form": "WWDWL"},
    "mali": {"rating": 71, "attack": 71, "defense": 70, "form": "WDWLW"},
    "مالي": {"rating": 71, "attack": 71, "defense": 70, "form": "WDWLW"},
    "tunisia": {"rating": 72, "attack": 70, "defense": 73, "form": "DWWLD"},
    "تونس": {"rating": 72, "attack": 70, "defense": 73, "form": "DWWLD"},
    "south africa": {"rating": 68, "attack": 67, "defense": 68, "form": "WDLWL"},
    "جنوب أفريقيا": {"rating": 68, "attack": 67, "defense": 68, "form": "WDLWL"},
    "cape verde": {"rating": 68, "attack": 68, "defense": 67, "form": "WWDLL"},
    "الرأس الخضراء": {"rating": 68, "attack": 68, "defense": 67, "form": "WWDLL"},
    "burkina faso": {"rating": 67, "attack": 67, "defense": 65, "form": "WDWLL"},
    "بوركينا فاسو": {"rating": 67, "attack": 67, "defense": 65, "form": "WDWLL"},
    "guinea": {"rating": 67, "attack": 67, "defense": 65, "form": "WDLWW"},
    "غينيا": {"rating": 67, "attack": 67, "defense": 65, "form": "WDLWW"},
    "zambia": {"rating": 65, "attack": 64, "defense": 65, "form": "DWLWL"},
    "زامبيا": {"rating": 65, "attack": 64, "defense": 65, "form": "DWLWL"},
    "ethiopia": {"rating": 59, "attack": 57, "defense": 60, "form": "LDWLL"},
    "إثيوبيا": {"rating": 59, "attack": 57, "defense": 60, "form": "LDWLL"},
    "tanzania": {"rating": 60, "attack": 59, "defense": 60, "form": "DWLLL"},
    "تنزانيا": {"rating": 60, "attack": 59, "defense": 60, "form": "DWLLL"},
    "uganda": {"rating": 61, "attack": 60, "defense": 61, "form": "WDLLL"},
    "أوغندا": {"rating": 61, "attack": 60, "defense": 61, "form": "WDLLL"},
    "kenya": {"rating": 60, "attack": 59, "defense": 60, "form": "LDWLL"},
    "كينيا": {"rating": 60, "attack": 59, "defense": 60, "form": "LDWLL"},
    "libya": {"rating": 62, "attack": 61, "defense": 62, "form": "DWWLL"},
    "ليبيا": {"rating": 62, "attack": 61, "defense": 62, "form": "DWWLL"},
    "mauritania": {"rating": 61, "attack": 60, "defense": 61, "form": "WDLWL"},
    "موريتانيا": {"rating": 61, "attack": 60, "defense": 61, "form": "WDLWL"},
    "angola": {"rating": 63, "attack": 62, "defense": 63, "form": "WDLWL"},
    "أنغولا": {"rating": 63, "attack": 62, "defense": 63, "form": "WDLWL"},
    "mozambique": {"rating": 59, "attack": 58, "defense": 59, "form": "LDWLL"},
    "موزمبيق": {"rating": 59, "attack": 58, "defense": 59, "form": "LDWLL"},
    "gabon": {"rating": 65, "attack": 65, "defense": 63, "form": "WDWLL"},
    "الغابون": {"rating": 65, "attack": 65, "defense": 63, "form": "WDWLL"},
    "congo": {"rating": 63, "attack": 62, "defense": 62, "form": "DWLWL"},
    "الكونغو": {"rating": 63, "attack": 62, "defense": 62, "form": "DWLWL"},
    "benin": {"rating": 62, "attack": 61, "defense": 62, "form": "WDLLL"},
    "بنين": {"rating": 62, "attack": 61, "defense": 62, "form": "WDLLL"},
    "sudan": {"rating": 58, "attack": 57, "defense": 58, "form": "LDWLL"},
    "السودان": {"rating": 58, "attack": 57, "defense": 58, "form": "LDWLL"},
    "comoros": {"rating": 58, "attack": 57, "defense": 58, "form": "WDLLL"},
    "جزر القمر": {"rating": 58, "attack": 57, "defense": 58, "form": "WDLLL"},
    "equatorial guinea": {"rating": 62, "attack": 61, "defense": 61, "form": "DWLWL"},
    "غينيا الاستوائية": {"rating": 62, "attack": 61, "defense": 61, "form": "DWLWL"},

    # ═══════════════════════════════════════
    #    منتخبات أمريكا اللاتينية (10)
    # ═══════════════════════════════════════
    "brazil": {"rating": 91, "attack": 92, "defense": 87, "form": "WWDWW"},
    "البرازيل": {"rating": 91, "attack": 92, "defense": 87, "form": "WWDWW"},
    "argentina": {"rating": 93, "attack": 92, "defense": 88, "form": "WWWWW"},
    "الأرجنتين": {"rating": 93, "attack": 92, "defense": 88, "form": "WWWWW"},
    "uruguay": {"rating": 80, "attack": 79, "defense": 80, "form": "WWDLW"},
    "أوروغواي": {"rating": 80, "attack": 79, "defense": 80, "form": "WWDLW"},
    "colombia": {"rating": 79, "attack": 80, "defense": 76, "form": "WWWDL"},
    "كولومبيا": {"rating": 79, "attack": 80, "defense": 76, "form": "WWWDL"},
    "chile": {"rating": 74, "attack": 74, "defense": 72, "form": "WDWLL"},
    "تشيلي": {"rating": 74, "attack": 74, "defense": 72, "form": "WDWLL"},
    "peru": {"rating": 72, "attack": 71, "defense": 72, "form": "DWLWL"},
    "بيرو": {"rating": 72, "attack": 71, "defense": 72, "form": "DWLWL"},
    "ecuador": {"rating": 72, "attack": 72, "defense": 71, "form": "WWDLL"},
    "الإكوادور": {"rating": 72, "attack": 72, "defense": 71, "form": "WWDLL"},
    "paraguay": {"rating": 70, "attack": 69, "defense": 70, "form": "DWLWL"},
    "باراغواي": {"rating": 70, "attack": 69, "defense": 70, "form": "DWLWL"},
    "venezuela": {"rating": 65, "attack": 64, "defense": 65, "form": "LDWLL"},
    "فنزويلا": {"rating": 65, "attack": 64, "defense": 65, "form": "LDWLL"},
    "bolivia": {"rating": 60, "attack": 58, "defense": 61, "form": "LDLWL"},
    "بوليفيا": {"rating": 60, "attack": 58, "defense": 61, "form": "LDLWL"},
    "mexico": {"rating": 76, "attack": 76, "defense": 73, "form": "WWDLW"},
    "المكسيك": {"rating": 76, "attack": 76, "defense": 73, "form": "WWDLW"},
    "usa": {"rating": 74, "attack": 74, "defense": 72, "form": "WWWDL"},
    "الولايات المتحدة": {"rating": 74, "attack": 74, "defense": 72, "form": "WWWDL"},
    "canada": {"rating": 72, "attack": 72, "defense": 71, "form": "WWDLW"},
    "كندا": {"rating": 72, "attack": 72, "defense": 71, "form": "WWDLW"},
    "costa rica": {"rating": 67, "attack": 65, "defense": 68, "form": "WDLWL"},
    "كوستاريكا": {"rating": 67, "attack": 65, "defense": 68, "form": "WDLWL"},
    "jamaica": {"rating": 63, "attack": 63, "defense": 62, "form": "DWLWL"},
    "جامايكا": {"rating": 63, "attack": 63, "defense": 62, "form": "DWLWL"},

    # ═══════════════════════════════════════
    #    منتخبات آسيا (47 منتخب)
    # ═══════════════════════════════════════
    "japan": {"rating": 78, "attack": 78, "defense": 76, "form": "WWWDW"},
    "اليابان": {"rating": 78, "attack": 78, "defense": 76, "form": "WWWDW"},
    "south korea": {"rating": 76, "attack": 76, "defense": 74, "form": "WWDWL"},
    "كوريا الجنوبية": {"rating": 76, "attack": 76, "defense": 74, "form": "WWDWL"},
    "iran": {"rating": 74, "attack": 73, "defense": 74, "form": "WWWLD"},
    "ايران": {"rating": 74, "attack": 73, "defense": 74, "form": "WWWLD"},
    "إيران": {"rating": 74, "attack": 73, "defense": 74, "form": "WWWLD"},
    "australia": {"rating": 73, "attack": 73, "defense": 71, "form": "WWDLW"},
    "استراليا": {"rating": 73, "attack": 73, "defense": 71, "form": "WWDLW"},
    "أستراليا": {"rating": 73, "attack": 73, "defense": 71, "form": "WWDLW"},
    "saudi arabia": {"rating": 71, "attack": 71, "defense": 70, "form": "WWDLW"},
    "السعودية": {"rating": 71, "attack": 71, "defense": 70, "form": "WWDLW"},
    "المملكة العربية السعودية": {"rating": 71, "attack": 71, "defense": 70, "form": "WWDLW"},
    "qatar": {"rating": 67, "attack": 66, "defense": 67, "form": "WDWLL"},
    "قطر": {"rating": 67, "attack": 66, "defense": 67, "form": "WDWLL"},
    "uae": {"rating": 65, "attack": 64, "defense": 65, "form": "DWLWL"},
    "الإمارات": {"rating": 65, "attack": 64, "defense": 65, "form": "DWLWL"},
    "iraq": {"rating": 65, "attack": 65, "defense": 64, "form": "WDWLL"},
    "العراق": {"rating": 65, "attack": 65, "defense": 64, "form": "WDWLL"},
    "china": {"rating": 64, "attack": 62, "defense": 65, "form": "DWLWL"},
    "الصين": {"rating": 64, "attack": 62, "defense": 65, "form": "DWLWL"},
    "uzbekistan": {"rating": 67, "attack": 67, "defense": 66, "form": "WWWLD"},
    "أوزبكستان": {"rating": 67, "attack": 67, "defense": 66, "form": "WWWLD"},
    "jordan": {"rating": 65, "attack": 64, "defense": 65, "form": "WDWLL"},
    "الأردن": {"rating": 65, "attack": 64, "defense": 65, "form": "WDWLL"},
    "syria": {"rating": 62, "attack": 61, "defense": 62, "form": "DWLWL"},
    "سوريا": {"rating": 62, "attack": 61, "defense": 62, "form": "DWLWL"},
    "palestine": {"rating": 61, "attack": 61, "defense": 60, "form": "WDLWL"},
    "فلسطين": {"rating": 61, "attack": 61, "defense": 60, "form": "WDLWL"},
    "oman": {"rating": 62, "attack": 61, "defense": 62, "form": "WDWLL"},
    "عُمان": {"rating": 62, "attack": 61, "defense": 62, "form": "WDWLL"},
    "bahrain": {"rating": 61, "attack": 60, "defense": 61, "form": "DWLWL"},
    "البحرين": {"rating": 61, "attack": 60, "defense": 61, "form": "DWLWL"},
    "kuwait": {"rating": 60, "attack": 59, "defense": 60, "form": "LDWLL"},
    "الكويت": {"rating": 60, "attack": 59, "defense": 60, "form": "LDWLL"},
    "lebanon": {"rating": 59, "attack": 58, "defense": 59, "form": "LDWLL"},
    "لبنان": {"rating": 59, "attack": 58, "defense": 59, "form": "LDWLL"},
    "india": {"rating": 60, "attack": 59, "defense": 60, "form": "DWLWL"},
    "الهند": {"rating": 60, "attack": 59, "defense": 60, "form": "DWLWL"},
    "thailand": {"rating": 61, "attack": 61, "defense": 60, "form": "WDWLL"},
    "تايلاند": {"rating": 61, "attack": 61, "defense": 60, "form": "WDWLL"},
    "vietnam": {"rating": 60, "attack": 59, "defense": 60, "form": "WDLLL"},
    "فيتنام": {"rating": 60, "attack": 59, "defense": 60, "form": "WDLLL"},
    "indonesia": {"rating": 59, "attack": 58, "defense": 59, "form": "WDLWL"},
    "إندونيسيا": {"rating": 59, "attack": 58, "defense": 59, "form": "WDLWL"},
    "yemen": {"rating": 53, "attack": 51, "defense": 54, "form": "LLDLL"},
    "اليمن": {"rating": 53, "attack": 51, "defense": 54, "form": "LLDLL"},
}

def get_team_data(team_name: str) -> dict:
    key = team_name.lower().strip()
    # بحث مباشر
    if key in TEAMS_DB:
        return TEAMS_DB[key]
    # بحث في العربية
    if team_name.strip() in TEAMS_DB:
        return TEAMS_DB[team_name.strip()]
    # فريق غير معروف
    rating = random.randint(62, 80)
    return {
        "rating": rating,
        "attack": rating + random.randint(-4, 5),
        "defense": rating + random.randint(-4, 5),
        "form": random.choice(["WWDLW", "WDWLW", "DWWLD", "LWWWL", "WDWWD"])
    }

def form_score(form: str) -> int:
    score = 0
    for r in form:
        if r == 'W': score += 3
        elif r == 'D': score += 1
    return score

def form_text(form: str) -> str:
    result = ""
    for r in form:
        if r == 'W': result += "✅"
        elif r == 'D': result += "⬜"
        elif r == 'L': result += "❌"
    return result

async def analyze_match(team1: str, team2: str) -> str:
    t1 = get_team_data(team1)
    t2 = get_team_data(team2)

    t1_score = (t1["rating"] * 0.4 + t1["attack"] * 0.3 +
                t1["defense"] * 0.2 + form_score(t1["form"]) * 0.7)
    t2_score = (t2["rating"] * 0.4 + t2["attack"] * 0.3 +
                t2["defense"] * 0.2 + form_score(t2["form"]) * 0.7)

    total = t1_score + t2_score
    t1_win = round((t1_score / total) * 100)
    t2_win = 100 - t1_win
    draw = random.randint(15, 28)
    t1_win = max(t1_win - draw // 3, 10)
    t2_win = max(t2_win - draw // 3, 10)

    if t1_win > t2_win + 10:
        prediction = f"🏆 {team1} مرشح للفوز"
        confidence = "عالية" if t1_win > 60 else "متوسطة"
    elif t2_win > t1_win + 10:
        prediction = f"🏆 {team2} مرشح للفوز"
        confidence = "عالية" if t2_win > 60 else "متوسطة"
    else:
        prediction = "⚖️ المباراة متكافئة — تعادل محتمل"
        confidence = "متوسطة"

    t1_form_score = form_score(t1["form"])
    t2_form_score = form_score(t2["form"])
    t1_form_desc = "ممتاز 🔥" if t1_form_score >= 12 else "جيد ✅" if t1_form_score >= 8 else "متذبذب ⚠️"
    t2_form_desc = "ممتاز 🔥" if t2_form_score >= 12 else "جيد ✅" if t2_form_score >= 8 else "متذبذب ⚠️"
    t1_strength = "الهجوم ⚔️" if t1["attack"] > t1["defense"] else "الدفاع 🛡️"
    t2_strength = "الهجوم ⚔️" if t2["attack"] > t2["defense"] else "الدفاع 🛡️"

    result = f"""
⚽ *تحليل تكتيكي | بوت Bola*
━━━━━━━━━━━━━━━━━━

🏠 *{team1}* vs 🏃 *{team2}*

━━━━━━━━━━━━━━━━━━
📊 *التقييم العام:*
• {team1}: ⭐ {t1["rating"]}/100
• {team2}: ⭐ {t2["rating"]}/100

━━━━━━━━━━━━━━━━━━
⚔️ *الهجوم:*
• {team1}: {t1["attack"]}/100
• {team2}: {t2["attack"]}/100

🛡️ *الدفاع:*
• {team1}: {t1["defense"]}/100
• {team2}: {t2["defense"]}/100

━━━━━━━━━━━━━━━━━━
📈 *الشكل الأخير (5 مباريات):*
• {team1}: {form_text(t1["form"])} — {t1_form_desc}
• {team2}: {form_text(t2["form"])} — {t2_form_desc}

━━━━━━━━━━━━━━━━━━
💪 *نقطة القوة:*
• {team1}: {t1_strength}
• {team2}: {t2_strength}

━━━━━━━━━━━━━━━━━━
🎯 *نسب التوقع:*
• فوز {team1}: *{t1_win}%*
• تعادل: *{draw}%*
• فوز {team2}: *{t2_win}%*

━━━━━━━━━━━━━━━━━━
🏆 *التوقع النهائي:*
{prediction}
🔮 درجة الثقة: {confidence}

━━━━━━━━━━━━━━━━━━
⚠️ *تنبيه:* هذا التحليل للاستفادة التحليلية فقط ولا يضمن أي نتيجة.
"""
    return result.strip()
