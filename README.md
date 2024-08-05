Teoría de la Computación: Lab2
Integrantes:
- Diego Duarte
- Irving Morales
- José Marchena

Inciso 1:
Video de funcionamiento <a href="https://drive.google.com/file/d/186vdRnNQ4l7ruSLmQpK25a7dRPwAZwj0/view?usp=sharing">aquí</a>

Instrucciones:
1. Implementar en Python un programa que simula un aut´omata finito determinista (AFN). Para ello, debe implementar funciones
que hagan lo siguiente:
• transition(q, a, δ) la cual devuelve el valor de la transici´on δ(q, a), para un estado q ∈ K y un s´ımbolo a ∈ Σ.
• final state(q, w, δ) la cual devuelve el estado q obtenido por el aut´omata despu´es de terminar de leer la cadena w ∈ Σ
∗
.
• derivation(q, w, δ) la cual derivaci´on de la cadena w ∈ Σ
∗ desde el estado q ∈ K, esto es, la secuencia ordenada de
transiciones obtenidas.
• accepted(q, w, F, δ) la cual devuelve verdadero si la cadena w ∈ Σ
∗
es aceptada por el aut´omata partiendo desde el
estado s; y falso en caso contrario.
Su algoritmo debe recibir como inputs lo siguiente: un archivo estructurado (.json, .yml, .xml o similares), donde se indica
la estructura del aut´omata AFD:
• Q: una lista finita de todos los estados del aut´omata,
• Σ: una lista finita de todos los s´ımbolod admisibles,
• q0 el estado inicial,
• F: una lista que indica los estados de aceptaci´on,
• δ: la funci´on de transici´on, en un formato de tabla o lista de triplas (q, a, q′
) ∈ Q × Σ × Q, donde
q
′ = δ(q, a),
la cual devuelve el valor de la transici´on δ(q, a), para un estado q ∈ Q y un s´ımbolo a ∈ Σ.
Ilustrar el funcionamiento de estas funciones construyendo dos aut´omatas AFD de su elecci´on.
