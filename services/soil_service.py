"""Soil standards and fertilizer recommendation algorithms."""

CROP_SOIL_STANDARDS = {
    "Paddy": {
        "ideal_ph": (5.5, 6.8),
        "ideal_moisture": (60, 85),
        "ideal_n": (140, 240),  # mg/kg (available)
        "ideal_p": (25, 55),
        "ideal_k": (120, 220),
        "recommendations": {
            "English": {
                "lime": "If pH < 5.5, apply Agricultural Lime or Gypsum (if sodic pH > 8.5) @ 500 kg/ha 14 days before transplanting.",
                "fertilizer": "For High Yielding Varieties (BPT 5204/MTU 1010): Recommended N:P:K is 120:60:40 kg/ha. Apply full P as basal, Nitrogen in 3 equal splits (basal, active tillering, panicle initiation), and Potassium in 2 splits (basal and panicle initiation).",
                "organic": "Incorporate green manure crops like Daincha or Sunnhemp (10-12 tonnes/ha) at flowering stage 10 days before puddling.",
                "micronutrient": "Apply Zinc Sulphate @ 50 kg/ha once every 3 seasons or spray Zinc Sulphate 0.2% + Lime 0.1% for Khaira/zinc deficiency."
            },
            "Telugu": {
                "lime": "నేల pH 5.5 కంటే తక్కువగా ఉంటే ఎకరాకు 200 కిలోల సున్నం, లేదా క్షార నేలల్లో జిప్సం దుక్కిలో వేయాలి.",
                "fertilizer": "సాధారణ వరి వంగడాలకు (బి.పి.టి 5204/ఎంటీయూ 1010) ఎకరాకు సిఫార్సు చేసిన N:P:K ఎరువులు 48:24:16 కిలోలు (యూరియా 105 కిలోలు, డి.ఎ.పి 52 కిలోలు, పొటాష్ 27 కిలోలు). భాస్వరం మొత్తం ఆఖరి దుక్కిలో, నత్రజని 3 దఫాలుగా, పొటాష్ 2 దఫాలుగా వేయాలి.",
                "organic": "ఎకరాకు 4-5 టన్నుల పశువుల ఎరువు లేదా జీలుగ, జనుము వంటి పచ్చిరొట్ట ఎరువులను పూత దశలో కలియదున్నాలి.",
                "micronutrient": "జింక్ లోపం గమనిస్తే ఎకరాకు 20 కిలోల జింక్ సల్ఫేట్ ఆఖరి దుక్కిలో వేయాలి లేదా లీటరు నీటికి 2 గ్రా. జింక్ సల్ఫేట్ కలిపి పిచికారీ చేయాలి."
            }
        }
    },
    "Cotton": {
        "ideal_ph": (6.5, 8.0),
        "ideal_moisture": (45, 70),
        "ideal_n": (120, 200),
        "ideal_p": (30, 60),
        "ideal_k": (150, 280),
        "recommendations": {
            "English": {
                "lime": "Cotton prefers neutral to slightly alkaline deep black soils. If pH > 8.5, apply Gypsum @ 1 t/ha; if pH < 6.0, apply Dolomite.",
                "fertilizer": "For Bt Hybrid Cotton: Recommended N:P:K is 150:60:60 kg/ha. Apply P as basal, N & K in 3-4 split doses at 20, 40, 60, and 80 days after sowing.",
                "organic": "Apply 10 tonnes/ha well-decomposed FYM or 2.5 tonnes vermicompost. Intercrop with cowpea or greengram to enrich nitrogen.",
                "micronutrient": "Spray Magnesium Sulphate (10g/L) and Boron (Solubor 1g/L) at square formation and flowering to prevent leaf reddening and boll drop."
            },
            "Telugu": {
                "lime": "పత్తి నల్లరేగడి నేలల్లో బాగా పెరుగుతుంది. క్షార నేలల్లో జిప్సం, ఆమ్ల నేలల్లో డోలమైట్ వినియోగించండి.",
                "fertilizer": "బిటి పత్తి హైబ్రిడ్లకు ఎకరాకు 60 కిలోల నత్రజని, 24 కిలోల భాస్వరం, 24 కిలోల పొటాష్ సిఫార్సు చేయబడింది. భాస్వరం ఆఖరి దుక్కిలో, నత్రజని మరియు పొటాష్‌లను విత్తిన 20, 40, 60, 80 రోజుల్లో సమభాగాలుగా వేయాలి.",
                "organic": "ఎకరాకు 4-5 టన్నుల మాగిన పశువుల ఎరువు లేదా వర్మీకంపోస్ట్ వేయాలి. అంతరపంటగా అలసందలు సాగుచేయడం మేలు.",
                "micronutrient": "ఆకులు ఎర్రబడటం నివారించడానికి లీటరు నీటికి 10 గ్రా. మెగ్నీషియం సల్ఫేట్, పూత రాలకుండా 1 గ్రా. బోరాన్ పిచికారీ చేయాలి."
            }
        }
    },
    "Chilli": {
        "ideal_ph": (6.0, 7.5),
        "ideal_moisture": (50, 75),
        "ideal_n": (140, 220),
        "ideal_p": (35, 65),
        "ideal_k": (160, 300),
        "recommendations": {
            "English": {
                "lime": "Ensure well-drained light loams or black clay soils with pH 6.5. Apply 400 kg/ha dolomite if soil is acidic.",
                "fertilizer": "For Guntur Chilli: Recommended N:P:K is 150:60:120 kg/ha. Apply 1/3 N, full P, and 1/3 K at transplanting, remaining in splits at 30, 60, and 90 DAT.",
                "organic": "Incorporate 15-20 tonnes/ha farmyard manure and 500 kg neem cake to prevent soil-borne Fusarium wilt and nematodes.",
                "micronutrient": "Spray Formula-4 micronutrient mixture or Zinc Sulphate (0.2%) + Boric Acid (0.1%) during peak flowering to enhance pod set and color."
            },
            "Telugu": {
                "lime": "మిరపకు తేలికపాటి గరప లేదా నల్లరేగడి నేలలు అనుకూలం. నీరు నిల్వ ఉండకుండా మురుగు కాలువలు తీయాలి.",
                "fertilizer": "ఎకరాకు 60 కిలోల నత్రజని, 24 కిలోల భాస్వరం, 48 కిలోల పొటాష్ అవసరం. భాస్వరం పూర్తిగా ఆఖరి దుక్కిలో, నత్రజని మరియు పొటాష్‌లను 3-4 దఫాలుగా నాటిన 30, 60, 90 రోజుల్లో వేయాలి.",
                "organic": "ఎకరాకు 8-10 టన్నుల పశువుల ఎరువు, 200 కిలోల వేపపిండి వేస్తే నెమటోడ్లు మరియు ఎండు తెగులు తగ్గుతాయి.",
                "micronutrient": "కాయ నాణ్యత, రంగు కోసం పూత సమయంలో లీటరు నీటికి 2 గ్రా. జింక్ సల్ఫేట్, 1 గ్రా. బోరాన్ పిచికారీ చేయాలి."
            }
        }
    },
    "Groundnut": {
        "ideal_ph": (6.0, 7.5),
        "ideal_moisture": (40, 65),
        "ideal_n": (80, 150),
        "ideal_p": (30, 60),
        "ideal_k": (100, 180),
        "recommendations": {
            "English": {
                "lime": "Apply Gypsum @ 500 kg/ha at peg penetration stage (40-45 DAS) around the root zone to ensure pod filling and shell hardening.",
                "fertilizer": "Recommended N:P:K is 20:40:40 kg/ha. Treat seeds with *Rhizobium* culture (30g/kg seed) to boost nitrogen fixation.",
                "organic": "Apply 5-8 tonnes/ha compost or FYM to improve sandy loam moisture retention in Rayalaseema tracts.",
                "micronutrient": "Spray 0.5% Ferrous Sulphate + 0.1% Citric Acid if iron chlorosis (yellowing of young leaves) appears in calcareous soils."
            },
            "Telugu": {
                "lime": "కాయలు బాగా ఊరడానికి, గింజ గట్టిపడటానికి ఊడలు దిగే దశలో (విత్తిన 40-45 రోజులకు) ఎకరాకు 200 కిలోల జిప్సం మొక్కల మొదళ్లలో వేయాలి.",
                "fertilizer": "ఎకరాకు 8 కిలోల నత్రజని, 16 కిలోల భాస్వరం, 16 కిలోల పొటాష్ సరిపోతాయి. విత్తనాలకు రైజోబియం కల్చర్ పట్టించడం మంచిది.",
                "organic": "రాయలసీమ మెట్ట నేలల్లో తేమ నిల్వ సామర్థ్యం కోసం ఎకరాకు 3-4 టన్నుల పశువుల ఎరువు వేయాలి.",
                "micronutrient": "సున్నపు నేలల్లో ఇనుము లోపం (చిగురుటాకులు పసుపు రంగులోకి మారడం) వస్తే లీటరు నీటికి 5 గ్రా. అన్నభేది (ఫెర్రస్ సల్ఫేట్) + 1 గ్రా. నిమ్మ ఉప్పు కలిపి పిచికారీ చేయాలి."
            }
        }
    },
    "Banana": {
        "ideal_ph": (6.0, 7.5),
        "ideal_moisture": (50, 75),
        "ideal_n": (160, 260),
        "ideal_p": (30, 65),
        "ideal_k": (200, 350),
        "recommendations": {
            "English": {
                "lime": "Apply 500g agricultural lime or gypsum per pit based on soil reaction in May-June.",
                "fertilizer": "For Grand Naine / Karpura: 200g N, 60g P2O5, 300g K2O per plant in 4-5 split doses up to shooting.",
                "organic": "Apply 10-15 kg well-rotted FYM and 1 kg neem cake per pit at planting.",
                "micronutrient": "Spray Banana Special micronutrient formulation (5g/L) at 4th, 5th, and 6th months after planting."
            },
            "Telugu": {
                "lime": "అరటి మొక్క నాటే గోతులలో 500 గ్రాముల సున్నం లేదా జిప్సం మట్టితో కలిపి వేయాలి.",
                "fertilizer": "ఒక్కో మొక్కకు 200 గ్రా. నత్రజని, 60 గ్రా. భాస్వరం, 300 గ్రా. పొటాష్ ఎరువులను నాటిన 2, 3, 4, 5 నెలల్లో సమభాగాలుగా అందించాలి.",
                "organic": "పిలక నాటేటప్పుడు గోతికి 10-15 కిలోల పశువుల ఎరువు మరియు 1 కిలో వేపపిండి వేస్తే వేరు పురుగులు అదుపులో ఉంటాయి.",
                "micronutrient": "గెల బరువు మరియు నాణ్యత కోసం నాటిన 4వ, 5వ, 6వ నెలల్లో 'బనానా స్పెషల్' సూక్ష్మపోషకాల మిశ్రమాన్ని లీటరు నీటికి 5 గ్రా. కలిపి పిచికారీ చేయాలి."
            }
        }
    },
    "Mango": {
        "ideal_ph": (5.5, 7.5),
        "ideal_moisture": (40, 65),
        "ideal_n": (120, 220),
        "ideal_p": (25, 55),
        "ideal_k": (140, 250),
        "recommendations": {
            "English": {
                "lime": "Apply 1-2 kg dolomite per tree basin if soil is acidic, or 2 kg gypsum in high sodium soils.",
                "fertilizer": "For mature tree (10+ years): 1000g N, 500g P2O5, 1000g K2O per year immediately after harvest in July-August.",
                "organic": "Apply 50 kg farmyard manure and 5 kg castor or neem cake per tree annually.",
                "micronutrient": "Foliar spray of 0.2% Borax and 0.5% Zinc Sulphate twice at flower panicle emergence to reduce blossom blight and improve fruit set."
            },
            "Telugu": {
                "lime": "ఆమ్ల నేలల్లో చెట్టు పాదులో 1-2 కిలోల డోలమైట్, క్షార నేలల్లో 2 కిలోల జిప్సం వేయాలి.",
                "fertilizer": "10 ఏళ్లు పైబడిన చెట్టుకు ఏటా 1 కిలో నత్రజని, 500 గ్రా. భాస్వరం, 1 కిలో పొటాష్‌ను కోతల అనంతరం జూలై-ఆగస్టులో వేయాలి.",
                "organic": "ప్రతి చెట్టుకు ఏటా 40-50 కిలోల పశువుల ఎరువు, 4-5 కిలోల వేప లేదా ఆముదం పిండి పాదుల్లో కలపాలి.",
                "micronutrient": "పూత మరియు పిందె నిలవడానికి పూత దశలో లీటరు నీటికి 2 గ్రా. బోరాక్స్, 5 గ్రా. జింక్ సల్ఫేట్ పిచికారీ చేయాలి."
            }
        }
    },
    "Coconut": {
        "ideal_ph": (5.5, 7.5),
        "ideal_moisture": (45, 70),
        "ideal_n": (120, 200),
        "ideal_p": (20, 50),
        "ideal_k": (150, 280),
        "recommendations": {
            "English": {
                "lime": "Apply 1 kg Agricultural lime or dolomite per adult palm in the basin during June-July.",
                "fertilizer": "For adult palm/year: 500g N, 320g P2O5, 1200g K2O (Urea: SSP: MOP = 1.1 kg : 2.0 kg : 2.0 kg). Apply in 2 splits (June-July and October-November).",
                "organic": "Apply 25-50 kg green leaf or compost per palm annually along with coir pith mulch.",
                "micronutrient": "Apply 500g Magnesium Sulphate (Epsom salt) and 100g Borax per palm annually to prevent crown rot and button shedding."
            },
            "Telugu": {
                "lime": "వర్షాకాలం ప్రారంభంలో (జూన్-జూలై) చెట్టు పాదులో 1 కిలో సున్నం లేదా డోలమైట్ వేయాలి.",
                "fertilizer": "చెట్టుకు ఏటా 500 గ్రా. నత్రజని, 320 గ్రా. భాస్వరం, 1200 గ్రా. పొటాష్ (యూరియా 1.1 కిలోలు, ఎస్.ఎస్.పి 2 కిలోలు, పొటాష్ 2 కిలోలు) రెండు సమభాగాలుగా జూన్ మరియు అక్టోబర్ నెలల్లో వేయాలి.",
                "organic": "చెట్టుకు ఏటా 30-40 కిలోల పశువుల ఎరువు లేదా పచ్చిరొట్ట ఎరువులు వేసి కొబ్బరి పిప్పి (కాయిర్ పిత్) తో పాదును కప్పాలి.",
                "micronutrient": "పిందె రాలడం నివారించడానికి మరియు మట్టలు పసుపు మారకుండా చెట్టుకు ఏటా 500 గ్రా. మెగ్నీషియం సల్ఫేట్, 100 గ్రా. బోరాక్స్ వేయాలి."
            }
        }
    },
    "Maize": {
        "ideal_ph": (6.0, 7.5),
        "ideal_moisture": (50, 75),
        "ideal_n": (140, 220),
        "ideal_p": (30, 60),
        "ideal_k": (130, 240),
        "recommendations": {
            "English": {
                "lime": "Maintain pH above 6.0. In acidic soil, apply 400 kg/ha Agricultural Lime before final ploughing.",
                "fertilizer": "Recommended per acre: N:P:K = 80:24:20 kg (Urea 150 kg, DAP 52 kg, MOP 34 kg). Apply entire P & K as basal, Nitrogen in 3 splits (knee-high, tasseling, grain-fill).",
                "organic": "Apply 5-6 tonnes well-decomposed FYM per acre before sowing.",
                "micronutrient": "Apply Zinc Sulphate @ 20 kg/acre basal to prevent white bud disease in maize seedlings."
            },
            "Telugu": {
                "lime": "నేల pH 6.0 కంటే తక్కువగా ఉంటే ఎకరాకు 150 కిలోల సున్నం దుక్కిలో వేయాలి.",
                "fertilizer": "ఎకరాకు సిఫార్సు చేసిన ఎరువులు: యూరియా 150 కిలోలు, డి.ఎ.పి 52 కిలోలు, పొటాష్ 34 కిలోలు. భాస్వరం మరియు పొటాష్ మొత్తం విత్తే సమయంలో, యూరియాను మోకాలు లోతు, పూత మరియు గింజ పాలుపోసుకునే దశలలో 3 దఫాలుగా వేయాలి.",
                "organic": "ఎకరాకు 4-5 టన్నుల పశువుల ఎరువు ఆఖరి దుక్కిలో కలియదున్నాలి.",
                "micronutrient": "జింక్ లోపం రాకుండా ఎకరాకు 20 కిలోల జింక్ సల్ఫేట్ ఆఖరి దుక్కిలో వేయాలి."
            }
        }
    },
    "Sugarcane": {
        "ideal_ph": (6.5, 8.0),
        "ideal_moisture": (60, 80),
        "ideal_n": (160, 260),
        "ideal_p": (35, 70),
        "ideal_k": (150, 300),
        "recommendations": {
            "English": {
                "lime": "In high pH saline/alkaline soils, apply Gypsum @ 1-2 tonnes/ha to improve soil permeability.",
                "fertilizer": "Per acre dose: 112 kg N, 40 kg P2O5, 48 kg K2O. Apply entire P as basal, Nitrogen & Potash in 3 equal splits at 30, 60, and 90 days after planting.",
                "organic": "Incorporate pressmud (10 tonnes/acre) or composted trash mulch between cane rows.",
                "micronutrient": "Foliar spray of Ferrous Sulphate (0.5%) + Zinc Sulphate (0.5%) + Urea (1%) if yellowing appears in early tillering stage."
            },
            "Telugu": {
                "lime": "చౌడు మరియు క్షార నేలల్లో ఎకరాకు 500 కిలోల జిప్సం వేసి నీరు పెట్టాలి.",
                "fertilizer": "ఎకరాకు సిఫార్సు చేసిన ఎరువులు: యూరియా 240 కిలోలు, డి.ఎ.పి 85 కిలోలు, పొటాష్ 80 కిలోలు. భాస్వరం నాటే సమయంలో, నత్రజని మరియు పొటాష్‌ను నాటిన 30, 60, 90 రోజులకు సమానంగా వేయాలి.",
                "organic": "ఎకరాకు 8-10 టన్నుల ప్రెస్‌మడ్ (చక్కెర మిల్లు వ్యర్థాలు) లేదా పచ్చిరొట్ట ఎరువులు వేయాలి.",
                "micronutrient": "మొలక దశలో ఆకులు పసుపుబారితే లీటరు నీటికి 5 గ్రా. అన్నభేది (ఫెర్రస్ సల్ఫేట్) + 5 గ్రా. జింక్ సల్ఫేట్ పిచికారీ చేయాలి."
            }
        }
    },
    "Turmeric": {
        "ideal_ph": (5.5, 7.5),
        "ideal_moisture": (50, 70),
        "ideal_n": (130, 210),
        "ideal_p": (25, 55),
        "ideal_k": (140, 260),
        "recommendations": {
            "English": {
                "lime": "Well-drained loose loamy soil is essential. Apply 300 kg/ha dolomite if soil is acidic.",
                "fertilizer": "Per acre: 25 kg N, 20 kg P2O5, 36 kg K2O. Full P as basal, N and K in 3 splits at 30, 60, and 90 days after planting.",
                "organic": "Heavy application of neem cake (200 kg/acre) and vermicompost (1.5 tonnes/acre) at planting for rhizome protection.",
                "micronutrient": "Foliar spray of micronutrient mixture (0.25%) at 60 and 90 days enhances rhizome weight and curcumin content."
            },
            "Telugu": {
                "lime": "మురుగునీరు నిలవని ఎర్ర గరప లేదా నల్లరేగడి నేలలు శ్రేష్టం. అవసరమైతే డోలమైట్ వేయాలి.",
                "fertilizer": "ఎకరాకు సిఫార్సు: యూరియా 55 కిలోలు, సింగిల్ సూపర్ ఫాస్ఫేట్ (SSP) 125 కిలోలు, పొటాష్ 60 కిలోలు. భాస్వరం దుక్కిలో, నత్రజని మరియు పొటాష్ 30, 60, 90 రోజుల్లో వేయాలి.",
                "organic": "కొమ్ము కుళ్లు నివారణకు ఎకరాకు 200 కిలోల వేపపిండి మరియు 1 టన్ను వర్మీకంపోస్ట్ దుక్కిలో వేయాలి.",
                "micronutrient": "కొమ్ము ఊరడానికి నాటిన 60 మరియు 90 రోజులకు సూక్ష్మపోషకాల మిశ్రమం పిచికారీ చేయాలి."
            }
        }
    },
    "Blackgram": {
        "ideal_ph": (6.5, 7.8),
        "ideal_moisture": (45, 65),
        "ideal_n": (100, 180),
        "ideal_p": (30, 60),
        "ideal_k": (120, 220),
        "recommendations": {
            "English": {
                "lime": "Prefers neutral to slightly alkaline soils. Gypsum @ 200 kg/ha provides essential sulphur.",
                "fertilizer": "Paddy fallow blackgram (Krishna delta practice): Apply 8 kg N, 20 kg P2O5 per acre (DAP 45 kg/acre as basal or foliar DAP 2% spray twice).",
                "organic": "Treat seeds with Rhizobium and PSB cultures (200g/acre seed) before sowing.",
                "micronutrient": "Foliar spray of 2% DAP + 1% Potassium Nitrate (13-0-45) at flowering and pod filling stage doubles yield."
            },
            "Telugu": {
                "lime": "కృష్ణా డెల్టా మాగాణి భూముల్లో వరి కోతకు 2-3 రోజుల ముందు తగినంత తేమలో విత్తాలి.",
                "fertilizer": "ఎకరాకు సిఫార్సు: డి.ఎ.పి 40-45 కిలోలు. పూత దశలో మరియు కాయ దశలో 2% డి.ఎ.పి ద్రావణం (లీటరుకు 20 గ్రా.) లేదా 13-0-45 పొటాషియం నైట్రేట్ (లీటరుకు 10 గ్రా.) పిచికారీ చేయాలి.",
                "organic": "కిలో విత్తనానికి 200 గ్రా. రైజోబియం మరియు భాస్వరం కరిగించే బ్యాక్టీరియా (PSB) తో విత్తన శుద్ధి చేయాలి.",
                "micronutrient": "పూత రాలకుండా మరియు కాయ నాణ్యతకు ప్లానోఫిక్స్ (లీటరుకు 0.25 మి.లీ) పిచికారీ చేయాలి."
            }
        }
    },
    "Tomato": {
        "ideal_ph": (6.0, 7.0),
        "ideal_moisture": (50, 75),
        "ideal_n": (140, 240),
        "ideal_p": (30, 65),
        "ideal_k": (140, 280),
        "recommendations": {
            "English": {
                "lime": "Soil pH 6.0-6.8 is optimal. Apply 500 kg agricultural lime in acidic soils 3 weeks before planting.",
                "fertilizer": "Per acre: 60 kg N, 40 kg P2O5, 60 kg K2O. Half N and full P as basal, remaining N and K in equal splits at 30, 45, and 60 days.",
                "organic": "Apply 10 tonnes well-rotted FYM and 100 kg neem cake per acre.",
                "micronutrient": "Foliar spray of 0.25% Borax + 0.5% Calcium Nitrate at flowering prevents Blossom End Rot (BER) in tomatoes."
            },
            "Telugu": {
                "lime": "నేల pH 6.0-6.8 మధ్య ఉండేలా చూసుకోవాలి. ఎకరాకు 200 కిలోల సున్నం దుక్కిలో వేయాలి.",
                "fertilizer": "ఎకరాకు సిఫార్సు: యూరియా 130 కిలోలు, డి.ఎ.పి 85 కిలోలు, పొటాష్ 100 కిలోలు. భాస్వరం నాటే సమయంలో, నత్రజని మరియు పొటాష్‌ను 30, 45, 60 రోజుల్లో వేయాలి.",
                "organic": "ఎకరాకు 6-8 టన్నుల పశువుల ఎరువు, 100 కిలోల వేపపిండి ఆఖరి దుక్కిలో వేయాలి.",
                "micronutrient": "కాయ కుళ్లు (బ్లాసమ్ ఎండ్ రాట్) రాకుండా పూత దశలో కాల్షియం నైట్రేట్ (5 గ్రా/లీ) మరియు బోరాక్స్ (2 గ్రా/లీ) పిచికారీ చేయాలి."
            }
        }
    }
}

def analyze_nutrient(val, low, high, is_tel):
    if val < low:
        return ("⚠️ తక్కువ (Low)" if is_tel else "⚠️ Deficit / Low", "#ff4d4f")
    elif val > high:
        return ("⚠️ ఎక్కువ (Excess)" if is_tel else "⚠️ Excess / High", "#faad14")
    else:
        return ("✅ సరైన స్థాయి (Optimal)" if is_tel else "✅ Optimal / Balanced", "#52c41a")
