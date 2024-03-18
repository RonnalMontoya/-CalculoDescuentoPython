def calcular_descuento(monto_total, porcentaje_descuento=15):
    """
    Calcula el descuento aplicando el porcentaje al monto total de la compra.

    Parámetros:
        monto_total (float): El monto total de la compra.
        porcentaje_descuento (float, opcional): El porcentaje de descuento a aplicar, 
                                                 por defecto es 10%.

    Retorna:
        float: El monto del descuento calculado.
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento

# Ejemplo de uso:
monto_total_compra = 100  # Monto total de la compra
descuento_calculado = calcular_descuento(monto_total_compra)  # Porcentaje de descuento predeterminado (10%)
print("El descuento aplicado es:", descuento_calculado)

