import web
render = web.template.render('templates/', base='layout')

urls = (
<<<<<<< HEAD
    '/', 'index', '/secondpage', 'secondpage', '/index', 'index', '/thirdpage', 'thirdpage'
=======
    '/', 'index', '/secondpage', 'secondpage', '/index', 'index'
>>>>>>> c8994afffaa8145f96de8ea8cc8683457a0e94fd
)

class index:
    def GET(self):
        return render.index()

class secondpage:
    def GET(self):
        return render.secondpage()

<<<<<<< HEAD
class thirdpage:
    def GET(self):
        return render.thirdpage()

=======
>>>>>>> c8994afffaa8145f96de8ea8cc8683457a0e94fd
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
