import os
import json
import codecs
import requests

from hearthstone.deckstrings import Deck
from hearthstone.enums import FormatType

from hts.NineGridDrawer import NineGridDrawer


QiJiZeiCode = 'AAEDAaIHBtyWBPqgBIahBLWhBNyhBKWjBAz8lQT9lQTqlgT7lgT4oATUoQTdoQTfoQTkoQTnoQTooQSTogQA'
PaoXiaoDeCode = 'AAEDAZICCK2hBLWhBNuhBO+hBJOiBJiiBNaiBI+jBAvZlQTblQTclQSwlgTdlgSvoQTpoQTwoQTxoQS9owTFqgQA'


CARD_RENDER_URL_TEMPLATE = \
    'https://art.hearthstonejson.com/v1/render/latest/%s/512x/%s.png'


def encode_decode_demo():
    # EncodingDemo
    # Create a deck from a deckstring
    deck = Deck()
    deck.heroes = [7]  # Garrosh Hellscream
    deck.format = FormatType.FT_WILD
    # Nonsense cards, but the deckstring doesn't validate.
    deck.cards = [(1, 3), (2, 3), (3, 3), (4, 3)]  # id, count pairs
    assert deck.as_deckstring == "AAEBAQcAAAQBAwIDAwMEAwA="

    # DecodingDemo 
    # Import a deck from a deckstring
    deck = Deck.from_deckstring("AAEBAQcAAAQBAwIDAwMEAw==")
    assert deck.heroes == [7]
    assert deck.format == FormatType.FT_WILD
    assert deck.cards == [(1, 3), (2, 3), (3, 3), (4, 3)]


def download_file_to_local(url, filepath):
    try:
        response = requests.get(url, stream=True)
        # 检查请求是否成功
        if response.status_code == 200:
            # 打开一个文件用于写入
            with open(filepath, 'wb') as f:
                # 将内容写入文件
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
        else:
            print(f'DownloadFile({url} Failed By status_code={response.status_code})')
    except Exception as e:
        print(f'DownloadFile({url} Failed By {e})')


class DeckManager(object):
    def __init__(self, cards_json_filepath,
                 images_cache_dirpath):
        self.cards_json_filepath = cards_json_filepath
        self.images_cache_dirpath = images_cache_dirpath
        self.nine_grid_drawer = NineGridDrawer()

        self.dbfId2CardsMap = dict()

        # indexing cards by dbfId
        with codecs.open(self.cards_json_filepath, 
                         mode='r', encoding='utf-8') as fp:
            json_card_array = json.loads(fp.read())
            for json_card in json_card_array:
                self.dbfId2CardsMap[json_card['dbfId']] = json_card

    def get_card_info_by_dbfId(self, dbfId):
        if dbfId in self.dbfId2CardsMap:
            return self.dbfId2CardsMap[dbfId]
        else:
            return None
    
    # TODO: get if an image is already in cache,
    # if not then download it to the cache.
    def get_image_by_dbfId(self, dbfId):
        card = self.get_card_info_by_dbfId(dbfId)
        filepath = os.path.join(self.images_cache_dirpath,
                                '%s.png' % card['id'])

        pass

    def decode(self, deckstring):
        deck = Deck.from_deckstring(deckstring)
        print(deck.heroes)
        print(deck.cards)
        return deck 


if __name__ == '__main__':
    deck_manager = DeckManager(
        cards_json_filepath='./data/cards.json',
        images_cache_dirpath='./imagecache')
    
    print(deck_manager.get_card_info_by_dbfId(dbfId=68348))
    deck_manager.decode(QiJiZeiCode)
    
