# Contrasinais seguras e autenticación en dous pasos <span id="contrasinais-2fa"></span>

As contrasinais seguras e a autenticación en dous pasos son ferramentas fundamentais para protexer a nosa privacidade e evitar accesos non autorizados ás nosas contas en liña. Nun mundo onde as ameazas dixitais son cada vez máis frecuentes, adoptar boas prácticas no manexo de contrasinais e implantar métodos adicionais de verificación convértese nunha barreira esencial contra posibles ataques. Neste capítulo, exploraremos as claves para crear contrasinais robustas, xestionar múltiples credenciais de forma segura e empregar a autenticación en dous pasos como unha capa extra de seguridade que pode marcar a diferenza.

## Contrasinais seguras

Crear contrasinais seguras é o primeiro paso para protexer a nosa información persoal e evitar accesos non autorizados ás nosas contas. Unha contrasinal débil pode ser descifrada con facilidade a través de técnicas como o ataque por forza bruta ou a adiviñación, deixando expostos datos sensibles. E preguntaraste, e que contrasinal é segura? Non existen contrasinais 100% seguras, ao igual que non existen pechaduras 100% seguras. Iso si, hai uns principios básicos á hora de escoller unha contrasinal:

- **Non uses a mesma contrasinal para distintos servizos**: Se empregas a mesma contrasinal para varios servizos, no caso de que haxa unha filtración nalgún deles, o resto de contas que teñan esa mesma contrasinal quedarán empostas. Un dos métodos básicos para acceder á conta de alguén é probar contrasinais que foron filtradas nalgún momento. Polo tanto, é importante empregar unha contrasinal distinta para cada servizo.

- **Non uses contrasinais curtas nin que inclúan información persoal**: As contrasinais deben ser o máis longas e complexas posibles. Normalmente tendemos a empregar contrasinais sinxelas que nos sexa doado de lembrar. Erro. Debemos empregar xestores de contrasinais como Bitwarden ou Proton Pass (como explicamos no capítulo [Alternativas libres e encriptadas](servizos_libres.md#cap:alt_libres)) que nos permitan empregar contrasinais complexas e distintas, sen preocuparnos por ter que lembralas. E como de segura? Pois moitos servizo de internet dinche o número mínimo e máximo de caracteres que poder ter unha contrasinal. Intenta poñer unha contrasinal o máis longa e aleatoria posible.

Ferramentas útiles para detectar filtracións das nosas contrasinais:

- [Have I Been Pwned?](https://haveibeenpwned.com/): Ferramenta útil para ser avisado se o teu correo aparece nalgunha filtración de nomes de usuaria e contrasinais dalgún servizo en liña.

- [Monitor de Mozilla](https://monitor.mozilla.org/): Mesma utilidade ca a ferramenta anterior.

## Autenticación en dous pasos

A autenticación en dous pasos (2FA, polas súas siglas en inglés) é unha medida adicional de seguridade que require dous factores distintos para verificar a identidade dunha usuaria ao iniciar sesión nun servizo ou acceder a unha conta. Isto vai máis alá do tradicional uso dun só contrasinal, aumentando a protección contra accesos non autorizados. É dicir, que ademais de introducir a contrasinal, tamén se che vai unha segunda autenticación. Os métodos de autenticación máis habituais son:

- Autenticación por SMS: Unha vez introduces correctamente a túa contrasinal, chégache un código por SMS que debes introducir para iniciar sesión.

- Autenticación por correo electrónico: neste caso, o código chegarache por correo.

- Empregando un xerador de códigos: Esta é a opción máis recomendada e segura. Neste caso o código obtense dende unha aplicación móbil específica, como pode ser [FreeOTP](https://freeotp.github.io/). Este código cambia cada poucos segundos (normalmente cada 30 segundos) e é válido só durante ese período de tempo, o que dificulta que alguén sen autorización acceda á conta.

  - **Configuración inicial:**

    - A usuaria activa a autenticación en dous pasos no servizo ou aplicación desexada. Isto sóese atopar na sección de seguridade ou similar.

    - O servizo proporciona un código QR ou unha chave secreta que debe ser introducida ou escaneada co xerador.

    - O xerador usa esta información para comezar a xerar códigos únicos vinculados á conta.

  - **Proceso de inicio de sesión:**

    - A usuaria introduce o seu contrasinal como de costume.

    - O servizo solicita o código xerado polo aplicación xeradora.

    - A usuaria abre o xerador, copia o código actual e introdúceo no servizo.

    - O servidor verifica o código comparándoo co que debería estar vixente nese momento. Se coinciden, o acceso é concedido.

  - **Dispositivos de respaldo e recuperación:** Moitos servizos ofrecen códigos de recuperación ou permiten configurar varios métodos de 2FA para evitar quedar sen acceso no caso de perda do dispositivo.
