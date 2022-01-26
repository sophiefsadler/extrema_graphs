import numpy as np

class BirastriginMax5d:
    @staticmethod
    def fitness(params):
        x = params[0]
        y = params[1]
        z = params[2]
        a = params[3]
        b = params[4]
        mu = 2.5
        s = 1 - (1/(2*np.sqrt(25)-8.2))
        mu_2 = np.sqrt(abs((mu**2 - 1)/s))
        sum_1 = 5 - np.cos(2*np.pi*(x-mu)) - np.cos(2*np.pi*(y-mu)) - np.cos(2*np.pi*(z-mu)) - np.cos(2*np.pi*(a-mu)) - np.cos(2*np.pi*(b-mu))
        sum_2 = (x-mu)**2 + (y-mu)**2 + (z-mu)**2 + (a-mu)**2 + (b-mu)**2
        sum_3 = (x-mu_2)**2 + (y-mu_2)**2 + (z-mu_2)**2 + (a-mu_2)**2 + (b-mu_2)**2
        return 10*sum_1 + min(sum_2, 5 + s*sum_3)

    @staticmethod
    def get_bounds():
        return [-5.12, -5.12, -5.12, -5.12, -5.12], [5.12, 5.12, 5.12, 5.12, 5.12]

class BirastriginMin5d:
    @staticmethod
    def fitness(params):
        x = params[0]
        y = params[1]
        z = params[2]
        a = params[3]
        b = params[4]
        mu = 2.5
        s = 1 - (1/(2*np.sqrt(25)-8.2))
        mu_2 = np.sqrt(abs((mu**2 - 1)/s))
        sum_1 = 5 - np.cos(2*np.pi*(x-mu)) - np.cos(2*np.pi*(y-mu)) - np.cos(2*np.pi*(z-mu)) - np.cos(2*np.pi*(a-mu)) - np.cos(2*np.pi*(b-mu))
        sum_2 = (x-mu)**2 + (y-mu)**2 + (z-mu)**2 + (a-mu)**2 + (b-mu)**2
        sum_3 = (x-mu_2)**2 + (y-mu_2)**2 + (z-mu_2)**2 + (a-mu_2)**2 + (b-mu_2)**2
        return -(10*sum_1 + min(sum_2, 5 + s*sum_3))

    @staticmethod
    def get_bounds():
        return [-5.12, -5.12, -5.12, -5.12, -5.12], [5.12, 5.12, 5.12, 5.12, 5.12]


class GriewankMax3d:
    @staticmethod
    def fitness(params):
        x = params[0]
        y = params[1]
        z = params[2]
        part1 = x**2 + y**2 + z**2
        part2 = np.cos(x)
        part2 *= np.cos(y / np.sqrt(2))
        part2 *= np.cos(z / np.sqrt(3))
        return 1 + (part1/4000.0) - part2

    @staticmethod
    def get_bounds():
        return [-5, -5, -5], [5, 5, 5]

class GriewankMin3d:
    @staticmethod
    def fitness(params):
        x = params[0]
        y = params[1]
        z = params[2]
        part1 = x**2 + y**2 + z**2
        part2 = np.cos(x)
        part2 *= np.cos(y / np.sqrt(2))
        part2 *= np.cos(z / np.sqrt(3))
        return -(1 + (part1/4000.0) - part2)

    @staticmethod
    def get_bounds():
        return [-5, -5, -5], [5, 5, 5]

    

class GriewankMaxNd:
    
    @staticmethod
    def fitness(params):
        sum_part = 0
        prod = 1
        for i in range(len(params)):
            sum_part += (params[i]**2/4000)
            prod *= np.cos(params[i]/np.sqrt(i+1))
        return 1 + sum_part + prod

    @staticmethod
    def get_bounds():
        return [-5]*30, [5]*30

class GriewankMinNd:

    @staticmethod
    def fitness(params):
        sum_part = 0
        prod = 1
        for i in range(len(params)):
            sum_part += (params[i]**2/4000)
            prod *= np.cos(params[i]/np.sqrt(i+1))
        return -(1 + sum_part + prod)

    @staticmethod
    def get_bounds():
        return [-5]*30, [5]*30
    
class RastriginMax3d:
    @staticmethod
    def fitness(params):
        x = params[0]
        y = params[1]
        z = params[2]
        sum_squares = x**2 + y**2 + z**2
        sum_cos = np.cos(2*np.pi*x) + np.cos(2*np.pi*y) + np.cos(2*np.pi*z)
        return 30 + sum_squares - 10*sum_cos

    @staticmethod
    def get_bounds():
        return [-5.12, -5.12, -5.12], [5.12, 5.12, 5.12]

class RastriginMin3d:
    @staticmethod
    def fitness(params):
        x = params[0]
        y = params[1]
        z = params[2]
        sum_squares = x**2 + y**2 + z**2
        sum_cos = np.cos(2*np.pi*x) + np.cos(2*np.pi*y) + np.cos(2*np.pi*z)
        return -(30 + sum_squares - 10*sum_cos)

    @staticmethod
    def get_bounds():
        return [-5.12, -5.12, -5.12], [5.12, 5.12, 5.12]

class AckleyMax3d:
    @staticmethod
    def fitness(params):
        x = params[0]
        y = params[1]
        z = params[2]
        sum_squares = x**2 + y**2 + z**2
        sum_cos = np.cos(2*np.pi*x) + np.cos(2*np.pi*y) + np.cos(2*np.pi*z)
        exp_1 = -0.2*np.sqrt((1/3)*sum_squares)
        exp_2 = (1/3)*sum_cos
        return -20*np.exp(exp_1) - np.exp(exp_2) + 20 + np.e

    @staticmethod
    def get_bounds():
        return [-32.768, -32.768, -32.768], [32.768, 32.768, 32.768]

class AckleyMin3d:
    @staticmethod
    def fitness(params):
        x = params[0]
        y = params[1]
        z = params[2]
        sum_squares = x**2 + y**2 + z**2
        sum_cos = np.cos(2*np.pi*x) + np.cos(2*np.pi*y) + np.cos(2*np.pi*z)
        exp_1 = -0.2*np.sqrt((1/3)*sum_squares)
        exp_2 = (1/3)*sum_cos
        return -(-20*np.exp(exp_1) - np.exp(exp_2) + 20 + np.e)

    @staticmethod
    def get_bounds():
        return [-32.768, -32.768, -32.768], [32.768, 32.768, 32.768]