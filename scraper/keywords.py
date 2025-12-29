# SHIELD 1.0: TARGET DICTIONARY
# Organized by Priority: Tier 1 (Most Common) -> Tier 6 (Regional/Hindi)

KEYWORD_DB = {
    "TIER_1": [ # High Priority - Most likely to yield results immediately
        'wickr menu', 'telegram plug', 'stealth shipping', 'darknet vendor',
        'buy xanax', 'buy weed', 'buy cocaine', 'buy mdma', 
        'ganja home delivery', 'maal for sale', 'chitta drug',
        'g@nja', 'w33d', 'c0caine', 'x@nax',
        'oxycodone for sale', 'painkillers dm'
    ],
    
    "TIER_2": [ # Health Hazards & Pharma
        'mtp kit buy', 'abortion pills', 'sleeping pills no rx', 'steroids for sale',
        'testosterone buy', 'hgh for sale', 'pharmacy no script', 
        'xanax bars', 'oxycontin', 'tramadol no rx'
    ],
    
    "TIER_3": [ # Specific Substances (Direct Names)
        'cocaine', 'crack cocaine', 'heroin', 'meth', 'crystal meth',
        'ketamine', 'lsd', 'mushrooms', 'dmt',
        'adderall', 'ritalin', 'vyvanse', 'percocet', 'vicodin',
        'mdma crystals', 'ecstasy pills'
    ],
    
    "TIER_4": [ # Chemical / Medical Names (Low noise, high specificity)
        'benzocaine', 'procaine', 'novocaine', 'lidocaine', 
        'methylphenidate', 'dextroamphetamine', 'alprazolam', 'diazepam',
        'fentanyl powder', 'carfentanil', 'etizolam', 'tetracaine', 
        'lignocaine', 'articaine', 'bupivacaine', 'ropivacaine', 
        'mepivacaine', 'prilocaine', 'chloroprocaine', 'oxybuprocaine',
        'proparacaine', 'propoxycaine', 'dimethocaine', 'piperocaine', 'amylocaine'
    ],
    
    "TIER_5": [ # Leetspeak, Slang & Deep Web Codes
        'bh4ang', 'ch4r@s', 'af!m', 'c0c4', 'cr4ck', 'b3nz0', 
        'pr0c41n3', 'n0v0c4in3', 't3tr4c41n3', 'l1d0c41n3', 
        '4rt1c41n3', 'bup1v4', 'r0p1v4', 'snow ganja', 'nose candy',
        'white lady', 'magic dust', 'special k', 'blue punisher',
        'pink champagne', 'china white', 'pr0k3n l4x', 'n0v0 p0wd3r',
        't3tr4 sn0w', 'l1d0 bl0w', 'l1gn0 y4y0', '4rt1 bup1', 'r0p1 sp33d',
        'm3ph3 ice', 'pr1l0 rock', 'chl0pr0 flake', 'oxybup snow', 'prop4 candy',
        'd1metho powder', 'pip3r meth', 'c0k4', 'cr4ck r0ck', 'b3nz0 cut'
    ],

    "TIER_6": [ # Hindi & Regional Slang (High Value Local Targets)
        'कोका', 'क्रैक', 'बेंजोकेन', 'प्रोकेन', 'नोवोकेन', 'टेट्राकेन', 
        'लिडोकेन', 'लिग्नोकेन', 'आर्टिकेन', 'बुपिवेकेन', 'रोपिवेकेन', 
        'मेफेड्रोन', 'प्रिलोकेन', 'क्लोरोप्रोकेन', 'ऑक्सीबुप्रोकेन', 
        'प्रोपाराकेन', 'डाइमेथोकेन', 'पाइपरोकेन', 'मिथाइलफेनिडेट', 
        'रिटालिन', 'एडरॉल', 'डेक्ट्रोएम्फेटामाइन', 'वायवांस', 
        'कोकेन हिन्दी', 'क्र4क चित्ता', 'b3nz0 देसी', 'प्र0केन पाउडर', 
        'नोवो स्पीड', 'ट3ट्रा आइस', 'ल1डो चरस', 'लिग्नो गाँजा', 
        'आर्ट1क meth', 'bup1 क्रिस्टल', 'r0पी फ्लक्का', 'm3फे बाथ', 
        'प्र1लो सॉल्ट्स', 'chl0प्रो यायो', 'ऑक्सीbup ब्लो', 'प्रोप4 स्नो', 
        'd1मेथो चार्ली', 'पाइप3र दंड्रफ', 'ग4ंजा कोका', 'चित्ता c0c4', 
        'स्पीd cr4ck', 'आइस् b3nz0', 'क्रिस्tal l1d0', 'फ्ल4क्का r1t4l1n', 
        'बाथ़ सॉल्ट्स 4dd3r4ll', 'यायो m3th', 'ब्लो चित्ता', 'स्नो गाँजा', 
        'च4र्ली स्पीड', 'देव1ल्स चित्ता', 'नाक कैंडी आइस', 'रॉक् क्रिस्टल', 
        'टूt फ्लक्का', 'ज़ॉम्बी बाथ', 'उप्प3र सॉल्ट्स', 'डेक्सी यायो', 
        'बेनी ब्लो', 'ब्लैक़ ब्यूटी स्नो', 'पेप़ पिल्स चार्ली', 
        'वेकअप्स दंड्रफ', 'कोका नाक', 'देसी कोक रॉक', 'व्हाइट़ लेडी टूt', 
        'पाउडर ज़ॉम्बी', 'सक् उप्प3र', 'फंक् डेक्सी', 'वॉश् बेनी', 
        'पाको ब्लैक़', 'बासुको पेप़', 'मेर्का वेकअप', 'गर्ल कोका', 
        'हेवन देसी', 'हेल व्हाइट़', 'ग़रीब कोक पाउडर', 'देसी स्पीड सक्', 
        'चित्ता पाउडर फंक्', 'मिर्रा वॉश', 'क़ात पाको', 'लेवाmiso बासुको', 
        'इनोसitol मेर्का', 'मैनिटोल गर्ल', 'कैफ़ कट हेवन', 'बेबी़ लैक्स हेल', 
        'बेकिंग़ सोडा ग़रीब', 'अमोनिया फ्री देसी', 'इथर वॉश् चित्ता', 
        'एसिटोन वॉश् मिर्रा', 'देसी लिडो क़ात', 'तमि़ल कोक लेवा', 
        'पंजा चित्ता इनोस', 'पंजाबी स्पीड मैनिट', 'मराठी रित कैफ़', 
        'गुज्जर अड्डा बेबी', 'बंगाली mdpv बेकिंग', 'तेलुगु मेफ़े अमोनिया', 
        'हिंदी स्पीडबॉल इथर', 'देसी मेथ् एसिटोन', 'ख़ात ख़ात तमि़ल', 
        'बाथ़ वेव पंजा', 'प्लांट फूड पंजाबी', '4-pvp मराठी', 
        'मेथलोन गुज्जर', 'bk-mdमा बंगाली', 'इथायलोन तेलुगु', 
        'पेंटिलो हिंदी', 'ब्यूटिलो देसी', 'मेथेद्रोन ख़ात', 
        'आइस क्रैंक बाथ', 'चित्ता स्नो प्लांट', 'गांजा वीड 4-pvp', 
        'कोका फायर मेथल', 'देसी स्पीड bk-md', 'रितालिन पिल इथायल', 
        'मेथ टियर पेंटिलो', 'क्रैक रॉक ब्यूटिलो', 'फ्लक्का फायर मेथेद्र', 
        'बाथ सॉल्ट्स आइस', 'चित्ता ब्लो चित्ता', 'पंजाबी आइस गांजा', 
        'हिंदी कोका कोका', 'तमिल स्पीड देसी', 'गुज्जर मेथ रितालिन', 
        'बंगाली बाथ़ मेथ', 'तेलुगु क्रिस्टल क्रैक', 'मराठी यायो फ्लक्का', 
        'देसी चित्ता बाथ', 'कोका पेरू चित्ता', 'गांजा स्पीड पंजाबी', 
        'चित्ता कोका हिंदी'
    ]
}

def get_mixed_batch(batch_size=5):
    """
    Returns a mix of keywords:
    - 50% from Tier 1 (High Probability)
    - 30% from Tier 6 (Regional/Hindi)
    - 20% from random other tiers (Deep Search)
    """
    import random
    
    tier1_count = int(batch_size * 0.5)
    tier6_count = int(batch_size * 0.3)
    other_count = batch_size - tier1_count - tier6_count
    
    batch = []
    
    # Get Tier 1 words
    if KEYWORD_DB["TIER_1"]:
        batch += random.sample(KEYWORD_DB["TIER_1"], min(len(KEYWORD_DB["TIER_1"]), tier1_count))
        
    # Get Tier 6 words (Hindi)
    if KEYWORD_DB["TIER_6"]:
        batch += random.sample(KEYWORD_DB["TIER_6"], min(len(KEYWORD_DB["TIER_6"]), tier6_count))
    
    # Get other words (Flatten other tiers)
    other_tiers = KEYWORD_DB["TIER_2"] + KEYWORD_DB["TIER_3"] + KEYWORD_DB["TIER_4"] + KEYWORD_DB["TIER_5"]
    if other_tiers:
        batch += random.sample(other_tiers, min(len(other_tiers), other_count))
    
    # If batch is still smaller than requested (due to empty tiers), fill with random
    if len(batch) < batch_size:
        all_words = other_tiers + KEYWORD_DB["TIER_1"] + KEYWORD_DB["TIER_6"]
        remaining = batch_size - len(batch)
        batch += random.sample(all_words, min(len(all_words), remaining))

    return batch