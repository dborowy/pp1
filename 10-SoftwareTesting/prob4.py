class Zbiory():
    @staticmethod
    def iloczyn(arr1,arr2):
        return arr1.intersection(arr2)
    @staticmethod
    def suma(arr1,arr2):
        return arr1.union(arr2)
    @staticmethod
    def roznica(arr1,arr2):
        return arr1.difference(arr2)
    