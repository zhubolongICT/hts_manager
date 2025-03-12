import time
from tqdm import tqdm
from hts.DeckManager import DeckManager


if __name__ == "__main__":
    manager = DeckManager(
        cards_json_filepath='data/cards.json',
        images_cache_dirpath='/mnt/d/imagecache')

    dbfId2CardsMap = manager.get_dbfId2CardsMap()
    pbar = tqdm(total=len(dbfId2CardsMap))
    for dbfId, card in dbfId2CardsMap.items():
        manager.get_image_filepath_by_dbfId(dbfId)
        pbar.update(1)
        time.sleep(0.5)
    pbar.close()

