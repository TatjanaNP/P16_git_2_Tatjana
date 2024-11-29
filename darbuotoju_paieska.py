def atranka(kandidatu_sarasas: dict[str: list[str | int]], pareigos: str, atlyginimo_riba) -> list[str]:
    tinkami_kandidatai = []
    netinkami_kandidatai = []
    for key, value in kandidatu_sarasas.items():
        if value[0] == pareigos and value[1] <= atlyginimo_riba:
            tinkami_kandidatai.append(key)
        else:
            netinkami_kandidatai.append(key)
    return tinkami_kandidatai
