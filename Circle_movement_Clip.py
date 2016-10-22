import simplegui

class ShapeAttributes:
    
    def __init__(self):
        self.line_width = 5
        self.line_color = "Blue"
        self.fill_color = "Orange"
        
class Circle:
    
    
    def __init__(self):
        self.radius = 50
        self.center_point = (100, 100)
       
    def update_x(self, shift_x):
        self.center_point = (
            self.center_point[0] + shift_x,
            self.center_point[1]
        )

class Character:
    key_map = {
            "right": 39,
            "left" : 37,
            "up"   : 38,
            "down" : 40}
   
    def __init__(self):
        self.circle_shape = Circle()
        self.shape_attributes = ShapeAttributes()
        self.movement = 20
        
    def draw_me(self, canvas):
        canvas.draw_circle(
            self.circle_shape.center_point,
            self.circle_shape.radius,
            self.shape_attributes.line_width,
            self.shape_attributes.line_color,
            self.shape_attributes.fill_color
        )
    def move(self, key):
        if key == self.key_map["right"]: 	
            self.circle_shape.update_x(self.movement) 
            print key
cliq = Character()


# Handler to draw on canvas
def draw(canvas):
    cliq.draw_me(canvas)


# Create a frame and assign callbacks to event handlers
 
frame = simplegui.create_frame("Home", 500, 500)
frame.set_keydown_handler(cliq.move)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()
