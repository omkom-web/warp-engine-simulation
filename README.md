# WARP ENGINE — Moteur de distorsion spaciale simulé

> "La réalité ne nous impose rien. Elle attend qu’on la plie."

Warp Engine est un projet open-source expérimental qui simule les effets d'une **métrique de type Alcubierre** permettant de conceptualiser un moteur à distorsion (warp drive). Il permet la **visualisation 2D, 3D et 4D** des composantes du tenseur métrique, avec export vers des logiciels libres de simulation avancée comme **Blender** ou **ParaView**.

---

## Objectifs

- Simuler les composantes du tenseur \( g_{\mu\nu} \) dans une bulle de distorsion mobile.
- Visualiser la métrique dans le temps et l’espace (2D → 4D).
- Générer des fichiers de surfaces exploitables (.obj, .csv) pour visualisation scientifique.
- Préparer l’extension vers des dimensions supplémentaires (théorie des cordes).

---

## Arborescence

```plaintext
warp_engine/
├── core/
│   └── metrics.py          # Modèles mathématiques (métriques)
├── render/
│   ├── 2d_matplotlib/      # Visualisation simple
│   ├── 3d_plotly/          # Surface interactive
│   ├── utils/
│   │   └── export_tools.py # Export OBJ et CSV
├── data/
│   ├── g11_surface.obj     # Surface 3D à t=10
│   └── g11_series/         # Animation .csv (30 frames)
├── template/
│   └── warp_surface_template.blend # Fichier Blender préparé
├── exporter.py             # Lancement CLI de tous les exports
└── README.md
```

---

## Instructions rapides

### 1. Lancer la génération depuis la racine :

```bash
python exporter.py
```

### 2. Visualiser dans ParaView :

- File > Open > `g11_series/g11_t0000.csv`
- Cocher “Open Time Series”
- Appliquer un Warp By Scalar

### 3. Visualiser dans Blender :

- File > Import > Wavefront (.obj) → `data/g11_surface.obj`
- Appliquer un Subdivision Surface, activer Smooth Shading

---

## Pour les IA collaboratrices

### Objectifs :

- Optimiser les performances (calculs vectoriels, GPU, etc.).
- Étendre à \( 3+1 \) ou \( 9+1 \) dimensions (string theory).
- Ajouter géodésiques (trajectoires de particules ou rayons lumineux).
- Ajouter détection automatique de singularités dans la métrique.
- Générer la même pipeline dans d’autres métriques (Kerr, Schwarzschild, etc.).

### Modules à améliorer :

- `metrics.py` (ajouter d'autres métriques paramétrables).
- `export_tools.py` (format .stl, .vtp, .usd).
- Ajout d'un `warp_analytics.py` pour extraire les signatures physiques clés.

---

## À venir

- Générateur de visualisation 4D par slicing.
- Interface web interactive (Streamlit / Jupyterlite).
- Import direct dans Unity ou Unreal Engine pour visualisation VR/AR.

---

## Licence

MIT – libre à utiliser, modifier, explorer et plier.

---

## Crédits

- Idée originale : @cubilizer
- Code et modélisation : Équipe Warp Hacker
- Design manifeste & AI ops : GPT Warp Assembly v1.0
