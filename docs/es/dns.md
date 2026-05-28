# DNS seguro. Qué es y alternativas seguras<span id="cap:dns"></span>

## ¿Qué es un DNS?

El DNS (**Sistema de Nombres de Dominio**) es un servicio fundamental de Internet que funciona como una especie de agenda telefónica de sitios web. Permite traducir los nombres de dominio (como **www.example.com**) en direcciones IP numéricas (como **192.168.1.1**) que los ordenadores utilizan para comunicarse entre sí. Sin el DNS, tendríamos que recordar la dirección IP exacta de cada sitio web que queremos visitar, lo que sería muy complicado. En resumen, el DNS facilita la navegación en Internet al hacer que los nombres de dominio sean más fáciles de usar, a la vez que permite la comunicación entre los dispositivos de red.

## Impacto del DNS en nuestra privacidad

El servicio DNS, aunque fundamental para la navegación en Internet, también puede afectar a nuestra privacidad. Cada vez que accedemos a una página web, nuestro dispositivo envía una solicitud al servidor DNS para obtener la dirección IP asociada al nombre de dominio. Durante este proceso, el servidor DNS puede registrar información sobre los sitios web que visitamos, junto con nuestra dirección IP, lo que permite el seguimiento y la creación de perfiles de navegación.

Si usamos servidores DNS públicos o los proporcionados por los proveedores de servicios de Internet (ISP), estos servidores pueden recopilar y almacenar nuestros datos de navegación, incluso compartirlos con terceros, como anunciantes o autoridades gubernamentales. Esto puede resultar en un riesgo para nuestra privacidad, especialmente si no se implementan medidas adecuadas para proteger la información que circula en nuestras conexiones.

Por otro lado, al utilizar servicios de DNS seguros y privados, como DNS sobre HTTPS (DoH) o DNS sobre TLS (DoT), podemos minimizar la posibilidad de que nuestros datos sean espiados o manipulados, garantizando así una mayor confidencialidad en nuestra navegación en Internet. Al encriptar las solicitudes DNS, se impide que terceros intercepten o registren las páginas que visitamos, mejorando nuestra privacidad en línea.

## Sistemas de DNS

Existen varios tipos de sistemas de DNS que difieren en la forma en que gestionan y protegen las solicitudes de nombre de dominio. A continuación, explicamos los principales:

### DNS tradicional

El sistema DNS tradicional se basa en la resolución de nombres de dominio a través de servidores DNS públicos o proporcionados por los proveedores de servicios de Internet (ISP). Cuando una usuaria quiere acceder a un sitio web, su solicitud de DNS es enviada a un servidor DNS, que resuelve el nombre de dominio y devuelve la dirección IP correspondiente. Este sistema, aunque útil, puede dejar nuestra información de navegación expuesta a posibles rastreos y vulnerabilidades, especialmente si no se utiliza cifrado.

### DNS sobre HTTPS (DoH)

El **DNS sobre HTTPS** (DoH) es un protocolo que cifra las solicitudes DNS al transmitirlas a través de HTTPS, lo que impide que terceros intercepten o registren nuestras solicitudes de DNS. Al usar DoH, las solicitudes de DNS son tratadas de manera similar a las solicitudes de páginas web y, por lo tanto, son difíciles de espiar. Este sistema mejora la privacidad y la seguridad en la navegación al proteger los datos de DNS de ataques de intermediarios, como los ataques man-in-the-middle.

### DNS sobre TLS (DoT)

El **DNS sobre TLS** (DoT) es otro protocolo que cifra las solicitudes DNS, pero a diferencia de DoH, DoT utiliza el protocolo de seguridad TLS (Transport Layer Security) para cifrar las solicitudes de DNS. El principal objetivo de DoT es garantizar que las solicitudes DNS no puedan ser espiadas ni manipuladas al pasar por la red. Similar a DoH, DoT también mejora la privacidad y la seguridad, protegiendo nuestras solicitudes de DNS de ser interceptadas por terceros.

### DNS privados o personalizados

Algunas personas u organizaciones optan por usar **DNS privados o personalizados**, que son servidores DNS configurados de forma específica para mejorar la privacidad y la seguridad. Estos servidores no registran o comparten los datos de navegación de la usuaria con terceros, garantizando un mayor nivel de confidencialidad. Ejemplos de servicios de DNS privados son [Cloudflare](https://www.cloudflare.com/) o [NextDNS](https://nextdns.io/).

## Ventajas de DoH y DoT

Tanto el **DNS sobre HTTPS** (DoH) como el **DNS sobre TLS** (DoT) mejoran la seguridad y la privacidad de las solicitudes DNS mediante el cifrado. Sin embargo, existen diferencias en las ventajas que ofrecen cada uno de estos protocolos:

### Ventajas de DNS sobre HTTPS (DoH)

- **Mejora de la privacidad**: Al usar DoH, las solicitudes de DNS son tratadas como tráfico HTTPS, lo que dificulta su identificación y espionaje por los ISP u otras entidades que monitorizan la red.

- **Integración con navegadores**: DoH es fácilmente integrable en navegadores web populares, como Firefox, mejorando la privacidad sin necesidad de configuración adicional a nivel de sistema operativo.

- **Evadir censura**: Dado que las solicitudes DNS a través de DoH son transportadas como tráfico HTTPS estándar, que es el mismo protocolo usado para acceder a páginas web seguras. Esto hace que el tráfico DNS se oculte dentro del tráfico normal de navegación por internet, siendo más difícil para los gobiernos o los ISP bloquear o filtrar las solicitudes DNS, lo que permite la navegación en redes con censura estricta.

- **Protocolo estándar web**: Como DoH usa HTTPS, se beneficia de la infraestructura segura existente de Internet, lo que facilita su implementación y mejora la interoperabilidad.

### Ventajas de DNS sobre TLS (DoT)

- **Menos impacto en la latencia**: DoT usa un puerto específico (853) para la transmisión de las solicitudes DNS cifradas, lo que permite que las solicitudes de DNS se realicen de forma más eficiente sin afectar otras aplicaciones o tráfico web.

- **Separación de tráficos**: A diferencia de DoH, que envía solicitudes DNS como tráfico HTTPS, DoT mantiene un puerto separado, lo que facilita la identificación y gestión del tráfico DNS cifrado en redes corporativas o servicios que desean monitorizar o filtrar solicitudes DNS de forma específica.

- **Seguridad y fiabilidad**: DoT ofrece una mayor fiabilidad y control en las conexiones, dado que puede ser configurado para asegurar la conectividad en redes que implementan proxys o firewalls más restrictivos. Aunque también cifra las solicitudes DNS, su implementación puede ser más simple en algunos ámbitos corporativos o de servicio.

### Resumen de las diferencias principales

En resumen, la principal diferencia entre DoH y DoT reside en la forma en que las solicitudes DNS son transportadas y en el uso de puertos. **DoH es ideal** para mejorar la privacidad al ocultar las solicitudes de DNS dentro del tráfico HTTPS, mientras que **DoT** puede ser preferible para aquellos que necesitan una solución más específica para servidores o redes con mayor control sobre el tráfico DNS, y que solo permiten el protocolo DoT.

## ¿Cómo configurar el DNS seguro?

La forma de configurar el DNS seguro varía en función del dispositivo, sistema operativo, etc. Lo más fácil es que le eches un vistazo a la [guía que tiene la gente de NextDNS](https://my.nextdns.io/start). En ella explican cómo configurar el DNS en distintos tipos de dispositivos. Como indican arriba de todo, para que el DNS no caduque a los siete días es necesario registrarse en su web. El plan gratuito es suficiente, mientras que los planes de pago están pensados para empresas o entidades que tienen un uso más elevado del servicio. La ventaja de este servicio de NextDNS es que, además de comunicar tus consultas de forma anónima, también incluye una serie de opciones para filtrar publicidad, bloquear ciertas páginas web, programar las horas de uso y muchas otras más.

## Ojo, el DNS seguro no nos hace completamente anónimas

A pesar de que los métodos de cifrado DNS como DoH (DNS sobre HTTPS) y DoT (DNS sobre TLS) protegen la privacidad al ocultar el dominio que consultas, al cifrar las solicitudes DNS, los proveedores de servicios de Internet (ISP) todavía tienen acceso a la dirección IP a la que te conectas. Esto significa que, aunque el ISP no pueda ver directamente el nombre del dominio (ejemplo.com) que estás consultando, puede ver la IP a la que el dominio resuelve (193.4.52.2). Dado que cada dominio tiene asociada una dirección IP, el ISP puede, a través del análisis de las IPs a las que te conectas, saber los dominios que visitas. Además, los ISP también podrían optar por bloquear directamente ciertas direcciones IP, en lugar de bloquear los dominios. Esto permitiría bloquear el acceso a sitios o servicios sin tener que censurar los nombres de los dominios, lo que puede ser más difícil de detectar para las usuarias. Por lo tanto, incluso con métodos de cifrado DNS, los ISP u otras entidades con acceso a la red pueden tener cierto grado de visibilidad sobre el tráfico que circula por su infraestructura.

Es probable que ahora mismo te preguntes: Entonces, ¿qué ventaja tiene usar DNS seguros si, al fin y al cabo, el ISP puede saber igualmente las webs que visito?

Para empezar, hay que tener en cuenta que el empleo de DNS seguros no solo te protege de tu ISP. Si no usas un DNS cifrado, existe el riesgo de que las solicitudes DNS sean manipuladas durante la transmisión. Los ataques de hombre en el medio (MITM, Man In The Middle) permiten a un atacante interponerse en las comunicaciones y cambiar las respuestas DNS, redirigiendo el tráfico a sitios falsos. Usar un DNS cifrado impide que esto suceda, haciendo que la conexión sea mucho más segura.

Además, muchos sitios web comparten la misma dirección IP a través de técnicas como el hospedaje compartido o CDNs (Content Delivery Networks), como CloudFare. Esto hace que, si el ISP bloquea una dirección IP, no está bloqueando un único sitio web, sino que se puede bloquear toda una serie (cientos de miles incluso) de sitios o servicios que comparten esa IP. Esto hace más difícil para un ISP o entidad censora bloquear un dominio específico solo por IP, siendo mucho más fácil bloquear el nombre del dominio directamente (bloqueo contra el que sí te protege el empleo de DNS seguros).

Por lo tanto, usar DNS seguros (DoH o DoT) puede mejorar la privacidad de las consultas DNS, pero, si bien no impide que el ISP sepa la IP del destino, la existencia de CDNs o sitios que comparten IP hace que el bloqueo por IP sea menos efectivo y más indiscriminado, además de que dificulta que el ISP sepa exactamente qué dominio estás visitando.

Para evitar que el ISP sepa la IP que visitas, además de emplear un servicio de DNS seguro, deberías emplear un servicio de VPN o la red TOR, ya mencionados en el capítulo anterior.
