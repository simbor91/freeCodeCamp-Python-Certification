# 06 Objects-Oriented Programming (OOP)
    # Abstraction
#017 Workshop: Build a Discount Calculator

from abc import ABC, abstractmethod
# abstract classes as blueprints for other classes. They serve as a contract, ensuring that all discount strategies will have certain required methods
# abstractmethod decorator for methods that must be implemented by any class that inherits from your abstract class
from typing import List
# to specify that a function parameter is a list containing specific types of objects, to manage multiple discount strategies

class Product:
    def __init__(self, name: str, price: float) -> None: # type hints "name: str" + return type hint "-> None"
        self.name = name
        self.price = price

    def __str__(self) -> str:
        return f'{self.name} - ${self.price}'

class DiscountStrategy(ABC):
    @abstractmethod
    def is_applicable(self, product: Product, user_tier: str) -> bool:
        pass

    @abstractmethod
    def apply_discount(self, product: Product) -> float:
        pass

class PercentageDiscount(DiscountStrategy):
    """first discount strategy"""
    def __init__(self, percent: int) -> None:
        self.percent = percent
    
    def is_applicable(self, product: Product, user_tier: str) -> bool:
        # if self.percent <= 70: return True
        # else: return False
        return self.percent <= 70
    
    def apply_discount(self, product: Product) -> float:
        return product.price * (1 - self.percent / 100)

class FixedAmountDiscount(DiscountStrategy):
    """second discount strategy"""
    def __init__(self, amount: int) -> None:
        self.amount = amount

    def is_applicable(self, product: Product, user_tier: str) -> bool:
        return product.price * 0.9 > self.amount

    def apply_discount(self, product: Product) -> float:
        return product.price - self.amount

class PremiumUserDiscount(DiscountStrategy):
    """third discount strategy for premium users"""
    def is_applicable(self, product: Product, user_tier: str) -> bool:
        return user_tier.lower() == 'premium'

    def apply_discount(self, product: Product) -> float:
        return product.price * 0.8

class DiscountEngine():
    """this class will manage all discount strategies and calculate the best price for a product"""
    def __init__(self, strategies: List[DiscountStrategy]) -> None:
        self.strategies = strategies

    def calculate_best_price(self, product: Product, user_tier: str) -> float:
        prices = [product.price]
        for strategy in self.strategies:
            if strategy.is_applicable(product, user_tier):
                discounted = strategy.apply_discount(product)
                prices.append(discounted)
        return min(prices)

if __name__ == '__main__':
    product = Product('Wireless Mouse', 50.0)
    user_tier = 'Premium'
    strategies = [
        PercentageDiscount(10), 
        FixedAmountDiscount(5), 
        PremiumUserDiscount()
    ]
    engine = DiscountEngine(strategies)
    best_price = engine.calculate_best_price(product, user_tier)

    print(f"Best price for '{product.name}' for {user_tier} user: ${best_price:.2f}")

# product = Product('Wireless Mouse', 50.0)
# print(product)
# discount = PercentageDiscount(10)
# print(discount.apply_discount(product))
# fixed_discount = FixedAmountDiscount(5)
# print(fixed_discount.apply_discount(product))

# print(discount.__doc__)
# print(fixed_discount.__doc__)
