from __future__ import annotations
from abc import ABC, abstractmethod

"""
当所需的一系列对象可以被一个二维表格所描述的话，那么就可以使用抽象工厂模式
这个模式的意义是，将对二维的决定转化为了两次一维的决定
这样就可以将共有的一维决定抽象出来，由实际调用者按照现实情况来决定另一维该如何决定
"""

class AbstractFactory(ABC):

    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass

    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        pass

class AbstractProduct(ABC):

    @abstractmethod
    def useful_func(self) -> str:
        pass


class ConcreteFactory1(AbstractFactory):

    def create_product_a(self) -> ConcreteProductA1:
        return ConcreteProductA1()

    def create_product_b(self) -> ConcreteProductB1:
        return ConcreteProductB1()

class ConcreteFactory2(AbstractFactory):

    def create_product_a(self) -> ConcreteProductA2:
        return ConcreteProductA2()

    def create_product_b(self) -> ConcreteProductB2:
        return ConcreteProductB2()

class ConcreteProductA1(AbstractProduct):

    def useful_func(self) -> str:
        return "concrete product a 1"

class ConcreteProductA2(AbstractProduct):

    def useful_func(self) -> str:
        return "concrete product a 2"

class ConcreteProductB1(AbstractProduct):

    def useful_func(self) -> str:
        return "concrete product b 1"

class ConcreteProductB2(AbstractProduct):

    def useful_func(self) -> str:
        return "concrete product b 2"

def client_code(factory: AbstractFactory) -> None:

    productA = factory.create_product_a()
    productB = factory.create_product_b()

    print(productA.useful_func())
    print(productB.useful_func())

if __name__ == "__main__":
    client_code(ConcreteFactory1())
    client_code(ConcreteFactory2())