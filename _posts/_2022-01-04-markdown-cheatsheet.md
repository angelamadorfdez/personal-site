---
layout: post
title:  Markdown Cheatsheet for styling
date:   2023-01-03 09:00:00 +0200
excerpt_separator: <!--end_excerpt-->
---

Esto es un texto normal escrito en markdown. Esto es un texto normal escrito en markdown. Esto es un texto normal escrito en markdown. Esto es un texto normal escrito en markdown. 

Esto es un texto normal escrito en markdown. Esto es un texto normal escrito en markdown. Esto es un texto normal escrito en markdown. Esto es un texto normal escrito en markdown. 

## Título 2
Esto es un texto normal escrito en markdown. Esto es un texto normal escrito en markdown. Esto es un texto normal escrito en markdown. Esto es un texto normal escrito en markdown. 

### Título 3
Esto es un texto normal escrito en markdown. Esto es un texto normal escrito en markdown. Esto es un texto normal escrito en markdown. Esto es un texto normal escrito en markdown. 

#### Título 4
Esto es un texto normal escrito en markdown. Esto es un texto normal escrito en markdown. Esto es un texto normal escrito en markdown. Esto es un texto normal escrito en markdown. 

---

### Encabezado de tercer nivel

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. [Ut enim ad minim veniam](), quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat **cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.**

> Esto es una cita. Esto es una cita. Esto es una cita. Esto es una cita. Esto es una cita. Esto es una cita. Esto es una cita. Esto es una cita. Esto es una cita. Esto es una cita. 

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. *"Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore"* eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

```rb
@product = Product.find(params[:id])
@product = Product.find_by(id: params[:id])
@product = Product.find_by!(id: params[:id])
@product = Product.where(id: params[:id], category: params[:category])
```

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. ~~Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore"* eu fugiat nulla pariatur~~. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

---

### Modificando la fuente

* *Texto en cursiva* (Cmd + i)
* **Texto en negrita** (Cmd + b)
* ***Texto en negrita y cursiva*** (Cmd + b -> Cmd + i)
* ~~Este texto está tachado~~ (Option + ñ)

---

### Citas

> Esto es una cita. Esto es una cita. Esto es una cita. Esto es una cita. Esto es una cita. Esto es una cita. Esto es una cita. Esto es una cita. Esto es una cita. Esto es una cita. 

---

### Listas desordenadas

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 

- elemento 1
	- elemento 1.1
	- elemento 1.2
- elemento 2
- elemento 3

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 

---

### Listas ordenadas

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 

1. Elemento 1
2. Elemento 2
  - Elemento 2.1
  - Elemento 2.2 
3. Elemento 3
4. Elemento 4

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 

---

### Código

```html
<p>Esto es un código</p>
```

```rb
@product = Product.find(params[:id])
@product = Product.find_by(id: params[:id])
@product = Product.find_by!(id: params[:id])
@product = Product.where(id: params[:id], category: params[:category])
```

---

### Tablas

| Nombre | Apellidos | Teléfono |
| --- | --- | --- |
| Ángel | Amador | 678547364 |
| José | Barranco | 876143524 |

---

### Enlaces externos

[Este enlace lleva a la web de Obsidian.md](https://obsidian.md/)
