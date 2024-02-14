def segment(items, segment_size):
    """
    Función para segmentar una lista de elementos en segmentos de tamaño específico.

    :param items: La lista de elementos a segmentar.
    :param segment_size: El tamaño de cada segmento.
    :return: Una lista de segmentos.
    """
    segments = [items[i:i + segment_size] for i in range(0, len(items), segment_size)]
    return segments

# Lista de ejemplo
data = [i for i in range(1, 21)]

# Tamaño del segmento
segment_size = 5

# Obtener los segmentos
segments = segment(data, segment_size)

# Imprimir los segmentos
for i, segment in enumerate(segments):
    print("Segmento", i + 1, ":", segment)
