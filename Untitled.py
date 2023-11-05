#!/usr/bin/env python
# coding: utf-8

# In[11]:


#Q1, Create a vehicle class with an init method having instance variables as name_of_vehicle, max_speed
#and average_of_vehicle.
class vehicle():
    def __init__(self,name_of_vehicle, max_speed,average_of_vehicle):
        self.name_of_vehicle = name_of_vehicle
        self.max_speed = max_speed
        self.average_of_vehicle = average_of_vehicle
veh=vehicle("Scooty",100,60)
print(veh.name_of_vehicle)
print(veh.max_speed)
print(veh.average_of_vehicle)


# In[ ]:


#Q2,Create a child class car from the vehicle class created in Que 1, which will inherit the vehicle class.
#Create a method named seating_capacity which takes capacity as an argument and returns the name of
#the vehicle and its seating capacity.


# In[18]:


class Vehicle:
    def __init__(self, name_of_vehicle, max_speed, average_of_vehicle):
        self.name_of_vehicle = name_of_vehicle
        self.max_speed = max_speed
        self.average_of_vehicle = average_of_vehicle


class Car(Vehicle):
    def seating_capacity(self, capacity):
        return f"The {self.name_of_vehicle} has a seating capacity of {capacity}."


# Example usage
car1 = Car("Bus", 180, 25)
print(car1.seating_capacity(30))


# In[21]:


#Q3,What is multiple inheritance? Write a python code to demonstrate multiple inheritance.
#if a child class is inheriting the properties of a single other class, we call it single 
#inheritance. However, if a child class inherits from more than one class, i.e. this child class 
#is derived from multiple classes, we call it multiple inheritance in Python.

class animal:
    def dog(self):
        print("I am dog")
        
        
class bird:
    def sparrow(self):
        print("I am sparrow")
        
        
class multiple_inheritance(animal,bird):
    def xyz(self):
        print("Method for multiple inheritance")
        
obj = multiple_inheritance()
obj.dog()
obj.xyz()
obj.sparrow()


# In[22]:


#Q4. What are getter and setter in python? Create a class and create a getter and a setter method in this class.
#In Python, getters and setters are used to control access to the attributes of an object. Getters are methods that
#are used to access the value of an attribute, and setters are methods that are used to modify the value of an attribute 
#while performing some checks or operations.

class MyClass:
    def __init__(self):
        self._value = 0  # private variable


    def get_value(self):
        print("Getting value")
        return self._value

    
    def set_value(self, new_value):
        print("Setting value")
        self._value = new_value

obj = MyClass()
print(obj.get_value())
obj.set_value(5)  
print(obj.get_value())  


# In[23]:


#Q5.What is method overriding in python? Write a python code to demonstrate method overriding.
#Method overriding is a feature in object-oriented programming that allows a subclass to provide a specific 
#implementation of a method that is already defined in its superclass. When a method in a subclass has the same
#name, same parameters, and same return type as a method in its superclass, it is said to override the superclass's method.

class ParentClass:
    def show(self):
        print("Parent class method")


class ChildClass(ParentClass):
    def show(self):
        print("Child class method")


parent_obj = ParentClass()
child_obj = ChildClass()

parent_obj.show()  
child_obj.show()  


# In[ ]:




