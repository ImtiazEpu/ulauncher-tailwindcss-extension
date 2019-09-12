from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.OpenUrlAction import OpenUrlAction

class TailwindcssExtension(Extension):

    def __init__(self):
        super(TailwindcssExtension, self).__init__()

        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())


class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):

        description = "Type in your query and press Enter..."

        url = "https://tailwindcss.com/docs/"

        if event.get_argument() != None:
            description = url + event.get_argument()

        return RenderResultListAction([
            ExtensionResultItem(
                icon='icons/tailwindcss.svg',
                name='Tailwind CSS Search',
                description=description,
                on_enter=OpenUrlAction(url + (event.get_argument() or ''))
            )
        ])

if __name__ == '__main__':
    TailwindcssExtension().run()