def generate_pitch(nombre, empresa, membresia, numero_lista, formacion, reuniones,
                   nombre_negocio, importe_negocio, referencias, tipo_ref,
                   servicio, ventaja, historia, cliente_ideal, duracion, tono):
    pitch = f"""Buenos días, soy {nombre}, de {empresa}, especializado en {membresia}. Esta semana soy el número {numero_lista} en la lista.\n\n"
    pitch += f"He realizado {int(reuniones)} reuniones 1 a 1 y {int(formacion)} unidad(es) de formación.\n"
    if nombre_negocio and importe_negocio:
        pitch += f"Gracias a {nombre_negocio} por un negocio cerrado de {importe_negocio} €.\n"
    if referencias:
        pitch += f"He pasado {int(referencias)} referencias {tipo_ref.lower()}.\n\n"
    pitch += f"Esta semana quiero destacar nuestro servicio de {servicio}. Nuestra ventaja es: {ventaja}.\n\n"
    pitch += f"Te cuento: {historia}\n\n"
    pitch += f"Estoy buscando: {cliente_ideal}\n\n"
    pitch += f"(Presentación estimada: {duracion} / Tono: {tono})"
    return pitch