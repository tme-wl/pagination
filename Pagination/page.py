class Pagination(object):
    """
    输入参数:
    lendata:为数据总数
    result_per_page:单页数据个数 默认为10
    pagenum_per_bar:分页里面要显示的页数
    pagenum_per_bar 要大于等于7

    <<  1  2  3  >>
    <<  1  2  3  4  5  6  7  >>
    <<  1  2  3  4  5  .. 14 >>
    <<  1 ..  4  5  6  7  8  >>
    <<  1 ..  4  5  6  .. 14 >>
    """
    def __init__(self, request, lendata, results_per_page=10, pagenum_per_bar=7):
        self.results_per_page = results_per_page
        if pagenum_per_bar <= 7:
            pagenum_per_bar = 7
        self.pagenum_per_bar = pagenum_per_bar
        self.page = int(request.GET.get('page', '1'))
        self.fullpath = request.get_full_path()
        self.hits = lendata

    def cleanpagepath(self, fullpath):
        path = fullpath
        pos = fullpath.find('?')
        if pos > -1:
            path = fullpath[:pos]
            querystring = fullpath[pos+1:]
            if querystring:
                pairs = [pair for pair in querystring.split('&') if not pair.startswith('page') and not pair.startswith('hits')]
                if pairs:
                    return path + '?' + '&'.join(pairs)
        return path

    def start(self):
        return (self.page - 1) * self.results_per_page

    def end(self):
        return self.page * self.results_per_page

    def pagination(self):
        try:
            pages = int(self.hits/self.results_per_page)    # 总共多少页
            if self.hits % self.results_per_page > 0:
                pages += 1
        except:
            pages = 0
        pagelist = []
        if 0 < pages <= self.pagenum_per_bar:     # 总页数少于要显示的页数<< 1 2 >>
            pagelist = [i for i in range(1, pages+1)]

        elif pages > self.pagenum_per_bar:
            a = self.page-int((self.pagenum_per_bar-4)/2)
            b = self.page+int((self.pagenum_per_bar-4)/2)
            if a > 3 and b < pages-2:
                pagelist = [1, 0]+[t for t in range(self.page-int((self.pagenum_per_bar-4)/2), self.page+int((self.pagenum_per_bar-4)/2)+1)]+[0, pages]
            elif a <= 3:
                pagelist = [t for t in range(1, self.pagenum_per_bar-1)]+[0, pages]
            elif b >= pages-2:
                pagelist = [1, 0]+[t for t in range(pages-self.pagenum_per_bar+3, pages+1)]
        if self.page < pages:   # 下一页
            next = self.page+1
        else:
            next = pages

        if self.page == 1:      # 上一页
            previous = 1
        else:
            previous = self.page-1
        pagenav = self.cleanpagepath(self.fullpath)
        if pagenav.find('?') > 0:
            pagenav += '&'
        else:
            pagenav += '?'

        mypagination = {
                'pages': pages,
                'page': self.page,
                'pagelist': pagelist,
                'previous': previous,
                'next': next,
                'pagenav': pagenav,
                'hits': self.hits,
            }
        # return pagination
        return mypagination
