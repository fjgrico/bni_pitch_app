def generate_pitch(user_data, list_number, units_completed, one_to_one, business_closed_name,
                   business_closed_amount, references_given, reference_type, service_highlight,
                   competitive_advantage, story_example, ideal_client, duration, tone):
    pitch = f"""
Buenos días, soy {user_data['name']} de {user_data['company']} ({user_data['membership']}). Esta semana soy el número {list_number} en la lista.
He realizado {one_to_one} reuniones 1 a 1 y completado {units_completed} unidades de formación.
Gracias a {business_closed_name} por un negocio cerrado de {business_closed_amount} €.
He pasado {references_given} referencias ({reference_type}).

Esta semana quiero destacar nuestro servicio: {service_highlight}.
Nuestra ventaja competitiva es: {competitive_advantage}.
Te cuento el caso: {story_example}.
Buscamos: {ideal_client}.

({tone} - {duration} segundos)
    """
    return pitch.strip()