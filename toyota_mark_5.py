Python 3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
from flask import Flask, render_template_string

app = Flask(__toyota_mark_2__)

HTML = """
<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Toyota Mark II JZX100 | 1JZ-GE</title>

<style>
* { box-sizing: border-box; }

body {
margin: 0;
background: #0b1017;
color: #edf2f7;
font-family: Arial, sans-serif;
line-height: 1.6;
}

header {
padding: 75px 20px;
text-align: center;
background: linear-gradient(135deg, #171f2c, #7d1722);
}

header h1 {
font-size: 42px;
margin: 0;
}

header p { color: #ffb5ba; }

nav {
background: #171e29;
padding: 15px;
text-align: center;
position: sticky;
top: 0;
z-index: 5;
}

nav a {
color: white;
text-decoration: none;
margin: 8px;
display: inline-block;
}

nav a:hover { color: #ff535e; }

main {
max-width: 1050px;
margin: auto;
padding: 20px;
}

section { margin: 45px 0; }

... h2 {
... color: #ff515d;
... border-left: 4px solid #e62c3c;
... padding-left: 12px;
... }
... 
... h3 { color: #ff858d; }
... 
... .card {
... background: #192330;
... border: 1px solid #303e4d;
... padding: 22px;
... border-radius: 12px;
... margin: 15px 0;
... }
... 
... .grid {
... display: grid;
... grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
... gap: 15px;
... }
... 
... .stat {
... background: #192330;
... padding: 20px;
... border-radius: 10px;
... border-bottom: 3px solid #ed3544;
... }
... 
... .stat strong {
... display: block;
... font-size: 26px;
... color: #ff737d;
... }
... 
... img {
... width: 100%;
... border-radius: 10px;
... margin-top: 15px;
... }

.diagram {
width: 100%;
overflow-x: auto;
background: #111a24;
border-radius: 10px;
padding: 10px;
}

svg {
width: 100%;
min-width: 600px;
}

.part { cursor: pointer; }

.part:hover { opacity: .7; }

#info {
background: #263547;
padding: 20px;
border-radius: 10px;
margin-top: 15px;
min-height: 100px;
}

table {
width: 100%;
border-collapse: collapse;
}

td {
padding: 12px;
border-bottom: 1px solid #394858;
}

td:first-child { color: #ff858d; }

footer {
text-align: center;
background: #171e29;
padding: 25px;
}

a { color: #ff8790; }

@media(max-width:600px) {
header h1 { font-size: 30px; }
main { padding: 12px; }
}
</style>
</head>

<body>

<header>
<h1>TOYOTA MARK II JZX100</h1>
<p>ENGINE 1JZ-GE | Техническая энциклопедия</p>
</header>

<nav>
<a href="#about">Автомобиль</a>
<a href="#engine">Двигатель</a>
<a href="#diagram">Схема</a>
<a href="#parts">Детали</a>
<a href="#systems">Системы</a>
<a href="#work">Работа</a>
</nav>

<main>

<section id="about">
<h2>О Toyota Mark II JZX100</h2>
<div class="card">
<p>
Toyota Mark II JZX100 — седан восьмого поколения
Mark II. Выпускался с 1996 года.
В зависимости от комплектации устанавливались
различные двигатели семейства JZ.
</p>
<p>
В этом проекте рассматривается атмосферный
бензиновый двигатель Toyota 1JZ-GE объёмом 2,5 литра.
</p>
</div>

<img src="https://commons.wikimedia.org/wiki/Special:FilePath/JZX100_Toyota_Mark_II.jpg"
alt="Toyota Mark II JZX100"
onerror="this.style.display='none'">
</section>

<section id="engine">
<h2>Характеристики 1JZ-GE</h2>

<div class="grid">
<div class="stat"><strong>2491</strong>Объём, см³</div>
<div class="stat"><strong>6</strong>Цилиндров</div>
<div class="stat"><strong>24</strong>Клапана</div>
<div class="stat"><strong>DOHC</strong>Газораспределение</div>
<div class="stat"><strong>200 PS</strong>Мощность распространённой версии</div>
<div class="stat"><strong>255 Н·м</strong>Крутящий момент, примерно</div>
</div>

<div class="card">
<h3>Технические данные</h3>
<table>
<tr><td>Код</td><td>1JZ-GE</td></tr>
<tr><td>Тип</td><td>Бензиновый, атмосферный</td></tr>
<tr><td>Объём</td><td>2491 см³</td></tr>
<tr><td>Цилиндры</td><td>Рядные, 6</td></tr>
<tr><td>Диаметр цилиндра</td><td>86 мм</td></tr>
<tr><td>Ход поршня</td><td>71,5 мм</td></tr>
<tr><td>Клапаны</td><td>24</td></tr>
<tr><td>Распределительные валы</td><td>2</td></tr>
<tr><td>Охлаждение</td><td>Жидкостное</td></tr>
<tr><td>Привод ГРМ</td><td>Ременной</td></tr>
</table>
<p>Показатели зависят от года выпуска и модификации.</p>
</div>

<img src="https://commons.wikimedia.org/wiki/Special:FilePath/1996_Toyota_Mark_II_Grande_G_2.5_1jz-ge_Engine.jpg"
alt="Двигатель 1JZ-GE"
onerror="this.style.display='none'">
</section>

<section id="diagram">
<h2>Интерактивная схема двигателя</h2>

<div class="card">
<p>Нажимай на детали схемы, чтобы узнать об их назначении.</p>

<div class="diagram">
<svg viewBox="0 0 800 430">

<g class="part" onclick="showInfo('head')">
<rect x="60" y="65" width="680" height="75"
rx="8" fill="#8293a4" stroke="white" stroke-width="2"/>
<text x="400" y="110" fill="#101820"
font-size="23" text-anchor="middle">ГОЛОВКА БЛОКА (ГБЦ)</text>
</g>

<g class="part" onclick="showInfo('cam')">
<rect x="100" y="25" width="600" height="22"
rx="10" fill="#e8b54c"/>
<text x="400" y="18" fill="#e8b54c"
font-size="15" text-anchor="middle">РАСПРЕДВАЛЫ</text>
</g>

<rect x="80" y="155" width="640" height="135"
rx="8" fill="#35475a" stroke="#a7b5c4" stroke-width="2"/>

<g class="part" onclick="showInfo('piston')" fill="#c4d0da">
<rect x="100" y="180" width="75" height="75" rx="5"/>
<rect x="205" y="180" width="75" height="75" rx="5"/>
<rect x="310" y="180" width="75" height="75" rx="5"/>
<rect x="415" y="180" width="75" height="75" rx="5"/>
<rect x="520" y="180" width="75" height="75" rx="5"/>
<rect x="625" y="180" width="75" height="75" rx="5"/>
</g>

<g fill="#14202b" font-size="17" text-anchor="middle">
<text x="137" y="220">1</text>
<text x="242" y="220">2</text>
<text x="347" y="220">3</text>
<text x="452" y="220">4</text>
<text x="557" y="220">5</text>
<text x="662" y="220">6</text>
</g>

<g class="part" onclick="showInfo('rod')"
stroke="#ed8b42" stroke-width="8">
<path d="M137 255 L160 330"/>
<path d="M242 255 L265 330"/>
<path d="M347 255 L370 330"/>
<path d="M452 255 L475 330"/>
<path d="M557 255 L580 330"/>
<path d="M662 255 L685 330"/>
</g>

<g class="part" onclick="showInfo('crank')">
<path d="M100 340 L700 340"
stroke="#69a9ec" stroke-width="17" stroke-linecap="round"/>
<text x="400" y="375" fill="#80b9fa"
font-size="22" text-anchor="middle">КОЛЕНВАЛ</text>
</g>

<g class="part" onclick="showInfo('oil')">
<path d="M120 390 L680 390 L650 420 L150 420 Z"
fill="#647586" stroke="white" stroke-width="2"/>
<text x="400" y="412" fill="white"
font-size="16" text-anchor="middle">МАСЛЯНЫЙ ПОДДОН</text>
</g>
</svg>
</div>

<div id="info">
<h3>Выбери деталь</h3>
<p>Нажми на элемент схемы.</p>
</div>
</div>
</section>

<section id="parts">
<h2>Основные детали</h2>

<div class="grid">
<div class="card">
<h3>Блок цилиндров</h3>
<p>Основная часть двигателя, в которой находятся шесть цилиндров.</p>
</div>

<div class="card">
<h3>Поршни</h3>
<p>Передают усилие сгорания топлива на шатуны.</p>
</div>

<div class="card">
<h3>Шатуны</h3>
<p>Соединяют поршни с коленчатым валом.</p>
</div>

<div class="card">
<h3>Коленвал</h3>
<p>Преобразует движение поршней во вращение.</p>
</div>

<div class="card">
<h3>Клапаны</h3>
<p>Регулируют поступление смеси и выход газов.</p>
</div>

<div class="card">
<h3>Свечи</h3>
<p>Обеспечивают искровое зажигание топливной смеси.</p>
</div>
</div>
