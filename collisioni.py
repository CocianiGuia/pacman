def collision_test(rect, tiles):
        listacollisioni = []
        for tile in tiles:
            if rect.colliderect(tile):
                listacollisioni.append(tile)
        return listacollisioni
        