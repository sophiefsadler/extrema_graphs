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


class AckleyMax2d:
    
    @staticmethod
    def fitness(params):
        dim = 2
        val = -20*np.exp(-0.2*np.sqrt((1/dim)*np.sum(params**2))) - np.exp((1/dim)*np.sum(np.cos(2*np.pi*params))) + 20 + np.exp(1)
        return val

    @staticmethod
    def get_bounds():
        return [-32.768]*2, [32.768]*2

class AckleyMin2d:
    
    @staticmethod
    def fitness(params):
        dim = 2
        val = -20*np.exp(-0.2*np.sqrt((1/dim)*np.sum(params**2))) - np.exp((1/dim)*np.sum(np.cos(2*np.pi*params))) + 20 + np.exp(1)
        return -val

    @staticmethod
    def get_bounds():
        return [-32.768]*2, [32.768]*2

class AckleyMax3d:
    
    @staticmethod
    def fitness(params):
        dim = 3
        val = -20*np.exp(-0.2*np.sqrt((1/dim)*np.sum(params**2))) - np.exp((1/dim)*np.sum(np.cos(2*np.pi*params))) + 20 + np.exp(1)
        return val

    @staticmethod
    def get_bounds():
        return [-32.768]*3, [32.768]*3

class AckleyMin3d:
    
    @staticmethod
    def fitness(params):
        dim = 3
        val = -20*np.exp(-0.2*np.sqrt((1/dim)*np.sum(params**2))) - np.exp((1/dim)*np.sum(np.cos(2*np.pi*params))) + 20 + np.exp(1)
        return -val

    @staticmethod
    def get_bounds():
        return [-32.768]*3, [32.768]*3

class AckleyMax5d:
    
    @staticmethod
    def fitness(params):
        dim = 5
        val = -20*np.exp(-0.2*np.sqrt((1/dim)*np.sum(params**2))) - np.exp((1/dim)*np.sum(np.cos(2*np.pi*params))) + 20 + np.exp(1)
        return val

    @staticmethod
    def get_bounds():
        return [-32.768]*5, [32.768]*5

class AckleyMin5d:
    
    @staticmethod
    def fitness(params):
        dim = 5
        val = -20*np.exp(-0.2*np.sqrt((1/dim)*np.sum(params**2))) - np.exp((1/dim)*np.sum(np.cos(2*np.pi*params))) + 20 + np.exp(1)
        return -val

    @staticmethod
    def get_bounds():
        return [-32.768]*5, [32.768]*5


class SchwefelMax2d:
    
    @staticmethod
    def fitness(params):
        dim = 2
        val = 418.9829*dim - np.sum(params*np.sin(np.sqrt(np.abs(params))))
        return val

    @staticmethod
    def get_bounds():
        return [-500]*2, [500]*2

class SchwefelMin2d:
    
    @staticmethod
    def fitness(params):
        dim = 2
        val = 418.9829*dim - np.sum(params*np.sin(np.sqrt(np.abs(params))))
        return -val

    @staticmethod
    def get_bounds():
        return [-500]*2, [500]*2

class SchwefelMax3d:
    
    @staticmethod
    def fitness(params):
        dim = 3
        val = 418.9829*dim - np.sum(params*np.sin(np.sqrt(np.abs(params))))
        return val

    @staticmethod
    def get_bounds():
        return [-500]*3, [500]*3

class SchwefelMin3d:
    
    @staticmethod
    def fitness(params):
        dim = 3
        val = 418.9829*dim - np.sum(params*np.sin(np.sqrt(np.abs(params))))
        return -val

    @staticmethod
    def get_bounds():
        return [-500]*3, [500]*3

class SchwefelMax5d:
    
    @staticmethod
    def fitness(params):
        dim = 5
        val = 418.9829*dim - np.sum(params*np.sin(np.sqrt(np.abs(params))))
        return val

    @staticmethod
    def get_bounds():
        return [-500]*5, [500]*5

class SchwefelMin5d:
    
    @staticmethod
    def fitness(params):
        dim = 5
        val = 418.9829*dim - np.sum(params*np.sin(np.sqrt(np.abs(params))))
        return -val

    @staticmethod
    def get_bounds():
        return [-500]*5, [500]*5


class RosenbrockMax2d:
    
    @staticmethod
    def fitness(params):
        dim = 2
        val = 0
        for i in range(len(params)-1):
            val += 100*((params[i+1]-params[i]**2)**2) + (params[i]-1)**2
        return val

    @staticmethod
    def get_bounds():
        return [-5]*2, [10]*2

class RosenbrockMin2d:
    
    @staticmethod
    def fitness(params):
        dim = 2
        val = 0
        for i in range(len(params)-1):
            val += 100*((params[i+1]-params[i]**2)**2) + (params[i]-1)**2
        return -val

    @staticmethod
    def get_bounds():
        return [-5]*2, [10]*2

class RosenbrockMax3d:
    
    @staticmethod
    def fitness(params):
        dim = 3
        val = 0
        for i in range(len(params)-1):
            val += 100*((params[i+1]-params[i]**2)**2) + (params[i]-1)**2
        return val

    @staticmethod
    def get_bounds():
        return [-5]*3, [10]*3

class RosenbrockMin3d:
    
    @staticmethod
    def fitness(params):
        dim = 3
        val = 0
        for i in range(len(params)-1):
            val += 100*((params[i+1]-params[i]**2)**2) + (params[i]-1)**2
        return -val

    @staticmethod
    def get_bounds():
        return [-5]*3, [10]*3

class RosenbrockMax5d:
    
    @staticmethod
    def fitness(params):
        dim = 5
        val = 0
        for i in range(len(params)-1):
            val += 100*((params[i+1]-params[i]**2)**2) + (params[i]-1)**2
        return val

    @staticmethod
    def get_bounds():
        return [-5]*5, [10]*5

class RosenbrockMin5d:
    
    @staticmethod
    def fitness(params):
        dim = 5
        val = 0
        for i in range(len(params)-1):
            val += 100*((params[i+1]-params[i]**2)**2) + (params[i]-1)**2
        return -val

    @staticmethod
    def get_bounds():
        return [-5]*5, [10]*5
