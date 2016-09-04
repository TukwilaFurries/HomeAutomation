#!/usr/bin/python

if __name__=='__main__':
    import import1
    import1.Import1A().begin()
    import1.Import1B().begin()
    try:
        import1.Import2A().begin()
    except: 
        print "Doesn't exist" 
