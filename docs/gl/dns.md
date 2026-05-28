# DNS seguro. Que é e alternativas seguras<span id="cap:dns"></span>

## Que é un DNS?

O DNS (**Sistema de Nomes de Dominio**) é un servizo fundamental de Internet que funciona como unha especie de axenda telefónica de sitios web. Permite traducir os nomes de dominio (como **www.example.com**) en direccións IP numéricas (como **192.168.1.1**) que os ordenadores utilizan para comunicarse entre si. Sen o DNS, teriamos que lembrar a dirección IP exacta de cada sitio web que queremos visitar, o que sería moi complicado. En resumo, o DNS facilita a navegación en Internet ao facer que os nomes de dominio sexan máis fáciles de usar, ao tempo que permite a comunicación entre os dispositivos de rede.

## Impacto do DNS na nosa privacidade

O servizo DNS, aínda que fundamental para a navegación en Internet, tamén pode afectar á nosa privacidade. Cada vez que accedemos a unha páxina web, o noso dispositivo envía unha solicitude ao servidor DNS para obter a dirección IP asociada ao nome de dominio. Durante este proceso, o servidor DNS pode rexistrar información sobre os sitios web que visitamos, xunto coa nosa dirección IP, o que permite o seguimento e a creación de perfís de navegación.

Se usamos servidores DNS públicos ou os proporcionados polos provedores de servizos de Internet (ISP), estes servidores poden recopilar e almacenar os nosos datos de navegación, incluso compartilos con terceiros, como anunciantes ou autoridades gobernamentais. Isto pode resultar nun risco para a nosa privacidade, especialmente se non se implantan medidas adecuadas para protexer a información que circula nas nosas conexións.

Por outra banda, ao utilizar servizos de DNS seguros e privados, como DNS sobre HTTPS (DoH) ou DNS sobre TLS (DoT), podemos minimizar a posibilidade de que os nosos datos sexan espiados ou manipulados, garantindo así unha maior confidencialidade na nosa navegación en Internet. Ao encriptar as solicitudes DNS, impídese que terceiros intercepten ou rexistren as páxinas que visitamos, mellorando a nosa privacidade en liña.

## Sistemas de DNS

Existen varios tipos de sistemas de DNS que difiren na forma en que xestionan e protexen as solicitudes de nome de dominio. A continuación, explicamos os principais:

### DNS tradicional

O sistema DNS tradicional baséase na resolución de nomes de dominio a través de servidores DNS públicos ou proporcionados polos provedores de servizos de Internet (ISP). Cando unha usuaria quere acceder a un sitio web, a súa solicitude de DNS é enviada a un servidor DNS, que resolve o nome de dominio e devolve a dirección IP correspondente. Este sistema, aínda que útil, pode deixar a nosa información de navegación exposta a posibles rastrexos e vulnerabilidades, especialmente se non se utiliza encriptado.

### DNS sobre HTTPS (DoH)

O **DNS sobre HTTPS** (DoH) é un protocolo que encripta as solicitudes DNS ao transmitilas a través de HTTPS, o que impide que terceiros intercepten ou rexistren as nosas solicitudes de DNS. Ao usar DoH, as solicitudes de DNS son tratadas de maneira similar ás solicitudes de páxinas web e, polo tanto, son difíciles de espiar. Este sistema mellora a privacidade e a seguridade na navegación ao protexer os datos de DNS de ataques de intermediarios, como os ataques man-in-the-middle.

### DNS sobre TLS (DoT)

O **DNS sobre TLS** (DoT) é outro protocolo que encripta as solicitudes DNS, pero a diferenza de DoH, DoT utiliza o protocolo de seguridade TLS (Transport Layer Security) para cifrar as solicitudes de DNS. O principal obxectivo de DoT é garantir que as solicitudes DNS non poidan ser espiadas nin manipuladas ao pasar pola rede. Semellante a DoH, DoT tamén mellora a privacidade e a seguridade, protexendo as nosas solicitudes de DNS de ser interceptadas por terceiros.

### DNS privados ou personalizados

Algunhas persoas ou organizacións optan por usar **DNS privados ou personalizados**, que son servidores DNS configurados de forma específica para mellorar a privacidade e a seguridade. Estes servidores non rexistran ou comparten os datos de navegación da usuaria con terceiros, garantindo un maior nivel de confidencialidade. Exemplos de servizos de DNS privados son [Cloudflare](https://www.cloudflare.com/) ou [NextDNS](https://nextdns.io/).

## Vantaxes de DoH e DoT

Tanto o **DNS sobre HTTPS** (DoH) como o **DNS sobre TLS** (DoT) melloran a seguridade e a privacidade das solicitudes DNS mediante a encriptado. Sen embargo, existen diferenzas nas vantaxes que ofrecen cada un destes protocolos:

### Vantaxes de DNS sobre HTTPS (DoH)

- **Mellora da privacidade**: Ao usar DoH, as solicitudes de DNS son tratadas como tráfico HTTPS, o que dificulta a súa identificación e espiado polos ISP ou outras entidades que monitorizan a rede.

- **Integración con navegadores**: DoH é facilmente integrable en navegadores web populares, como Firefox, mellorando a privacidade sen necesidade de configuración adicional a nivel de sistema operativo.

- **Evadir censura**: Dado que as solicitudes DNS a través de DoH son transportadas como tráfico HTTPS estándar, que é o mesmo protocolo usado para acceder a páxinas web seguras. Isto fai que o tráfico DNS se oculte dentro do tráfico normal de navegación por internet, sendo máis difícil para os gobernos ou os ISP bloquear ou filtrar as solicitudes DNS, o que permite a navegación en redes con censura estrita.

- **Protocolo estándar web**: Como DoH usa HTTPS, beneficiase da infraestrutura segura existente de Internet, o que facilita a súa implantación e mellora a interoperabilidade.

### Vantaxes de DNS sobre TLS (DoT)

- **Menos impacto na latencia**: DoT usa un porto específico (853) para a transmisión das solicitudes DNS cifradas, o que permite que as solicitudes de DNS se realicen de forma máis eficiente sen afectar outras aplicacións ou tráfico web.

- **Separación de tráficos**: A diferenza de DoH, que envía solicitudes DNS como tráfico HTTPS, DoT mantén un porto separado, o que facilita a identificación e xestión do tráfico DNS cifrado en redes corporativas ou servizos que desexan monitorizar ou filtrar solicitudes DNS de forma específica.

- **Seguridade e fiabilidade**: DoT ofrece unha maior fiabilidade e control nas conexións, dado que pode ser configurado para asegurar a conectividade en redes que implantan proxys ou firewalls máis restritivos. Aínda que tamén cifra as solicitudes DNS, a súa implantación pode ser máis simple nalgúns ámbitos corporativos ou de servizo.

### Resumo das diferencias principais

En resumo, a principal diferenza entre DoH e DoT reside na forma en que as solicitudes DNS son transportadas e no uso de portos. **DoH é ideal** para mellorar a privacidade ao ocultar as solicitudes de DNS dentro do tráfico HTTPS, mentres que **DoT** pode ser preferible para aqueles que necesitan unha solución máis específica para servidores ou redes con maior control sobre o tráfico DNS, e que so permiten o protocolo DoT protocolos.

## Como configurar o DNS seguro?

A forma de configurar o DNS seguro varía en función do dispositivo, sistema operativo, etc. O máis doado é que lle botes un ollo á [guía que ten a xente de NextDNS](https://my.nextdns.io/start). Nela explican como configurar o DNS en distintos tipos de dispositivos. Como indican arriba de todo, para que o DNS non caduque aos sete días é preciso rexistrarse na súa web. O plan de balde é suficiente, mentres o que os plans de pago están pensados para empresas ou entidades que teñen un uso máis elevado do servizo. A vantaxe deste servizo de NextDNS é que, ademais de comunicar as túas consultas de forma anónima, tamén inclúe unha serie de opcións para filtrar publicidade, bloquear certas páxinas web, programar as horas de uso e moitas outras máis.

## Ollo, o DNS seguro non nos fai completamente anónimas

A pesar de que os métodos de cifrado DNS como DoH (DNS sobre HTTPS) e DoT (DNS sobre TLS) protexen a privacidade ao ocultar o dominio que consultas, ao cifrar as solicitudes DNS, os provedores de servizos de Internet (ISP) aínda teñen acceso á dirección IP á que te conectas. Isto significa que, aínda que o ISP non poida ver directamente o nome do dominio (exemplo.com) que estás consultando, pode ver á IP ao que o dominio resolve (193.4.52.2). Dado que cada dominio ten asociada unha dirección IP, o ISP pode, a través da análise das IPs ás que te conectas, saber os dominios que visitas. Ademais, os ISP tamén poderían optar por bloquear directamente certas direccións IP, en lugar de bloquear os dominios. Isto permitiría bloquear o acceso a sitios ou servizos sen ter que censurar os nomes dos dominios, o que pode ser máis difícil de detectar para os usuarias. Por tanto, mesmo con métodos de cifrado DNS, os ISP ou outras entidades con acceso á rede poden ter certo grao de visibilidade sobre o tráfico que circula pola súa infraestrutura.

É probable que agora mesmo te preguntes: Entón que vantaxe ten usar DNS seguros se total o ISP pode saber igualmente as webs que visito?

Para comezar, hai que ter en conta que o emprego de DNS seguros non so te protexe do teu ISP. Se non usas un DNS cifrado, existe o risco de que as solicitudes DNS sexan manipuladas durante a transmisión. Os ataques de man no medio (MITM, Man In The Middle) permiten a un atacante interpoñerse nas comunicacións e cambiar as respostas DNS, redirixindo o tráfico a sitios falsos. Usar un DNS cifrado impide que isto suceda, facendo que a conexión sexa moito máis segura.

Ademais, moitos sitios web comparten a mesma dirección IP a través de técnicas como o hospedaxe compartida ou CDNs (Content Delivery Networks), como CloudFare. Isto fai que, se o ISP bloquea unha dirección IP, non está bloqueando un único sitio web, senón que se pode bloquear toda unha serie (centos de miles incluso) de sitios ou servizos que comparten esa IP. Isto fai máis difícil para un ISP ou entidade censora bloquear un dominio específico só por IP, sendo moito máis doado bloquear o nome do dominio directamente (bloqueo contra o que si te protexe o emprego de DNS seguros).

Polo tanto, usar DNS seguros (DoH ou DoT) pode mellorar a privacidade das consultas DNS, pero, se ben non impide que o ISP saiba a IP do destino, a existencia de CDNs ou sitios que comparten IP fai que o bloqueo por IP sexa menos efectivo e máis indiscriminado, ademais de que dificulta que o ISP saiba exactamente que dominio estás a visitar.

Para evitar que o ISP saiba a IP que visitas, ademais de empregar un servizo de DNS seguro, deberías empregar un servizo de VPN ou a rede TOR, xa mencionados no capítulo anterior.
