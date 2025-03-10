def is_leap_year(year):
    """判断是否是闰年"""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def calculate_days(year, month, day):
    """计算是一年中的第几天"""
    # 每个月的天数（非闰年）
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # 如果是闰年，2月份有29天
    if is_leap_year(year):
        days_in_month[1] = 29
    
    # 计算总天数
    total_days = sum(days_in_month[:month-1]) + day
    
    return total_days

def main():
    try:
        # 获取用户输入
        year = int(input("请输入年份："))
        month = int(input("请输入月份（1-12）："))
        day = int(input("请输入日期（1-31）："))
        
        # 输入验证
        if month < 1 or month > 12:
            print("月份必须在1到12之间！")
            return
            
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if is_leap_year(year):
            days_in_month[1] = 29
            
        if day < 1 or day > days_in_month[month-1]:
            print(f"{month}月份的日期必须在1到{days_in_month[month-1]}之间！")
            return
        
        # 计算天数
        result = calculate_days(year, month, day)
        print(f"{year}年{month}月{day}日是{year}年的第{result}天。")
        
    except ValueError:
        print("请输入有效的数字！")

if __name__ == "__main__":
    main() 