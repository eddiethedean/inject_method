def injector_model(function, mod=None):
    name = function.__name__
    def wrapper(k):
        if mod == None:
            setattr(k, name, eval(name))
        else:
            setattr(k, name, mod(eval(name)))
        return k
    return wrapper

def inject_static_method(function):
    return injector_model(function, staticmethod)

def inject_class_method(function):
    return injector_model(function, classmethod)

def inject_instance_method(function):
    return injector_model(function)

def static_test():
    print("I'm static")

def class_test(cls):
    print(cls)
    
def instance_test(self):
    print(self)

@inject_static_method(static_test)
@inject_class_method(class_test)
@inject_instance_method(instance_test)
class TestClass:
    pass
