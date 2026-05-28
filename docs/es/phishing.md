# Ciberataques Típicos <span id="cap:ciberataques"></span>

Los ataques cibernéticos son una de las mayores amenazas para la seguridad y privacidad en Internet. Estos ataques, que varían en complejidad y alcance, tienen como objetivo obtener acceso no autorizado a información sensible, interrumpir la comunicación o causar daños a sistemas informáticos. A continuación, describimos algunos de los ataques más comunes, sus objetivos y las mejores prácticas para protegerse de ellos.

## Phishing<span id="sec:phishing"></span>

El phishing es una técnica de ataque que se utiliza para engañar a las víctimas para que revelen información personal sensible, como contraseñas, números de tarjetas de crédito o datos bancarios. Los atacantes envían correos electrónicos o mensajes que simulan ser de una entidad de confianza (como un banco o un servicio en línea popular) para engañar a la víctima y que esta haga clic en un enlace que la redirigirá a una página falsa.

En este tipo de ataques se imitan los enlaces web o direcciones de correo reales cambiando algún carácter o simulando ser direcciones reales. Los correos electrónicos o mensajes de phishing son cada vez más sofisticados, y muchas veces incluyen logotipos y diseños de páginas web reales, haciendo que sea difícil distinguir entre un correo electrónico auténtico y uno de phishing. La principal diferencia es que los enlaces o formularios que incluyen nos dirigen a sitios web falsos, donde los atacantes recogen tus datos personales.

**Ejemplos**: Existen diversos tipos de correos o mensajes de phishing, algunos de los cuales incluyen:

- **Páginas web falsas que imitan páginas reales**: Un ejemplo común de phishing es la creación de páginas web falsas que imitan perfectamente la página oficial de una empresa, banco o servicio en línea. Estas páginas utilizan el mismo diseño, logotipos e incluso la misma URL (con pequeñas variaciones, como un número o letra adicional). La principal diferencia es que, al introducir tus datos personales o contraseñas, estos son recogidos por el atacante. Un ejemplo típico puede ser una página falsa de inicio de sesión, donde la URL puede parecer similar, como https://www.paypall.com en vez de https://www.paypal.com. Si te fijas, la diferencia está en la ’l’ añadida al final.

- **Enlaces falsos con texto engañoso**: Otro ejemplo común de phishing es cuando se muestra un enlace con un texto que parece fiable, pero en realidad el enlace dirige al atacante a un sitio web malicioso. Por ejemplo, un correo electrónico puede contener un enlace que dice ”Para más información, accede a [https://gl.wikipedia.org](https://galicia.isf.es/)”, pero cuando pases el cursor sobre el enlace, verás que la URL realmente lleva a un sitio completamente diferente. En este caso, puedes ver que al pinchar en https://gl.wikipedia.org realmente estás siendo redirigido a https://galicia.isf.es/.

- **Uso de caracteres de alfabeto diferente**: Otro truco que se emplea en el phishing es el uso de caracteres que se parecen a los del alfabeto latino, pero que realmente pertenecen a otro alfabeto. Por ejemplo, un atacante puede utilizar caracteres cirílicos o griegos que son visualmente semejantes a las letras del alfabeto latino. Una URL falsa como http://www.google.com (donde la ’o’ es un [carácter cirílico](https://es.wikipedia.org/wiki/%D0%9E) que parece una ’o’ normal) puede engañar a la víctima haciendo que piense que está visitando el sitio web oficial de Google, cuando en realidad está siendo dirigida a un sitio malicioso.

- **Subdominios:**Un ejemplo común de ataque de phishing relacionado con los subdominios es cuando un atacante crea un subdominio que parece oficial, pero que en realidad no lo es, intercambiando el subdominio y el dominio principal. Por ejemplo, un correo en el que nos envían un correo diciendo que tenemos una notificación pendiente y que tenemos que iniciar sesión en https://xunta.sede.gal/identificate, para robarnos la contraseña, cuando la dirección real de la sede electrónica de la xunta es https://sede.xunta.gal/identificate. Recordatorio importante: los subdominios deben ser leídos de derecha a izquierda. Otro ejemplo similar ocurre cuando intentan hacernos creer que tenemos que entrar en https://sede.xunta.gal-identificate.gal, en lugar de https://sede.xunta.gal/identificate. Es importante leer las direcciones enteras.

- **Códigos QR falsos**: Hoy en día estamos habituadas a tener que escanear códigos QR para muchas cosas: ver el menú en un restaurante, ver información sobre cuándo llega el próximos autobús, etc. Escaneamos el QR, le damos a abrir, y listo. Sin embargo, debemos tener más cuidado. Cuando escaneamos un código QR debemos fijarnos antes de darle a abrir a qué página nos está dirigiendo (la mayoría de las aplicaciones muestran primero el enlace y luego piden confirmación para abrirlo), y tener en cuenta los consejos mencionados anteriormente. Por ejemplo, alguien podría haber pegado un QR falso encima del auténtico, y redirigirnos a una página muy semejante a la auténtica, pero con el objetivo de robarnos información de algún tipo.

## Spoofing

El spoofing es un ataque en el que un atacante finge ser otra persona o sistema para engañar al destinatario o a la red. Este ataque puede ocurrir en diversas formas, como spoofing de direcciones de correo electrónico, de IP o de DNS. El objetivo principal es engañar a las usuarias o sistemas para que confíen en el atacante y, así, obtengan acceso a datos o sistemas.

**Ejemplos**:

- **Spoofing de correo electrónico**: El spoofing de correo electrónico es un ataque en el que el atacante falsifica la dirección del remitente de un correo electrónico para que parezca que proviene de una fuente fiable, cuando en realidad fue enviado desde otra fuente. Por ejemplo, aunque en el encabezado del correo aparezca que fue enviado desde a@email.com, el atacante puede modificar los datos para que parezca que el correo proviene de esa dirección, cuando en realidad fue enviado desde otro servidor. Esto puede engañar a la víctima, haciéndola creer que el correo es de confianza, lo que puede llevar a que realice acciones como hacer clic en enlaces o descargar archivos maliciosos.

  Esto ocurre porque el protocolo de correo electrónico, como SMTP (Simple Mail Transfer Protocol), no verifica de forma exhaustiva la autenticidad de la dirección del remitente. La dirección del remitente que aparece en el encabezado de un correo electrónico puede ser manipulada fácilmente por el atacante. El servidor de correo que envía el mensaje solo transmite la información del remitente que se le indica, sin realizar validaciones profundas sobre si esa dirección realmente pertenece a quien dice que pertenece.

  Para evitar este tipo de ataques, es recomendable verificar la autenticidad de los correos, no hacer clic en enlaces sospechosos y emplear protocolos de seguridad.

- **SMS Spoofing**: El spoofing por SMS es un tipo de ataque en el que los ciberdelincuentes envían mensajes de texto que parecen venir de una fuente fiable, como un banco o una empresa conocida. Para ello, los atacantes pueden manipular el número de teléfono o el nombre que aparece en el encabezado del mensaje, haciendo que se asemeje a que el mensaje viene de, por ejemplo, tu banco y aparezca en la misma conversación en la que el banco te envió previamente otros SMS. Esto se consigue a través de una técnica llamada alphanumeric sender ID o sender name, que permite que, en lugar de ver un número de teléfono, se muestre un nombre o etiqueta, como el nombre del banco. Así, al recibir el SMS, la usuaria puede ver algo como ”BANCO” en vez de un número, lo que genera confianza en el mensaje.

  Aunque este mecanismo puede ser útil para identificar mensajes oficiales, también puede ser explotado por los atacantes para falsificar el origen del SMS y hacer que parezca venir de una fuente fiable. Por ejemplo, el atacante puede configurar su sistema para que aparezca el nombre de un banco o de una empresa conocida, cuando en realidad está enviando el mensaje desde un número diferente. Esto facilita que las víctimas caigan en un intento de phishing o fraudes, ya que confían en la apariencia del mensaje sin verificar su autenticidad.

  Por eso, es importante ser cauteloso con los mensajes recibidos, incluso cuando parece que vienen de una fuente oficial, y no confiar únicamente en el nombre o número que aparece en el encabezado del SMS. Verificar siempre los enlaces, números y remitentes puede evitar caer en ataques de spoofing.

## Ataque Man-in-the-Middle (MITM)

Un **ataque Man-in-the-Middle (MITM)** es un tipo de ataque en el que la persona atacante intercepta y, en algunas ocasiones, manipula la comunicación entre dos partes que están intentando comunicarse entre sí. En este ataque, la víctima y el destino de la comunicación (por ejemplo, un servidor u otra usuaria) creen que se están comunicando de forma directa, pero en realidad, todo el tráfico pasa por el atacante, que puede leer, alterar o redirigir esa información.

### ¿Cómo funciona un ataque MITM?

- **Intercepción de comunicación**: El atacante se coloca entre las dos partes que se están comunicando. Esto puede ocurrir, por ejemplo, en redes Wi-Fi públicas o no seguras, donde el atacante se hace pasar por un punto de acceso (access point) legítimo, conocido como un ataque de Evil Twin. Las víctimas se conectan a su red, y todo su tráfico de datos pasa por ella.

- **Descifrado de la comunicación**: Si las comunicaciones entre las dos partes están cifradas (como sucede con el protocolo HTTPs), el atacante puede ser capaz de realizar un downgrade o forzar la conexión a un protocolo menos seguro (por ejemplo, HTTP sin cifrar), o en ciertos casos, aprovechar vulnerabilidades en protocolos de encriptado para descifrar el tráfico.

- **Manipulación de datos**: El atacante también puede modificar los datos que se están transmitiendo entre las víctimas. Por ejemplo, puede alterar una transacción financiera, cambiando el número de la cuenta al que se debe realizar un pago, o añadir datos maliciosos en un mensaje que la víctima espera recibir.

- **Falsificación de identidad**: El atacante también puede hacerse pasar por una de las partes en la comunicación. Esto puede implicar enviar mensajes o solicitar información como si fuese una de las víctimas, añadiendo más complejidad al ataque.

### Ejemplo típico de un ataque MITM

Un ejemplo común ocurre cuando una usuaria se conecta a una red Wi-Fi pública no segura, como las que se encuentran en cafeterías o aeropuertos. El atacante establece un punto de acceso que simula ser una red pública abierta. Las víctimas que se conectan a esa red envían tráfico sin cifrar que pasa directamente por el atacante. En este punto, el atacante puede espiar todo el tráfico entre la usuaria y los servidores a los que está intentando conectarse, y puede incluso alterar las solicitudes o respuestas.

Otro escenario en el que se puede producir un MITM es cuando se establece una comunicación HTTPS, pero el atacante consigue engañar a la víctima para que la conexión no se cifre correctamente o pueda acceder a claves de cifrado. Esto puede ser hecho, por ejemplo, mediante un ataque de SSL Stripping, donde el atacante redirige el tráfico HTTPS a HTTP no cifrado. Hay que tener en cuenta que hay páginas que tienen versión HTTP y versión HTTPs.

### Cómo evitar un ataque MITM

- **Usar HTTPS**: Siempre que sea posible, asegurate de que las webs utilicen HTTPS en vez de HTTP. El HTTPS cifra la comunicación entre el navegador y el servidor, haciendo mucho más difícil que un atacante pueda interceptar o modificar los datos.

- **Verificar los certificados SSL/TLS**: Al acceder a sitios web, revisa que el certificado SSL/TLS sea válido y que el navegador indique que la conexión es segura (normalmente aparece un candado verde en la barra de dirección).

- **Evitar redes Wi-Fi públicas no seguras**: Siempre que sea posible, evita conectarte a redes Wi-Fi públicas o no cifradas e intente compartir wifi desde tu móvil. Si tienes que usar una Wi-Fi pública usa una VPN para cifrar todo el tráfico y evitar que un atacante pueda interceptarlo.

- **Habilitar la autenticación de dos factores (2FA)**: La autenticación en dos pasos puede evitar que un atacante obtenga acceso a cuentas importantes, incluso si consigue interceptar la contraseña.

### Resumen

Un ataque MITM permite al atacante interceptar, manipular o falsificar la comunicación entre dos partes, lo que puede llevar al robo de información sensible o a la alteración de transacciones. La mejor manera de defenderse contra este tipo de ataque es garantizar que las comunicaciones sean seguras (usando HTTPS), evitar redes no seguras y usar mecanismos de protección adicionales como las VPNs o la autenticación de dos factores.

## Ransomware

El **ransomware** es un tipo de malware que tiene como objetivo secuestrar los datos de una víctima y pedir un rescate para liberarlos. Este tipo de ataque está orientado a la extorsión, pues el atacante intenta forzar a la víctima a pagar una suma de dinero, normalmente en criptomonedas, para que la víctima pueda recuperar el acceso a sus archivos o sistemas. Existen diferentes tipos de ransomware, pero todos comparten la misma estrategia básica de encriptar los archivos o bloquear el acceso al sistema.

### Cómo funciona el Ransomware

- **Infección inicial**: El primer paso de un ataque de ransomware es la infiltración en el sistema víctima. Esto puede ocurrir de diversas maneras, como a través de correos electrónicos de phishing, sitios web comprometidos o vulnerabilidades de software. Los ciberdelincuentes también pueden emplear bots u otros métodos automatizados para propagar el malware.

- **Encriptado de archivos**: Una vez que el malware se ejecuta en el sistema de la víctima, este comienza a encriptar los archivos. La mayoría de los ransomware usa algoritmos de cifrado fuertes para garantizar que los archivos no puedan ser abiertos o utilizados sin la clave de descifrado (que solo tiene el atacante). Los archivos afectados pueden ser documentos, fotos, vídeos, bases de datos o cualquier otro tipo de archivo valioso.

- **Exhibición del rescate**: Después de encriptar los archivos, el ransomware muestra un mensaje a la víctima, informando sobre el secuestro y exigiendo un rescate. Normalmente, este mensaje especifica el importe que debe pagar la víctima, así como las instrucciones para realizar el pago (normalmente en criptomonedas, debido a su naturaleza anónima).

- **Bloqueo del sistema**: Algunos tipos de ransomware también pueden bloquear completamente el acceso al sistema o a la red de la víctima, impidiendo que se puedan realizar cualquier actividad hasta que se pague el rescate. Este tipo de ataque también puede incluir el cifrado de dispositivos de almacenaje conectados a la máquina principal o a redes internas.

- **Filtración de datos**: Algunas variantes de ransomware, como el *Ransomware as a Service* (RaaS), también roban datos sensibles antes de encriptarlos, para usarlos como parte de la extorsión. En estas variantes, los atacantes amenazan con divulgar o vender los datos robados si la víctima no paga el rescate.

### Ejemplos de Ransomware Famosos

Existen varios tipos de ransomware que se hicieron famosos por afectar a organizaciones e individuos en todo el mundo:

- **WannaCry**: Este ataque, que se produjo en mayo de 2017, afectó a miles de dispositivos en todo el mundo, incluyendo hospitales, empresas y agencias gubernamentales. Utilizó una vulnerabilidad en el sistema operativo Windows, conocida como EternalBlue, para propagar el malware y encriptar los archivos de las usuarias.

- **NotPetya**: Otro ataque importante, dirigido también a dispositivos con el sistema operativo Windows, afectó a empresas y entidades en Europa, especialmente en el sector financiero y en el ámbito de las infraestructuras críticas. Aunque inicialmente parecía ser un ataque de ransomware, su objetivo real era la destrucción de datos, ya que la clave de descifrado nunca fue proporcionada.

- **Ryuk**: Este es un ransomware que fue dirigido principalmente a organizaciones grandes y gobiernos, y dirigido a dispositivos con el sistema operativo Windows. A diferencia de otros tipos de ransomware, Ryuk está muy enfocado en el robo de datos de alto valor y en la exigencia de grandes sumas de dinero por el rescate. Ryuk también se usa en combinación con otros tipos de malware, como TrickBot, para obtener acceso a las redes internas de las víctimas.

### Cómo protegerse del Ransomware

- **Realiza copias de seguridad regulares**: Tener copias de seguridad actualizadas es la mejor defensa contra el ransomware. Si un sistema es secuestrado, puede restaurarse rápidamente a partir de una copia de seguridad sin tener que pagar el rescate. Es importante que las copias de seguridad estén almacenadas en lugares externos o en nubes seguras que no sean accesibles desde la red local. Hay que tener en cuenta que no es una solución segura al 100%, ya que el ransomware puede ser preparado para que se ejecute tiempo después de infectar a los dispositivos, por lo que las copias de seguridad podrían llegar a estar infectadas también,

- **Mantén el software actualizado**: La mayoría de las infecciones de ransomware aprovechan vulnerabilidades de software para infiltrarse en los sistemas. Mantener los sistemas operativos, las aplicaciones y los programas antivirus actualizados puede reducir el riesgo de infecciones.

- **No hagas clic en enlaces o archivos sospechosos**: Muchas veces, los ataques de ransomware comienzan a través de correos electrónicos de phishing o sitios web comprometidos. No hagas clic en enlaces o descargues archivos de fuentes no fiables. También debes ser cautelosa cuando se reciben mensajes de remitentes desconocidos, especialmente si incluyen archivos adjuntos o enlaces.

- **Usar software de seguridad robusto**: Asegúrate de tener instalado un programa antivirus actualizado y configurar un firewall para impedir la entrada de malware en tu red. Algunos programas antivirus también tienen detección de ransomware, lo que puede ayudar a bloquear el malware antes de que se ejecute. También hay que tener en cuenta que casi la totalidad de ataques están dirigidos a dispositivos con el sistema operativo Windows, por lo que emplear alternativas libres como GNU/Linux disminuye las posibilidades de ser infectada.

### Conclusión

El ransomware sigue siendo una amenaza significativa para empresas e individuos, causando daños financieros y pérdida de datos. Adoptar buenas prácticas de seguridad, como realizar copias de seguridad regulares, mantener el software actualizado y ser cautelosa con las fuentes y enlaces de correos electrónicos, puede ayudar a minimizar los riesgos y proteger la información personal y corporativa. Si bien pagar el rescate puede parecer una solución, es importante recordar que no hay garantías de que el atacante libere los datos o no vuelva a atacar en el futuro. Y si eres infectada, el primer paso debe ser avisar a las autoridades.

## Keylogging

El **keylogging** es un tipo de ataque informático en el que el atacante instala un programa malicioso (conocido como keylogger) en el sistema de la víctima. El objetivo del keylogger es registrar las teclas que la víctima pulsa en el teclado, pudiendo capturar información sensible como contraseñas, números de tarjetas de crédito, mensajes privados y otra información confidencial.

### Cómo funciona el Keylogging

Un keylogger puede operar de diferentes formas. Lo más común es que el software malicioso se instale sin el conocimiento de la víctima, por ejemplo, a través de correos electrónicos de phishing o software de descargas comprometidas. Una vez instalado en el sistema, el keylogger comienza a monitorizar las acciones del teclado y a almacenar los datos sobre las teclas pulsadas.

Los keyloggers pueden ser de diferentes tipos:

- **Keyloggers de software**: Este tipo de keylogger es una aplicación maliciosa que se ejecuta en el sistema de la víctima. Puede ocultarse en el fondo y ser difícil de detectar. Los keyloggers de software son los más comunes y pueden registrar todas las teclas, incluyendo contraseñas y datos bancarios, sin que la víctima se dé cuenta.

- **Keyloggers de hardware**: Este tipo de keylogger es un dispositivo físico que se conecta entre el teclado y el ordenador. Puede ser colocado en el conector USB o PS/2, o en el propio teclado, para registrar las teclas pulsadas. Su ventaja es que no depende del sistema operativo, por lo que puede registrar las teclas incluso cuando el sistema operativo está infectado o no funciona correctamente.

  **Keyloggers de pantalla táctil**: En los dispositivos móviles, los keyloggers también pueden capturar las acciones realizadas en pantallas táctiles. Aunque no registran las teclas de forma directa, pueden capturar los movimientos de giros o toques realizados en la pantalla e incluso las teclas virtuales que se pulsan en dispositivos móviles.

### Ejemplos de Keylogging

Un ejemplo de keylogger muy común es el software malicioso que se infiltra a través de correos electrónicos de phishing. Vamos a imaginar que un atacante envía un correo de phishing simulando ser una entidad fiable, como un banco o un servicio en línea. El correo puede incluir un enlace que lleva a un sitio web falso o un archivo adjunto. Si la víctima hace clic en el enlace o abre el archivo, el keylogger puede ser instalado en su sistema sin que se percate, comenzando a registrar las teclas pulsadas.

Un ejemplo más específico de keylogger de hardware sería un dispositivo que se conecta entre el teclado y el ordenador, siendo invisible a la víctima. Estos dispositivos pueden ser usados, por ejemplo, en cibercafés o en ordenadores públicos para robar información sensible sin que la víctima sea consciente de su presencia.

### Cómo protegerse del Keylogging

- **Mantén el sistema operativo y las aplicaciones actualizadas**: Los keyloggers, como otros tipos de malware, a menudo explotan vulnerabilidades en los sistemas operativos o en las aplicaciones para infiltrarse. Mantener el sistema y las aplicaciones actualizadas ayuda a cerrar esas brechas de seguridad.

- **Evitar clics en enlaces sospechosos**: No hagas clic en enlaces o descargues archivos de fuentes no confiables. Los keyloggers de software suelen instalarse cuando se hace clic en un enlace malicioso o se descarga un archivo de phishing.

- **Usar contraseñas de dos factores**: Incluso si un keylogger captura tus contraseñas, el uso de contraseñas de dos factores (2FA) puede añadir una capa adicional de seguridad. Aunque el atacante tenga tu contraseña, necesitaría acceso al dispositivo adicional (como un teléfono móvil) para completar la autenticación.

- **Evitar dispositivos públicos o compartidos**: No emplees teclados públicos u ordenadores compartidos para introducir información sensible, como contraseñas o datos bancarios. Si tienes que usar un equipo compartido, considera usar un teclado virtual o una aplicación de autenticación adicional.

- **Usar teclados virtuales o programas de protección contra keyloggers**: Algunas herramientas permiten introducir texto sin usar el teclado físico, como teclados virtuales en la pantalla o programas que protegen contra keyloggers detectados. Estas herramientas pueden ofrecer una capa adicional de seguridad cuando se introducen datos sensibles.

### Conclusión

El keylogging es una amenaza importante para la seguridad y la privacidad de las usuarias. Las víctimas pueden sufrir robo de datos sensibles sin saber que están siendo vigiladas. Para protegerse de este tipo de ataque, es fundamental tomar medidas preventivas como el uso de software de seguridad actualizado, la práctica de buenos hábitos de navegación y la adopción de medidas de autenticación fuertes, como la autenticación en dos pasos.

## Conclusión de los ataques informáticos

Los ataques informáticos son una amenaza constante en nuestra vida digital, y los ejemplos que presentamos son solo algunos de los muchos que existen. Desde el phishing hasta los ataques de man-in-the-middle o el uso de malware como los keyloggers, los atacantes emplean técnicas sofisticadas para obtener acceso a información sensible y vulnerar nuestra privacidad. Sin embargo, con cuidado y conocimiento, podemos reducir considerablemente el riesgo de ser víctimas de estos ataques. La implantación de prácticas de seguridad, como el uso de contraseñas fuertes, la autenticación en dos pasos, y la precaución al interactuar con nuestras cuentas en línea, puede ayudar a proteger nuestra información. Lo más importante es mantenerse informado, estar alerta ante posibles amenazas y actuar para garantizar nuestra seguridad en el mundo digital.
