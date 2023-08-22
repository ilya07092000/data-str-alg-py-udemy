class Cookie:
  def __init__(self, color):
    self.color = color

  def get_color(self):
    return self.color
  
  def set_color(self, color):
    self.color = color

cookie1 = Cookie('Red')
print('Cookie1 color:', cookie1.get_color())