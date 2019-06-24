def user(request):
    return {'user':request.session.get('user','')}
