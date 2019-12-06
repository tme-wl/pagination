# coding=utf-8

from page import Pagination
def test(request):
    """
    视图函数,演示分页功能,
    reurn_data为所有的数据列表,里面一list形式装载所有数据
    这里演示为从Models里面取出的所有数据
    """
    # return_data = Models.objects.all()
    return_data = [
        {"number": x, "name": '张三', "sex": '男', "year": 18, "value": 80} for x in range(999)
    ]
    obj = Pagination(request, len(return_data))
    start = obj.start()
    end = obj.end()
    pagination = obj.pagination()
    msg = {"my_data": return_data[start: end], "pagination": pagination}
    # return data
    return render(request, "show_data.html", msg)
