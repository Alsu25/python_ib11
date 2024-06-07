def score(ring, sector=0):
    global scoring
    if not sector:
        return scoring[ring]
    return scoring[ring][sector]
