# Django - MiniERP

## 1. Modelo de datos

Para organizar el proyecto, se han dividido las tablas en dos grupos:

**Tablas Maestras (App core):**
Son los catálogos con los datos fijos que necesitamos para trabajar: `Cliente`, `Producto` y `Estado`.

**Tablas Transaccionales (App ventas):**
Son los datos del movimiento diario de la empresa.`Pedido` para guardar los datos generales de la compra y `LineaPedido` para guardar los artículos concretos de esa compra.

**Relaciones y cardinalidades:**
* **Un Cliente tiene N Pedidos** (1:N). Un cliente puede comprar muchas veces.
* **Un Estado tiene N Pedidos** (1:N). Un mismo estado (ej. "Borrador") puede estar en muchos pedidos distintos.
* **Un Pedido tiene N Líneas** (1:N). Un pedido puede contener varios productos diferentes en sus líneas.
* **Un Producto está en N Líneas** (1:N). Un mismo producto puede venderse en muchos pedidos distintos.

**Políticas de borrado (on_delete):**
* `RESTRICT` en las relaciones de Cliente, Producto y Estado. Así el sistema no permitirá dejar huerfano a un producto que esté relacionado.
* `CASCADE` en la relación de las líneas con el Pedido. Si borramos un pedido entero, sus líneas se borran automáticamente.

---

**Restricciones de seguridad (Constraints):**
* En la tabla `LineaPedido` se ha añadido `CheckConstraint` para obligar a que la cantidad sea siempre mayor que 0 (`cantidad > 0`).

## 2. Diagrama Entidad-Relación

Estructura de las tablas y sus relaciones:

| Tabla | Campos principales | Claves |
| :--- | :--- | :--- |
| **Cliente** | id, nombre, nif, telefono, email | **PK:** id |
| **Producto** | id, nombre, sku, precio_base, iva | **PK:** id |
| **Estado** | id, codigo, descripcion | **PK:** id |
| **Pedido** | id, fecha_pedido, total | **PK:** id <br> **FK:** cliente_id, estado_id |
| **LineaPedido** | id, cantidad, precio_aplicado | **PK:** id <br> **FK:** pedido_id, producto_id |