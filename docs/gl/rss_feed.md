# Evade o algoritmo empregando o RSS <span id="cap:rss"></span>

Cada vez é máis complicado estar ben informada, no sentido de que nos chegue a información útil e beneficiosa para nós.

Por unha banda, o volume de información dispoñible é excesivo. É imprescindible xestionar a nosa **economía da atención**, para enfrontarnos a todos os elementos que nola reclaman constantemente. Sen facer un esforzo consciente, a maior parte do tempo non somos nós quen decidimos onde investimos a nosa **atención** senón axentes externos con intereses propios.

Ese mecanismo que permite a outros elementos centrar a nosa atención no que eles queren, insire cada vez máis capas de intermediarios entre nós e as creadoras de contido, empobrecéndonos a ambas.

O panorama parece máis sombrío coa insistencia de engadir a intelixencia artificial (IA) ao mecanismo. A IA xa non é un simple intermediario entre creadoras de contido e público, senón que substitúe o contido orixinal por un refrito de *AI slop* que nos empobrecerá aínda máis.

Se che preocupa esta situación e queres retomar o control da información que che chega, unha forma de recuperar a túa independencia é usar **o protocolo RSS**.

**RSS** son as siglas de *Really Simple Syndication*. En inglés o termo *Syndication* denomina (entre outras cousas) a práctica por parte dunha fonte (por exemplo un *freelance*) de colocar unha noticia en varios xornais distintos ao mesmo tempo. E é que a idea detrás do protocolo **RSS** é precisamente esa: que cada unha de nós se compoña o seu propio xornal dixital subscribíndose ás fontes de novas que nos interesen e conveñan.

O funcionamento do protocolo é realmente sinxelo: calquera sitio de internet que publique contido pode optar por xerar un *RSS feed*, un ficheiro en texto plano que calquera pode descargar e que detalla os contidos publicados. O ficheiro seguirá un dos dous estándares utilizados: o **RSS** ou o **Atom**. Estes estándares especifican como se organiza o contido nun formato `xml` moi sinxelo. Pero se isto che soa a marciano e non sabes que significa tampouco ten moita importancia. O que si é interesante é que o protocolo é tan robusto como sinxelo, proba diso é que segue funcionando a perfección a pesar de non ter cambios dende 2005 para **Atom** e dende 2009 para **RSS**.

Como usuarias o que de verdade nos interesa saber do **RSS** é que podemos instalarnos un cliente, un **agregador de novas**, no noso dispositivo favorito (ou en varios dispositivos). Temos clientes para Windows, macOS, GNU/Linux, Android e iOS. Temos clientes multiplataforma e, para as máis tecnófilas, temos clientes en liña de comandos ou integrados no noso editor favorito ou clientes integrados con navegadores web. Máis adiante recomendaremos algúns clientes que coñecemos, pero se non che gustan as nosas recomendacións a oferta é inmensa. Como dixemos antes trátase dunha tecnoloxía moi madura e hai clientes para todos os gustos.

Ben, temos un protocolo sinxelo, robusto e maduro e, ademais, temos variedade de clientes dispoñibles. ¿Que podemos facer con iso? Vexamos algúns exemplos:

- **Novas**: É case seguro que todos os xornais (falamos dos xornais de novas, é dicir a prensa) con presenza dixital teñen implantado o protocolo RSS e podes subscribirte a eles. Normalmente, aos clientes **RSS** de hoxe en día, basta con pasarlles unha URL xenérica do xornal dixital para que “descubran” todos os *feeds* dispoñibles. Dependendo do coidado que poña o diario, pode ofrecernos dende un único *feed* (xeralmente cos titulares do xornal) ata un conxunto completo de *feeds* con novas segregadas por edicións, por seccións, por colaboradores do xornal, etc. Proba a meter no teu agregador de novas a URL dun xornal de tirada nacional e ver que *feeds* che ofrece.

- **Blogs**: Se acostumas a buscar información en internet sobre un tema concreto seguramente sigas algún blog. Calquera blog cun pouco de coidado debería ter implantado o protocolo RSS e poderás subscribirte ao mesmo para non perder ningunha publicación. Igual que no caso dos xornais, algunhas autoras non ofrecen un único *feed* do seu blog senón varios, separados por temáticas, por exemplo.

- **Podcast**: O “podcastverso” utilizou o protocolo RSS desde o seu nacemento. Normalmente non é difícil atopar *feeds* para os teus podcasts favoritos, aínda que moitas podcasters non manteñen o seu propio *feed* e confían nunha plataforma centralizada para publicar. Tamén hai que sinalar que habitualmente para *podcasts* úsase algún cliente especializado, orientado ao audio, que nos permita escoitar podcasts á velocidade que queiramos, avanzar e retroceder no audio, etc. Pero ao fin e ao cabo segue sendo un agregador RSS especializado. Na sección de clientes falaremos de algúns clientes de *podcast*. Do mesmo xeito que os agregadores RSS temos clientes de podcast para todas as plataformas.

- **Fediverso**: O fediverso integrou o protocolo RSS desde o seu nacemento; de feito houbo incluso propostas para usar o protocolo RSS (coas extensións necesarias, claro) para implementar redes sociais descentralizadas. Así que agora podes seguir calquera conta do Fediverso co teu cliente RSS. Se queres ver as publicacións de ESF Galicia no Fediverso, no teu agregador de RSS a URL sería <https://mastodon.gal/@ESFGalicia.rss>. Ou se queres ver todas as publicacións coa etiqueta `Fediverso` na instancia `mastodon.gal` podes subscribirte a <https://mastodon.gal/tags/Fediverso.rss>. Pero coidado, este mecanismo non se limita a Mastodon; está dispoñible para outros servizos do Fediverso, polo que poderías subscribirte a contas ou canles en PeerTube, contas en Pixelfed, en BookWyrm, etc.

- **Boletíns**: Algúns lectores de RSS ofrecen a posibilidade de xestionar os boletíns aos que estás subscrito. Ademais, temos tamén o servizo [Kill the Newsletter](https://kill-the-newsletter.com/) (que opcionalmente podes autoaloxar e é software libre) que permite converter calquera boletín nun *Atom Feed* ao que podes seguir co teu agregador de novas.

- **Compartir as nosas subscripcións**: Todos os agregadores RSS permiten exportar as nosas subscripcións, ou importalas desde, un fichero `.opml`. Así que temos un xeito doado de compartir as nosas fontes de noticias favoritas cós mais.

- **Case calquera cousa**: O protocolo RSS é extremadamente sinxelo de implantar, polo que practicamente calquera servizo de internet pode incorporalo. As wikis adoitan ter complementos para ofrecer un *RSS feed* coas últimas publicacións ou modificacións. **OpenStreetMap** ofrece diferentes tipos de *feed* para estar ao tanto dos últimos cambios. Unha canle de YouTube pode agregarse como un *RSS feed* no teu lector de novas, etc. Por dar un exemplo das cousas máis sofisticadas que se poden facer con RSS podemos citar arXiv, a plataforma aberta de publicación de artigos científicos, que ofrece unha interface RSS moi completa onde podemos compor consultas detallando exactamente que temas queremos subscribir na propia URL do *feed* (ver [aquí](https://ronpay.github.io/arxiv-rss-feed-generator/) un exemplo dun *frontend* para compor URLs de *feed*s de arXiv).

## Algúns clientes RSS (Agregadores de Novas)

En todas as plataformas (sistemas operativos) hai unha ampla oferta de agregadores ou lectores de novas, como os queiramos chamar. En GNU/Linux é habitual ter agregadores de novas dispoñibles, dende os que veñen integrados con clientes de correo como Thunderbird ou Evolution ata clientes RSS de liña de comandos.

Centrarémonos nos que usamos e son software libre, aínda que citaremos algún que non cumpre ese criterio.

### Android

- **Feeder**: Un cliente sinxelo dispoñible en F-Droid, ideal para iniciarse neste mundo.

- **CapyReader**: Un cliente moi completo, algo máis avanzado, soporta contas en agregadores en liña, pode usarse con agregadores *“Selfhosted”*.

- **Readrops**: Semellante a **Capy Reader**, moi completo e con soporte para agregadores en liña, pode usarse con agregadores *“Selfhosted”*.

- **AntennaPod**: O noso agregador de *podcast* favorito en Android.

### iOS

Desafortunadamente non temos experiencia con lectores de novas en iOS; usamos Feedly en Android, pero ao final sustitúmoa por Feeder, que é software libre. Non obstante, Feedly funcionaba moi ben en Android e por iso inclúemo como opción para iOS.

- **Feedly**: Probado en Android, funciona correctamente e é fácil de usar. É multiplataforma e está dispoñible en iOS, **non é software libre**.

### GNU/Linux

- **Quiterss**: Baseado na biblioteca Qt, moi completo, con soporte para podcasts, permite un filtrado detallado dos nosos *feeds*.

- **Liferea**: Mais sinxelo que o anterior, moi fácil de usar e con soporte para *podcasts*.

- **RSSGuard**: Se che preocupa a seguridade e o anonimato tes que probar este lector de novas.

- **Clientespara podcasts**: En GNU/Linux hai moitos clientes de *podcast*, pero vale a pena mencionar que os reprodutores de música máis coñecidos, como **Amarok**, **Rhythmbox** ou **Clementine**, levan integrada a funcionalidade para subscribirse a *podcasts*.

### Multiplataforma

Non temos experiencia recente usando un lector de RSS nin en Windows nin en macOS, pero usamos un lector de RSS multiplataforma:

- **Thunderbird**, o xestor de correo electrónico de Mozilla, tamén soporta a subscrición a *feed RSS*.

## Organizando o noso xornal, ou mellor o noso fluxo de novas personalizado

Todos os agregadores permítennos organizar as fontes de novas por categorías.

A medida que o número de subscricións aumente no noso agregador (ou lector) de novas teremos que organizar as subscricións. Por un lado chegará un momento no que non poidamos ler todas as novas que nos chegan (loxicamente non pode unha persoa ler todas as novas do mundo) así que probablemente non queiramos clasificalas só por temática. Pode que queiramos clasificalas por importancia ou polo momento en que as queiramos ler. Por exemplo ler os titulares da prensa á primeira hora do día, e ter novas do noso hobby favorito para ler os domingos pola tarde.

O importante aquí é non abafarse polo número de novas que nos chegan; de ningunha maneira hai que pretender lelas absolutamente todas. Hai que coidar a nosa **economía da atención** e intentar refinar o noso propio sistema de forma que nos sexa útil e non nos provoque infoxicación. Basta con ser un pouco selectiva coas subscricións pero sen obsesionarse, e ir afinando o método paso a paso. É boa práctica ter titulares das novas de actualidade de xornais con diferentes puntos de vista, para botar unha ollada rápida ás novas pola mañá (e non todos os días) e ler algunha especialmente interesante. Por exemplo, ter un par de temas de interese que sigas máis de preto e novas de ciencia e opinión para ler con calma nos momentos mortos ou no fin de semana.

## Outros servizos interesantes no universo RSS

Ao tratarse de un algoritmo aberto, o ecosistema de software libre está moi arraigado neste campo e podemos atopar todo tipo de servizos. Aquí van algúns exemplos dispoñibles:

- **Agregadores*selfhosted***: Exemplos típicos son `FreshRSS` ou `TinyTinyRSS`. Estes agregadores/servidores permítenche manter de forma centralizada as túas subscricións de novas e podes lelas con calquera navegador usando a súa interface web ou apuntar os teus clientes RSS a eles desde o móbil ou o portátil. Pero non só iso, estes agregadores son moito máis potentes que os típicos clientes RSS. Normalmente son capaces de xerar un *feed RSS* a partir dun sitio de internet que non o teña, ou crear outros *feeds* personalizados a partir dos *feeds* subscritos especificando unha consulta. Evidentemente poderías, á súa vez, subscribirte a estes *feeds* con un cliente RSS normal. Se tes un destes “servidores”, os teus dispositivos poden sincronizarse entre si: se liches unha nova no teu móbil, aparecerá marcada como lida no teu ordenador, tablet ou na interface web do teu agregador auto‑aloxado.

- **RSSBridge**: É unha aplicación PHP que pode xerar un *feed RSS* para sitios web que non o implantan directamente. <https://github.com/RSS-Bridge/rss-bridge>

- <https://openrss.org>: Unha web que busca os *feeds* dispoñibles nun sitio de internet, para facilitarche a tarefa de engadilos ao teu agregador.

## Referencias

- <https://www.citationneeded.news/curate-with-rss/>

- <https://researchbuzz.me/2025/01/19/a-reminder-about-mastodon-and-rss-resources/>
