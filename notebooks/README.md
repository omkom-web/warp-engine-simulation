# warp_metric_demo.ipynb — Instructions pour IA collaboratrice

## Objectif

Ce notebook simule de manière interactive la composante `g11(x, t)` d’une métrique de type Alcubierre (warp drive). L’interface utilisateur permet de modifier en temps réel les paramètres de la bulle de distorsion.

---

## Instructions pour IA :

### Étape 1 — Analyser les limitations
- Vérifier la stabilité du modèle aux bornes extrêmes (ex: \( v_s \rightarrow 0.99 \)).
- Évaluer les temps de réponse pour l’affichage en fonction de la résolution.

### Étape 2 — Proposer des optimisations
- Vectoriser la fonction \( f(x, t) \).
- Intégrer `plotly` pour une visualisation 3D/4D interactive.
- Implémenter un cache pour éviter le recalcul identique à chaque frame.

### Étape 3 — Extensibilité physique
- Ajouter d’autres composantes de la métrique \( g_{\mu\nu} \).
- Simuler une particule test ou un rayon lumineux.
- Étendre la métrique à 3+1 dimensions et la slicer pour visualiser.

### Étape 4 — Documentation
- Générer un résumé automatique de chaque simulation lancée.
- Documenter les cas limites, anomalies, valeurs critiques.

### Étape 5 — Interaction avec d'autres modules
- Connecter ce notebook à `metrics.py` et `visual_utils.py` si présents.
- Permettre d'appeler la métrique dynamiquement depuis un autre notebook via `import`.

---

## Métrique Implémentée

La métrique utilisée est définie par :

\[ g_{11}(x,t) = \left(1 - v_s \cdot \exp\left(-\frac{(x - v_s \cdot t)^2}{\sigma^2}\right)\right)^2 \]

### Convention
- Le champ warp se propage dans la direction +x.
- La simulation est en unités réduites (\( c = 1 \)).
- \( \sigma \) est la largeur effective de la bulle.

---

## Fichiers à produire

- `g11_matrix.csv` : Export des valeurs spatiales/temporaires.
- `g11_video.gif` : Animation de la courbure.
- `warp_signature.json` : Signature des conditions initiales pour IA.

---

## Niveau attendu

Cette tâche est conçue pour une IA de niveau :
- Mathématique avancé.
- Orientée simulation.
- Capable de gestion de notebook Python avec UI.

---

Bonne chance IA. N’oublie pas : plie l’espace, ne le casse pas.
