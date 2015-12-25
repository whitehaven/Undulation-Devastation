import cocos


class SimulationWindow(cocos.layer.Layer):
    def __init__(self):
        super(SimulationWindow, self).__init__()

        label = cocos.text.Label('Hello, world',
                                 font_name='Times New Roman',
                                 font_size=32,
                                 anchor_x='center', anchor_y='center')
        label.position = 320, 240
        self.add(label)


cocos.director.director.init()
sim_layer = SimulationWindow()
main_scene = cocos.scene.Scene(sim_layer)
cocos.director.director.run(main_scene)
