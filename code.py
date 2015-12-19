import web
render = web.template.render('templates/', base='layout')

urls = (
    '/', 'index', '/secondpage', 'secondpage', '/index', 'index', '/thirdpage', 'thirdpage'
)

class index:
    def GET(self):
        return render.index()

class secondpage:
    def GET(self):
        return render.secondpage()

class thirdpage:
    def GET(self):
        return render.thirdpage()

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
