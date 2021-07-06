from dearpygui import core as idpg


__updated__ = "20210704"
__dpg_ver__ = "0.8.12"


def supports_version_check(show_ver = True):
    dpg_ver = idpg.get_dearpygui_version()

    supported = True
    for dpg_n, pkg_n in zip(dpg_ver, __dpg_ver__):
        if dpg_n != pkg_n:
            supported = False
            break

    if show_ver:
        print(f"Supported: v{__dpg_ver__}")
        print(f"DearPyGui: v{dpg_ver}")

    return supported
    