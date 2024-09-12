import os
from screeninfo import get_monitors


def screen_size() -> tuple:
    """
    This function returns the width and heigh of the primary monitor.

    :return:  height and width of the primary monitor.
    :rtype: tuple
    """
    for monitor in get_monitors():
        if monitor.is_primary is True:
            screen_width = monitor.width
            screen_height = monitor.height
    return (screen_width, screen_height)


def photo_list(pic_path) -> list:
    """
    This function return the list of photos with accepted extentions.

    :param pic_path: Path of the photos
    :param type: str

    :return: List of the photos for accepted extentions.
    :rtype: list
    """
    filtered_pics = []
    pics_list = os.listdir(pic_path)
    for pic in pics_list:
        pic_name, pic_ext = os.path.splitext(pic)
        if pic_ext.lower() in ['.jpeg', '.jpg']:
            absolute_path_pic = pic_path + '/' + pic
            filtered_pics.append(absolute_path_pic)
    return filtered_pics
