# SGS — IA & Conformité : Présentation Interactive

> Présentation web autonome (HTML unique, zéro dépendance serveur) expliquant comment l'Intelligence Artificielle transforme les démarches de mise en conformité ISO/GFSI dans le contexte du groupe SGS.

---

## 🏗️ Architecture du fichier

Un seul fichier **`ia-conformite-presentation.html`** contient :

| Bloc | Lignes | Rôle |
|---|---|---|
| `<style>` | ~1–792 | Système de design complet (variables CSS, composants, animations) |
| `<body>` sidebar | ~797–896 | Navigation latérale + barre de progression |
| `<body>` slides | ~913–2634 | Les 18 slides de contenu |
| `<script>` | ~2637–2798 | Navigation, animations, particules |

---

## 🎨 Système de Design

### Palette de couleurs (variables CSS)
```css
--bg          : #0d1117   /* Fond principal, très sombre */
--bg2         : #131a2e   /* Fond secondaire */
--bg3         : #1a2040   /* Fond cartes */
--bg4         : #1d2340   /* Fond cartes flip back */
--accent      : #f37021   /* Orange SGS — couleur primaire */
--amber       : #f59e0b   /* Ambre — IA déterministe */
--green       : #10b981   /* Vert — succès, conformité */
--red         : #ef4444   /* Rouge — alertes, limites */
--cyan        : #06b6d4   /* Cyan — traçabilité, digital */
--text        : #f0f4ff   /* Texte principal */
--text2       : #a8b3cf   /* Texte secondaire */
--text3       : #5a6585   /* Texte tertiaire, labels */
```

### Typographie
- **Titres** : `Montserrat 700/800` — impact, premium
- **Corps** : `Inter 400/600` — lisibilité maximale
- **Code** : `JetBrains Mono` — extraits techniques
- **Import** : Google Fonts (CDN, pas de téléchargement)

### Tailles de police (variables CSS `--fs-XX`)
```css
--fs-10 : 0.625rem   → Labels, hints
--fs-11 : 0.6875rem  → Texte secondaire
--fs-12 : 0.75rem    → Corps compact
--fs-13 : 0.8125rem  → Corps flip card back ✨
--fs-14 : 0.875rem   → Corps standard, descriptions
--fs-15 : 0.9375rem  → Titres flip card back
--fs-17 : 1.0625rem  → Descriptions slides
--fs-18 : 1.125rem   → Titres flip card front
--fs-24 : 1.5rem     → Grandes valeurs
--fs-30 : 1.875rem   → Badges, KPI
--fs-42 : 2.625rem   → Titres slides (h1)
```

---

## 🃏 Flip Cards — Principes de Design

### Structure HTML
```html
<div class="flip-card" onclick="this.classList.toggle('flipped')">
  <div class="fci">                     <!-- Container 3D -->
    <div class="fc-front">              <!-- Recto (visible) -->
      <div class="fc-icon"><i class="fas fa-..."></i></div>
      <div class="fc-title">Titre</div>
      <div class="fc-hint">Sous-titre</div>
      <div class="fc-flip-hint">⟳ Détail</div>
    </div>
    <div class="fc-back">               <!-- Verso (au clic) -->
      <div class="fc-back-title">Titre détail</div>
      <div class="fc-back-body">Texte libre...</div>
      <!-- OU liste -->
      <ul>
        <li><i class="fas fa-..."></i> Point clé</li>
      </ul>
    </div>
  </div>
</div>
```

### Règles de contenu (fond)
- **Recto** : 1 icône FontAwesome large + 1 titre court (2-3 mots) + 1 hint (stat ou sous-titre)
- **Verso** : 1 titre + soit un texte libre court, soit une liste de 3-6 points
- **Max. points par liste** : 6 (3 colonnes) ou 4 (2 colonnes)
- **Longueur texte** : préférer des phrases courtes (< 15 mots/point)
- **Termes techniques** : mettre en `<em>` ou `<span class="code-badge">` → ils ne se coupent pas

### Règles de forme (CSS)
- **Grilles** : `.flip-grid-2` (2 colonnes, `min-height: 300px`) ou `.flip-grid-3` (3 colonnes, `min-height: 260px`)
- **Icônes** : 90×90px circulaires, effet `iconGlow` pulsé (rendu via `!important` du bloc WOW)
- **Glassmorphism** : `backdrop-filter: blur(12px)` + gradient sombre sur le recto
- **Caesure** : `hyphens: auto; lang="fr"` sur `<html>` → césure automatique française
- **Retour à la ligne** : `overflow-wrap: break-word` sur tous les éléments `.fc-back`
- **Termes protégés** : `.fc-back .code-badge, .fc-back em { white-space: nowrap; }`

---

## 📐 Layouts Disponibles

| Classe | Colonnes | Usage |
|---|---|---|
| `.grid-2` | 2 × 1fr | Contenu bipartite (ex: LLM vs Code) |
| `.grid-3` | 3 × 1fr | 3 cartes informatives |
| `.grid-4` | 4 × 1fr | KPIs / statistiques |
| `.flip-grid-2` | 2 flip cards | Comparatifs longs |
| `.flip-grid-3` | 3 flip cards | 6+ cas d'usage |
| `.flow-row` | Horizontal flex | Processus / étapes |
| `.compare-wrap` | 3 (col / vs / col) | Avant vs Après |

### Composants spéciaux
- **`.quote-block`** — Citation mise en évidence (bordure gauche orange)
- **`.highlight-box`** — Encadré d'attention (`.amber`, `.green` disponibles)
- **`.timeline`** — Étapes chronologiques verticales
- **`.kpi-card`** — Valeur métrique avec animation compteur au changement de slide
- **`.matrix`** — Tableau de comparaison normes/outils

---

## 🪄 Effets Visuels & Animations

### Animations d'entrée
Chaque `card`, `flip-card`, `timeline-item`, `kpi-card` s'anime à l'entrée du slide via :
```css
@keyframes slideFadeUp {
  0%   → opacity:0, translateY(24px), scale(0.97)
  100% → opacity:1, translateY(0),    scale(1)
}
```
Délais décalés automatiquement par `:nth-child`.

### Effets Hover
| Élément | Effet |
|---|---|
| `.card` | `translateY(-6px) scale(1.015)` + glow orange |
| `.flip-card` | Ombre profonde + anneau orange |
| `.fc-icon` | `scale(1.08)` + glow amplifié |
| `.kpi-card` | `translateY(-4px) scale(1.02)` |
| `.fc-front` | Shimmer sweep (reflet lumineux) |
| `.img-3d` | Ombre renforcée + glow orange |

### Icônes Pulsantes
Les `.fc-icon` ont un `animation: iconGlow 3s ease-in-out infinite` qui pulse doucement le halo orange (ou la couleur de la variante : amber, green, red, cyan).

### Compteur KPI
À chaque changement de slide, les `.kpi-val` s'animent de 0 jusqu'à leur valeur réelle via une fonction `animateCounters()` avec easing cubique.

### Particules (slide Couverture)
Un canvas avec 55 particules orange animées + réseau de lignes entre particules proches (inspiré D3 force-graph).

---

## 🖼️ Assets Visuels

| Fichier | Usage | Slide |
|---|---|---|
| `ai_compliance_3d.png` | Illustration IA (générée) | Couverture |
| `factory_iot_3d.png` | Usine IoT (générée) | Architectures hybrides |
| `0ugL9myc.png` | Logo SGS Excellence | Conclusion / SGS |
| `9ljjUGl0.jpg` | Vision AR en usine | - *(retiré du slide 02 — trop lourd)* |
| `Er5GH5IJ.jpg` | Illustration certification | ISO 42001 |
| `U5VdQVSH.jpg` | Smart production line | ISO 22000 Impact |

---

## 🧭 Navigation

| Action | Commande |
|---|---|
| Slide suivant | `→` ou `Space` ou bouton `›` |
| Slide précédent | `←` ou bouton `‹` |
| Plein écran | `F` ou bouton `⛶` |
| Réduire sidebar | Bouton `‹` en haut du menu |
| Retourner flip card | **Clic** sur la carte |

---

## 📁 Structure du Dossier

```
SGS_IA4NORM/
├── ia-conformite-presentation.html   ← Fichier principal (TOUT-EN-UN)
├── ia-conformite-presentation-v0.html ← Version d'origine (NE PAS MODIFIER)
├── README.md                          ← Ce fichier
├── enhance.py                         ← Script Python de refactoring
├── ai_compliance_3d.png
├── factory_iot_3d.png
├── 0ugL9myc.png
├── 9ljjUGl0.jpg
├── Er5GH5IJ.jpg
└── U5VdQVSH.jpg
```

---

## 📋 Plan des 18 Slides

| # | ID | Titre | Section |
|---|---|---|---|
| 01 | `slide-0` | Couverture & enjeux | Introduction |
| 02 | `slide-1` | Pourquoi l'IA maintenant ? | Introduction |
| 03 | `slide-2` | IA générative vs déterministe | Comprendre l'IA |
| 04 | `slide-3` | LLM : forces & limites | Comprendre l'IA |
| 05 | `slide-4` | IA déterministe & code | Comprendre l'IA |
| 06 | `slide-5` | Architectures hybrides | Comprendre l'IA |
| 07 | `slide-6` | Panorama normes ISO/GFSI | Applications |
| 08 | `slide-7` | ISO 9001 Qualité | Applications |
| 09 | `slide-8` | ISO 14001 & 45001 | Applications |
| 10 | `slide-9` | ISO 22000 / GFSI | Applications |
| 11 | `slide-9b` | ISO 22000 — Matrice & Impact *(nouveau)* | Applications |
| 12 | `slide-10` | Audit assisté IA | Applications |
| 13 | `slide-11` | Métriques & validation | Mise en œuvre |
| 14 | `slide-12` | Défis & garde-fous | Mise en œuvre |
| 15 | `slide-13` | Roadmap d'implémentation | Mise en œuvre |
| 16 | `slide-14` | Conclusion & next steps | Mise en œuvre |
| 17 | `slide-15` | ISO 42001 — Standard IA | Services SGS |
| 18 | `slide-16` | SGS — Certification ISO 42001 | Services SGS |

---

## ⚙️ Modifier la Présentation

### Changer une couleur globale
Modifier la variable dans `:root` au début du `<style>` :
```css
:root {
  --accent: #f37021;   /* Orange SGS → changer ici pour toute la présentation */
}
```

### Ajouter un slide
1. Ajouter un `<div class="slide" id="slide-N">` dans la `.slide-area`
2. Ajouter un `<div class="nav-item" data-slide="N">` dans le sidebar
3. Ajouter le titre dans le tableau `const titles = [...]` dans le `<script>`
4. Incrémenter les numéros suivants dans le sidebar

### Modifier la taille des flip cards
```css
/* Dans le <style> */
.flip-grid-3 .flip-card,
.flip-grid-3 .flip-card .fci,
.flip-grid-3 .fc-front,
.flip-grid-3 .fc-back { min-height: 260px; }  /* ↑ augmenter si débordement */
```

### Bonnes pratiques flip card back
- ✅ Utiliser `<ul><li>` pour les listes (elles bénéficient du flex + gap élégant)
- ✅ Utiliser `<em>` pour les termes techniques (protégés du word-wrap)
- ✅ Utiliser `<span class="tag tag-amber">Python</span>` pour les technos
- ❌ Éviter les longues chaînes sans espace (ex: `CamelCaseVeryLong`)
- ❌ Éviter plus de 6 items de liste dans une grille 3 colonnes

---

*Présentation réalisée avec HTML/CSS/JS vanilla · FontAwesome 6 · Google Fonts · Chart.js · Pas de framework*
