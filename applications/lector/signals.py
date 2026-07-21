def update_libro_stok(sender, instance, **kwargs):
    # Al eliminar un prestamo el stok incrementa, dado que es como si devolviera el libro
    instance.libro.stok = instance.libro.stok + 1
    instance.libro.save()