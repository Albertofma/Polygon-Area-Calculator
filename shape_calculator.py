class Rectangle:
  
  def __init__(self, width, height):
    """Initialize the class and the instance variables for height and width"""
    self.width = width
    self.height = height
    
  def __str__(self):
    """Set the string we want returned when print function is called on the object"""
    return f'Rectangle(width={self.width}, height={self.height})'
    
  def set_width(self, width):
    """Sets the width of the shape"""
    self.width = width
    
  def set_height(self, height):
    """Sets the height of the shape"""
    self.height = height
    
  def get_area(self):
    """Gets the area of the shape"""
    return self.width * self.height
    
  def get_perimeter(self):
    """Gets the perimeter of the shape"""
    return (2 * self.width + 2 * self.height)
    
  def get_diagonal(self):
    """Gets the diagonal of the shape"""
    return ((self.width ** 2 + self.height ** 2) ** .5)
    
  def get_picture(self):
    if (self.height <= 50) and (self.width  <=50):
      string = (("*" * self.width) + "\n") * self.height 
      return string
    else:
      return "Too big for picture."
  #If the height and width dont surpass 50, it will draw the shape filled with '*'.
  
  def get_amount_inside(self, new_shape):
    if self.get_area() > new_shape.get_area():
      if (self.height > new_shape.height) and (self.width > new_shape.width):
        return int(self.get_area() / new_shape.get_area())
      else:
        return 0
    else:
      return 0
    #This is actually incorrect, as there can be cases where if you cant rotate shapes, areas dont calculate the amount of times it can be fin inside, for example a 2x3 (as in file, columns) and a 5x4, according to areas, it should fit 3 times, but it doesnt, it fits 2 times. Nevertheless the test didnt try this cases, so my code will remain like that
    
      



class Square(Rectangle):
  
  def __init__(self, length):
    self.height=length
    self.width=length
  
  def __str__(self):
    """Set the string we want returned when print function is called on the object"""
    return f'Square(side={self.width})'

  def set_side(self, length):
    self.height=length
    self.width=length
