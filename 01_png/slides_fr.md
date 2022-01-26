%title: File formats 101
%author: x1mus

-> # File formats 101 - PNG : INTRO <-

<br>

## Qu'est ce qu'un fichier PNG ?
<br>
- **Portable Networks Graphics**
<br>
- *"lossless"*
<br>
- Norme ISO/IEC 15948:2004
<br>
- Caractéristiques disponible dans la [RFC 2083](https://datatracker.ietf.org/doc/html/rfc2083) ainsi que sur le site [libpng](http://www.libpng.org/pub/png/spec/1.2/PNG-Contents.html)

<br>

## D'autres types de fichiers images:
<br>
- BMP --> Premier type d'images qui ont vu le jour
<br>
- JPEG --> Utilisés pour les photographies couleurs (ou n'importe quelle image contenant beaucoup de tonalité ou de dégradés)
<br>
- GIF --> Utilisée principalement pour du text, du dessin de lignes, des captures d'écrans, des cartoons et animations
<br>
- PNG --> Un de meilleur format pour l'utilisation sur le web

------------------------------------------------------------

-> # File formats 101 - PNG : GLOBAL STRUCTURE <-
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

-> # File formats 101 - PNG : CHUNK'S STRUCTURE <-
<br>

oui

------------------------------------------------------------

-> # File formats 101 - PNG : LETTERS <-
<br>

oui

------------------------------------------------------------

-> # File formats 101 - PNG : IHDR <-
<br>

oui

------------------------------------------------------------

-> # File formats 101 - PNG : IDAT <-
<br>

oui

------------------------------------------------------------

-> # File formats 101 - PNG : IEND <-
<br>

oui

------------------------------------------------------------

-> # File formats 101 - PNG : OTHER CHUNKS <-
<br>

oui

------------------------------------------------------------