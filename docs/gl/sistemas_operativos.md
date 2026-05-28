# Os Sistemas Operativos. Alternativas libres e seguras.<span id="cap:SO"></span>

Neste capítulo falarémosvos do sistema operativo, explicando que é e a importancia de usar alternativas libre.

## Que é un sistema operativo?

Un **sistema operativo** é o software fundamental que xestiona e controla o hardware dun ordenador, móbil ou outro dispositivo electrónico. Actúa como unha ponte entre a usuaria e o hardware, permitindo que se executen aplicacións e garantindo que os recursos do sistema (procesador, memoria, almacenamento, dispositivos de entrada/saída, etc.) se utilicen de forma eficiente.

### Funcións principais dun sistema operativo

- **Xestión de procesos**: controla a execución dos programas, asignando tempo de procesador e garantindo que funcionen correctamente sen interferencias.

- **Xestión da memoria**: distribúe a memoria dispoñible entre os diferentes programas en execución.

- **Xestión de almacenamento**: organiza e controla o acceso aos ficheiros e directorios no disco duro ou outros medios de almacenamento.

- **Xestión de dispositivos**: permite que o hardware, como impresoras, teclados ou cámaras, funcione correctamente e sexa recoñecido polo sistema.

- **Seguridade e permisos**: protexe os datos da usuaria, evita accesos non autorizados e xestiona contas de usuaria.

- **Interface de usuaria**: ofrece unha forma de interactuar co ordenador, xa sexa mediante unha liña de comandos (CLI) ou unha interface gráfica (GUI).

### Exemplos de sistemas operativos

- **Para ordenadores**: GNU/Linux (Ubuntu, Debian, Fedora…), Windows, macOS.

- **Para móbiles**: Android, iOS.

- **Para servidores e dispositivos embebidos**: FreeBSD, OpenWRT...

Sen un sistema operativo, os dispositivos electrónicos serían moi difíciles de usar, xa que cada programa tería que xestionar directamente o hardware.

## Por que é importante empregar sistemas operativos libres?

Un **sistema operativo libre** é aquel que respecta as liberdades das usuarias para executar, estudar, modificar e distribuír o software. Exemplos destacados son **GNU/Linux** e **FreeBSD**. Optar por un sistema operativo libre ofrece múltiples vantaxes, tanto en termos de seguridade como de privacidade e control sobre o propio dispositivo.

### Vantaxes de empregar software libre

- **Transparencia e seguridade**: O código fonte está dispoñible para que calquera poida revisalo, detectar vulnerabilidades e melloralo. Isto reduce a posibilidade de portas traseiras ou software malicioso oculto.

- **Privacidade**: Sistemas privativos como Windows recollen datos das usuarias sen o seu consentimento explícito. Os sistemas libres, en cambio, permiten un maior control sobre a información persoal.

- **Control total**: As usuarias poden modificar e adaptar o sistema ás súas necesidades, sen restricións impostas por empresas que buscan maximizar os seus beneficios.

- **Personalización**: Existen múltiples distribucións (versións) de GNU/Linux, permitindo escoller a que mellor se adapte a cada uso (traballo, xogos, servidores, etc.).

- **Actualizacións constantes**: A comunidade desenvolvedora mantén e mellora os sistemas operativos libres de maneira continua, asegurando que os erros e vulnerabilidades sexan corrixidos rapidamente.

- **Sustentabilidade e revalorización do hardware**: Moitos sistemas operativos libres están optimizados para funcionar en equipos antigos, dándolles unha nova vida e reducindo a necesidade de comprar novos dispositivos.

- **Independencia tecnolóxica**: O software libre non está controlado por unha única corporación, evitando situacións onde unha empresa pode decidir deixar de dar soporte a un sistema, forzando ás usuarias a cambiar de hardware ou software.

### Problemas do software privativo

- **Código pechado**: Non se pode ver nin modificar, polo que as usuarias dependen totalmente da empresa desenvolvedora.

- **Monopolios e restricións**: Empresas como Microsoft e Apple impoñen condicións sobre como usar os seus sistemas, limitando a liberdade das usuarias.

- **Recollida de datos**: Moitos sistemas privativos integran sistemas de rastrexo e telemetría que espían os hábitos das usuarias.

- **Obsolescencia programada**: Algúns sistemas operativos privativos deixan de dar soporte a hardware antigo para incentivar a compra de novos dispositivos, aumentado o lixo electrónico.

## Alternativa libre para o ordenador. Que é GNU/Linux e como instalalo

GNU/Linux é un sistema operativo baseado no núcleo **Linux** e no conxunto de ferramentas do proxecto **GNU**. A combinación destes elementos permite crear un sistema libre, seguro e altamente personalizable, empregado tanto en servidores como en dispositivos persoais.

### Diferenza entre o núcleo (kernel) e unha distribución

Para comprender GNU/Linux, é importante diferenciar entre o **núcleo** e as **distribucións**:

- **Kernel**: É a parte fundamental do sistema operativo, encargada de xestionar o hardware e permitir a comunicación entre o software e os compoñentes físicos do ordenador (procesador, memoria, disco duro, etc.). Linux é o núcleo usado en todas as distribucións GNU/Linux.

- **Distribución**: É unha versión de GNU/Linux que inclúe o núcleo Linux, ferramentas de software, xestores de paquetes e unha interface gráfica. Existen moitas distribucións, adaptadas a diferentes usos e necesidades.

### Exemplos de distribucións populares

- **[Linux Mint](https://linuxmint.com/)**: Baseada en Ubuntu ou Debian ([a versión LMDE](https://linuxmint.com/download_lmde.php)), cunha interface semellante a Windows para facilitar a transición de novas usuarias.

- **[Ubuntu](https://ubuntu.com/desktop)**: Tamén ideal para usuarias principiantes, con boa compatibilidade de hardware e unha gran comunidade de soporte.

- **[Debian](https://www.debian.org)**: Estable e segura, preferida en servidores e sistemas que requiren fiabilidade a longo prazo.

- **[Arch Linux](https://archlinux.org/)**: Para usuarias avanzados que queren personalizar completamente o seu sistema desde cero.

### Sabores dunha distribución: os entornos de escritorio

En GNU/Linux, o núcleo do sistema e as súas aplicacións poden funcionar con diferentes **entornos de escritorio**, que determinan a aparencia e funcionalidade da interface gráfica. Moitas distribucións ofrecen distintos “sabores” baseados no mesmo sistema, pero con distintos entornos de escritorio para adaptarse ás preferencias da usuaria.

#### Que é un entorno de escritorio?

Un entorno de escritorio é un conxunto de software que proporciona unha interface gráfica de usuaria (GUI). Inclúe xestores de ventás, paneis, iconas, menús e ferramentas de configuración. A diferenza doutros sistemas operativos que teñen unha única interface predeterminada (como Windows), en GNU/Linux pódese escoller entre varias opcións segundo o rendemento, a estética ou as funcionalidades que se prefiran.

#### Principais entornos de escritorio

- **[Cinnamon](https://projects.linuxmint.com/cinnamon/)**:

  - Deseño clásico e intuitivo, moi semellante a Windows.

  - Interface elegante e con efectos visuais agradables sen perder rendemento.

  - Distribucións que o usan: Linux Mint (entorno por defecto), Debian Cinnamon, etc.

- **[GNOME](https://www.gnome.org/)**:

  - Usa un deseño baseado en xestos e unha barra lateral (chamada dock) en lugar do menú clásico.

  - Consume máis recursos.

  - Distribucións que o usan: Ubuntu (edición principal), Fedora, Debian, etc.

- **[KDE Plasma](https://kde.org/plasma-desktop/)**:

  - Altamente personalizable e con efectos visuais avanzados.

  - Ofrece moitas opcións de configuración e ferramentas nativas potentes.

  - Distribucións que o usan: Kubuntu, KDE Neon, openSUSE, etc.

- **[XFCE](https://www.xfce.org/)**:

  - Enfoque en ser lixeiro e rápido, ideal para equipos con poucos recursos.

  - Interface clásica e sinxela, sen consumir demasiada memoria RAM.

  - Distribucións que o usan: Xubuntu, Manjaro XFCE, Debian XFCE, etc.

- **[LXQt](https://lxqt-project.org/)**:

  - Aínda máis lixeiro que XFCE, pensado para equipos antigos ou con pouca potencia.

  - Interface sinxela e funcional, con baixo consumo de recursos.

  - Distribucións que o usan: Lubuntu, LXQt en Arch Linux, etc.

- **[MATE](https://mate-desktop.org/)**:

  - Baseado no antigo GNOME 2, mantendo un deseño tradicional e eficiente.

  - Distribucións que o usan: Ubuntu MATE, Debian MATE, Manjaro MATE, etc.

#### Como escoller un entorno de escritorio?

A elección dun entorno de escritorio depende das necesidades e preferencias da usuaria. Se se busca un sistema lixeiro para un ordenador antigo, opcións como XFCE ou LXQt son recomendables. Se se quere unha experiencia moderna e fluída, GNOME ou KDE Plasma son boas opcións. Por outra banda, Cinnamon e MATE son ideais para quen prefira unha interface clásica e fácil de usar, balanceando consumo de recursos e estética.

Moitas distribucións permiten instalar múltiples entornos de escritorio e cambialos na pantalla de inicio de sesión, polo que sempre é posible probar diferentes opcións ata atopar a máis axeitada.

### Como instalar GNU/Linux nun ordenador

A instalación e iso de GNU/Linux pode parecer complexa ao principio, pero segue un proceso sinxelo. En ESF temos unha serie de [Bancos de Reciclaxe Electrónica con Software Libre](https://galicia.isf.es/bancos-de-reciclaxe-electronica-con-software-libre/) onde estaremos encantas de axudarche. Tamén temos un [vídeo no que un voluntario explica os distintos pasos](https://archive.org/details/instalacion-de-lubuntu.-nova-vida-a-vellos-ordenadores). Os pasos básicos son os seguintes:

1.  **Escoller unha distribución**: Dependendo das necesidades da usuaria, pódese descargar unha ISO desde o sitio web oficial da distribución elixida.

2.  **Crear un USB de instalación**: Pódese empregar o comando `dd` ou ferramentas como **[Balena Etcher](https://etcher.balena.io)**.

3.  **Arrancar dende o USB**: Reiniciar o ordenador e acceder á BIOS/UEFI (normalmente premendo F2, F12 ou Supr ao iniciar) para seleccionar o USB como dispositivo de arranque.

4.  **Probar ou instalar**: Moitas distribucións permiten probar o sistema en modo Live antes de instalalo. Se se decide instalar:

    - Seleccionar o idioma e a configuración do teclado.

    - Configurar as particións do disco (a opción automática é suficiente para a maioría das usuarias).

    - Escoller un nome de usuaria e contrasinal.

    - Iniciar o proceso de instalación.

5.  **Reiniciar o ordenador**: Unha vez finalizada a instalación, retirar o USB cando o indique na pantalla e iniciar o sistema GNU/Linux instalado. E listo.

## Alternativas libres para móbiles e como instalalas<span id="sec:alt_so_mobiles"></span>

A maioría dos teléfonos intelixentes funcionan con sistemas operativos privativos como Android (a versión que inclúe os Google Play Services, e que é a instalada na maioría dos dispositivos) ou iOS, que restrinxen a liberdade da usuaria e recollen unha gran cantidade de datos persoais. Afortunadamente, existen alternativas libres e máis respectuosas coa privacidade que permiten recuperar o control sobre o dispositivo.

### Sistemas operativos libres para móbiles

Existen varias opcións de sistemas operativos libres baseados en Android, pero que non inclúen servizos e telemetría de Google. Aquí imos destacar tres:

- **<img src="logos/grapheneos.jpg" style="height:0.5cm" alt="image" /> [GrapheneOS](https://grapheneos.org/)**:

  - Baseada en Android, pero con importantes melloras de seguridade e privacidade.

  - Non inclúe servizos de Google, garantindo máis independencia e menor rastrexo.

  - So é compatible con dispositivos Pixel.

- **<img src="logos/lineageos.jpg" style="height:0.5cm" alt="image" /> [LineageOS](https://lineageos.org/)**:

  - Unha das opcións máis populares, baseada en Android pero sen software privativo de Google.

  - Permite instalar microG opcionalmente, para compatibilidade con aplicacións que requiren os servizos de Google.

  - Compatible cunha ampla variedade de dispositivos. [Aquí podedes ver a lista de dispositivos compatibles.](https://wiki.lineageos.org/devices/). E dentro de cada un atoparás unha guía detallada da instalación.

- **<img src="logos/e-os.jpg" style="height:0.5cm" alt="image" /> [/e/OS](https://e.foundation/es/e-os/)**:

  - Sistema operativo libre con servizos substitutivos de Google. Basease en Android, polo que é compatible coa maioría de aplicacións.

  - Ofrece unha tenda de aplicacións con aplicacións libres e privativas analizadas en termos de rastrexo.

  - [Aquí podes ver a lista de dispositivos compatibles.](https://doc.e.foundation/easy-installer#list-of-devices-supported-by-the-easy-installer).Tamén atoparás as instrucións de como instalalo.

### Non sempre se pode

Por desgraza, a diferenza do caso dos ordenadores, non todos os móbiles permiten cambiar o sistema operativo, xa que algúns veñen bloqueados de fábrica. Un exemplo máis de como os fabricantes buscan que vaias cambiando de móbil cada poucos anos e xerando máis lixo. Á hora de mercar un móbil novo, é recomendable visitar as páxinas web de proxectos como LineageOS ou GrapheneOS para ver a lista de dispositivos soportados.

Instalar un sistema operativo libre no móbil permite recuperar a privacidade e o control sobre o dispositivo, pero require certa planificación e coñecemento técnico. Se se elixe a opción axeitada, pode ser unha excelente alternativa a Android con Google ou a iOS.

## Tails OS, un sistema operativo para ir un paso máis alá.

[Tails OS](https://tails.net/) (The Amnesic Incognito Live System) é unha distribución de Linux baseada en Debian, deseñada especificamente para preservar a privacidade e o anonimato das súas usuarias. Funciona como un sistema en vivo, executándose dende un USB sen deixar rastros no ordenador utilizado. Isto convérteo nunha ferramenta ideal para aquelas persoas que necesitan protexer a súa identidade e comunicacións en casos máis extremos.

### Características principais

- **Anonimato en liña:** Todas as conexións de Tails están obrigatoriamente canalizadas a través da rede Tor, garantindo que a actividade da usuaria permaneza oculta.

- **Non deixa rastros:** Ao executarse en modo live, Tails non garda ningunha información no ordenador a menos que a usuaria o especifique. Unha vez apaguemos o ordenador, todo o noso rastro bórrase inmediatamente, como se non fixeramos nada.

- **Ferramentas de seguridade integradas:** Inclúe aplicacións como o navegador Tor, mensaxería cifrada e ferramentas de cifrado de ficheiros para unha comunicación segura.

### Para quen está pensado?

Tails é especialmente útil para xornalistas, activistas, denunciantes e calquera persoa que precise traballar en condicións de alta seguridade. Un exemplo coñecido é Edward Snowden, quen utilizou Tails para comunicarse con xornalistas ao revelar documentos clasificados.

### Instalación e uso

Para empregar Tails, cómpre unha memoria USB de polo menos 8 GB e un ordenador que poida arrancar dende USB. O proceso de instalación implica descargar a imaxe do sistema desde o sitio oficial de Tails e seguir as instrucións para crear o medio de arranque. Na súa web tedes unha [guía completa sobre como instala.](https://tails.net/install/index.es.html)

En resumo, Tails é unha ferramenta poderosa para aqueles que buscan manter a súa privacidade no mundo dixital, proporcionando un contorno seguro e efémero para realizar actividades sensibles sen deixar pegadas.

## Conclusión

O uso de sistemas operativos libres é fundamental para garantir a liberdade dixital, a privacidade e a seguridade das usuarias. Ademais, contribúe a un modelo tecnolóxico máis ético e sustentable. Optar por sistemas como **GNU/Linux** non só permite maior control sobre os nosos dispositivos, senón que tamén fomenta unha sociedade máis xusta e independente das grandes corporacións tecnolóxicas.
