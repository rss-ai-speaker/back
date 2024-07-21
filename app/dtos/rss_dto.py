class RssLinkDto:
    def __init__(self, link: str):
        self._link = link

    @property
    def link(self):
        return self._link


