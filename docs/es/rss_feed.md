# Evade el algoritmo empleando el RSS <span id="cap:rss"></span>

Cada vez es más complicado estar bien informada, en el sentido de que nos llegue la información útil y beneficiosa para nosotras.

Por un lado el volumen de información disponible es excesivo. Es imprescindible gestionar nuestra **economía de la atención**, para enfrentarnos a todos los pedigüeños que nos la reclaman constantemente. Sin hacer un esfuerzo consciente, la mayor parte del tiempo no somos nosotras quien decidimos donde invertimos nuestra **atención** si no agentes externos con intereses propios.

Ese mecanismo que permite a otros centrar nuestra atención en lo que ellos quieren, inserta cada vez más capas de intermediación entre nosotras y las creadoras de contenido, empobreciendonos a ambas.

El panorama parece más sombrío con la insistencia de añadir la IA al mecanismo. La IA ya no es un simple intermediario entre creadoras de contenido y público, si no que sustituye el contenido original por un refrito de *AI slop* que nos emprobrecerá todavía más.

Si te preocupa esta situación y quieres retomar el control de la información que te llega, una forma de recuperar tu independencia es usar **el protocolo RSS**.

**RSS** son las siglas de *Really Simple Syndication*. En inglés el término *Syndication* denomina (entre otras cosas) la práctica por parte de una fuente (por ejemplo un *freelance*) de colocar una noticia en varios periódicos distintos al mismo tiempo. Y es que la idea detrás del protocolo **RSS** es justamente esa, que cada uno de nosotros se componga su propio periódico digital subscribiéndonos a las fuentes de noticias que nos interesen y convengan.

El funcionamiento del protocolo es realmente simple: cualquier sitio de internet que publique contenido puede optar por generar un *RSS feed*, un fichero en texto plano que cualquiera puede descargar y que detalla los contenidos publicados. El fichero seguirá uno de los dos estándares utilizados: el **RSS** o el **Atom**. Estos estándares especifican como se organiza el contenido en un formato `xml` muy simple. Pero si esto te suena a marciano y no sabes que significa tampoco tiene mucha importancia. Lo que si es interesante es que el protocolo es tan robusto como sencillo, prueba de ello es que sigue funcionando a la perfección pese a no tener cambios desde el 2005 para **Atom** y desde el 2009 para **RSS**.

Como usuarios lo que de verdad nos interesa saber del **RSS** es que podemos instalarnos un cliente, un **agregador de noticias**, en nuestro dispositivo favorito (o en varios dispositivos). Tenemos clientes para Windows, MacOS, Linux, Android e IOs. Tenemos clientes multiplataforma y para las más tecnófilas tenemos clientes en linea de comandos o integrados en nuestro editor favorito o clientes integrados con navegadores Web. Más adelante recomendamos algunos clientes que conocemos, pero si no te gustan nuestras recomendaciones la oferta es amplísima. Como hemos dicho antes se trata de una tecnología muy madura y hay clientes para todos los gustos.

Bien, tenemos un protocolo sencillo, robusto y maduro y además tenemos variedad de clientes disponibles ¿qué podemos hacer con eso? Veamos algunos ejemplos:

- **Noticias**: Es casi seguro que todos los periódicos (hablamos de los periodicos de noticias, es decir la prensa) con presencia digital tienen implementado el protocolo RSS y puedes suscribirte a ellos. Generalmente, a los clientes **RSS** de hoy en dia, basta con pasarles una url genérica del periódico digital para que "descubran" todos los *feed* disponibles. Dependiendo del cuidado que haya puesto el diario, nos puede ofrecer desde un único *feed* (generalmente con los titulares del periódico) hasta un conjunto completo de *feeds* con noticias segregadas por ediciones, por secciones, por colaboradores del periódico, etc. etc. Prueba a meter en tu agregador de noticias la url de un periódico de tirada nacional y ver que *feeds* te ofrece.

- **Blogs**: Si acostumbras a buscar información en internet de un tema concreto seguramente sigues algún blog. Cualquier blog un poco cuidado debería tener implementado el protocolo RSS y podrás suscribirte al mismo para no perderte ninguna publicación. Igual que en el caso de los periódicos, algunas autoras no ofrecen un único *feed* de su blog sino varios, separados por temáticas por ejemplo.

- **Podcast**: El “podcastverso” usó el protocolo RSS desde su nacimiento. Generalmente no es difícil encontrar *feeds* para tus podcast favoritos, aunque muchas podcasters no mantienen su propio *feed* y confian en alguna plataforma centralizada para publicar. También hay que señalar que normalmente para *podcasts* se usa algún cliente especializado, orientado a audio, que nos permita escuchar podcasts a la velocidad que queramos, avanzar y retroceder en el audio, etc. Pero al fin y al cabo no deja de ser un agregador RSS especializado. En la sección de clientes hablaremos de algunos clientes de *podcast*. Al igual que los agregadores RSS tenemos clientes de podcast para todas las plataformas.

- **Fediverso**: El fediverso integró el protocolo RSS desde su nacimiento, de hecho hubo incluso propuestas para usar el protocolo RSS (con las extensiones necesarias, claro) para implementar redes sociales descentralizadas. Así que ahora puedes seguir cualquier cuenta del Fediverso con tu cliente RSS. Si quieres ver las publicaciones de ESF Galicia en el Fediverso, en tu agregador de RSS la url sería <https://mastodon.gal/@ESFGalicia.rss>. O si quieres ver todas las publicaciones con la etiqueta `Fediverso` en la instancia `mastodon.gal` puedes suscribirte a <https://mastodon.gal/tags/Fediverso.rss> Pero ojo este mecanismo no se limita a Mastodon, está disponibles para otros servicios del Fediverso, así que podrías suscribirte a cuentas o canales en Peertube, cuentas en Pixelfed, en BookWyrm, etc.

- **Newsletters**: Algunos lectores de RSS ofrecen la posibilidad de gestionar las Newsletter a las que estés suscrito. Además tenemos también el servicio [Kill the Newsletter](https://kill-the-newsletter.com/) (que opcionalmentepuedes auto-alojar y es software libre) que te permite convertir cualquier Newsletter en un *Atom Feed* al que puedes seguir con tu agregador de noticias.

- **Compartir nuestras subscripciones**: Todos los agregadores RSS permiten exportar nuestras subscripciones, o importarlas desde, un fichero `.opml`. Así que podemos compartir fácilmente nuestras fuentes de noticias favoritas con los demás.

- **Casi cualquier otra cosa**: El protocolo RSS es extremadamente sencillo de implementar, así que prácticamente cualquier servicio de internet puede incorporarlo. Las wiki suelen tener plugins para ofrecer un *RSS feed* con las últimas publicaciones o modificaciones. **Open Street Map** ofrece diferentes tipos de *feed* para estar al tanto de los últimos cambios. Un canal de Youtube puede agregarse como un *RSS feed* en tu lector de noticias. Etc. Etc. Por poner un ejemplo de las cosas más sofisticadas que se pueden hacer con RSS podemos citar a arXiv, la plataforma abierta de publicación de artículos científicos, que ofrece un completísimo interfaz RSS donde podemos componer consultas detallando exactamente que temas queremos subscribir en la propia URL del *feed* (ver [aquí](https://ronpay.github.io/arxiv-rss-feed-generator/) un ejemplo de un *frontend* para componer URLs de *feed* de arXiv)

## Algunos clientes RSS (Agregadores de Noticias)

En todas las plataformas (sistemas operativos) hay una amplísima oferta de agregadores o lectores de noticias, como los queramos llamar. En Linux es habitual tener agregadores de noticias disponibles, desde los que vienen integrados con clientes de correo como Thunderbird o Evolution hasta clientes RSS de linea de comandos.

Nos vamos a centrar en los que hemos usado y son software libre, aunque citaremos alguno que no cumple esos criterios.

### Android

- **Feeder**: Un cliente sencillo disponible en F-Droid, ideal para iniciarse en este mundillo

- **Capy Reader**: Un cliente muy completo, algo más avanzado, soporta cuentas en agregadores online, puede usarse con agregadores *"Selfhosted"*

- **Readrops**: Igual que **Capy Reader** muy completo y con soporte para agregadores online, puede usarse con agregadores *"Selfhosted"*

- **AntennaPod**: Nuestro agregador de *podcast* favorito en Android.

### iOS

Desgraciadamente no tenemos experiencia con lectores de noticias en IOs, hemos usado Feedly en Android, pero al final lo sustituimos con Feeder que es software libre. No obstante Feedly funcionaba muy bien en Android y por eso lo incluimos como opción para iOS

- **Feedly**: Probado en Android, funciona correctemante y es fácil de usar. Es multiplataforma y está disponible en IOs **no es software libre**

### Linux

- **Quiterss**: Basado en la biblioteca QT, muy completo, con soporte para Podcast, permite un filtrado detallado de nuestros *feeds*

- **Liferea**: Más simple que el anterior, muy fácil de usar y con soporte para *podcasts*.

- **RSSGuard**: Si te preocupa la seguridad y el anonimato tienes que probar este lector de noticias

- **Clientes para podcast**: En Linux tenemos cantidad de clientes de *podcast*, pero merece la pena comentar que los reproductores de música más conocidos, como **Amarok**, **Rythmbox** o **Clementine** llevan integrada la funcionalidad para suscribirse a *podcasts*

### Multiplataforma

No tenemos experiencia reciente usando un lector de RSS ni en Windows ni en MacOS, pero si hemos usado un lector de RSS multiplataforma:

- **Thunderbird**, el gestor de correo electrónico de Mozilla soporta también la subscripción a *feed RSS*

## Organizando nuestro periódico, o más bien nuestro flujo de noticias personalizado

Todos los agregadores nos permiten organizar las fuentes de noticias por categorías.

A medida que el número de subscripciones aumente en nuestro agregador (o lector) de noticias tendremos que organizar las subscripciones. Por un lado llegará un momento en que no podremos leer todas las noticias que nos llegan (lógicamente no puede uno leer todas las nuevas noticias del mundo) así que probablemente no querremos clasificarlas únicamente por temática. Quizás queramos clasificarlas por importancia o por el momento en que las queramos leer. Por ejemplo leer los titulares de prensa a primera hora del dia, y tener noticias de nuestro hobby favorito para leer los domingos por la tarde.

Lo importante aquí es no agobiarse por el número de noticias que nos llegan; de ninguna manera hay que pensar en leerlo absolutamente todo. Hay que cuidar nuestra **Economía de la Atención** y tenemos que intentar refinar nuestro propio sistema de forma que nos sea útil y no nos provoque infoxicación. Basta con ser un poco selectivo con las subscripciones pero sin obsesionarse, e ir refinando el método poco a poco. A mi personalmente me gusta tener titulares de las noticias de actualidad de periodicos con diferentes puntos de vista, para echar un vistazo rápido a las noticias por la mañana (y no todos los dias) y leer alguna especialmente interesante. Tengo un par de temas de interés que sigo más de cerca y noticias de ciencia y opinión para leer con calma en tiempos muertos o en el fin de semana.

## Otros servicios interesantes en el universo RSS

Al tratarse de un algoritmo abierto el ecosistema de software libre está muy arraigado en este campo y podemos encontrar todo tipo de servicios, vamos a poneros algunos ejemplos de servicios disponibles:

- **Agregadores *selfhosted***: Ejemplos típicos son `FreshRSS` o `TinyTinyRSS`. Estos agregadores/servidores, te permiten mantener de forma centralizada tus suscripciones de noticias y puedes leerlas con cualquier navegador usuando su interfaz web o bien apuntar tus clientes RSS a ellos desde tu móvil o tu portátil. Pero no solo eso, estos agregadores son mucho más potentes que los tipicos clientes RSS. Normalmente son capaces de generar un *feed RSS* a partír de un sitio de internet que no lo tenga, o generar otros *feeds* personalizados a partir de los *feed* suscritos especificando una consulta. Evidentemente podríamos a su vez suscribirnos a estos *feed* con un cliente RSS normal. Si tienes uno de estos todos "servidores" tus dispositivos pueden estar sincronizados entre si, en el sentido de que si lees una noticia en tu móvil, te aparecerá marcada como leida en tu ordenador, o en tu tablet o en la interfaz web de tu agregador auto-alojado.

- **RSS Bridge**: Es una aplicación PHP que puede generar un *feed RSS* para sitios web que no lo implementan directamente. <https://github.com/RSS-Bridge/rss-bridge>

- <https://openrss.org>: Una web que busca los *feed* disponibles en un sitio de internet, para facilitarte la tarea de añadirlos a tu agregador.

## Referencias

- <https://www.citationneeded.news/curate-with-rss/>

- <https://researchbuzz.me/2025/01/19/a-reminder-about-mastodon-and-rss-resources/>
