path = "assets/images"

def GetImageById(imageId: str):
    try:
        imageStr = imageId[:1].upper() + imageId[1::]
        print(imageStr)
        filePath = f"{path}/{imageStr}.png"
        return filePath
    except:
        raise ImportError("imageId does not exist.")