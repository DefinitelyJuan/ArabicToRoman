## Cuestionario
### 1. ¿Qué es un coding dojo?
Según la información provista en el url de referencia "https://lorenzosolano.com/what-is-coding-dojo/", un coding dojo puede ser definido como una reunión de programadores, en la cual estos trabajan de manera conjunta para resolver desafío de programación, en un espacio de colaboración y no competitivo, con el objetivo de mejorar sus habilidades y probar cosas nuevas.
### 2. Diferencia entre Requerimientos, Criterios de Aceptación y Escenarios de Prueba. Dar ejemplos a partir de un problema distinto a la referencia ( https://lorenzosolano.com/requirements-acceptance-criteria-and/).
Tras leer el material de referencia, puedo concluir que la diferencia entre los tres conceptos mencionados es la siguiente: Los ***requerimientos*** describen las características que se desea tenga el sistema, los ***criterios de aceptación*** indican cualidades que debe cumplir cada requerimiento para ser válido y los ***escenarios de prueba*** proponen situaciones para validar que cada criterio se cumple y por tanto, si se cumplen todos los criterios, se dice que el sistema cumple con el requerimiento.

Teniendo lo anterior en cuenta, puede deducirse que un ***requerimiento*** es validado a través de sus ***criterios de aceptación***, los cuales a su vez deben comprobados por medio de los ***escenarios de prueba***. "***Pruebas*** comprueban criterios, ***criterios*** validan ***requerimientos***"


Para ilustrar la diferencia entre estos conceptos, propongo el siguiente ejemplo:
Digamos que se desea construir un software de notas. Para dicho software, los requerimientos, criterios de aceptación, y escenarios de prueba podrían ser definidos de la siguiente manera:

**Requerimientos**

Definimos las siguientes funcionalidades básicas para el sistema propuesto:
- Requerimiento 1: Crear nota
- Requerimiento 2: Editar nota
- Requerimiento 3: Borrar nota

**Criterios de aceptación**

Sobre el requerimiento, definimos criterios de aceptación sobre el requerimiento 1:
- Criterio de aceptación 1-1: La nota deberá contener al menos un carácter.
- Criterio de aceptación 1-2: La nota deberá aceptar cualquier tipo de carácter.
- Criterio de aceptación 1-3: La nota deberá contener un máximo de 20000 caracteres.

**Escenarios de prueba**

Sobre el criterio de aceptación, definimos escenarios de prueba:
- Escenario 1-1-1: Presionar guardar sin incluir nada en la nota.
- Escenario 1-2-1: Escribir la cadena "test1@$!" en la nota.
- Escenario 1-2-2: Escribir la cadena "Test '2' !" en la nota.
### 3. De dos ejemplos de requerimientos no-funcionales, y especifique cuál es su categoría (seguridad, performance, portabilidad, etc.)++
1. Downtime de máximo 4 horas (Disponibilidad).
2. La página cargará en 3 segundos o menos (Performance).
### 4. ¿Qué es TDD?
Es una metodología de desarrollo de software que se basa en desarrollar en base a las pruebas (generalmente unitarias), como bien indica su nombre "Test Driven Development". Más concretamente, propone desarrollar casos de prueba iniciales antes de empezar a codear, proceso durante el cual solo se modificará el código si alguna de las pruebas falla. El siguiente diagrama de flujo ilustra el proceso a seguir cuando se desarrolla utilizando esta metodología:
![ProcesoTDD](https://3fxtqy18kygf3on3bu39kh93-wpengine.netdna-ssl.com/wp-content/uploads/2021/01/Screenshot-2020-12-31-at-4.02.29-PM.png)

Imagen tomada desde la web https://www.browserstack.com/guide/what-is-test-driven-development
### 5. ¿Qué son pruebas unitarias automatizadas?
Este concepto va de la mano con TDD, pues esta metodología hace uso principalmente de las pruebas unitarias. Una prueba unitaria automatizada es un tipo de prueba donde se testea una sección pequeña de código (unit), con el objetivo de verificar su correcto funcionamiento en todos los casos posibles y haciendo uso de un test script. De esta manera, quien prueba el software es la máquina, automatizando el proceso de prueba, logrando una mayor eficiencia en este propósito en comparación a si se hiciera manualmente.
### 6. ¿Cuál fue el 1er framework de pruebas unitarias y para cual lenguaje fue creado?
Kent Beck (Creador de eXtreme Programming) creó SUnit, el primer framework de pruebas unitarias, desarrollado para el lenguaje SmallTalk. Un dato interesante es que aunque ya existían las pruebas automatizadas anteriormente, no eran capaces de ser ejecutadas de manera totalmente independiente (eran dependientes unas de otras), cosa que si logró Beck con SUnit, que permite ejecutar cada prueba de manera aislada, es decir, separada de las otras pruebas.
### 7. ¿Describa los componentes de la arquitectura xUnit?
Una arquitectura xUnit posee los siguientes componentes:
- Test runner: Ejecutable que corre las pruebas e informa los resultados obtenidos.
- Test case: Hace referencia al caso de prueba, sobre el cual se crea una clase elemental de la cual todas las pruebas unitarias son herederas.
- Test fixtures: Indica el estado o condiciones previas necesarias para que pueda ser ejecutada una prueba.
- Test suites: Conjunto de pruebas que comparten un mismo test fixture.
- Test execution: Ejecución de la prueba, donde primero se prepara el entorno de prueba, es decir, se adecua el entorno al text fixture definido, para luego ejecutar la prueba, y tras obtener los resultados, reiniciar el entorno dejándolo como estaba antes de la prueba.
- Test result formatter: Toma los resultados obtenidos de la prueba tras la ejecución de un test runner, y genera una salida en formato XML.
- Assertions: Función o macro que representa una condición lógica que es verdadera para los resultados esperados en una ejecución correcta del sistema, y verifica el comportamiento de la unidad de código que se prueba.
### 8. Indique al menos tres desventajas de las pruebas unitarias automatizadas
- Implica tiempo de desarrollo adicional para diseñar y codificar las pruebas
- Son difíciles de implementar para pruebas de la interfaz de usuario.
- Es necesario realizarle mantenimiento a las pruebas, algo que lógicamente toma su tiempo
- Las pruebas unitarias no pueden detectar todos los errores (como por ejemplo, errores de integración). Por ello, resulta necesario combinar pruebas de otros tipos para eliminar la mayor cantidad posible de bugs.
### 9. Indique al menos tres ventajas de las pruebas unitarias automatizadas
- El unit testing permite encontrar bugs más tempranamente.
- El unit testing fomenta una codificación de calidad, con buena estructura y mejor diseño en general.
- El unit testing ayuda a que el proceso de refactoring sea más sencillo y/o llevadero, pues te permiten reconocer fácilmente si algún cambio en el código ha generado errores.
- El unit testing es un gran contribuidor al aseguramiento de la calidad, pues permite probar el código constantemente.
- El unit testing puede reducir costos del desarrollo, gracias a la anteriormente mencionada ventaja de la detección temprana de bugs.
### 10. Cree un documento donde se listen los Requerimientos, Criterios de Aceptación y Casos de Prueba para la aplicación de conversión arábigo-romano
[Requerimientos, Criterios de Aceptación y Casos de Prueba](https://github.com/DefinitelyJuan/ArabicToRoman/blob/main/Docs/RCT.md)
### 11. Utilizando el lenguaje de su preferencia cree cinco o más casos de prueba unitarios automatizados utilizando un framework de automatización de pruebas para el algoritmo en cuestión
[Carpeta con las pruebas unitarias](https://github.com/DefinitelyJuan/ArabicToRoman/blob/main/Tests)

## Referencias
https://lorenzosolano.com/what-is-coding-dojo/

https://lorenzosolano.com/requirements-acceptance-criteria-and/

https://reqtest.com/requirements-blog/functional-vs-non-functional-requirements/
https://www.browserstack.com/guide/what-is-test-driven-development

https://www.agilealliance.org/glossary/tdd/
https://tanzu.vmware.com/content/blog/what-is-a-unit-test-the-answer-might-surprise-you#:~:text=Before%20SUnit%20(SmallTalk%20Unit%2C%20the,manual%20parts%20of%20their%20work.
https://en.wikipedia.org/wiki/XUnit

https://theqalead.com/topics/unit-testing/

https://methodpoet.com/unit-testing-advantages-and-disadvantages/#:~:text=Advantages%20of%20unit%20testing%20are,won't%20catch%20all%20bugs.


