def page_size(name: str):
    sizes = {
        "A4": (595, 842),  # points at 72dpi
        "A3": (842, 1191),
    }
    return sizes.get(name, sizes["A4"])
