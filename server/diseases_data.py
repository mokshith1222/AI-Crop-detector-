# Detailed Disease Database for Plant Disease Detection and Solution Server

DISEASE_DATABASE = {
    "apple apple scab": {
        "crop": "Apple",
        "disease": "Apple Scab",
        "status": "Diseased",
        "severity": "Moderate to High",
        "cause": "Fungal infection caused by Venturia inaequalis",
        "symptoms": [
            "Olive-green to brown velvety spots on upper surface of leaves",
            "Deformed, cracked, or corky lesions on fruit surface",
            "Premature yellowing and defoliation of infected leaves"
        ],
        "management": "Apply fungicide early in spring before bloom. Prune infected branches to promote airflow.",
        "organic_solution": "Spray neem oil or copper sulfate. Rake up and burn or compost fallen leaf litter in autumn.",
        "prevention": "Plant scab-resistant apple cultivars like Honeycrisp, Enterprise, or Liberty. Ensure good tree spacing."
    },
    "apple black rot": {
        "crop": "Apple",
        "disease": "Black Rot",
        "status": "Diseased",
        "severity": "High",
        "cause": "Fungal infection caused by Botryosphaeria obtusa",
        "symptoms": [
            "Frog-eye leaf spots (purple margins with tan centers)",
            "Sunken reddish-brown cankers on branches and tree bark",
            "Blackened, shriveled mummy fruits remaining attached to branches"
        ],
        "management": "Prune out dead tissue, mummified fruits, and bark cankers. Apply captan or sulfur-based fungicides.",
        "organic_solution": "Apply liquid copper spray during blossom phase. Maintain proper orchard hygiene.",
        "prevention": "Remove dead wood immediately; avoid physical damage to bark during pruning."
    },
    "apple cedar apple rust": {
        "crop": "Apple",
        "disease": "Cedar Apple Rust",
        "status": "Diseased",
        "severity": "Moderate",
        "cause": "Fungal pathogen Gymnosporangium juniperi-virginianae",
        "symptoms": [
            "Bright yellow-orange leaf spots appearing in late spring",
            "Small raised black dots (pycnia) inside orange leaf spots",
            "Tubular spore cups (aecia) under the leaf underside"
        ],
        "management": "Spray systemic fungicides like myclobutanil or propiconazole at pink bud stage.",
        "organic_solution": "Apply sulfur or copper sprays every 7-10 days during warm wet spring periods.",
        "prevention": "Remove nearby eastern red cedar / juniper trees within a 1-mile radius where feasible."
    },
    "apple healthy": {
        "crop": "Apple",
        "disease": "None (Healthy)",
        "status": "Healthy",
        "severity": "None",
        "cause": "N/A",
        "symptoms": [
            "Vibrant green leaves with crisp edges",
            "No discoloration, leaf spots, or fungal lesions",
            "Vigorous stem and leaf growth"
        ],
        "management": "Maintain regular watering and balanced nitrogen-phosphorus-potassium fertilizing.",
        "organic_solution": "Use organic compost and leaf mulch to nourish root ecosystem.",
        "prevention": "Continue standard crop rotation, weed management, and periodic tree inspection."
    },
    "blueberry healthy": {
        "crop": "Blueberry",
        "disease": "None (Healthy)",
        "status": "Healthy",
        "severity": "None",
        "cause": "N/A",
        "symptoms": [
            "Healthy deep green leaves",
            "Strong fruit production without leaf curl or spots"
        ],
        "management": "Keep soil acidic (pH 4.5 to 5.5). Water consistently with drip irrigation.",
        "organic_solution": "Mulch with pine needles or oak leaves to maintain acidic soil pH.",
        "prevention": "Prune older canes annually to maintain sunlight exposure."
    },
    "cherry including sour powdery mildew": {
        "crop": "Cherry",
        "disease": "Powdery Mildew",
        "status": "Diseased",
        "severity": "Moderate",
        "cause": "Fungal infection by Podosphaera clandestina",
        "symptoms": [
            "White powder-like fungal coating on young leaves and twigs",
            "Leaf curling upwards and stunting of foliage shoot tips",
            "Premature leaf drop and smaller fruit yield"
        ],
        "management": "Apply sulfur fungicides or potassium bicarbonate solution upon first sign of infection.",
        "organic_solution": "Spray dilute neem oil or potassium silicate spray on infected foliage.",
        "prevention": "Avoid overhead watering; prune canopy tree tops to improve sun penetration."
    },
    "cherry including sour healthy": {
        "crop": "Cherry",
        "disease": "None (Healthy)",
        "status": "Healthy",
        "severity": "None",
        "cause": "N/A",
        "symptoms": [
            "Dark green shiny leaves without white coating",
            "Normal foliage expansion and fruit clustering"
        ],
        "management": "Provide balanced deep irrigation during dry spells.",
        "organic_solution": "Apply well-composted organic fertilizer around drip line.",
        "prevention": "Inspect leaves weekly during humid conditions."
    },
    "corn maize cercospora leaf spot gray leaf spot": {
        "crop": "Corn (Maize)",
        "disease": "Gray Leaf Spot (Cercospora)",
        "status": "Diseased",
        "severity": "High",
        "cause": "Fungal infection by Cercospora zeae-maydis",
        "symptoms": [
            "Rectangular gray-to-tan leaf lesions bounded by leaf veins",
            "Blighting of entire leaves leading to premature stalk dieback",
            "Reduced grain fill and yield loss"
        ],
        "management": "Apply foliar fungicides like strobilurin or triazole derivatives at tasseling phase.",
        "organic_solution": "Practice strict 2-year crop rotation with non-host crops like legumes or soybeans.",
        "prevention": "Plant resistant hybrid corn strains. Tillage of crop residue reduces spore wintering."
    },
    "corn maize common rust": {
        "crop": "Corn (Maize)",
        "disease": "Common Rust",
        "status": "Diseased",
        "severity": "Moderate",
        "cause": "Fungal pathogen Puccinia sorghi",
        "symptoms": [
            "Cinnamon-brown oval pustules on both upper and lower leaf surfaces",
            "Pustules rupture releasing powdery rust spores",
            "Chlorotic halos surrounding older rust spots"
        ],
        "management": "Apply fungicide if rust covers >10% of leaves before silking.",
        "organic_solution": "Spray sulfur or neem extract early in cool, damp weather.",
        "prevention": "Select rust-resistant maize seed hybrids."
    },
    "corn maize northern leaf blight": {
        "crop": "Corn (Maize)",
        "disease": "Northern Leaf Blight",
        "status": "Diseased",
        "severity": "High",
        "cause": "Fungal pathogen Exserohilum turcicum",
        "symptoms": [
            "Large cigar-shaped grayish-green lesions (1 to 6 inches long)",
            "Dark grayish spores forming on lesions during moist weather",
            "Heavy browning and premature leaf death"
        ],
        "management": "Apply triazole or QoI fungicides when symptoms reach lower leaves prior to silking.",
        "organic_solution": "Deep plow corn residues post-harvest. Practice 2-3 year crop rotation.",
        "prevention": "Plant resistant hybrid seed varieties (Ht gene resistant hybrids)."
    },
    "corn maize healthy": {
        "crop": "Corn (Maize)",
        "disease": "None (Healthy)",
        "status": "Healthy",
        "severity": "None",
        "cause": "N/A",
        "symptoms": [
            "Vibrant green uniform leaves with clean venation",
            "Robust stalk and ear development"
        ],
        "management": "Ensure adequate nitrogen supply during early growth stages.",
        "organic_solution": "Use composted manure and cover crops (clover, vetch).",
        "prevention": "Maintain soil health and optimal plant population density."
    },
    "grape black rot": {
        "crop": "Grape",
        "disease": "Black Rot",
        "status": "Diseased",
        "severity": "High",
        "cause": "Fungal pathogen Guignardia bidwellii",
        "symptoms": [
            "Small reddish-brown circular spots on leaf surface",
            "Infected berries turn brown, shrivel, and transform into hard black mummies",
            "Black pinhead-size fruiting bodies (pycnidia) inside spots"
        ],
        "management": "Spray Mancozeb, Ziram, or Myclobutanil fungicides starting at bud break.",
        "organic_solution": "Apply copper-based sprays. Remove all mummified berries from vines.",
        "prevention": "Prune foliage to maximize sunlight and wind ventilation through canopy."
    },
    "grape esca black measles": {
        "crop": "Grape",
        "disease": "Esca (Black Measles)",
        "status": "Diseased",
        "severity": "High",
        "cause": "Complex fungal vascular disease (Phaeomoniella, Phaeoacremonium)",
        "symptoms": [
            "Tiger-stripe pattern on leaves (yellowing/reddening between veins)",
            "Small dark spots (measles) on berries",
            "Drying of berry clusters and sudden vine apoplexy"
        ],
        "management": "Remove and burn severely infected wood tissue; apply wound paint after pruning.",
        "organic_solution": "Apply Trichoderma-based bio-fungicides to fresh pruning cuts.",
        "prevention": "Avoid pruning during rainy wet conditions to prevent spore entry."
    },
    "grape leaf blight isariopsis leaf spot": {
        "crop": "Grape",
        "disease": "Leaf Blight (Isariopsis Spot)",
        "status": "Diseased",
        "severity": "Moderate",
        "cause": "Pseudocercospora vitis fungus",
        "symptoms": [
            "Irregular brown spots on leaves with dark borders",
            "Underneath leaves show olive-black velvety spore growth",
            "Defoliation starting from lower leaves"
        ],
        "management": "Apply copper oxychloride or carbendazim sprays post-harvest and pre-bloom.",
        "organic_solution": "Spray Bordeaux mixture (copper sulfate + lime).",
        "prevention": "Destroy fallen leaves; ensure adequate vine spacing."
    },
    "grape healthy": {
        "crop": "Grape",
        "disease": "None (Healthy)",
        "status": "Healthy",
        "severity": "None",
        "cause": "N/A",
        "symptoms": [
            "Lush green foliage without necrotic spots",
            "Healthy fruit cluster development"
        ],
        "management": "Prune excess shoots to optimize canopy sun exposure.",
        "organic_solution": "Mulch vine bases with compost.",
        "prevention": "Regular vineyard scouting and soil testing."
    },
    "orange haunglongbing citrus greening": {
        "crop": "Orange / Citrus",
        "disease": "Citrus Greening (Huanglongbing / HLB)",
        "status": "Diseased",
        "severity": "Critical",
        "cause": "Bacterial pathogen Candidatus Liberibacter africanus/asiaticus spread by Asian citrus psyllid",
        "symptoms": [
            "Asymmetrical blotchy yellow mottle pattern on leaves",
            "Yellowing of leaf veins and shoot yellowing (yellow shoots)",
            "Small, lopsided, bitter green fruit that drops prematurely"
        ],
        "management": "Control Asian citrus psyllid vector with systemic insecticides (imidacloprid, thiamethoxam).",
        "organic_solution": "Use horticultural oil sprays and introduce beneficial insect predators (Tamarixia radiata).",
        "prevention": "Plant certified disease-free nursery stock. Remove infected trees immediately to prevent spread."
    },
    "peach bacterial spot": {
        "crop": "Peach",
        "disease": "Bacterial Spot",
        "status": "Diseased",
        "severity": "High",
        "cause": "Bacterium Xanthomonas arboricola pv. pruni",
        "symptoms": [
            "Small water-soaked angular spots on leaves turning purple-black",
            "Shot-hole appearance as infected leaf centers drop out",
            "Pitted spots, cracks, and gumming on fruit surface"
        ],
        "management": "Apply oxytetracycline or copper sprays at dormancy break.",
        "organic_solution": "Apply low rates of copper hydroxide mixed with lime to prevent leaf burn.",
        "prevention": "Select resistant peach cultivars (e.g., Candor, Reliance, Sentinel)."
    },
    "peach healthy": {
        "crop": "Peach",
        "disease": "None (Healthy)",
        "status": "Healthy",
        "severity": "None",
        "cause": "N/A",
        "symptoms": [
            "Healthy green leaves with smooth surface",
            "Unblemished bark and fruit skin"
        ],
        "management": "Apply balanced tree fertilizer and deep water during fruit development.",
        "organic_solution": "Apply organic compost around orchard root zones.",
        "prevention": "Annual pruning for light penetration and air circulation."
    },
    "pepper bell bacterial spot": {
        "crop": "Pepper (Bell)",
        "disease": "Bacterial Spot",
        "status": "Diseased",
        "severity": "High",
        "cause": "Bacterium Xanthomonas euvesicatoria",
        "symptoms": [
            "Small yellowish-green raised spots on leaf undersides",
            "Lesions turn brown with dark borders and water-soaked halos",
            "Leaves turn yellow and drop off, leaving fruits vulnerable to sunscald"
        ],
        "management": "Spray copper-based bactericides combined with mancozeb.",
        "organic_solution": "Spray neem oil or bio-bactericide (Bacillus subtilis). Practice 3-year crop rotation.",
        "prevention": "Use certified disease-free seeds; avoid handling plants when wet."
    },
    "pepper bell healthy": {
        "crop": "Pepper (Bell)",
        "disease": "None (Healthy)",
        "status": "Healthy",
        "severity": "None",
        "cause": "N/A",
        "symptoms": [
            "Dark green leaves with smooth margins",
            "Strong flowering and solid fruit set"
        ],
        "management": "Water evenly at plant base to prevent blossom end rot.",
        "organic_solution": "Add calcium and organic compost to soil.",
        "prevention": "Mulch soil surface to retain moisture balance."
    },
    "potato early blight": {
        "crop": "Potato",
        "disease": "Early Blight",
        "status": "Diseased",
        "severity": "Moderate",
        "cause": "Fungal pathogen Alternaria solani",
        "symptoms": [
            "Concentric target-board rings inside brown spots on older lower leaves",
            "Yellow chlorotic tissue surrounding brown leaf lesions",
            "Sunken dark lesions on tubers"
        ],
        "management": "Apply protective fungicides like chlorothalonil, mancozeb, or azoxystrobin.",
        "organic_solution": "Apply copper spray; prune off lower infected foliage.",
        "prevention": "Rotate crops with non-solanaceous plants. Ensure adequate nitrogen levels."
    },
    "potato late blight": {
        "crop": "Potato",
        "disease": "Late Blight",
        "status": "Diseased",
        "severity": "Critical",
        "cause": "Oomycete pathogen Phytophthora infestans",
        "symptoms": [
            "Large pale green to dark brown water-soaked lesions on leaves",
            "White cottony fungal growth on undersides of leaves during humid weather",
            "Rapid leaf collapse, brown rotting tubers emitting foul odor"
        ],
        "management": "Apply systemic fungicides like metalaxyl or cymoxanil immediately.",
        "organic_solution": "Apply copper hydroxide preventive sprays before wet humid weather sets in.",
        "prevention": "Destroy seed potatoes showing rot; plant late blight resistant potato varieties."
    },
    "potato healthy": {
        "crop": "Potato",
        "disease": "None (Healthy)",
        "status": "Healthy",
        "severity": "None",
        "cause": "N/A",
        "symptoms": [
            "Broad green leaves free of blighted edges",
            "Vigorous stem branching and tuber growth"
        ],
        "management": "Hill soil around plant stems as tubers grow.",
        "organic_solution": "Use compost tea and well-rotted manure.",
        "prevention": "Maintain drip irrigation to keep leaf canopy dry."
    },
    "raspberry healthy": {
        "crop": "Raspberry",
        "disease": "None (Healthy)",
        "status": "Healthy",
        "severity": "None",
        "cause": "N/A",
        "symptoms": [
            "Green compound leaves without rust spots or wilting",
            "Sturdy erect canes"
        ],
        "management": "Prune fruited canes to ground level after harvest.",
        "organic_solution": "Mulch with wood chips to suppress weeds.",
        "prevention": "Ensure well-draining soil to prevent root rot."
    },
    "soybean healthy": {
        "crop": "Soybean",
        "disease": "None (Healthy)",
        "status": "Healthy",
        "severity": "None",
        "cause": "N/A",
        "symptoms": [
            "Deep green trifoliate leaves",
            "Uniform pod formation along stem nodes"
        ],
        "management": "Monitor soil phosphorus and potassium levels.",
        "organic_solution": "Inoculate seed with Rhizobium bacteria for nitrogen fixation.",
        "prevention": "Practice standard crop rotation."
    },
    "squash powdery mildew": {
        "crop": "Squash",
        "disease": "Powdery Mildew",
        "status": "Diseased",
        "severity": "Moderate",
        "cause": "Fungi Podosphaera xanthii / Erysiphe cichoracearum",
        "symptoms": [
            "White talcum-powder-like spots on upper and lower leaf surfaces",
            "Leaves turn yellow, brown, and dry up into paper-like texture",
            "Premature leaf drop leading to sunburned squash fruit"
        ],
        "management": "Apply sulfur or potassium bicarbonate foliar sprays.",
        "organic_solution": "Spray milk-water solution (1:9 ratio) or neem oil on affected leaves.",
        "prevention": "Plant resistant squash varieties; ensure direct sunlight."
    },
    "strawberry leaf scorch": {
        "crop": "Strawberry",
        "disease": "Leaf Scorch",
        "status": "Diseased",
        "severity": "Moderate",
        "cause": "Fungus Diplocarpon earlianum",
        "symptoms": [
            "Small dark purple spots on upper leaf surfaces",
            "Spots enlarge and coalesce into dark reddish-purple scorched patches",
            "Leaf edges dry up and turn brown, resembling drought fire damage"
        ],
        "management": "Apply captan or thiram fungicides in spring.",
        "organic_solution": "Remove and burn old blighted leaf foliage after harvest renovate bed.",
        "prevention": "Avoid over-fertilizing with excess nitrogen."
    },
    "strawberry healthy": {
        "crop": "Strawberry",
        "disease": "None (Healthy)",
        "status": "Healthy",
        "severity": "None",
        "cause": "N/A",
        "symptoms": [
            "Vibrant green trifoliate leaves",
            "Abundant blossom and crown development"
        ],
        "management": "Mulch strawberry beds with clean straw.",
        "organic_solution": "Feed with compost and kelp meal.",
        "prevention": "Replace strawberry plants every 3-4 years."
    },
    "tomato bacterial spot": {
        "crop": "Tomato",
        "disease": "Bacterial Spot",
        "status": "Diseased",
        "severity": "High",
        "cause": "Bacterium Xanthomonas vesicatoria",
        "symptoms": [
            "Small dark water-soaked spots on leaves with yellow halos",
            "Leaf center dries and drops, giving a shot-hole appearance",
            "Raised dark scab-like spots on immature green tomatoes"
        ],
        "management": "Apply copper bactericides combined with mancozeb.",
        "organic_solution": "Spray liquid copper octanoate or Bacillus subtilis. Avoid overhead watering.",
        "prevention": "Use certified seed; sanitize stakes and cages."
    },
    "tomato early blight": {
        "crop": "Tomato",
        "disease": "Early Blight",
        "status": "Diseased",
        "severity": "Moderate to High",
        "cause": "Fungal pathogen Alternaria solani",
        "symptoms": [
            "Dark concentric bullseye rings on lower leaves",
            "Yellowing surrounding leaf lesions followed by leaf drop",
            "Dark sunken lesions near fruit stem attachment"
        ],
        "management": "Apply chlorothalonil, copper, or difenoconazole sprays.",
        "organic_solution": "Prune lower 12 inches of leaves to prevent soil splash. Apply copper fungicide.",
        "prevention": "Mulch soil around base; rotate nightshade crops yearly."
    },
    "tomato late blight": {
        "crop": "Tomato",
        "disease": "Late Blight",
        "status": "Diseased",
        "severity": "Critical",
        "cause": "Oomycete Phytophthora infestans",
        "symptoms": [
            "Large greasy dark green/brown leaf spots with white fuzzy mold underside",
            "Stems develop dark brown to black greasy lesions",
            "Firm brown leathery rot on tomato fruits"
        ],
        "management": "Apply systemic fungicides (cymoxanil, propamocarb) immediately upon sighting.",
        "organic_solution": "Apply copper sulfate preventive spray. Destroy infected plants immediately.",
        "prevention": "Plant resistant tomato cultivars (e.g., Defiant, Mountain Merit)."
    },
    "tomato leaf mold": {
        "crop": "Tomato",
        "disease": "Leaf Mold",
        "status": "Diseased",
        "severity": "Moderate",
        "cause": "Fungus Passalora fulva (Fulvia fulva)",
        "symptoms": [
            "Pale green or yellow spots on upper surface of older leaves",
            "Olive-green to velvety brown mold growth on leaf undersides",
            "Leaves turn brown, curl, and drop off"
        ],
        "management": "Apply copper or chlorothalonil fungicides; lower greenhouse humidity below 85%.",
        "organic_solution": "Increase greenhouse ventilation using exhaust fans. Spray neem oil.",
        "prevention": "Space tomato plants widely to improve canopy air movement."
    },
    "tomato septoria leaf spot": {
        "crop": "Tomato",
        "disease": "Septoria Leaf Spot",
        "status": "Diseased",
        "severity": "High",
        "cause": "Fungus Septoria lycopersici",
        "symptoms": [
            "Numerous small circular spots with gray centers and dark borders",
            "Tiny black specks (pycnidia) inside center of gray spots",
            "Severe leaf yellowing and defoliation from bottom of plant upward"
        ],
        "management": "Apply mancozeb or chlorothalonil fungicides every 7-10 days.",
        "organic_solution": "Remove infected lower leaves; apply copper fungicide or sulfur powder.",
        "prevention": "Stake tomato vines off the ground; mulch bed floor."
    },
    "tomato spider mites two spotted spider mite": {
        "crop": "Tomato",
        "disease": "Two-Spotted Spider Mites",
        "status": "Diseased (Pest Infection)",
        "severity": "High in Dry Weather",
        "cause": "Pest infestation by Tetranychus urticae",
        "symptoms": [
            "Fine yellow or white stippling dots on leaf surface",
            "Leaves turn bronze, dry out, and turn brown",
            "Fine silk webbing on leaf undersides and branch tips"
        ],
        "management": "Apply miticides such as abamectin or bifenazate.",
        "organic_solution": "Release predatory mites (Phytoseiulus persimilis). Spray insecticidal soap or neem oil.",
        "prevention": "Maintain adequate moisture; overhead misting reduces mite dust build-up."
    },
    "tomato target spot": {
        "crop": "Tomato",
        "disease": "Target Spot",
        "status": "Diseased",
        "severity": "Moderate",
        "cause": "Fungus Corynespora cassiicola",
        "symptoms": [
            "Small pinpoint water-soaked spots on leaves expanding to target-like rings",
            "Leaf spots coalesce causing leaf collapse and drop",
            "Sunken crater-like spots on tomato fruits"
        ],
        "management": "Spray azoxystrobin or chlorothalonil fungicides.",
        "organic_solution": "Apply copper octanoate; ensure plant rows are well spaced.",
        "prevention": "Keep foliage dry; eliminate host weeds."
    },
    "tomato yellow leaf curl virus": {
        "crop": "Tomato",
        "disease": "Yellow Leaf Curl Virus (TYLCV)",
        "status": "Diseased (Viral)",
        "severity": "Critical",
        "cause": "Geminivirus transmitted by Silverleaf Whitefly (Bemisia tabaci)",
        "symptoms": [
            "Severe stunting of plant growth and upright cupping of leaves",
            "Yellowing of leaf margins (chlorosis) between leaf veins",
            "Flower abortion resulting in severe fruit yield loss"
        ],
        "management": "Control whitefly vectors using imidacloprid, spirotetramat, or insecticidal soaps.",
        "organic_solution": "Use yellow sticky traps. Cover plants with fine insect mesh screens.",
        "prevention": "Plant TYLCV-resistant tomato hybrids (e.g., Tycoon, Inbar)."
    },
    "tomato mosaic virus": {
        "crop": "Tomato",
        "disease": "Tomato Mosaic Virus (ToMV)",
        "status": "Diseased (Viral)",
        "severity": "High",
        "cause": "Tobamovirus transmitted mechanically via contact and tools",
        "symptoms": [
            "Mottled light green and dark green mosaic patterns on leaves",
            "Leaf distortion, leaf fern-like narrowing ('shoestring' appearance)",
            "Internal browning and uneven ripening of tomato fruit"
        ],
        "management": "No chemical cure exists for viral infection. Remove infected plants.",
        "organic_solution": "Wash hands with milk or trisodium phosphate before handling plants.",
        "prevention": "Use virus-indexed seeds. Sanitize pruners between plants."
    },
    "tomato healthy": {
        "crop": "Tomato",
        "disease": "None (Healthy)",
        "status": "Healthy",
        "severity": "None",
        "cause": "N/A",
        "symptoms": [
            "Vibrant green compound leaves without spots or mottling",
            "Strong erect stems and healthy flowering clusters"
        ],
        "management": "Maintain consistent drip watering and balanced tomato fertilizer.",
        "organic_solution": "Apply compost tea, bone meal, and crushed eggshells for calcium.",
        "prevention": "Prune suckers and support with sturdy tomato cages."
    },
    "background": {
        "crop": "Non-Plant / Background",
        "disease": "No Plant Detected",
        "status": "N/A",
        "severity": "N/A",
        "cause": "Image does not contain a recognizable plant leaf",
        "symptoms": [
            "The image frame appears to contain non-plant subjects or unclear foliage"
        ],
        "management": "Please point the camera clearly at an infected or healthy plant leaf and capture again.",
        "organic_solution": "Ensure good lighting and single-leaf focus.",
        "prevention": "Hold camera steady 15-30 cm from leaf surface."
    }
}
