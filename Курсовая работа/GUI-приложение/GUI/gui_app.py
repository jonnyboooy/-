from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class Container(BoxLayout):
    pass


class TheOptimalWayApp(App):
    def build(self):
        # bl = BoxLayout()
        # button1 = Button(text='Сохранить')
        # button2 = Button(text='Отмена')
        # bl.add_widget(button1)
        # bl.add_widget(button2)

        return Container()


if __name__ == '__main__':
    TheOptimalWayApp().run()
