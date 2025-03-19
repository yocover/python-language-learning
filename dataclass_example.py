from dataclasses import dataclass, field, FrozenInstanceError
from datetime import datetime
from typing import List, Optional
from enum import Enum

class BookCategory(Enum):
    """图书分类枚举"""
    FICTION = "小说"
    SCIENCE = "科学"
    TECHNOLOGY = "技术"
    HISTORY = "历史"
    OTHER = "其他"

@dataclass
class Author:
    """作者信息"""
    name: str
    email: Optional[str] = None
    
    def __str__(self) -> str:
        if self.email:
            return f"{self.name} ({self.email})"
        return self.name

@dataclass(frozen=True)
class BookId:
    """图书ID，设置为不可变类型"""
    isbn: str
    
    def __post_init__(self):
        # 验证ISBN格式
        if not self.isbn.replace("-", "").isdigit():
            raise ValueError("ISBN必须是数字或带连字符的数字")

@dataclass
class Book:
    """图书信息"""
    id: BookId
    title: str
    author: Author
    category: BookCategory
    price: float
    publication_date: datetime
    tags: List[str] = field(default_factory=list)
    description: Optional[str] = None
    borrowed: bool = field(default=False, repr=False)  # repr=False表示在字符串表示中不显示此字段
    
    def __post_init__(self):
        # 验证价格
        if self.price < 0:
            raise ValueError("价格不能为负数")
    
    @property
    def is_new_book(self) -> bool:
        """判断是否为新书（出版时间在3个月内）"""
        age = datetime.now() - self.publication_date
        return age.days <= 90

@dataclass
class Library:
    """图书馆"""
    name: str
    books: List[Book] = field(default_factory=list)
    
    def add_book(self, book: Book):
        """添加图书"""
        self.books.append(book)
    
    def find_books_by_category(self, category: BookCategory) -> List[Book]:
        """按分类查找图书"""
        return [book for book in self.books if book.category == category]
    
    def get_total_value(self) -> float:
        """计算所有图书总价值"""
        return sum(book.price for book in self.books)

def main():
    # 创建作者
    author1 = Author("张三", "zhangsan@example.com")
    author2 = Author("李四")
    
    # 创建图书ID
    book_id1 = BookId("978-7-111-11111-1")
    book_id2 = BookId("978-7-222-22222-2")
    
    try:
        # 这将引发错误
        invalid_book_id = BookId("invalid-isbn")
    except ValueError as e:
        print(f"创建无效的ISBN时出错: {e}")
    
    # 创建图书
    book1 = Book(
        id=book_id1,
        title="Python编程",
        author=author1,
        category=BookCategory.TECHNOLOGY,
        price=59.9,
        publication_date=datetime(2023, 1, 1),
        tags=["Python", "编程", "入门"]
    )
    
    book2 = Book(
        id=book_id2,
        title="历史的长河",
        author=author2,
        category=BookCategory.HISTORY,
        price=45.0,
        publication_date=datetime(2023, 12, 1),
        description="一本精彩的历史书"
    )
    
    # 创建图书馆
    library = Library("示例图书馆")
    library.add_book(book1)
    library.add_book(book2)
    
    # 展示数据类的各种用法
    print("\n=== 基本信息打印 ===")
    print(f"作者信息: {author1}")
    print(f"图书信息: {book1}")
    
    print("\n=== 属性访问 ===")
    print(f"书名: {book1.title}")
    print(f"作者: {book1.author.name}")
    print(f"是否新书: {book1.is_new_book}")
    
    print("\n=== 图书查询 ===")
    tech_books = library.find_books_by_category(BookCategory.TECHNOLOGY)
    print(f"技术类图书数量: {len(tech_books)}")
    
    print("\n=== 图书馆统计 ===")
    print(f"图书馆藏书总价值: {library.get_total_value():.2f}元")
    
    print("\n=== 不可变对象测试 ===")
    try:
        book_id1.isbn = "new-isbn"  # 这将引发错误
    except FrozenInstanceError as e:
        print(f"尝试修改不可变对象时出错: {e}")

if __name__ == "__main__":
    main()