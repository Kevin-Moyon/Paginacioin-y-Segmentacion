def paginate(items, page_number, page_size):
    """
    Función para paginar una lista de elementos.

    :param items: La lista de elementos a paginar.
    :param page_number: El número de página que se desea obtener.
    :param page_size: El tamaño de cada página.
    :return: Una tupla que contiene la página solicitada y el número total de páginas.
    """
    total_pages = (len(items) + page_size - 1) // page_size
    start_index = (page_number - 1) * page_size
    end_index = start_index + page_size
    return items[start_index:end_index], total_pages

# Lista de ejemplo
data = [i for i in range(1, 101)]

# Número de página y tamaño de página
page_number = 2
page_size = 10

# Obtener la página solicitada y el número total de páginas
page, total_pages = paginate(data, page_number, page_size)

# Imprimir la página y el número total de páginas
print("Página", page_number, ":", page)
print("Número total de páginas:", total_pages)
