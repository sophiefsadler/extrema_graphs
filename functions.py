import numpy as np

class SphereMax2d:
    
    @staticmethod
    def fitness(params):
        return np.sum(params**2)

    @staticmethod
    def get_bounds():
        return [-5.12]*2, [5.12]*2

class SphereMin2d:
    
    @staticmethod
    def fitness(params):
        return -np.sum(params**2)

    @staticmethod
    def get_bounds():
        return [-5.12]*2, [5.12]*2

class SphereMax3d:
    
    @staticmethod
    def fitness(params):
        return np.sum(params**2)

    @staticmethod
    def get_bounds():
        return [-5.12]*3, [5.12]*3

class SphereMin3d:
    
    @staticmethod
    def fitness(params):
        return -np.sum(params**2)

    @staticmethod
    def get_bounds():
        return [-5.12]*3, [5.12]*3

    
class SphereMax5d:
    
    @staticmethod
    def fitness(params):
        return np.sum(params**2)

    @staticmethod
    def get_bounds():
        return [-5.12]*5, [5.12]*5
    
class SphereMin5d:
    
    @staticmethod
    def fitness(params):
        return -np.sum(params**2)

    @staticmethod
    def get_bounds():
        return [-5.12]*5, [5.12]*5
    
class SphereMax10d:
    
    @staticmethod
    def fitness(params):
        return np.sum(params**2)

    @staticmethod
    def get_bounds():
        return [-5.12]*10, [5.12]*10
    
class SphereMin10d:
    
    @staticmethod
    def fitness(params):
        return -np.sum(params**2)

    @staticmethod
    def get_bounds():
        return [-5.12]*10, [5.12]*10
    
class SphereMax20d:
    
    @staticmethod
    def fitness(params):
        return np.sum(params**2)

    @staticmethod
    def get_bounds():
        return [-5.12]*20, [5.12]*20
    
class SphereMin20d:
    
    @staticmethod
    def fitness(params):
        return -np.sum(params**2)

    @staticmethod
    def get_bounds():
        return [-5.12]*20, [5.12]*20
    
    
class RastriginMin2d:
    
    @staticmethod
    def fitness(params):
        dim = 2
        val = 10*dim + np.sum(params**2 - 10 * np.cos(2 * np.pi * params))
        return -val

    @staticmethod
    def get_bounds():
        return [-5.12]*2, [5.12]*2

class RastriginMax2d:
    
    @staticmethod
    def fitness(params):
        dim = 2
        val = 10*dim + np.sum(params**2 - 10 * np.cos(2 * np.pi * params))
        return val

    @staticmethod
    def get_bounds():
        return [-5.12]*2, [5.12]*2

class RastriginMin3d:
    
    @staticmethod
    def fitness(params):
        dim = 3
        val = 10*dim + np.sum(params**2 - 10 * np.cos(2 * np.pi * params))
        return -val

    @staticmethod
    def get_bounds():
        return [-5.12]*3, [5.12]*3

class RastriginMax3d:
    
    @staticmethod
    def fitness(params):
        dim = 3
        val = 10*dim + np.sum(params**2 - 10 * np.cos(2 * np.pi * params))
        return val

    @staticmethod
    def get_bounds():
        return [-5.12]*3, [5.12]*3
    
class RastriginMin5d:
    
    @staticmethod
    def fitness(params):
        dim = 5
        val = 10*dim + np.sum(params**2 - 10 * np.cos(2 * np.pi * params))
        return -val

    @staticmethod
    def get_bounds():
        return [-5.12]*5, [5.12]*5

class RastriginMax5d:
    
    @staticmethod
    def fitness(params):
        dim = 5
        val = 10*dim + np.sum(params**2 - 10 * np.cos(2 * np.pi * params))
        return val

    @staticmethod
    def get_bounds():
        return [-5.12]*5, [5.12]*5
    
class RastriginMin10d:
    
    @staticmethod
    def fitness(params):
        dim = 5
        val = 10*dim + np.sum(params**2 - 10 * np.cos(2 * np.pi * params))
        return -val

    @staticmethod
    def get_bounds():
        return [-5.12]*5, [5.12]*5

class RastriginMax10d:
    
    @staticmethod
    def fitness(params):
        dim = 5
        val = 10*dim + np.sum(params**2 - 10 * np.cos(2 * np.pi * params))
        return val

    @staticmethod
    def get_bounds():
        return [-5.12]*5, [5.12]*5
    
    
class GriewankMax2d:
    
    @staticmethod
    def fitness(params):
        dim = 2
        val = (np.sum(params**2)/4000) + 1 - np.prod(np.cos(params/np.sqrt(np.arange(len(params))+1)))
        return val
        

    @staticmethod
    def get_bounds():
        return [-5]*2, [5]*2
    
class GriewankMin2d:
    
    @staticmethod
    def fitness(params):
        dim = 2
        val = (np.sum(params**2)/4000) + 1 - np.prod(np.cos(params/np.sqrt(np.arange(len(params))+1)))
        return -val
        

    @staticmethod
    def get_bounds():
        return [-5]*2, [5]*2

class GriewankMax3d:
    
    @staticmethod
    def fitness(params):
        dim = 3
        val = (np.sum(params**2)/4000) + 1 - np.prod(np.cos(params/np.sqrt(np.arange(len(params))+1)))
        return val
        

    @staticmethod
    def get_bounds():
        return [-5]*3, [5]*3
    
class GriewankMin3d:
    
    @staticmethod
    def fitness(params):
        dim = 3
        val = (np.sum(params**2)/4000) + 1 - np.prod(np.cos(params/np.sqrt(np.arange(len(params))+1)))
        return -val
        

    @staticmethod
    def get_bounds():
        return [-5]*3, [5]*3

    
class GriewankMax5d:
    
    @staticmethod
    def fitness(params):
        dim = 5
        val = (np.sum(params**2)/4000) + 1 - np.prod(np.cos(params/np.sqrt(np.arange(len(params))+1)))
        return val
        

    @staticmethod
    def get_bounds():
        return [-5]*5, [5]*5
    
class GriewankMin5d:
    
    @staticmethod
    def fitness(params):
        dim = 5
        val = (np.sum(params**2)/4000) + 1 - np.prod(np.cos(params/np.sqrt(np.arange(len(params))+1)))
        return -val
        

    @staticmethod
    def get_bounds():
        return [-5]*5, [5]*5
