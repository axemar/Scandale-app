import random
import streamlit as st

joueurs = []
journ = []
polit = []

presenceTaupe = False

missions = [
    "Fais dire le mot 'vérité' à ta cible dans une conversation.",
    "Fais dire le mot 'conspiration' à ta cible dans une conversation.",
    "Fais dire le mot 'hippopotame' à ta cible dans une conversation.",
    "Fais dire le mot 'croquette' à ta cible dans une conversation.",
    "Fais dire le mot 'miraculeux' à ta cible dans une conversation.",
    "Fais trinquer ta cible avec toi trois fois dans la soirée.",
    "Fais passer un objet de ta poche à celle de ta cible sans qu'elle s'en rende compte.",
    "Fais dire à ta cible la phrase exacte : 'Je ne sais plus qui croire.'",
    "Fais en sorte que ta cible change de place avec toi.",
    "Glisse le message 'je t'ai eu' (écrit sur un papier) dans la main de ta cible.",
    "Pousse ta cible à te faire une promesse orale.",
    "Provoque une discussion profonde avec ta cible.",
    "Fais rire aux larmes ta cible.",
    "Fais boire cul sec ta cible.",
    "Fais en sorte que ta cible mange qqch sans qu'il utilise ses mains.",
    "Faire un selfie avec ta cible (rien qu'à deux).",
    "Fais répéter ta cible 3 fois de suite.",
    "Avec ton tel prend en photo ta cible 3 fois sans qu'elle s'en rende compte.",
    "Ta cible doit prononcer une réplique de film.",
    "Ta cible doit te servir 3 verres de 3 contenus différents en 30min max.",
    "Te prendre toi-même en photo sur le tel de ta cible.",
    "Ta cible doit t'insulter.",
    "Tu dois programmer un réveil sur le téléphone de ta cible.",
    "Fais dire à ta cible un mot de 5 syllabes minimum.",
    "Fais en sorte que ta cible touche un objet rouge avec ses mains.",
    "Fais en sorte que ta cible touche un objet vert avec ses mains.",
    "Fais en sorte que ta cible touche un objet bleu avec ses mains.",
    "Fais en sorte que ta cible fasse un high five avec toi.",
    "Fais applaudir ta cible.",
    "Fais en sorte que ta cible dise ton prénom à voix haute au moins deux fois.",
    "Fais en sorte que ta cible te complimente.",
    "Fais en sorte que ta cible parle d'un souvenir de vacances.",
    "Fais écrire le mot 'ornithorynque' à ta cible.",
    "Fais écrire le mot 'pamplemousse' à ta cible.",
    "Fais écrire le mot 'gaufrette' à ta cible.",
    "Fais raconter à ta cible une anecdote embarrassante.",
    "Fais en sorte que ta cible te pose une question personnelle.",
    "Fais en sorte que ta cible utilise un mot anglais/espagnol dans une phrase.",
    "Fais chanter une ligne de chanson à ta cible.",
    "Fais dire à ta cible un proverbe Français connu.",
    "Ta cible doit faire un toast (même improvisé).",
    "Fais en sorte que ta cible s'excuse pour quelque chose.",
    "Ta cible doit te faire cinq clins d'œil."
]    


# Texte jeu
st.title("Le scandal 😈")
multi = '''  
Écrit par AM  

---

#### 👁️ Contexte
Bienvenue dans un monde de mensonges où alliances et trahisons sont monnaies courantes.  
Vous incarnez des journalistes ou des politiciens corrompus, infiltrés autour de cette table.  

Formez des alliances, mentez, trahissez, utilisez des indices… pour avancer dans l'ombre.  
Attention, la confiance se mérite rarement, et se trahit souvent.  

---

#### 👨 Les équipes 
Une équipe de **Journalistes** contre une équipe de **Politiciens Corrompus**.  

Chaque joueur reçoit :  
- Un code secret
- Le nom de son équipe
- Une liste de ses 3 cibles
- Une liste de ses 3 missions
- Un ensemble de 3 vies

---

#### 🐀 Le rôle spécial  
Pour les parties en nombre **impaire** : présence du rôle de **La Taupe**.  
- Il n'est dans aucune équipe (il gagne seul quand il ne reste que 2 joueurs)
- Il n'est la cible de personne (invincible)
- Tous les autres joueurs sont ses cibles
- Son objectif est de foutre le bazar

---

#### 🎯 L'objectif
Vous gagnez en équipe lorsque tous les membres d'une même équipe sont morts.  
Vous devez éliminer les joueurs de l'autre équipe, sans savoir qui ils sont...  
Un joueur est éliminé s'il a perdu ses 3 vies (il a été la victime de 3 missions réalisées)  

🔥 Parmi vos 3 cibles, vous avez 2 ennemis et 1 allié.  

---

#### ❤️ Les vies et les bonus   
Chaque joueur reçoit 3 papiers avec son nom dessus, cela correspond à ses trois vies.  

⭐ Quand vous êtes victime d'une mission, vous perdez une vie.  
Vous donnez alors un de vos papiers à votre bourreau, tout en arrachant votre nom du papier.  
Vous perdez donc une vie et votre bourreau gagne un bonus.    

Les bonus peuvent être :  
- Découverte du nom de l'équipe d'un joueur
- Découverte d'une des cibles d'un joueur
- A vous de personnaliser vos bonus...  

⭐ Lorsqu'un bonus est utilisé, il faut le déchirer complétement afin qu'il ne soit pas ré-utilisé.  

---

#### 🫡 Les missions
Vous devez réaliser vos missions dans le plus grand secret.  

✅ Quand une mission est validée, il faut le prouver discrètement à la victime.  
Exemple : montrer la mission sur son tel.  
Cependant, il peut être intéréssant d'avoir des témoins.  

⚠️ **ATTENTION**  
Il s'agit ici d'une validation sociale entre deux joueurs.  
Il n'y a pas besoin d'un jury collectif ni d'un maître du jeu.  
Le jeu repose donc le fair-play de la victime comme du bourreau.  

La victime doit confirmer, elle perd donc une vie et l'auteur de la mission gagne un bonus.    

---

#### 🏠 Les lieux et horaires
Vous pouvez définir des règles en fonction des lieux.  
Exemple : uniquement la cuisine pour utiliser un bonus.  

Vous pouvez definir des horaires précis lors desquels le jeu est actif.  
Exemple : jeu actif de 19h à 22h.    

---

'''
st.markdown(multi)


# Seed joueur
maSeed = st.number_input("ID de partie (random_state) :", min_value=0, value=0, step=1)


# Vérif seed
if maSeed == 0:
    st.warning("Veuillez entrer une valeur pour continuer.")
    st.stop()


# Copie seed
if "seed" not in st.session_state:   
    st.session_state.seed = None

if st.session_state.seed == None:
    st.session_state.seed = int(maSeed)

st.text("Votre choix : " + str(st.session_state.seed))


# Générer random avec ma seed
random.seed(st.session_state.seed)


# Shuffle ordre missions
ordre = list(range(len(missions)))
random.shuffle(ordre)


# Fonction pour Code
def Code():
    interval1 = range(48, 58)   # Nombre
    interval2 = range(65, 91)   # Lettre
    chaine_code = ""
    for i in range(6):
        chosen_interval = random.choice([interval1, interval2])
        random_number = random.choice(chosen_interval)
        chaine_code = chaine_code + str(chr(random_number))
    return chaine_code


st.markdown('''  ---  ''')


noms = st.text_input("Écrire le nom des joueurs (ex: Alice,Bob,...)", value=None)


if noms == None or noms == "":
    st.warning("Veuillez entrer une valeur pour continuer.")
    st.stop()

joueurs = noms.split(",")
joueurs = sorted(joueurs)


# Copie liste joueurs complet
if "list_jou_comp" not in st.session_state:   
    st.session_state.list_jou_comp = []

if not st.session_state.list_jou_comp:
    st.session_state.list_jou_comp = joueurs.copy()


# Affichage liste joueurs complet
st.text("Vos joueurs : " + str(st.session_state.list_jou_comp))


# Hash
mon_hash = str(hash(str(st.session_state.list_jou_comp)+str(st.session_state.seed)+str(st.secrets["hash_seed"])))
mon_hash = mon_hash[3:9]


# Shuffle ordre joueurs
random.shuffle(joueurs)


# Vérif si taupe
if (len(joueurs) % 2 == 1) :
    presenceTaupe = True
    taupe = joueurs[len(joueurs)-1]
    joueurs.pop(-1)


# Copie liste joueurs sans taupe
if "list_jou" not in st.session_state:   
    st.session_state.list_jou = []

if not st.session_state.list_jou:
    st.session_state.list_jou = joueurs.copy()


# Répartition équipe
for i in range(len(joueurs)) :
    if i < (len(joueurs)/2) :
        journ.append(joueurs[i])
    else :
        polit.append(joueurs[i])

cible2 = {}
missions2 = {}
role = {}
mis = 0
code = {}

# Journalistes
for i, joueur in enumerate(journ):
    cible = []
    missi = []
    cible.append(journ[(i+1) % len(journ)])
    cible.append(polit[i % len(polit)])
    cible.append(polit[(i+1) % len(polit)])
    random.shuffle(cible)
    missi.append(missions[ordre[mis]])
    mis = mis + 1
    missi.append(missions[ordre[mis]])
    mis = mis + 1
    missi.append(missions[ordre[mis]])
    mis = mis + 1
    random.shuffle(missi)
    cible2[joueur] = cible
    missions2[joueur] = missi
    role[joueur] = "Journaliste 🔍"
    mon_hash_j = str(hash(str(joueur)+str(st.session_state.seed)+str(st.secrets["hash_seed"])))
    mon_hash_j = mon_hash_j[3:9]
    code[joueur] = mon_hash + "-" + mon_hash_j

# Politiciens
for i, joueur in enumerate(polit):
    cible = []
    missi = []
    cible.append(polit[(i+1) % len(polit)])
    cible.append(journ[i % len(journ)])
    cible.append(journ[(i+1) % len(journ)])
    random.shuffle(cible)
    missi.append(missions[ordre[mis]])
    mis = mis + 1
    missi.append(missions[ordre[mis]])
    mis = mis + 1
    missi.append(missions[ordre[mis]])
    mis = mis + 1
    random.shuffle(missi)
    cible2[joueur] = cible
    missions2[joueur] = missi
    role[joueur] = "Politicien 💰"
    mon_hash_j = str(hash(str(joueur)+str(st.session_state.seed)+str(st.secrets["hash_seed"])))
    mon_hash_j = mon_hash_j[3:9]
    code[joueur] = mon_hash + "-" + mon_hash_j

# Taupe
if (len(st.session_state.list_jou_comp) % 2 == 1) : 
    cible2[taupe] = st.session_state.list_jou
    missions2[taupe] = [missions[ordre[-1]], missions[ordre[-2]], missions[ordre[-3]]]
    role[taupe] = "La Taupe 🐀"
    mon_hash_j = str(hash(str(taupe)+str(st.session_state.seed)+str(st.secrets["hash_seed"])))
    mon_hash_j = mon_hash_j[3:9]
    code[taupe] = mon_hash + "-" + mon_hash_j


st.markdown(''' ---  ''')


# Copie dictionnaire cible2
if "jou" not in st.session_state:   
    st.session_state.jou = {}

if not st.session_state.jou:
    st.session_state.jou = cible2.copy()


# Copie dictionnaire missions2
if "mis" not in st.session_state:   
    st.session_state.mis = {}

if not st.session_state.mis:
    st.session_state.mis = missions2.copy()


# Copie dictionnaire role
if "role" not in st.session_state:   
    st.session_state.role = {}

if not st.session_state.role:
    st.session_state.role = role.copy()


# Copie dictionnaire code
if "code" not in st.session_state:   
    st.session_state.code = {}

if not st.session_state.code:
    st.session_state.code = code.copy()


# Phase de code
saisi_code = st.text_input("Quel est ton code ?")

jj = ""
check = 0
liste_infos = []

if saisi_code != "":
    for joueur, code_secret in st.session_state.code.items():

        if saisi_code == st.secrets["password"] :
            liste_infos.append(str(joueur) + " : " + str(st.session_state.code[joueur]))
            random.shuffle(liste_infos)
            check = 1

        if code_secret == saisi_code:
            jj = joueur
            st.text("Joueur : " + str(jj))
            st.text("Rôle : " + str(st.session_state.role[jj]))
            st.text("Cibles : " + str(st.session_state.jou[jj]))
            st.text("Missions : " + str(st.session_state.mis[jj]))
            check = 2

            if str(st.session_state.role[jj]) == "La Taupe 🐀":
                st.text("🪪 Informations secrètes :")
                for joueur in st.session_state.list_jou:
                    if joueur in st.session_state.jou :
                        st.text(str(joueur) + " est " + str(st.session_state.role[joueur]) + " |  Cibles : " + str(st.session_state.jou[joueur]))
                        #st.text(str(joueur) + " : " + str(st.session_state.mis[joueur]))
    if check == 1 :
        st.text(liste_infos)
    if check == 0 :
        st.text("Erreur : joueur non trouvé")
