%title: File formats 101
%author: x1mus

-> # PNG - Introduction <-

<br>

## Qu'est ce qu'un fichier PNG ?
<br>
- **Portable Networks Graphics**
<br>
- lossless, portable, well-compressed, bitmapped image (définition de chaque pixel)
<br>
- indexed-color, grayscale, truecolor
<br>
- Norme ISO/IEC 15948:2004
<br>
- Caractéristiques disponible dans la [RFC 2083](https://datatracker.ietf.org/doc/html/rfc2083) ainsi que sur le site [libpng](http://www.libpng.org/pub/png/spec/1.2/PNG-Contents.html)

<br>

## Un objectif - Remplacer le format GIF:
<br>
- Ce qu'avait GIF :
<br>
	- 256 couleurs
	- Accessible
	- Affichage progressif
	- Gestion de l'opacité / transparence
	- Informations auxiliaires
	- Indépendant de l'architecture
	- Efficace avec une compression à 100% lossless
<br>
- Ce qu'ajoute PNG:
<br>
	- Couleurs jusqu'à 48 bits/pixel
	- Nuances de gris jusqu'à 16 bits/pixel
	- Canal *alpha* complet
	- Information gamma
	- Fiable (détection de corruption)
	- Affichage progressif + rapide

------------------------------------------------------------

-> # PNG - Représentation des données <-

<br>
1. **Entiers et ordres des octets** --> Entier non-signé (MSB first)

<br>
2. **Valeur des couleurs** --> Nuances de gris ou triplet RGB

<br>
3. **Disposition d'une image** --> Tableau rectangulaire de pixels
	<br>
	- Chaque pixel apparait de gauche à droite dans une "scanline"
	- Chaque scanline apparait de haut en bas
	<br>
	- Taille pixel : bit-depth (nombre de bits par sample)
	<br>
	- Il existe 3 types de pixels différents:
		1. [Indexed-color](https://www.pcmag.com/encyclopedia/term/indexed-color) : 1 sample (index vers une palette)
		2. Grayscale : 1 sample (niveau de gris)
		3. Truecolor : 3 samples (rgb)
	<br>
	- De plus, "grayscale" et "truecolor" peuvent inclure un canal alpha

<br>
4. **Canal alpha** --> Représente la transparence d'un pixel
	- Une autre façon de gérer la transparence ? le chunk tRNS

<br>
5. **Filtrage** --> Permet d'améliorer la compression future d'une image

<br>
6. **Entrelacement** --> Permet l'affichage d'une image de manière progressive
	- Méthode 0 : Stocker de manière séquentielle
	- Méthode 1 : Algorithme Adam7

<br>
7. **Correction gamma** --> Chunk gAMA, ajout de données afin d'obtenir un résultat se rapprochant le + possible de la réalité

<br>
8. **Chaînes de caractères** --> Possibilité d'ajout de texte (latin-1)

------------------------------------------------------------

-> # PNG - Structure globale <-
<br>

- Utilisation de chunks (contenant diverses informations)
- Le PNG le plus simple possible ne contient que **3** chunks \!
<br>

┌────────────────┐
│      SIGN      │
├────────────────┤
│      IHDR      │
├────────────────┤
│                │
│      IDAT      │
│                │
├────────────────┤
│      IEND      │
└────────────────┘

<br>
- SIGN --> Définis le type de fichier (Signature/magic number)
	- L'extension ne définis pas le type de fichier
	- Pour le format PNG, la signature est : "89 50 4E 47 0D 0A 1A 0A" ≈ ".PNG ...."

------------------------------------------------------------

-> # PNG - Structure d'un chunk <-
<br>

oui

------------------------------------------------------------

-> # PNG - Compression <-
<br>

oui

------------------------------------------------------------

-> # PNG - Algorithmes de filtrage <-
<br>

oui

------------------------------------------------------------

-> # PNG - Règles sur l'ordre des chunks <-
<br>

oui

------------------------------------------------------------

-> # PNG - Informations complémentaires <-
<br>

oui

------------------------------------------------------------