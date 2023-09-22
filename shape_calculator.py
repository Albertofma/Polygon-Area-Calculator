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
        return int((self.width//new_shape.width)*(self.height//new_shape.height)) 
      else:
        return 0
    else:
      return 0
    #New code works as intended, older one passed the tests but was wrong. In this case, even if it is not asked, we make sure that the shape that has
    #To fit inside actually does fit inside. Once done, a way of getting the number of times it fits inside taking into account that it cannot rotate is:
    #First we check how many times the width fits inside, then we do the same for the height and then we multiply this values.
    #Old code was int(self.get_area()/new_shape.get_area()).
    
      



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
