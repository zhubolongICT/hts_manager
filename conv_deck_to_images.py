from hts.DeckManager import DeckManager
from hts.DeckManager import QiJiZeiCode, PaoXiaoDeCode


if __name__ == '__main__':
    deck_manager = DeckManager(
        cards_json_filepath='./data/cards.json',
        images_cache_dirpath='./imagecache')
    
    deck_manager.conv_deckstring_list_to_grid_images(
        deckstring_list=[QiJiZeiCode, PaoXiaoDeCode],
        output_keyname='test',
        output_image_dirpath='./grid_images',
        extra_card_id_list=['EX1_158t', 'EX1_158t', 'EX1_158t'])

    # https://hearthstone.fandom.com/wiki/Card_back
    # https://static.wikia.nocookie.net/hearthstone_gamepedia/images/a/a8/CardBack119.png/revision/latest?cb=20230612200128
    deck_manager.conv_deckstring_list_to_grid_images(
        deckstring_list=[],
        output_keyname='cardback_01',
        output_image_dirpath='./grid_images',
        extra_card_id_list=['CardBack232'] * 9,
        isCardBack=True) 
    deck_manager.conv_deckstring_list_to_grid_images(
        deckstring_list=[],
        output_keyname='cardback_02',
        output_image_dirpath='./grid_images',
        extra_card_id_list=['CardBack119'] * 9,
        isCardBack=True) 
    
