# 🔧 AutoTrack — Guide de démarrage

## Installation (à faire une seule fois)

### 1. Ouvre un Terminal sur ton Mac
Cherche "Terminal" dans Spotlight (Cmd + Espace)

### 2. Va dans le dossier du projet
```bash
cd chemin/vers/autotrack
```
Par exemple si tu as mis le dossier sur ton bureau :
```bash
cd ~/Desktop/autotrack
```

### 3. Installe les dépendances Python
```bash
pip3 install -r requirements.txt
```

---

## Lancer l'application

```bash
python3 app.py
```

Tu devrais voir :
```
✅ Base de données initialisée.
👤 Admin : admin / admin123
 * Running on http://0.0.0.0:5000
```

## Accéder à l'application

- **Sur ton PC** : ouvre http://localhost:5000
- **Sur un téléphone (même réseau WiFi)** : http://[IP_DE_TON_MAC]:5000
  - Pour trouver l'IP : Préférences Système → Réseau

---

## Compte par défaut

| Identifiant | Mot de passe | Rôle |
|-------------|--------------|------|
| admin       | admin123     | Admin |

⚠️ **Change le mot de passe admin dès la première connexion !**

---

## Structure du projet

```
autotrack/
├── app.py              ← Le programme principal
├── requirements.txt    ← Dépendances Python
├── instance/
│   └── autotrack.db    ← La base de données (créée automatiquement)
├── static/
│   └── uploads/        ← Photos des véhicules
└── templates/
    ├── base.html        ← Gabarit commun
    ├── login.html       ← Page de connexion
    ← dashboard.html    ← Page principale
    ├── nouvelle_fiche.html
    ├── detail_fiche.html
    ├── export.html
    └── admin.html
```

---

## Arrêter l'application
Dans le Terminal : **Ctrl + C**

## Prochaines étapes (déploiement en ligne)
Quand tu es prêt à mettre l'app accessible depuis partout :
- Option A : **Railway.app** (gratuit, simple, recommandé)
- Option B : **Render.com** (gratuit, un peu plus lent)
- Option C : **VPS OVH** (payant ~5€/mois, full contrôle)
