# Ciberataques Típicos <span id="cap:ciberataques"></span>

Os ataques cibernéticos son unha das maiores ameazas para a seguridade e privacidade na Internet. Estes ataques, que varían en complexidade e alcance, teñen como obxectivo obter acceso non autorizado a información sensible, interromper a comunicación ou causar danos a sistemas informáticos. A continuación, describimos algúns dos ataques máis comúns, os seus obxectivos e as mellores prácticas para protexerse deles.

## Phishing<span id="sec:phishing"></span>

O phishing é unha técnica de ataque que se utiliza para enganar ás vítimas para que revelen información persoal sensible, como contrasinais, números de tarxetas de crédito ou datos bancarios. Os atacantes envían correos electrónicos ou mensaxes que simulan ser dunha entidade de confianza (como un banco ou un servizo en liña popular) para enganar á vítima e que esta faga clic nun enlace que a redirixirá a unha páxina falsa.

Neste tipo de ataques imítanse os enlaces web ou direccións de correo reais cambiando algún caracter ou simulando ser direccións reais. Os correos electrónicos ou mensaxes de phishing son cada vez máis sofisticados, e moitas veces inclúen logotipos e deseños de páxinas web reais, facendo que sexa difícil distinguir entre un correo electrónico auténtico e un de phishing. A principal diferenza é que os enlaces ou formularios que inclúen diríxenos a sitios web falsos, onde os atacantes recollen os teus datos persoais.

**Exemplos**: Existen diversos tipos de correos ou mensaxes de phishing, algúns dos cales inclúen:

- **Páxinas web falsas que imitan páxinas reais**: Un exemplo común de phishing é a creación de páxinas web falsas que imitan perfectamente a páxina oficial dunha empresa, banco ou servizo en liña. Estas páxinas utilizan o mesmo deseño, logotipos e incluso a mesma URL (con pequenas variacións, como un número ou letra adicional). A principal diferenza é que, ao introducir os teus datos persoais ou contrasinais, estes son recollidos polo atacante. Un exemplo típico pode ser unha páxina falsa de inicio de sesión, onde a URL pode parecer semellante, como https://www.paypall.com en vez de https://www.paypal.com. Se te fixas, a diferenza está no ’l’ engadido ao final.

- **Enlaces falsos con texto enganoso**: Outro exemplo común de phishing é cando se mostra un enlace cun texto que parece fiable, pero en realidade o enlace dirixe ao atacante a un sitio web malicioso. Por exemplo, un correo electrónico pode conter un enlace que di ”Para máis información, accede a [https://gl.wikipedia.org](https://galicia.isf.es/)”, pero cando pases o cursor sobre o enlace, verás que a URL realmente leva a un sitio completamente diferente. Neste caso, podes ver que ao pinchar en https://gl.wikipedia.org realmente estás sendo redirixido a https://galicia.isf.es/.

- **Uso de caracteres de alfabeto diferente**: Outro truco que se emprega no phishing é o uso de caracteres que se parecen aos do alfabeto latino, pero que realmente pertencen a outro alfabeto. Por exemplo, un atacante pode utilizar caracteres cirílicos ou gregos que son visualmente semellantes ás letras do alfabeto latino. Unha URL falsa como http://www.google.com (onde o ’o’ é un [carácter cirílico](https://es.wikipedia.org/wiki/%D0%9E) que parece un ’o’ normal) pode enganar á vítima facendo que pense que está visitando o sitio web oficial de Google, cando en realidade está a ser dirixida a un sitio malicioso.

- **Subdominios:**Un exemplo común de ataque de phishing relacionado cos subdominios é cando un atacante crea un subdominio que parece oficial, pero que en realidade non o é, intercambiando o subdominio e o dominio principal. Por exemplo, un correo no que nos envían un correo dicindo que temos unha notificación pendente e que temos que iniciar sesión en https://xunta.sede.gal/identificate, para roubarnos o contrasinal, cando o enderezo real da sede electrónica da xunta é https://sede.xunta.gal/identificate. Lembranza importante: os subdominios deben ser lidos de dereita a esquerda. Outro exemplo similar é que nos intentaran facer crer que temos que entrar en https://sede.xunta.gal-identificate.gal, en lugar de https://sede.xunta.gal/identificate. É importante ler os enderezos enteiros.

- **Códigos QR falsos**: Hoxe en día estamos habituadas a ter que escanear códigos QR para moitas cousas: ver o menú nun restaurante, ver información sobre cando chega o próximos autobús, etc. Escaneamos o QR, dámoslle a abrir, e listo. Sen embargo, debemos ter máis coidado. Cando escaneamos un código QR debemos de fixarnos antes de darlle a abrir a que páxina nos está dirixindo (a maioría das aplicacións amosan primeiro o enlace e logo piden confirmación para abrilo), e ter en conta os consellos mencionados anteriormente. Por exemplo, alguén podería ter pegado un QR falso enriba do auténtico, e redirixirnos a unha páxina moi semellante á auténtica, pero co obxectivo de roubarnos información dalgún tipo.

## Spoofing

O spoofing é un ataque no que un atacante finxe ser outra persoa ou sistema para enganar ao destinatario ou á rede. Este ataque pode ocorrer en diversas formas, como spoofing de direccións de correo electrónico, de IP ou de DNS. O obxectivo principal é enganar ás usuarias ou sistemas para que confíen no atacante e, así, obteñan acceso a datos ou sistemas.

**Exemplos**:

- **Spoofing de correo electrónico**: O spoofing de correo electrónico é un ataque no que o atacante falsifica a dirección do remitente dun correo electrónico para que pareza que provén dunha fonte fiable, cando en realidade foi enviado dende outra fonte. Por exemplo, aínda que no encabezado do correo apareza que foi enviado dende a@email.com, o atacante pode modificar os datos para que pareza que o correo provén de esa dirección, cando en realidade foi enviado desde outro servidor. Isto pode enganar á vítima, facéndoa crer que o correo é de confianza, o que pode levar a que realice accións como facer clic en enlaces ou descargar arquivos maliciosos.

  Isto ocorre porque o protocolo de correo electrónico, como SMTP (Simple Mail Transfer Protocol), non verifica de forma exhaustiva a autenticidade da dirección do remitente. A dirección do remitente que aparece no encabezado dun correo electrónico pode ser manipulada facilmente polo atacante. O servidor de correo que envía o mensaxe só transmite a información do remitente que se lle indica, sen realizar validacións profundas sobre se esa dirección realmente pertence a quen di que pertence.

  Para evitar este tipo de ataques, é recomendable verificar a autenticidade dos correos, non facer clic en enlaces sospeitosos e empregar protocolos de seguridade.

- **SMS Spoofing**: O spoofing por SMS é un tipo de ataque no que os ciberdelincuentes envían mensaxes de texto que parecen vir dunha fonte fiable, como un banco ou unha empresa coñecida. Para iso, os atacantes poden manipular o número de teléfono ou o nome que aparece no encabezado do mensaxe, facendo que semelle que a mensaxe vén de, por exemplo, o teu banco e apareza na mesma conversa na que o banco che enviou previamente outros SMS. Isto conséguese a través dunha técnica chamada alphanumeric sender ID ou sender name, que permite que, en lugar de ver un número de teléfono, se mostre un nome ou etiqueta, como o nome do banco. Así, ao recibir o SMS, á usuaria pode ver algo como ”BANCO” en vez de un número, o que xera confianza no mensaxe.

  Aínda que este mecanismo pode ser útil para identificar mensaxes oficiais, tamén pode ser explotado polos atacantes para falsificar a orixe do SMS e facer que pareza vir dunha fonte fiable. Por exemplo, o atacante pode configurar o seu sistema para que apareza o nome dun banco ou dunha empresa coñecida, cando en realidade está enviando o mensaxe desde un número diferente. Isto facilita que as vítimas caian nun intento de phishing ou fraudes, xa que confían na aparencia do mensaxe sen verificar a súa autenticidade.

  Por iso, é importante ser cauteloso coas mensaxes recibidas, mesmo cando parece que veñen dunha fonte oficial, e non confiar unicamente no nome ou número que aparece no encabezado do SMS. Verificar sempre os enlaces, números e remitentes pode evitar caer en ataques de spoofing.

## Ataque Man-in-the-Middle (MITM)

Un **ataque Man-in-the-Middle (MITM)** é un tipo de ataque no que a persoa atacante intercepta e, nalgunhas ocasións, manipula a comunicación entre dúas partes que están intentando comunicarse entre si. Neste ataque, a vítima e o destino da comunicación (por exemplo, un servidor ou outra usuaria) cren que están a comunicarse de forma directa, pero en realidade, todo o tráfico pasa polo atacante, que pode ler, alterar ou redirixir esa información.

### Como funciona un ataque MITM?

- **Interceptación de comunicación**: A atacante colócase entre as dúas partes que están a comunicarse. Isto pode ocorrer, por exemplo, en redes Wi-Fi públicas ou non seguras, onde o atacante se fai pasar por un punto de acceso (access point) lexítimo, coñecido como un ataque de Evil Twin. As vítimas conéctanse á súa rede, e todo o seu tráfico de datos pasa por ela.

- **Desencriptado da comunicación**: Se as comunicacións entre as dúas partes están cifradas (como sucede co protocolo HTTPs), a atacante pode ser capaz de realizar un downgrade ou forzar a conexión a un protocolo menos seguro (por exemplo, HTTP sen cifrar), ou en certos casos, aproveitar vulnerabilidades en protocolos de enriptado para descifrar o tráfico.

- **Manipulación de datos**: A atacante tamén pode modificar os datos que se están a transmitir entre as vítimas. Por exemplo, pode alterar unha transacción financeira, cambiando o número da conta ao que se debe realizar un pagamento, ou engadir datos maliciosos nunha mensaxe que a vítima espera recibir.

- **Falsificación de identidade**: A atacante tamén pode facerse pasar por unha das partes na comunicación. Isto pode implicar enviar mensaxes ou solicitar información como se fose unha das vítimas, engadindo máis complexidade ao ataque.

### Exemplo típico dun ataque MITM

Un exemplo común ocorre cando unha usuaria se conecta a unha rede Wi-Fi pública non segura, como as que se atopan en cafeterías ou aeroportos. O atacante establece un punto de acceso que simula ser unha rede pública aberta. As vítimas que se conectan a esa rede envían tráfico sen cifrar que pasa directamente polo atacante. Neste punto, o atacante pode espiar todo o tráfico entre a usuaria e os servidores aos que está intentando conectarse, e pode incluso alterar as solicitudes ou respostas.

Outro escenario no que se pode producir un MITM é cando se establece unha comunicación HTTPS, pero o atacante consegue enganar á vítima para que a conexión non se cifre correctamente ou poida acceder a claves de cifrado. Isto pode ser feito, por exemplo, mediante un ataque de SSL Stripping, onde o atacante redirixe o tráfico HTTPS a HTTP non cifrado. Hai que ter en conta que hai páxinas que teñen versión HTTP e versión HTTPs.

### Como evitar un ataque MITM

- **Usar HTTPS**: Sempre que sexa posible, asegurate de que as webs utilicen HTTPS en vez de HTTP. O HTTPS cifra a comunicación entre o navegador e o servidor, facendo moito máis difícil que un atacante poida interceptar ou modificar os datos.

- **Verificar os certificados SSL/TLS**: Ao acceder a sitios web, revisa que o certificado SSL/TLS sexa válido e que o navegador indique que a conexión é segura (normalmente aparece un cadeado verde na barra de enderezo).

- **Evitar redes Wi-Fi públicas non seguras**: Sempre que sexa posible, evita conectarte a redes Wi-Fi públicas ou non cifradas e intente compartir wifi dende o teu móbil. Se tes que usar unha Wi-Fi pública usa unha VPN para cifrar todo o tráfico e evitar que un atacante poida interceptalo. se

- **Habilitar a autenticación de dous factores (2FA)**: A autenticación en dous pasos pode evitar que un atacante obteña acceso a contas importantes, mesmo se consegue interceptar a contrasinal.

### Resumo

Un ataque MITM permite ao atacante interceptar, manipular ou falsificar a comunicación entre dúas partes, o que pode levar ao roubo de información sensible ou á alteración de transaccións. A mellor maneira de defenderse contra este tipo de ataque é garantir que as comunicacións sexan seguras (usando HTTPS), evitar redes non seguras e usar mecanismos de protección adicionais como as VPNs ou a autenticación de dous factores.

## Ransomware

O **ransomware** é un tipo de malware que ten como obxectivo secuestrar os datos dunha vítima e pedir un rescate para liberalos. Este tipo de ataque está orientado á extorsión, pois a atacante tenta forzar á vítima a pagar unha suma de diñeiro, normalmente en cripto moedas, para que a vítima poida recuperar o acceso aos seus arquivos ou sistemas. Existen diferentes tipos de ransomware, pero todos comparten a mesma estratexia básica de encriptar os arquivos ou bloquear o acceso ao sistema.

### Como funciona o Ransomware

- **Infección inicial**: O primeiro paso dun ataque de ransomware é a infiltración no sistema vítima. Isto pode ocorrer de diversas maneiras, como a través de correos electrónicos de phishing, sitios web comprometidos ou vulnerabilidades de software. As ciberdelincuentes tamén poden empregar bots ou outros métodos automatizados para propagar o malware.

- **Encriptado de arquivos**: Unha vez que o malware se executa no sistema da vítima, este comeza a encriptar os arquivos. A maioría dos ransomware usa algoritmos de cifrado fortes para garantir que os arquivos non poidan ser abertos ou utilizados sen a clave de descifrado (que so ten a atacante). Os arquivos afectados poden ser documentos, fotos, vídeos, bases de datos ou calquera outro tipo de arquivo valioso.

- **Exhibición do rescate**: Despois de encriptar os arquivos, o ransomware mostra unha mensaxe á vítima, informando sobre o secuestro e exixindo un rescate. Normalmente, esta mensaxe especifica o importe que debe pagar a vítima, así como as instrucións para realizar o pago (normalmente en cripto moedas, debido á súa natureza anónima).

- **Bloqueo do sistema**: Algúns tipos de ransomware tamén poden bloquear completamente o acceso ao sistema ou á rede da vítima, impedindo que se poidan realizar calquera actividade até que se pague o rescate. Este tipo de ataque tamén pode incluír o cifrado de dispositivos de almacenaxe conectados á máquina principal ou a redes internas.

- **Filtración de datos**: Algunhas variantes de ransomware, como o *Ransomware as a Service* (RaaS), tamén rouban datos sensibles antes de encriptalos, para usalos como parte da extorsión. Nestas variantes, as atacantes ameazan con divulgar ou vender os datos roubados se a vítima non paga o rescate.

### Exemplos de Ransomware Famosos

Existen varios tipos de ransomware que se fixeron famosos por afectar a organizacións e individuos en todo o mundo:

- **WannaCry**: Este ataque, que se produciu en maio de 2017, afectou a miles de dispositivos en todo o mundo, incluíndo hospitais, empresas e axencias gobernamentais. Utilizou unha vulnerabilidade no sistema operativo Windows, coñecida como EternalBlue, para propagar o malware e encriptar os arquivos das usuarias.

- **NotPetya**: Outro ataque importante, dirixido tamén a dispositivos co sistema operativo Windows, afectou a empresas e entidades en Europa, especialmente no sector financeiro e no ámbito das infraestruturas críticas. Aínda que inicialmente parecía ser un ataque de ransomware, o seu obxectivo real era a destrución de datos, xa que a clave de descifrado nunca foi proporcionada.

- **Ryuk**: Este é un ransomware que foi dirixido principalmente a organizacións grandes e gobernos, e dirixido a dispositivos co sistema operativo Windows. A diferenza doutros tipos de ransomware, Ryuk está moi enfocado no roubo de datos de alto valor e na exixencia de grandes sumas de diñeiro polo rescate. Ryuk tamén se usa en combinación con outros tipos de malware, como TrickBot, para obter acceso ás redes internas das vítimas.

### Como protexerse do Ransomware

- **Realiza copias de seguridade regulares**: Ter copias de seguridade actualizadas é a mellor defensa contra o ransomware. Se un sistema é secuestrado, pode restaurarse rapidamente a partir dunha copia de seguridade sen ter que pagar o rescate. É importante que as copias de seguridade estean almacenadas en lugares externos ou en nubes seguras que non sexan accesibles desde a rede local. Hai que ter en conta que non é unha solución segura ao 100%, xa que o ransomware pode ser preparado para que se execute tempo despois de infectar aos dispositivos, polo que as copia de seguridade poderían chegar a estar infectadas tamén,

- **Manten o software actualizado**: A maioría das infeccións de ransomware aproveitan vulnerabilidades de software para infiltrarse nos sistemas. Manter os sistemas operativos, as aplicacións e os programas antivirus actualizados pode reducir o risco de infeccións.

- **Non fagas clic en enlaces ou arquivos sospeitosos**: Moitas veces, os ataques de ransomware comezan a través de correos electrónicos de phishing ou sitios web comprometidos. Non fagas clic en enlaces ou descargues arquivos de fontes non fiables. Tamén debes ser cautelosa cando se reciben mensaxes de remitentes descoñecidas, especialmente se inclúen arquivos adxuntos ou enlaces.

- **Usar software de seguridade robusto**: Asegúrate de ter instalado un programa antivirus actualizado e configurar un firewall para impedir a entrada de malware na túa rede. Algúns programas antivirus tamén teñen detección de ransomware, o que pode axudar a bloquear o malware antes de que se execute. Tamén hai que ter en conta que case a totalidade de ataques están dirixidos a dispositivos co sistema operativo Windows, polo que empregar alternativas libres como GNU/Linux diminúe as posibilidades de ser infectada.

### Conclusión

O ransomware segue sendo unha ameaza significativa para empresas e individuos, causando danos financeiros e perda de datos. Adoptar boas prácticas de seguridade, como realizar copias de seguridade regulares, manter o software actualizado e ser cautelosa coas fontes e enlaces de correos electrónicos, pode axudar a minimizar os riscos e protexer a información persoal e corporativa. Se ben pagar o rescate pode parecer unha solución, é importante lembrar que non hai garantías de que o atacante libere os datos ou non volva atacar no futuro. E se es infectada, o primeiro paso debe ser avisar ás autoridades.

## Keylogging

O **keylogging** é un tipo de ataque informático no que o atacante instala un programa malicioso (conocido como keylogger) no sistema da vítima. O obxectivo do keylogger é rexistrar as teclas que a vítima premia no teclado, podendo capturar información sensible como contrasinais, números de tarxetas de crédito, mensaxes privadas e outra información confidencial.

### Como funciona o Keylogging

Un keylogger pode operar de diferentes formas. O máis común é que o software malicioso se instale sen o coñecemento da vítima, por exemplo, a través de correos electrónicos de phishing ou software de descargas comprometidas. Unha vez instalado no sistema, o keylogger comeza a monitorizar as accións do teclado e a almacenar os datos sobre as teclas premidas.

Os keyloggers poden ser de diferentes tipos:

- **Keyloggers de software**: Este tipo de keylogger é unha aplicación maliciosa que se executa no sistema da vítima. Pode ocultarse no fondo e ser difícil de detectar. Os keyloggers de software son os máis comúns e poden rexistrar todas as teclas, incluíndo contrasinais e datos bancarios, sen que a vítima se dea conta.

- **Keyloggers de hardware**: Este tipo de keylogger é un dispositivo físico que se conecta entre o teclado e o ordenador. Pode ser colocado no conector USB ou PS/2, ou no propio teclado, para rexistrar as teclas premidas. A súa vantaxe é que non depende do sistema operativo, polo que pode rexistrar as teclas mesmo cando o sistema operativo está infectado ou non funciona correctamente.

- **Keyloggers de pantalla táctil**: Nos dispositivos móbiles, os keyloggers tamén poden capturar as accións realizadas en pantallas táctiles. Aínda que non rexistran as teclas de forma directa, poden capturar os movementos de xiros ou toques realizados na pantalla e mesmo as teclas virtuais que se premian en dispositivos móbiles.

### Exemplos de Keylogging

Un exemplo de keylogger moi común é o software malicioso que se infiltra a través de correos electrónicos de phishing. Imos imaxinar que unha atacante envía un correo de phishing simulando ser unha entidade fiable, como un banco ou un servizo en liña. O correo pode incluír un enlace que leva a un sitio web falso ou un arquivo adxunto. Se a vítima fai clic no enlace ou abre o arquivo, o keylogger pode ser instalado no seu sistema sen que se decate, comezando a rexistrar as teclas premidas.

Un exemplo máis específico de keylogger de hardware sería un dispositivo que se conecta entre o teclado e o ordenador, sendo invisible á vítima. Estes dispositivos poden ser usados, por exemplo, en cibercafés ou en ordenadores públicos para roubar información sensible sen que a vítima sexa consciente da súa presenza.

### Como protexerse do Keylogging

- **Manten o sistema operativo e as aplicacións actualizadas**: Os keyloggers, como outros tipos de malware, a miúdo explotan vulnerabilidades nos sistemas operativos ou nas aplicacións para infiltrarse. Manter o sistema e as aplicacións actualizadas axuda a pechar esas brechas de seguridade.

- **Evitar clics en enlaces sospeitosos**: Non fagas clic en enlaces ou descargues arquivos de fontes non confiables. Os keyloggers de software adoitan instalarse cando se fai clic nun enlace malicioso ou se descarga un arquivo de phishing.

- **Usar contrasinais de dous factores**: Incluso se un keylogger captura os teus contrasinais, o uso de contrasinais de dous factores (2FA) pode engadir unha capa adicional de seguridade. Aínda que o atacante teña o teu contrasinal, necesitaría acceso ao dispositivo adicional (como un teléfono móbil) para completar a autenticación.

- **Evitar dispositivos públicos ou compartidos**: Non empregues teclados públicos ou ordenadores compartidos para introducir información sensible, como contrasinais ou datos bancarios. Se tes que usar un equipo compartido, considera usar un teclado virtual ou unha aplicación de autenticación adicional.

- **Usar teclados virtuais ou programas de protección contra keyloggers**: Algunhas ferramentas permiten introducir texto sen usar o teclado físico, como teclados virtuais na pantalla ou programas que protexen contra keyloggers detectados. Estas ferramentas poden ofrecer unha capa adicional de seguridade cando se introducen datos sensibles.

### Conclusión

O keylogging é unha ameaza importante para a seguridade e a privacidade das usuarias. As vítimas poden sufrir roubo de datos sensibles sen saber que están sendo vixiadas. Para protexerse deste tipo de ataque, é fundamental tomar medidas preventivas como o uso de software de seguridade actualizado, a práctica de boas hábitos de navegación e a adopción de medidas de autenticación fortes, como a autenticación en dous pasos.

## Conclusión dos ataques informáticos

Os ataques informáticos son unha ameaza constante na nosa vida dixital, e os exemplos que presentamos son só algúns dos moitos que existen. Desde o phishing até os ataques de man-in-the-middle ou o uso de malware como os keyloggers, as atacantes empregan técnicas sofisticadas para obter acceso a información sensible e vulnerar a nosa privacidade. Con todo, con coidado e coñecemento, podemos reducir considerablemente o risco de ser vítimas destes ataques. A implantación de prácticas de seguridade, como o uso de contrasinais fortes, a autenticación en dous pasos, e a precaución ao interactuar coas nosas contas en liña, pode axudar a protexer a nosa información. O máis importante é manterse informado, estar alerta ante posibles ameazas e actuar para garantir a nosa seguridade no mundo dixital.
