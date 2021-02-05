import utils
from kivymd.app import MDApp
from kivy.lang import Builder

KV = '''
MDBoxLayout:
    orientation: "vertical"

    MDToolbar:
        title: "Digit-Reco"
        right_action_items: [["reload", lambda x: app.callback(x), "Load other examples"]]

    BoxLayout:
        orientation: 'vertical'
        ScrollView:
            MDList:
                Image:
                    nocache: True 
                    id: im1
                    size_hint: None, None
                    size: 50, 50
                    pos_hint_x: .5
                MDLabel:
                    id: lbl1
                
                Image:
                    id: im2
                    size_hint: None, None
                    size: 50, 50
                    pos_hint_x: .5
                MDLabel:
                    id: lbl2
                Image:
                    id: im3
                    size_hint: None, None
                    size: 50, 50
                    pos_hint_x: .5
                MDLabel:
                    id: lbl3
                Image:
                    id: im4
                    size_hint: None, None
                    size: 50, 50
                    pos_hint_x: .5
                MDLabel:
                    id: lbl4
                Image:
                    id: im5
                    size_hint: None, None
                    size: 50, 50
                    pos_hint_x: .5
                MDLabel:
                    id: lbl5
               
'''


class Test(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        x_images, y_images = utils.get_batch(5)
        predictions = utils.predict(x_images)
        for i in range(1, 6):
            x, y = x_images[i - 1], y_images[i - 1]
            self.root.ids[f'im{i}'].texture = utils.to_texture(x)
            self.root.ids[f'lbl{i}'].text = f'Predicted label: {predictions[i - 1]}    Real label: {y}'

    def callback(self, button):
        x_images, y_images = utils.get_batch(5)
        predictions = utils.predict(x_images)
        for i in range(1, 6):
            x, y = x_images[i - 1], y_images[i - 1]
            self.root.ids[f'im{i}'].texture = utils.to_texture(x)
            self.root.ids[f'lbl{i}'].text = f'Predicted label: {predictions[i - 1]}    Real label: {y}'


try:
    Test().run()
except KeyboardInterrupt:
    pass
