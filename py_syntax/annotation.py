"""
https://www.jianshu.com/p/7a644520418b
"""

def logDec(fn):
    def doLogDec(*args):
        print(f"start function: {fn} args: {args}")
        return fn(*args)
    return doLogDec

def attrs(**kwds):
    def decorate(fn):
        for key in kwds:
            setattr(fn, key, kwds[key])
        return fn
    return decorate


@attrs(versionadded="2.2",
       author="Guido van Rossum")
@logDec
def foo_test(param):
    print(getattr(foo_test,'versionadded',0))
    print(getattr(foo_test,'author',0))
    return f"foo_test({param}) invoked."


if __name__=="__main__":
    print(foo_test("test"))