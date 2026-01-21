### Le language HTML

1. HTML

HyperText Markup Language *Langage de balises hypertexte*

Un fichier `.html` est un fichier de texte (comme le markdown par exemple). On ouvre un fichier de 2 façons :
- le développeur => avec un éditeur de code (ex:VisualStudio Code)
- l'utilisateur => avec un navigateur (ex : firefox)

Le plus souvent les balises html sont en couple (ouvrante / fermante) mais il existe aussi des balises *orpheline*:
- `<MaBalise></MaBalise>`
- `<Mabalise>`

La structure minimale d'une page web est :
```html
<!DOCTYPE html>
<html>
<head></head>
<body></body>
</html>

``` 
Le site de référence pour les langages du WEB est le site des développeurs de Mozilla.
[https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements)

QUelques balises à connaître :
- `<body></body>` contient tout ce qui est visible sur le page
- `<head></head>` contient ce qui n'est pas visible sur la page (ex : `<title></title>`)
- `<h1></h1>` permet de faire des titres sur la page
- `<p></p>` permet de faire un paragraphe
- `<a href = ""></a>` permet d'accrocher le curseur pour cliquer vers un lien
- `<img src="">` pour insérer une image
- `<br>` pour casser la ligne
- `<ul></ul>`pour réaliser une liste sans ordre
- `<ol></ol>` pour réaliser une liste ordonnée
- `<li></li>` pour insérer des items dans une liste


Les balises ouvrantes peuvent contenir des attributs définis sur le site de référence ou l'attribut `class=""` : <br>
`<maBalise attribut = ""></maBalise>`


---------------------------
Pour donner le chemin relatif vers un fichier on utilise :
- `./` pour chercher dans le dossier courant
- `../` pour chercher dans le dossier au dessus

2. Le CSS
Cascading Style Sheet *feuille de style en cascade*
[https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties)

Pour définir du style, il faut un sélcteur (element html ou class), des accolades, une propriété, une valeur.

```css
selecteur{
    propriete:valeur;
}
```

On peut écrire le CSS :
- dans le fichier html entre les balises `<style></style>`
- dans un ficher dédié avec l'extension `.css` ; il faut ajouter une balise `<link rel="stylesheet" href="">`

Il existe plus de 500 propriétés et encore d'avantage de valeurs possible mais souvent, les valeurs sont :
- des couleurs (soit un nom soit un code comme RGB(0-255, 0-255, 0-255))
- des tailles plusieurs unités sont possibles 
    - `px` pour pixels
    - `em` relatif à la taille de la police
    - `%` relatif à la taille du contenant

Remarque : Quand le sélecteur css est un élément HTML (par exemple `p`) alors les propriétés s'appliquent à tous les éléments du même type.

Pour différencier des éléments de même nature, on peut utiliser l'attribut `class` ou `id`. Dans ce cas, le sélecteur est le nom de la classe précédé d'un `.` ou le nom de l'identifiant précédé d'un `#`.


Remarque : le contenu d'un élément html suit le principle du modèle en boîte.
[https://www.w3schools.com/Css/css_boxmodel.asp](https://www.w3schools.com/Css/css_boxmodel.asp)



Trois propriétés importantes sont liées à ce modèle :
- `border` pour le style de la bordure
- `padding` pour l'espace interne
- `margin` pour la marge autour de la bordure

Remarque : Il existe des propriétés spécifiques au texte, en particulier : 
- `text-align` pour justifier le texte.
- `font` pour la police de caractères



Il existe deux balises html universelles qui permettent de grouper des éléments ou du texte :
- `<div></div>`
- `<span></span>`

3. Javascript

Ctrl + Shift + i

Il s'agit d'un langage de programation comme Python mais initialement dédié au WEB.

C'est un langage prévu pour intéragir avec une page HTML : le document peut se présenter aisin :


Image du DOM (Document Object Model)

Le JS permet de rendre une page HTML plus dynamique notament grâce aux formulaires `<form></form>`.

Les éléments HTML intéractifs sont généralement des `<input type="">`:
- button
- checkbox
- text
- range
- password ...

Pour écrire du JS in utilise les balies `<script></script>`et :
- on écrit directement le code dans le fichier HTML
- on écrit le code dans un fichier JS

Pour attraper un élément sur la page afin de la manipuler avec JS, on peut utiliser :
- `querySelection()`
- `getElementById()`


On écrira :
```js
let elementHTML = document.querySelector(""); //avec un sélecteur css
let elementHTML = document.getElementById(""); //avec un id
```


La plupart des éléments HTML inéractifs ont une propriété `value`.

```js
console.log(elementHTML.value);
```


Js est capable d'associer un évènement à un élément HTML :
- click
- change
- input
- mouseover ...


On utilise la méthode `addEventListener()`

```js
elementHTML.addEventListener("click", function(){

//faire quelque chose
});


```