# -*- coding: utf-8 -*-
"""vector.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xnkXQWJ-_U21SSb2mX3V-kmma8nzRqVY
"""

import numpy as np



class VectorCartesiano:
  def __init__(self,x,y,z):
    self.x = float(x)
    self.y = float(y)
    self.z = float(z)
    self.magnitud = np.sqrt(np.power(x,2)+np.power(y,2)+np.power(z,2))
#se sobrecarga multiplicacion
  def __mul__(self, other):
    return VectorCartesiano(self.x * other.x + self.y * other.y + self.z * other.z)

#se crea el producto cruz
  def Cruz(self,other):
    return VectorCartesiano((self.y * other.z - self.z * other.y), (-self.x * other.z + self.z*other.x), (self.x * other.y -self.y*other.x))
    
  def __add__(self,other):
        '''Sobrecarga del operador suma'''
        return VectorCartesiano(self.x + other.x, self.y + other.y, self.z + other.z)
           
  def __sub__(self,other):        
        '''Sobrecarga del operador resta'''
        return VectorCartesiano(self.x - other.x, self.y - other.y, self.z - other.z)

  def Print(self):
    '''Imprime el vector'''
    print(f"[{self.x},{self.y},{self.z}]")
    print("la magnitud del vector es:",self.magnitud)

#a = VectorCartesiano(4,0,3)
#b= VectorCartesiano(0,1,0)

#c= a.Cruz(b)
#c.Print()



class VectorPolar(VectorCartesiano):
  def __init__(self,r,theta,phi):
    self.r = float(r)
    self.theta = float(theta)
    self.phi = float(phi)
    if r < 0:
      print("por favor ingrese un radio positivo")
    if theta <0 or theta>np.pi:
      print("por favor ingrese theta dentro del rago: 0<Theta< pi")
    if phi<0 or phi> 2*np.pi:
      print("por favor ingrese phi dentro del rago: 0<Phi< 2*pi")
    
  def esfericasAcartesianas(self):
    return VectorCartesiano((self.r*np.sin(self.phi)*np.cos(self.theta)), (self.r*np.sin(self.theta)*np.sin(self.phi) ), (self.r*self.theta))
    
  def cartesianasAesfericas(self):

    return VectorCartesiano((np.sqrt(np.power(x,2)+np.power(y,2)+np.power(z,2))), (np.arccos(z/(np.sqrt(np.power(x,2)+np.power(y,2)+np.power(z,2))))), (np.arctan(y/x)))
 
  def Print(self):
    '''Imprime el vector'''
    print(f"[{self.x},{self.y},{self.z}]")



a = VectorCartesiano(1.5,0,2.4)
b = VectorCartesiano(0,1,9)
c = VectorCartesiano(4.2,.05,0)





