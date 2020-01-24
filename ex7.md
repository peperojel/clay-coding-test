# Ejercicio 7

## Pregunta 1

*Los arrendatarios que arriendan la casa ubicada en la Av. Vitacura 4380, Vitacura*.

Las tablas relevantes son:

- arrendatario(id, rut, nombre, apellido)
- arrienda(id_arrendatario, id_casa, deuda)
- casa(id, id_dueño, numero, calle, comuna)

**SQL**

```sql
SELECT arrendatario.nombre, arrendatario.apellido
FROM casa
INNER JOIN arrienda
	ON casa.id = arrienda.id_casa
        AND casa.calle = 'Av. Vitacura'
        AND casa.numero = 4380
	    AND casa.comuna = 'Vitacura'
INNER JOIN arrendatario
	ON arrienda.id_arrendatario = arrendatario.id;
```

**MongoDB**

```
-
```

## Pregunta 2

*Indique los dueños que poseen tres o más casas.*

Las tablas relevantes son:

- dueño(id, rut, nombre, apellido)
- casa(id, id_dueño, numero, calle, comuna)

**SQL**

```sql
SELECT dueño.nombre, dueño.apellido
FROM casa
INNER JOIN dueño
	ON casa.id_dueño = dueño.id
GROUP BY casa.id_dueño
HAVING COUNT(*) >= 3;
```

**MongoDB**

```
-
```

## Pregunta 3

*¿Cual es la deuda total para cada dueño?*

Las tablas relevantes son:

- arrienda(id_arrendatario, id_casa, deuda)
- casa(id, id_dueño, numero, calle, comuna)
- dueño(id, rut, nombre, apellido)

**SQL**

```sql
SELECT SUM(deuda) as deuda_total, dueño.nombre, dueño.apellido
FROM arrienda
INNER JOIN casa
	ON arrienda.id_casa = casa.id
INNER JOIN dueño
	ON casa.id_dueño = dueño.id
GROUP BY casa.id_dueño
```

**MongoDB**

```
-
```