def division():
    """功能：分苹果。"""
    print("============================分苹果了=====================")
    apple = int(input("请输入苹果的个数："))
    children = int(input("请输入孩子的个数："))
    if apple < children:
        raise ValueError("苹果太少了，不够分呀。。。")
    result = apple // children
    remain = apple - result * children

    if remain > 0:
        print(apple,"个苹果，平均分给",children,"个小朋友，每个小朋友",result,"个苹果，还剩下",remain,"个")
    else:
        print(apple,"个苹果，平均分给",children,"个小朋友，每个小朋友",result,"个苹果")

if __name__=='__main__':
    try:
        division()
    # except ZeroDivisionError as e:
    #     print("出错了，苹果不能被0个小朋友分。",e)
    # except ValueError as e2:
    #     print("输入错误。",e2)
    except (ZeroDivisionError,ValueError) as e:
        print("出错了。", e)
    else:
        print("分苹果顺利完成。")
    finally:
        print("进行了一次分苹果的活动。")