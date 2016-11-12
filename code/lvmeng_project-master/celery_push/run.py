from .push import APNSPush


#push to objects
def run(objects, message, **kwargs):
    # APNSPush.apply_async((objects, message),kwargs={"badge":0}, queue='push')
    APNSPush.apply_async((objects, message),kwargs=kwargs, queue='push')