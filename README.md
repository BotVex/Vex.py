<div align="center">
  <img src="https://user-images.githubusercontent.com/88998991/201827239-37187529-d010-4dd5-a7ea-cecf26f478d1.png" width=65%>
</div>

<br>

<div align="center">
  <img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/BotVex/Vex.py?style=for-the-badge">
  <img alt="GitHub commit activity" src="https://img.shields.io/github/commit-activity/w/BotVex/Vex.py?style=for-the-badge">
  <img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/BotVex/Vex.py?style=for-the-badge">
  <img alt="GitHub top language" src="https://img.shields.io/github/languages/top/BotVex/Vex.py?style=for-the-badge">
  <img alt="GitHub" src="https://img.shields.io/github/license/BotVex/Vex.py?style=for-the-badge">
  <img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg?style=for-the-badge">
</div>

<hr>

<div align="center">
    <h2>Traduções</h2>
    <div style="display: inline-block;">
        <a href="./README_EN.md">English</a>
        <a href="./README.md">Português</a>
    </div>
</div>

<hr>

<h1 align="center">Olá, eu sou a Vex!</h1>

<div align="center">
  <img align="right" src="https://user-images.githubusercontent.com/88998991/230775419-78927307-dd68-4cb7-9c4a-d3d1c45b83e0.png" width="200px" alt="Vex avatar" draggable="false"></img>
  <p align="left">Sou um simples bot brasileiro 🇧🇷 para o Discord, focada em diversão e entretenimento!</p>
  <p align="left">Tenho vários comandos, alguns úteis, outros não 😅</p>
</div>

<h2>Executando</h2>
<p>Caso queira executar a Vex, siga estas etapas:</p>
<blockquote>
  <p>Certifique-se de utilizar o Python 3.11+. Também é extremamente recomentado utilizar um ambiente virtual para instalar as dependências.</p>
</blockquote>
<ol>
  <li>
    <p>Instalando as dependências:</p>
    <pre><code>pip install -r requirements</code></pre>
  </li>
  <li>
    <p>Configure as variáveis de ambiente:</p>
    <p>Crie um arquivo chamado <code>.env</code> com as variáveis <code>TOKEN</code>, que pode ser obtida <a href="https://discord.com/developers/applications">aqui</a>, <code>OWNER_ID</code>, que é o ID do dono do bot, e <code>GUILD_ID</code>, que é o ID do servidor de suporte.</p>
    <pre><code>python main.py</code></pre>
  </li>
  <li>
    <p>Configure a aplicação:</p>
    <p>em <code>Privileged Gateway Intents</code>, habilite apenas a opção <code>SERVER MEMBERS INTENT</code>. E em <code>Bot Permissions</code>, marque <code>Administrator</code>, mas caso queira, utilize as INTENTS em <a href="./src/bot.py">bot.py</a></p>
  </li>
  <li>
    <p>Execute:</p>
    <pre><code>python main.py</code></pre>
  </li>
</ol>


<h2>Contribuindo</h2>
<p>Se deseja contribuir para a construção da Vex, siga estas etapas:</p>
<ol>
  <li>Faça um fork desde repositório</li>
  <li>Crie uma nova branch</li>
  <li>Faça as suas mudanças</li>
  <li>Faça um push das suas mudanças para seu fork</li>
  <li>Envie um pull request</li>
</ol>

<h2>Licença</h2>
<p>A vex está sob licença <code>Apache-2.0 license</code>. Veja <a href="./LICENCE">LICENCE</a> para mais detalhes.</p>
