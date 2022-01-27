%title: File formats 101
%author: x1mus

-> # PNG - Introduction <-

<br>

## Qu'est ce qu'un fichier PNG ?
<br>
- *Portable Networks Graphics*
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
1. *Entiers et ordres des octets* --> Entier non-signé (MSB first)

<br>
2. *Valeur des couleurs* --> Nuances de gris ou triplet RGB

<br>
3. *Disposition d'une image* --> Tableau rectangulaire de pixels
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
4. *Canal alpha* --> Représente la transparence d'un pixel
	- Une autre façon de gérer la transparence ? le chunk tRNS

<br>
5. *Filtrage* --> Permet d'améliorer la compression future d'une image

<br>
6. *Entrelacement* --> Permet l'affichage d'une image de manière progressive
	- Méthode 0 : Stocker de manière séquentielle
	- Méthode 1 : Algorithme Adam7

<br>
7. *Correction gamma* --> Chunk gAMA, ajout de données afin d'obtenir un résultat se rapprochant le + possible de la réalité

<br>
8. *Chaînes de caractères* --> Possibilité d'ajout de texte (latin-1)

------------------------------------------------------------

-> # PNG - Structure globale <-

<br>
- Utilisation de chunks (contenant diverses informations)
- Le PNG le plus simple possible ne contient que *3* chunks \!
- Ajout de chunks supplémentaires possible (auxiliaire/critique)
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
Un chunk est composé de 4 champs distincts
<br>

┌────────┬──────┬──────┬─────┐
│ LENGTH │ TYPE │ DATA │ CRC │
└────────┴──────┴──────┴─────┘

<br>
- _Longueur :_ 4 octets non-signé - Se réfère à la longueur du champ "data"
<br>
- _Type :_ 4 octets - Code de 4 lettres ASCII (maj/min)
<br>
- _Data :_ Données liées au chunk (peut être 0)
<br>
- _CRC :_ 4 octets - Calculé sur le type + data

<br>
Le type d'un chunk est soumis a des conventions de nommage afin de garantir de la flexibilité, évolutivité, ...

<br>
1. *Première lettre* --> Majuscule = Critique / Minuscule = Auxiliaire
	- _Intuition :_ Nécéssité du chunk

<br>
2. *Deuxième lettre* --> Majusucule = Publique / Minuscule = Privé
	- _Intuition :_ Défini dans le standard ou défini par le public

<br>
3. *Troisième lettre* --> Majusucule = Norme / Minuscule = Expansion future
	- _Intuition :_ Tout le temps en majuscule actuellement

<br>
4. *Quatrième lettre* --> Majusucule = Copie non sûr / Minuscule = Copie sûr
	- _Intuition :_ Le chunk est-il dépendant des données de l'image ?

<br>
```
bLOb  <-- 32 bit chunk type code represented in text form
||||
|||+- Safe-to-copy bit is 1 (lower case letter; bit 5 is 1)
||+-- Reserved bit is 0     (upper case letter; bit 5 is 0)
|+--- Private bit is 0      (upper case letter; bit 5 is 0)
+---- Ancillary bit is 1    (lower case letter; bit 5 is 1)
.
Therefore, this name represents an ancillary, public, safe-to-copy chunk.
```

<br>
Le CRC est calculé selon la méthode standard, en utilisant ce polynôme :
`x^32+x^26+x^23+x^22+x^16+x^12+x^11+x^10+x^8+x^7+x^5+x^4+x^2+x+1`

------------------------------------------------------------

-> # PNG - Caractéristiques de chunks <-
<br>

_1. Chunks critiques_
	<br>
	- *IHDR (Image HeaDeR)*
		<br>
		- Width (4) --> Largeur de l'image en pixels
		<br>
		- Height (4) --> Hauteur de l'image en pixels
		<br>
		- Bit depth (1) --> Représente le nombre de bits/sample (1, 2, 4, 8 ou 16)
		<br>
		- Color type (1) --> Inteprétation de l'image (truecolor / grayscale / plte / ...)
		<br>
		- Compression method (1) --> Comment est effécutée la compression ("deflate/inflate compression with a 32K sliding window)
		<br>
		- Filter method (1) --> Quelle méthode de filtrage est utilisée avant la compression ("adaptive filtering with five basic filter types")
		<br>
		- Interlace method (1) --> Entrelacement utilisé (no / adam7)
	<br>
	- *PLTE (PaLeTtE)*
		<br>
		- Pallette de couleur avec 256 entrées (couleurs les + utilisées)
		<br>
		- Chaque entrée est une combinaison de RGB
	<br>
	- *IDAT (Image DATa)*
		<br>
		- Contient les données de l'image (pixels)
		<br>
		- Afin d'obtenir les données dans les chunks, il faudra (pour chaque scanline):
		`1. Filtrer les données`
		`2. Compresser celles-ci `
		<br>
		- Retrouver les données : inverser le processus
	<br>
	- *IEND (Image END/trailer)*
		<br>
		- Marque la fin du fichier PNG
		<br>
		- Ne contient pas de données

<br>
_2. Chunks auxiliaires_
	<br>
	- *bKGD (Background color)* --> Spécifie une couleur de fond par défaut
	<br>
	- *cHRM (Primary chromaticities and white point)*
	<br>
	- *gAMA (Image gamma)* --> Spécifier la luminosté de la photo afin de respecter au mieux le scénario réel
	<br>
	- *hIST (Image histogram)* --> Approximation de la fréquence d'utilisation d'un couleur dans une palette
	<br>
	- *pHYs (Physical pixel dimension)* --> Spécifie la dimension physique d'un pixel/ratio d'affichage
	<br>
	- *sBIT (Significant bits)*
	<br>
	- *tEXt (Textual data)* --> Informations supplémentaires
	<br>
	- *tIME (Image last-modification time)*
	<br>
	- *tRNS (Transparency)* --> Indication de l'utilisation de la transparence
	<br>
	- *zTXT (Compressed textual data)* --> Pareil que tEXt mais compressé
	<br>

<br>
_3. D'autres chunks peuvent être créé et ajouté au standard s'ils sont prouvés utiles/essentiels._

------------------------------------------------------------

-> # PNG - Deflate/inflate compression <-
<br>

Même algorithme utilisé dans les fichiers zip, zlib, ...
- Un seul flux compressé peut être séparés entre plusieurs chunk IDAT
- Si vous souhaitez plus de détails : [RFC-1951](https://datatracker.ietf.org/doc/html/rfc1951)

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


TO-DO algo : CRC / compression method / filter method / adam7