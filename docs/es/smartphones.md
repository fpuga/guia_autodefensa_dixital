# Smartphones: los mayores recaudadores de información. Consejos para aumentar nuestra seguridad.

Los teléfonos móviles se han convertido en un elemento esencial en nuestra vida diaria, pero también representan un riesgo para nuestra privacidad. Además de todos los consejos mencionados en los capítulos anteriores, en este se dan una serie de consejos específicos para proteger tu privacidad en los dispositivos móviles.

## Consejos generales

- **Actualizaciones del sistema y de las aplicaciones**: Mantener el sistema operativo y las aplicaciones siempre actualizados es una de las mejores defensas contra vulnerabilidades. Las actualizaciones suelen incluir parches de seguridad que corrigen fallos descubiertos recientemente, por lo que es esencial instalar las actualizaciones cuanto antes.

- **Uso de un pin o patrón para proteger tu dispositivo**: es recomendable que para usar tu dispositivo tengas que introducir algún pin, contraseña o patrón de desbloqueo. Esto evita que alguien que tenga acceso a tu dispositivo no pueda acceder a tus aplicaciones y datos. **Ojo con la biometría**. Es cierto que usar nuestra huella o nuestro rostro para desbloquear nuestro dispositivo es muy práctico, sin tener que andar metiendo el pin, patrón o contraseña. Sin embargo, alguien podría acceder a tu dispositivo (e incluso a tu cuenta del banco) si por ejemplo te quedas inconsciente. En el caso del desbloqueo facial, incluso hay casos en los que se logró desbloquear el dispositivo usando una fotografía.

- **Bloqueo específico de aplicaciones:<span id="sec:biometria"></span>** Si quieres usar igualmente el desbloqueo por biometría, es recomendable que para aplicaciones críticas como puede ser la del banco o tu gestor de contraseñas actives de forma específica el bloqueo por patrón o pin.

- **Permisos de las aplicaciones**: Revisa y controla los permisos que concedemos a las aplicaciones. Muchas aplicaciones piden acceso innecesario a datos o funciones del dispositivo, como la cámara, el micrófono o la localización. Solo concede los permisos estrictamente necesarios para el funcionamiento de la aplicación.

- **Descarga de aplicaciones de fuentes oficiales**: Evita instalar aplicaciones de fuentes no verificadas, e instálalas solo a través de tiendas oficiales como F-Droid, Google Play o la App Store. Las aplicaciones descargadas de fuentes externas pueden contener malware u otros programas maliciosos.

- **Configurar un DNS privado**: Como comentamos en el capítulo [DNS seguro. Qué es y alternativas seguras](dns.md#cap:dns) sobre DNS seguros, recomendamos configurar un DNS seguro en tu móvil.

- **Emplear aplicaciones libres en la medida de lo posible**: Échale un ojo al capítulo [Alternativas libres y encriptadas](servizos_libres.md#cap:alt_libres) en el que te hablamos sobre alternativas libres a las que usar en tu día a día.

- **Emplear sistemas operativos libres**: En el capítulo [Los Sistemas Operativos. Alternativas libres y seguras.](sistemas_operativos.md#cap:SO) te hablamos de qué es un sistema operativo, y en la sección [Alternativas libres para móviles y cómo instalarlas](sistemas_operativos.md#sec:alt_so_mobiles) te damos una serie de sistemas operativos libres alternativos al Android de Google y a iOS.

## Riesgos de la previsualización de las notificaciones

Muchos dispositivos móviles permiten que las notificaciones de las aplicaciones se muestren en la pantalla de bloqueo o como pancartas emergentes, incluso sin desbloquear el dispositivo. Aunque esta funcionalidad puede ser útil para ver rápidamente mensajes o alertas importantes, también presenta riesgos de seguridad y privacidad.

### Exposición de información personal

Si las notificaciones muestran contenido sensible, otras personas podrían acceder a esa información sin necesidad de desbloquear el dispositivo. Esto puede incluir:

- **Códigos de verificación enviados por SMS o aplicaciones de autenticación**, facilitando ataques de suplantación de identidad.

- **Mensajes privados en aplicaciones de mensajería**

- **Correos electrónicos con información confidencial**, como datos bancarios o detalles laborales.

- **Notificaciones de aplicaciones financieras** que podrían revelar saldos o movimientos bancarios.

### Facilidad para ataques de Shoulder Surfing

El llamado **Shoulder Surfing** consiste en que alguien observe la pantalla del dispositivo sin permiso, aprovechando situaciones cotidianas, como el uso del móvil en transporte público o en lugares concurridos. Si la previsualización de las notificaciones está activada, una persona puede:

- Leer mensajes privados sin que la usuaria se percate.

- Ver códigos de autenticación de un solo uso (OTP) en tiempo real.

- Obtener información sobre contactos, eventos u otras actividades de la usuaria.

### Filtración de información en ambientes laborales

En un entorno profesional, la previsualización de notificaciones puede comprometer información sensible:

- Mensajes con datos de clientes o proyectos que no deberían ser vistos por terceras personas.

- Correos electrónicos internos con información estratégica de la empresa.

- Notificaciones de reuniones o eventos confidenciales que pueden ser aprovechados por terceros.

### Medidas de protección

Para minimizar los riesgos asociados a la previsualización de las notificaciones, se recomienda:

- **Desactivar la previsualización en la pantalla de bloqueo**: En los ajustes del sistema, se puede configurar para que solo se vea el remitente o que no se muestre ninguna información hasta que el dispositivo esté desbloqueado.

- **Usar la autenticación biométrica o PIN para ver notificaciones**: En muchos sistemas, es posible configurar que las notificaciones solo se muestren tras la autenticación de la usuaria.

- **Restringir notificaciones sensibles**: Muchas aplicaciones permiten configurar cómo se muestran sus notificaciones, evitando que contenido crítico aparezca en lugares accesibles.

- **Tener cuidado en lugares públicos**: Evitar exponer la pantalla del móvil en lugares donde otras personas puedan ver la información que aparece.

## Riesgos de los smartwatches y el acceso a las notificaciones

Los relojes inteligentes (smartwatches) se han convertido en dispositivos populares que permiten recibir notificaciones, monitorizar actividad física e interactuar con el teléfono sin necesidad de sacarlo del bolsillo. Sin embargo, su comodidad viene acompañada de ciertos riesgos para la privacidad y la seguridad, especialmente cuando tienen acceso total a las notificaciones y a su contenido.

### Acceso total a mensajes y datos sensibles

Muchos smartwatches requieren permiso para acceder a todas las notificaciones del teléfono para poder mostrarlas en su pantalla. Esto significa que pueden recibir y almacenar:

- Mensajes privados de aplicaciones

- Correos electrónicos completos

- Códigos de verificación de doble factor (2FA), facilitando ataques de suplantación de identidad.

- Notificaciones de bancos u otras entidades financieras con información sensible.

La mayoría de los smartwatch contienen software privativo, por lo que no podemos saber qué tratamiento le da el fabricante a esos datos. Por ejemplo, podría compartirlos con terceros para distintos tipos de usos. Además, si el smartwatch no tiene mecanismos de seguridad adecuados, cualquier persona puede acceder a esos datos simplemente observando su pantalla o manipulándolo sin restricciones.

### Interceptación de datos mediante Bluetooth

Los smartwatches suelen conectarse al teléfono a través de Bluetooth, una tecnología que puede ser vulnerable a ataques como:

- **Ataques de sniffing**: Un atacante puede interceptar la comunicación entre el smartwatch y el teléfono si la conexión no está cifrada correctamente.

- **Ataques Man-in-the-Middle (MitM)**: Si la conexión Bluetooth es comprometida, un atacante puede modificar o escuchar las notificaciones sin que la usuaria lo sepa.

- **Emparejamientos no autorizados**: Algunas vulnerabilidades permiten que dispositivos desconocidos se conecten a un smartwatch sin autorización de la usuaria.

### Medidas de protección

Para minimizar los riesgos asociados al uso de smartwatches con acceso a notificaciones, se recomienda:

- **Configurar la privacidad de las notificaciones**: Desactivar la previsualización de mensajes completos en el smartwatch y permitir solo las más necesarias.

- **Activar mecanismos de bloqueo**: Si el smartwatch permite establecer un PIN o algún tipo de bloqueo, activarlo para evitar accesos no autorizados.

- **Revisar los permisos de las aplicaciones**: Asegurarse de que solo las aplicaciones esenciales tienen acceso a las notificaciones.

- **Proteger la conexión Bluetooth**: Mantener Bluetooth desactivado cuando no se use y evitar emparejamientos en lugares públicos.

### Conclusión

La integración de los smartwatches con las notificaciones del teléfono es muy útil, pero también introduce riesgos de seguridad y privacidad. La configuración adecuada de los permisos y el uso de medidas de protección puede ayudar a reducir estos riesgos y garantizar un uso más seguro de estos dispositivos.
