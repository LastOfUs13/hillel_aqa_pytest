from HW23.base_db import BaseDb


class PsGamesCollection(BaseDb):
    def __init__(self):
        super().__init__('Games', 'PS_Games')
