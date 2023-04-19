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
    <h2>Translations</h2>
    <div style="display: inline-block;">
        <a href="./README_EN.md">English</a>
        <a href="./README.md">Português</a>
    </div>
</div>

<hr>

<h1 align="center">Hello, I'm Vex!</h1>
<div align="center">
  <img align="right" src="https://user-images.githubusercontent.com/88998991/233083029-3fc5b1e6-eb74-4425-b935-9ab043bf0a9e.png" width="200px" alt="Vex avatar" draggable="false"></img>
  <p align="left">I am a simple Brazilian bot 🇧🇷 for Discord, focused on fun and entertainment!</p>
  <p align="left">I have several commands, some useful, some not so much 😅</p>
</div>
<h2>Running</h2>
<p>If you want to run Vex, follow these steps:</p>
<blockquote>
  <p>Make sure to use Python 3.11+. It is also highly recommended to use a virtual environment to install dependencies.</p>
</blockquote>
<ol>
  <li>
    <p>Installing dependencies:</p>
    <pre><code>pip install -r requirements</code></pre>
  </li>
  <li>
    <p>Set up environment variables:</p>
    <p>Create a file named <code>.env</code> with the <code>TOKEN</code> variable, which can be obtained <a href="https://discord.com/developers/applications">here</a>, <code>OWNER_ID</code>, which is the bot owner's ID, and <code>GUILD_ID</code>, which is the support server ID.</p>
  </li>
  <li>
    <p>Set up the application:</p>
    <p>In <code>Privileged Gateway Intents</code>, enable only the <code>SERVER MEMBERS INTENT</code> option. And in <code>Bot Permissions</code>, check <code>Administrator</code>, but if you prefer, use INTENTS in <a href="./src/bot.py">bot.py</a></p>
  </li>
  <li>
    <p>Run:</p>
    <pre><code>python main.py</code></pre>
  </li>
</ol>
<h2>Contributing</h2>
<p>If you wish to contribute to the development of Vex, follow these steps:</p>
<ol>
  <li>Fork this repository</li>
  <li>Create a new branch</li>
  <li>Make your changes</li>
  <li>Push your changes to your fork</li>
  <li>Submit a pull request</li>
</ol>
<h2>License</h2>
<p>Vex is under the <code>Apache-2.0 license</code>. See <a href="./LICENCE">LICENCE</a> for more details.</p>
