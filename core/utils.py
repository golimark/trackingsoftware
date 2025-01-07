import os, uuid

# utility functions
def save_image_save_path(instance, filename):
    ext = filename.split(".")[-1]
    filename = "%s-%s.%s" % (instance.__str__(), uuid.uuid4(), ext)
    return os.path.join(f"{instance.__class__.__name__}/images/", filename)