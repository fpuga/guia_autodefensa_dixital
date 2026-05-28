# Contraseñas seguras y autenticación en dos pasos <span id="contrasinais-2fa"></span>

Las contraseñas seguras y la autenticación en dos pasos son herramientas fundamentales para proteger nuestra privacidad y evitar accesos no autorizados a nuestras cuentas en línea. En un mundo donde las amenazas digitales son cada vez más frecuentes, adoptar buenas prácticas en el manejo de contraseñas e implantar métodos adicionales de verificación se convierte en una barrera esencial contra posibles ataques. En este capítulo, exploraremos las claves para crear contraseñas robustas, gestionar múltiples credenciales de forma segura y emplear la autenticación en dos pasos como una capa extra de seguridad que puede marcar la diferencia.

## Contraseñas seguras

Crear contraseñas seguras es el primer paso para proteger nuestra información personal y evitar accesos no autorizados a nuestras cuentas. Una contraseña débil puede ser descifrada con facilidad a través de técnicas como el ataque por fuerza bruta o la adivinación, dejando expuestos datos sensibles. Y te preguntarás, ¿y qué contraseña es segura? No existen contraseñas 100% seguras, al igual que no existen cerraduras 100% seguras. Eso sí, hay unos principios básicos a la hora de elegir una contraseña:

- **No uses la misma contraseña para distintos servicios**: Si empleas la misma contraseña para varios servicios, en caso de que haya una filtración en alguno de ellos, el resto de cuentas que tengan esa misma contraseña quedarán comprometidas. Uno de los métodos básicos para acceder a la cuenta de alguien es probar contraseñas que fueron filtradas en algún momento. Por lo tanto, es importante emplear una contraseña distinta para cada servicio.

- **No uses contraseñas cortas ni que incluyan información personal**: Las contraseñas deben ser lo más largas y complejas posibles. Normalmente tendemos a emplear contraseñas sencillas que nos sea fácil de recordar. Error. Debemos emplear gestores de contraseñas como Bitwarden o Proton Pass (como explicamos en el capítulo [Alternativas libres y encriptadas](servizos_libres.md#cap:alt_libres)) que nos permitan emplear contraseñas complejas y distintas, sin preocuparnos por tener que recordarlas. ¿Y cómo de segura? Pues muchos servicios de internet te dicen el número mínimo y máximo de caracteres que puede tener una contraseña. Intenta poner una contraseña lo más larga y aleatoria posible.

Herramientas útiles para detectar filtraciones de nuestras contraseñas:

- [Have I Been Pwned?](https://haveibeenpwned.com/): Herramienta útil para ser avisado si tu correo aparece en alguna filtración de nombres de usuaria y contraseñas de algún servicio en línea.

- [Monitor de Mozilla](https://monitor.mozilla.org/): Misma utilidad que la herramienta anterior.

## Autenticación en dos pasos

La autenticación en dos pasos (2FA, por sus siglas en inglés) es una medida adicional de seguridad que requiere dos factores distintos para verificar la identidad de una usuaria al iniciar sesión en un servicio o acceder a una cuenta. Esto va más allá del tradicional uso de una sola contraseña, aumentando la protección contra accesos no autorizados. Es decir, que además de introducir la contraseña, también se te solicita una segunda autenticación. Los métodos de autenticación más habituales son:

- Autenticación por SMS: Una vez introduces correctamente tu contraseña, te llega un código por SMS que debes introducir para iniciar sesión.

- Autenticación por correo electrónico: en este caso, el código te llegará por correo.

- Empleando un generador de códigos: Esta es la opción más recomendada y segura. En este caso el código se obtiene desde una aplicación móvil específica, como puede ser [FreeOTP](https://freeotp.github.io/). Este código cambia cada pocos segundos (normalmente cada 30 segundos) y es válido solo durante ese período de tiempo, lo que dificulta que alguien sin autorización acceda a la cuenta.

  - **Configuración inicial:**

    - La usuaria activa la autenticación en dos pasos en el servicio o aplicación deseada. Esto se suele encontrar en la sección de seguridad o similar.

    - El servicio proporciona un código QR o una clave secreta que debe ser introducida o escaneada con el generador.

    - El generador usa esta información para empezar a generar códigos únicos vinculados a la cuenta.

  - **Proceso de inicio de sesión:**

    - La usuaria introduce su contraseña como de costumbre.

    - El servicio solicita el código generado por la aplicación generadora.

    - La usuaria abre el generador, copia el código actual y lo introduce en el servicio.

    - El servidor verifica el código comparándolo con el que debería estar vigente en ese momento. Si coinciden, el acceso es concedido.

  - **Dispositivos de respaldo y recuperación:** Muchos servicios ofrecen códigos de recuperación o permiten configurar varios métodos de 2FA para evitar quedarse sin acceso en caso de pérdida del dispositivo.
