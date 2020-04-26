def __common_path( remotepath, oldpath):
    if len(remotepath) < len(oldpath):
        remotepath, oldpath = oldpath, remotepath

    for _idnex, _char in enumerate(remotepath):
        if _char != oldpath[_idnex]:
            break
    print(_idnex)
    return remotepath[:_idnex]

# print(__common_path('/5/11','/5/2'))
print('/5/11'.lstrip('/5/2'))