from PIL import Image
import os

def webp(image, toFormat: str, storage_path:str, keep: bool = True) -> str:

    path = getPath(storage_path)

    img = Image.open(image)
    original_file = img.filename
    extension = img.format.lower()
    name = img.filename.rsplit(".", 1)[0].rsplit("/", 1)[-1]

    new_file = f"{name}.{toFormat}"
    new_file_path = os.path.join(path, new_file)

    toFormat = toFormat.lower()
    if extension == toFormat:
        return f"File is already in {toFormat}"
    if toFormat == "ico":
        img.save(new_file_path, toFormat, sizes=[(128, 128)])
    elif toFormat in ["jpeg", "jpg"]:
        img.save(new_file_path, "jpeg", quality=80)
    elif toFormat == "webp":
        img.save(new_file_path, toFormat, quality=50)
    elif toFormat == "png":
        img.save(new_file_path, toFormat, optimize=True)
    else:
        pass

    if not keep:
        os.remove(original_file)
    return new_file


def getPath(pathname: str):
    full_path = os.getcwd() + pathname
    os.makedirs(full_path, exist_ok=True)
    return full_path


webp('./media/images/IMG_6543.JPG', 'ico', '/media/images')