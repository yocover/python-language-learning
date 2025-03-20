from datetime import datetime, date
from typing import List, Optional
from pydantic import BaseModel, Field, model_validator, computed_field

class Product(BaseModel):
    """商品模型"""
    name: str = Field(..., description="商品名称")
    price: float = Field(..., gt=0, description="商品价格")
    quantity: int = Field(default=0, ge=0, description="库存数量")
    created_at: datetime = Field(default_factory=datetime.now, description="创建时间")
    
    @computed_field
    @property
    def is_in_stock(self) -> bool:
        """是否有库存"""
        return self.quantity > 0
    
    @computed_field
    @property
    def total_value(self) -> float:
        """商品总价值"""
        return self.price * self.quantity

class Order(BaseModel):
    """订单模型"""
    order_id: str = Field(..., pattern=r"^ORD\d{6}$", description="订单ID")
    customer_name: str = Field(..., min_length=2, description="客户名称")
    items: List[Product] = Field(default_factory=list, description="订单商品")
    order_date: date = Field(default_factory=date.today, description="订单日期")
    discount: float = Field(default=0, ge=0, le=1, description="折扣率")
    
    @computed_field
    @property
    def total_items(self) -> int:
        """商品总数量"""
        return sum(item.quantity for item in self.items)
    
    @computed_field
    @property
    def subtotal(self) -> float:
        """订单小计"""
        return sum(item.total_value for item in self.items)
    
    @computed_field
    @property
    def total(self) -> float:
        """订单总价（含折扣）"""
        return self.subtotal * (1 - self.discount)
    
    @model_validator(mode='after')
    def validate_order(self) -> 'Order':
        """验证订单"""
        # 验证订单至少包含一个商品
        if not self.items:
            raise ValueError("订单必须包含至少一个商品")
        
        # 验证所有商品都有库存
        out_of_stock = [item.name for item in self.items if not item.is_in_stock]
        if out_of_stock:
            raise ValueError(f"以下商品无库存: {', '.join(out_of_stock)}")
        
        return self

def main():
    # 创建商品
    try:
        phone = Product(
            name="iPhone 15",
            price=6999,
            quantity=10
        )
        
        laptop = Product(
            name="MacBook Pro",
            price=12999,
            quantity=5
        )
        
        # 创建订单
        order = Order(
            order_id="ORD123456",
            customer_name="张三",
            items=[phone, laptop],
            discount=0.1  # 10% 折扣
        )
        
        # 打印订单信息
        print("=== 订单信息 ===")
        print(f"订单号: {order.order_id}")
        print(f"客户: {order.customer_name}")
        print(f"订单日期: {order.order_date}")
        print("\n商品列表:")
        for item in order.items:
            print(f"- {item.name}")
            print(f"  价格: ¥{item.price}")
            print(f"  数量: {item.quantity}")
            print(f"  库存状态: {'有货' if item.is_in_stock else '无货'}")
            print(f"  总价值: ¥{item.total_value}")
        
        print(f"\n商品总数: {order.total_items}")
        print(f"订单小计: ¥{order.subtotal}")
        print(f"折扣率: {order.discount * 100}%")
        print(f"订单总价: ¥{order.total}")
        
        # 测试验证器
        print("\n=== 测试验证器 ===")
        # 尝试创建无库存商品的订单
        no_stock_product = Product(
            name="测试商品",
            price=100,
            quantity=0
        )
        
        invalid_order = Order(
            order_id="ORD654321",
            customer_name="李四",
            items=[no_stock_product]
        )
        
    except ValueError as e:
        print(f"\n验证错误: {e}")
    except Exception as e:
        print(f"\n其他错误: {e}")

if __name__ == "__main__":
    main() 