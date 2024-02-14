

def my_md(next):
    def wrap(request):
        url = 0

        print()
        print( request.get_full_path() )
        print()
        response = next(request)
        return response
    return wrap