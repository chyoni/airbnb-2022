def isLoggedIn(request):
    if request.user.is_anonymous is True:
        return False
    else:
        return True
