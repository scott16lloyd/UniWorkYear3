class ceoSingletonClass(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ceoSingletonClass, cls).__new__(cls)
        return cls.instance
    
ceoSingleton = ceoSingletonClass()
new_ceoSingleton = ceoSingletonClass()

print(ceoSingleton is new_ceoSingleton)

ceoSingleton.singl_variable = "Singleton variable"
print(new_ceoSingleton.singl_variable)