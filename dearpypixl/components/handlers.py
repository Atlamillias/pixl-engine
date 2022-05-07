import functools
from inspect import signature, _KEYWORD_ONLY, _VAR_POSITIONAL
from types import MethodType
from typing import Callable, Any, Union
from dearpygui import dearpygui
from dearpypixl.components.item import Item
from dearpypixl.components.configuration import ItemAttribute, item_attribute, CONFIGURATION


__all__ = [
    "KeyDownHandler",
    "KeyPressHandler",
    "KeyReleaseHandler",
    "MouseMoveHandler",
    "MouseWheelHandler",
    "MouseClickHandler",
    "MouseDoubleClickHandler",
    "MouseDownHandler",
    "MouseReleaseHandler",
    "MouseDragHandler",
    "HoverHandler",
    "ResizeHandler",
    "FocusHandler",
    "ActiveHandler",
    "VisibleHandler",
    "ActivatedHandler",
    "DeactivatedHandler",
    "EditedHandler",
    "DeactivatedAfterEditHandler",
    "ToggledOpenHandler",
    "ClickedHandler",
]


class HandlerItem(Item):
    """Generic class for handler items.
    """
    def __init__(self, callback: Callable | None, **kwargs):
        super().__init__(**kwargs)
        self.callback = callback

    @property
    @item_attribute(category=CONFIGURATION)
    def callback(self) -> Callable | None:
        return dearpygui.get_item_configuration(self._tag)["callback"]
    @callback.setter
    def callback(self, _callback: Callable | None) -> None:
        # Wrapping is done for a couple of reasons. Firstly, to ensure that
        # the Item instance of `sender` is returned instead of the identifier.
        # And second; nuitka compilation doesn't like DPG callbacks unless
        # they are wrapped (lambda, etc.)...for some reason.
        @functools.wraps(_callback)
        def call_object(_, app_data, user_data):
            args = (self, app_data, user_data)[0:pos_arg_cnt]
            _callback(*args)

        # Emulating how DearPyGui doesn't require callbacks having 3 positional
        # arguments. Only pass sender/app_data/user_data if there's "room" to 
        # do so.
        pos_arg_cnt = 0
        for param in signature(_callback).parameters.values():
            if param.kind == _VAR_POSITIONAL:
                pos_arg_cnt = 3
            elif param.kind != _KEYWORD_ONLY:
                pos_arg_cnt += 1

            if pos_arg_cnt >= 3:
                pos_arg_cnt = 3
                break

        wrapper     = None
        if callable(_callback):
            wrapper = call_object
        elif _callback is None:
            wrapper = None
        else:
            raise ValueError(f"`callback` is not callable (got {type(_callback)!r}.")

        dearpygui.configure_item(self._tag, callback=wrapper)



class KeyDownHandler(HandlerItem):
    """Adds a key down handler.
    
    	Args:
    		key (int, optional): Submits callback for all keys
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		callback (Callable, optional): Registers a callback.
    		show (bool, optional): Attempt to render widget.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """
    key              : int      = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    show             : bool     = ItemAttribute("configuration", "get_item_config", "set_item_config", None)

    __is_container__ : bool     = False                                                                     
    __is_root_item__ : bool     = False                                                                     
    __is_value_able__: bool     = False                                                                     
    __able_parents__ : tuple    = ('Stage', 'TemplateRegistry', 'HandlerRegistry')                          
    __able_children__: tuple    = ()                                                                        
    __commands__     : tuple    = ()                                                                        
    __constants__    : tuple    = ('mvKeyDownHandler',)                                                     
    __command__      : Callable = dearpygui.add_key_down_handler                                            

    def __init__(
        self                                      ,
        key               : int             = -1  ,
        label             : str             = None,
        user_data         : Any             = None,
        use_internal_label: bool            = True,
        callback          : Callable        = None,
        show              : bool            = True,
        parent            : Union[int, str] = 11  ,
        **kwargs                                  ,
    ) -> None:
        super().__init__(
            key=key,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            callback=callback,
            show=show,
            parent=parent,
            **kwargs,
        )


class KeyPressHandler(HandlerItem):
    """Adds a key press handler.
    
    	Args:
    		key (int, optional): Submits callback for all keys
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		callback (Callable, optional): Registers a callback.
    		show (bool, optional): Attempt to render widget.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """
    key              : int      = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    show             : bool     = ItemAttribute("configuration", "get_item_config", "set_item_config", None)

    __is_container__ : bool     = False                                                                     
    __is_root_item__ : bool     = False                                                                     
    __is_value_able__: bool     = False                                                                     
    __able_parents__ : tuple    = ('Stage', 'TemplateRegistry', 'HandlerRegistry')                          
    __able_children__: tuple    = ()                                                                        
    __commands__     : tuple    = ()                                                                        
    __constants__    : tuple    = ('mvKeyPressHandler',)                                                    
    __command__      : Callable = dearpygui.add_key_press_handler                                           

    def __init__(
        self                                      ,
        key               : int             = -1  ,
        label             : str             = None,
        user_data         : Any             = None,
        use_internal_label: bool            = True,
        callback          : Callable        = None,
        show              : bool            = True,
        parent            : Union[int, str] = 11  ,
        **kwargs                                  ,
    ) -> None:
        super().__init__(
            key=key,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            callback=callback,
            show=show,
            parent=parent,
            **kwargs,
        )


class KeyReleaseHandler(HandlerItem):
    """Adds a key release handler.
    
    	Args:
    		key (int, optional): Submits callback for all keys
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		callback (Callable, optional): Registers a callback.
    		show (bool, optional): Attempt to render widget.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """
    key              : int      = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    show             : bool     = ItemAttribute("configuration", "get_item_config", "set_item_config", None)

    __is_container__ : bool     = False                                                                     
    __is_root_item__ : bool     = False                                                                     
    __is_value_able__: bool     = False                                                                     
    __able_parents__ : tuple    = ('Stage', 'TemplateRegistry', 'HandlerRegistry')                          
    __able_children__: tuple    = ()                                                                        
    __commands__     : tuple    = ()                                                                        
    __constants__    : tuple    = ('mvKeyReleaseHandler',)                                                  
    __command__      : Callable = dearpygui.add_key_release_handler                                         

    def __init__(
        self                                      ,
        key               : int             = -1  ,
        label             : str             = None,
        user_data         : Any             = None,
        use_internal_label: bool            = True,
        callback          : Callable        = None,
        show              : bool            = True,
        parent            : Union[int, str] = 11  ,
        **kwargs                                  ,
    ) -> None:
        super().__init__(
            key=key,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            callback=callback,
            show=show,
            parent=parent,
            **kwargs,
        )


class MouseMoveHandler(HandlerItem):
    """Adds a mouse move handler.
    
    	Args:
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		callback (Callable, optional): Registers a callback.
    		show (bool, optional): Attempt to render widget.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """
    show             : bool     = ItemAttribute("configuration", "get_item_config", "set_item_config", None)

    __is_container__ : bool     = False                                                                     
    __is_root_item__ : bool     = False                                                                     
    __is_value_able__: bool     = False                                                                     
    __able_parents__ : tuple    = ('TemplateRegistry', 'Stage', 'HandlerRegistry')                          
    __able_children__: tuple    = ()                                                                        
    __commands__     : tuple    = ()                                                                        
    __constants__    : tuple    = ('mvMouseMoveHandler',)                                                   
    __command__      : Callable = dearpygui.add_mouse_move_handler                                          

    def __init__(
        self                                      ,
        label             : str             = None,
        user_data         : Any             = None,
        use_internal_label: bool            = True,
        callback          : Callable        = None,
        show              : bool            = True,
        parent            : Union[int, str] = 11  ,
        **kwargs                                  ,
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            callback=callback,
            show=show,
            parent=parent,
            **kwargs,
        )


class MouseWheelHandler(HandlerItem):
    """Adds a mouse wheel handler.
    
    	Args:
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		callback (Callable, optional): Registers a callback.
    		show (bool, optional): Attempt to render widget.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """
    show              : bool     = ItemAttribute("configuration", "get_item_config", "set_item_config", None)

    __is_container__ : bool     = False                                                                     
    __is_root_item__ : bool     = False                                                                     
    __is_value_able__: bool     = False                                                                     
    __able_parents__ : tuple    = ('TemplateRegistry', 'Stage', 'HandlerRegistry')                          
    __able_children__: tuple    = ()                                                                        
    __commands__     : tuple    = ()                                                                        
    __constants__    : tuple    = ('mvMouseWheelHandler',)                                                  
    __command__      : Callable = dearpygui.add_mouse_wheel_handler                                         

    def __init__(
        self                                      ,
        label             : str             = None,
        user_data         : Any             = None,
        use_internal_label: bool            = True,
        callback          : Callable        = None,
        show              : bool            = True,
        parent            : Union[int, str] = 11  ,
        **kwargs                                  ,
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            callback=callback,
            show=show,
            parent=parent,
            **kwargs,
        )


class MouseClickHandler(HandlerItem):
    """Adds a mouse click handler.
    
    	Args:
    		button (int, optional): Submits callback for all mouse buttons
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		callback (Callable, optional): Registers a callback.
    		show (bool, optional): Attempt to render widget.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    button           : int      = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    show             : bool     = ItemAttribute("configuration", "get_item_config", "set_item_config", None)

    __is_container__ : bool     = False                                                                     
    __is_root_item__ : bool     = False                                                                     
    __is_value_able__: bool     = False                                                                     
    __able_parents__ : tuple    = ('Stage', 'TemplateRegistry', 'HandlerRegistry')                          
    __able_children__: tuple    = ()                                                                        
    __commands__     : tuple    = ()                                                                        
    __constants__    : tuple    = ('mvMouseClickHandler',)                                                  
    __command__      : Callable = dearpygui.add_mouse_click_handler                                         

    def __init__(
        self                                      ,
        button            : int             = -1  ,
        label             : str             = None,
        user_data         : Any             = None,
        use_internal_label: bool            = True,
        callback          : Callable        = None,
        show              : bool            = True,
        parent            : Union[int, str] = 11  ,
        **kwargs                                  ,
    ) -> None:
        super().__init__(
            button=button,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            callback=callback,
            show=show,
            parent=parent,
            **kwargs,
        )


class MouseDoubleClickHandler(HandlerItem):
    """Adds a mouse double click handler.
    
    	Args:
    		button (int, optional): Submits callback for all mouse buttons
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		callback (Callable, optional): Registers a callback.
    		show (bool, optional): Attempt to render widget.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """
    button           : int      = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    show             : bool     = ItemAttribute("configuration", "get_item_config", "set_item_config", None)

    __is_container__ : bool     = False                                                                     
    __is_root_item__ : bool     = False                                                                     
    __is_value_able__: bool     = False                                                                     
    __able_parents__ : tuple    = ('TemplateRegistry', 'Stage', 'HandlerRegistry')                          
    __able_children__: tuple    = ()                                                                        
    __commands__     : tuple    = ()                                                                        
    __constants__    : tuple    = ('mvMouseDoubleClickHandler',)                                            
    __command__      : Callable = dearpygui.add_mouse_double_click_handler                                  

    def __init__(
        self                                      ,
        button            : int             = -1  ,
        label             : str             = None,
        user_data         : Any             = None,
        use_internal_label: bool            = True,
        callback          : Callable        = None,
        show              : bool            = True,
        parent            : Union[int, str] = 11  ,
        **kwargs                                  ,
    ) -> None:
        super().__init__(
            button=button,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            callback=callback,
            show=show,
            parent=parent,
            **kwargs,
        )


class MouseDownHandler(HandlerItem):
    """Adds a mouse down handler.
    
    	Args:
    		button (int, optional): Submits callback for all mouse buttons
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		callback (Callable, optional): Registers a callback.
    		show (bool, optional): Attempt to render widget.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """
    button           : int      = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    show             : bool     = ItemAttribute("configuration", "get_item_config", "set_item_config", None)

    __is_container__ : bool     = False                                                                     
    __is_root_item__ : bool     = False                                                                     
    __is_value_able__: bool     = False                                                                     
    __able_parents__ : tuple    = ('TemplateRegistry', 'Stage', 'HandlerRegistry')                          
    __able_children__: tuple    = ()                                                                        
    __commands__     : tuple    = ()                                                                        
    __constants__    : tuple    = ('mvMouseDownHandler',)                                                   
    __command__      : Callable = dearpygui.add_mouse_down_handler                                          

    def __init__(
        self                                      ,
        button            : int             = -1  ,
        label             : str             = None,
        user_data         : Any             = None,
        use_internal_label: bool            = True,
        callback          : Callable        = None,
        show              : bool            = True,
        parent            : Union[int, str] = 11  ,
        **kwargs                                  ,
    ) -> None:
        super().__init__(
            button=button,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            callback=callback,
            show=show,
            parent=parent,
            **kwargs,
        )


class MouseReleaseHandler(HandlerItem):
    """Adds a mouse release handler.
    
    	Args:
    		button (int, optional): Submits callback for all mouse buttons
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		callback (Callable, optional): Registers a callback.
    		show (bool, optional): Attempt to render widget.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """
    button           : int      = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    show             : bool     = ItemAttribute("configuration", "get_item_config", "set_item_config", None)

    __is_container__ : bool     = False                                                                     
    __is_root_item__ : bool     = False                                                                     
    __is_value_able__: bool     = False                                                                     
    __able_parents__ : tuple    = ('TemplateRegistry', 'Stage', 'HandlerRegistry')                          
    __able_children__: tuple    = ()                                                                        
    __commands__     : tuple    = ()                                                                        
    __constants__    : tuple    = ('mvMouseReleaseHandler',)                                                
    __command__      : Callable = dearpygui.add_mouse_release_handler                                       

    def __init__(
        self                                      ,
        button            : int             = -1  ,
        label             : str             = None,
        user_data         : Any             = None,
        use_internal_label: bool            = True,
        callback          : Callable        = None,
        show              : bool            = True,
        parent            : Union[int, str] = 11  ,
        **kwargs                                  ,
    ) -> None:
        super().__init__(
            button=button,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            callback=callback,
            show=show,
            parent=parent,
            **kwargs,
        )


class MouseDragHandler(HandlerItem):
    """Adds a mouse drag handler.
    
    	Args:
    		button (int, optional): Submits callback for all mouse buttons
    		threshold (float, optional): The threshold the mouse must be dragged before the callback is ran
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		callback (Callable, optional): Registers a callback.
    		show (bool, optional): Attempt to render widget.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """
    button           : int      = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    threshold        : float    = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    show             : bool     = ItemAttribute("configuration", "get_item_config", "set_item_config", None)

    __is_container__ : bool     = False                                                                     
    __is_root_item__ : bool     = False                                                                     
    __is_value_able__: bool     = False                                                                     
    __able_parents__ : tuple    = ('TemplateRegistry', 'Stage', 'HandlerRegistry')                          
    __able_children__: tuple    = ()                                                                        
    __commands__     : tuple    = ()                                                                        
    __constants__    : tuple    = ('mvMouseDragHandler',)                                                   
    __command__      : Callable = dearpygui.add_mouse_drag_handler                                          

    def __init__(
        self                                      ,
        button            : int             = -1  ,
        threshold         : float           = 10.0,
        label             : str             = None,
        user_data         : Any             = None,
        use_internal_label: bool            = True,
        callback          : Callable        = None,
        show              : bool            = True,
        parent            : Union[int, str] = 11  ,
        **kwargs                                  ,
    ) -> None:
        super().__init__(
            button=button,
            threshold=threshold,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            callback=callback,
            show=show,
            parent=parent,
            **kwargs,
        )


class HoverHandler(HandlerItem):
    """Adds a hover handler.
    
    	Args:
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		callback (Callable, optional): Registers a callback.
    		show (bool, optional): Attempt to render widget.
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """
    show             : bool     = ItemAttribute("configuration", "get_item_config", "set_item_config", None)

    __is_container__ : bool     = False                                                                     
    __is_root_item__ : bool     = False                                                                     
    __is_value_able__: bool     = False                                                                     
    __able_parents__ : tuple    = ('Stage', 'TemplateRegistry', 'ItemHandlerRegistry')                      
    __able_children__: tuple    = ()                                                                        
    __commands__     : tuple    = ()                                                                        
    __constants__    : tuple    = ('mvHoverHandler',)                                                       
    __command__      : Callable = dearpygui.add_item_hover_handler                                          

    def __init__(
        self                                      ,
        label             : str             = None,
        user_data         : Any             = None,
        use_internal_label: bool            = True,
        parent            : Union[int, str] = 0   ,
        callback          : Callable        = None,
        show              : bool            = True,
        **kwargs                                  ,
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            callback=callback,
            show=show,
            **kwargs,
        )


class ResizeHandler(HandlerItem):
    """Adds a resize handler.
    
    	Args:
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		callback (Callable, optional): Registers a callback.
    		show (bool, optional): Attempt to render widget.
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """
    show             : bool     = ItemAttribute("configuration", "get_item_config", "set_item_config", None)

    __is_container__ : bool     = False                                                                     
    __is_root_item__ : bool     = False                                                                     
    __is_value_able__: bool     = False                                                                     
    __able_parents__ : tuple    = ('Stage', 'TemplateRegistry', 'ItemHandlerRegistry')                      
    __able_children__: tuple    = ()                                                                        
    __commands__     : tuple    = ()                                                                        
    __constants__    : tuple    = ('mvResizeHandler',)                                                      
    __command__      : Callable = dearpygui.add_item_resize_handler                                         

    def __init__(
        self                                      ,
        label             : str             = None,
        user_data         : Any             = None,
        use_internal_label: bool            = True,
        parent            : Union[int, str] = 0   ,
        callback          : Callable        = None,
        show              : bool            = True,
        **kwargs                                  ,
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            callback=callback,
            show=show,
            **kwargs,
        )


class FocusHandler(HandlerItem):
    """Adds a focus handler.
    
    	Args:
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		callback (Callable, optional): Registers a callback.
    		show (bool, optional): Attempt to render widget.
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """
    show             : bool     = ItemAttribute("configuration", "get_item_config", "set_item_config", None)

    __is_container__ : bool     = False                                                                     
    __is_root_item__ : bool     = False                                                                     
    __is_value_able__: bool     = False                                                                     
    __able_parents__ : tuple    = ('Stage', 'TemplateRegistry', 'ItemHandlerRegistry')                      
    __able_children__: tuple    = ()                                                                        
    __commands__     : tuple    = ()                                                                        
    __constants__    : tuple    = ('mvFocusHandler',)                                                       
    __command__      : Callable = dearpygui.add_item_focus_handler                                          

    def __init__(
        self                                      ,
        label             : str             = None,
        user_data         : Any             = None,
        use_internal_label: bool            = True,
        parent            : Union[int, str] = 0   ,
        callback          : Callable        = None,
        show              : bool            = True,
        **kwargs                                  ,
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            callback=callback,
            show=show,
            **kwargs,
        )


class ActiveHandler(HandlerItem):
    """Adds a active handler.
    
    	Args:
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		callback (Callable, optional): Registers a callback.
    		show (bool, optional): Attempt to render widget.
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """
    show             : bool     = ItemAttribute("configuration", "get_item_config", "set_item_config", None)

    __is_container__ : bool     = False                                                                     
    __is_root_item__ : bool     = False                                                                     
    __is_value_able__: bool     = False                                                                     
    __able_parents__ : tuple    = ('Stage', 'TemplateRegistry', 'ItemHandlerRegistry')                      
    __able_children__: tuple    = ()                                                                        
    __commands__     : tuple    = ()                                                                        
    __constants__    : tuple    = ('mvActiveHandler',)                                                      
    __command__      : Callable = dearpygui.add_item_active_handler                                         

    def __init__(
        self                                      ,
        label             : str             = None,
        user_data         : Any             = None,
        use_internal_label: bool            = True,
        parent            : Union[int, str] = 0   ,
        callback          : Callable        = None,
        show              : bool            = True,
        **kwargs                                  ,
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            callback=callback,
            show=show,
            **kwargs,
        )


class VisibleHandler(HandlerItem):
    """Adds a visible handler.
    
    	Args:
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		callback (Callable, optional): Registers a callback.
    		show (bool, optional): Attempt to render widget.
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """
    show             : bool     = ItemAttribute("configuration", "get_item_config", "set_item_config", None)

    __is_container__ : bool     = False                                                                     
    __is_root_item__ : bool     = False                                                                     
    __is_value_able__: bool     = False                                                                     
    __able_parents__ : tuple    = ('Stage', 'TemplateRegistry', 'ItemHandlerRegistry')                      
    __able_children__: tuple    = ()                                                                        
    __commands__     : tuple    = ()                                                                        
    __constants__    : tuple    = ('mvVisibleHandler',)                                                     
    __command__      : Callable = dearpygui.add_item_visible_handler                                        

    def __init__(
        self                                      ,
        label             : str             = None,
        user_data         : Any             = None,
        use_internal_label: bool            = True,
        parent            : Union[int, str] = 0   ,
        callback          : Callable        = None,
        show              : bool            = True,
        **kwargs                                  ,
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            callback=callback,
            show=show,
            **kwargs,
        )


class ActivatedHandler(HandlerItem):
    """Adds a activated handler.
    
    	Args:
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		callback (Callable, optional): Registers a callback.
    		show (bool, optional): Attempt to render widget.
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """
    show             : bool     = ItemAttribute("configuration", "get_item_config", "set_item_config", None)

    __is_container__ : bool     = False                                                                     
    __is_root_item__ : bool     = False                                                                     
    __is_value_able__: bool     = False                                                                     
    __able_parents__ : tuple    = ('Stage', 'TemplateRegistry', 'ItemHandlerRegistry')                      
    __able_children__: tuple    = ()                                                                        
    __commands__     : tuple    = ()                                                                        
    __constants__    : tuple    = ('mvActivatedHandler',)                                                   
    __command__      : Callable = dearpygui.add_item_activated_handler                                      

    def __init__(
        self                                      ,
        label             : str             = None,
        user_data         : Any             = None,
        use_internal_label: bool            = True,
        parent            : Union[int, str] = 0   ,
        callback          : Callable        = None,
        show              : bool            = True,
        **kwargs                                  ,
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            callback=callback,
            show=show,
            **kwargs,
        )


class DeactivatedHandler(HandlerItem):
    """Adds a deactivated handler.
    
    	Args:
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		callback (Callable, optional): Registers a callback.
    		show (bool, optional): Attempt to render widget.
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """
    show             : bool     = ItemAttribute("configuration", "get_item_config", "set_item_config", None)

    __is_container__ : bool     = False                                                                     
    __is_root_item__ : bool     = False                                                                     
    __is_value_able__: bool     = False                                                                     
    __able_parents__ : tuple    = ('Stage', 'TemplateRegistry', 'ItemHandlerRegistry')                      
    __able_children__: tuple    = ()                                                                        
    __commands__     : tuple    = ()                                                                        
    __constants__    : tuple    = ('mvDeactivatedHandler',)                                                 
    __command__      : Callable = dearpygui.add_item_deactivated_handler                                    

    def __init__(
        self                                      ,
        label             : str             = None,
        user_data         : Any             = None,
        use_internal_label: bool            = True,
        parent            : Union[int, str] = 0   ,
        callback          : Callable        = None,
        show              : bool            = True,
        **kwargs                                  ,
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            callback=callback,
            show=show,
            **kwargs,
        )


class EditedHandler(HandlerItem):
    """Adds an edited handler.
    
    	Args:
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		callback (Callable, optional): Registers a callback.
    		show (bool, optional): Attempt to render widget.
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """
    show             : bool     = ItemAttribute("configuration", "get_item_config", "set_item_config", None)

    __is_container__ : bool     = False                                                                     
    __is_root_item__ : bool     = False                                                                     
    __is_value_able__: bool     = False                                                                     
    __able_parents__ : tuple    = ('Stage', 'TemplateRegistry', 'ItemHandlerRegistry')                      
    __able_children__: tuple    = ()                                                                        
    __commands__     : tuple    = ()                                                                        
    __constants__    : tuple    = ('mvEditedHandler',)                                                      
    __command__      : Callable = dearpygui.add_item_edited_handler                                         

    def __init__(
        self                                      ,
        label             : str             = None,
        user_data         : Any             = None,
        use_internal_label: bool            = True,
        parent            : Union[int, str] = 0   ,
        callback          : Callable        = None,
        show              : bool            = True,
        **kwargs                                  ,
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            callback=callback,
            show=show,
            **kwargs,
        )


class DeactivatedAfterEditHandler(HandlerItem):
    """Adds a deactivated after edit handler.
    
    	Args:
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		callback (Callable, optional): Registers a callback.
    		show (bool, optional): Attempt to render widget.
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """
    show             : bool     = ItemAttribute("configuration", "get_item_config", "set_item_config", None)

    __is_container__ : bool     = False                                                                     
    __is_root_item__ : bool     = False                                                                     
    __is_value_able__: bool     = False                                                                     
    __able_parents__ : tuple    = ('Stage', 'TemplateRegistry', 'ItemHandlerRegistry')                      
    __able_children__: tuple    = ()                                                                        
    __commands__     : tuple    = ()                                                                        
    __constants__    : tuple    = ('mvDeactivatedAfterEditHandler',)                                        
    __command__      : Callable = dearpygui.add_item_deactivated_after_edit_handler                         

    def __init__(
        self                                      ,
        label             : str             = None,
        user_data         : Any             = None,
        use_internal_label: bool            = True,
        parent            : Union[int, str] = 0   ,
        callback          : Callable        = None,
        show              : bool            = True,
        **kwargs                                  ,
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            callback=callback,
            show=show,
            **kwargs,
        )


class ToggledOpenHandler(HandlerItem):
    """Adds a togged open handler.
    
    	Args:
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		callback (Callable, optional): Registers a callback.
    		show (bool, optional): Attempt to render widget.
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """
    show             : bool     = ItemAttribute("configuration", "get_item_config", "set_item_config", None)

    __is_container__ : bool     = False                                                                     
    __is_root_item__ : bool     = False                                                                     
    __is_value_able__: bool     = False                                                                     
    __able_parents__ : tuple    = ('Stage', 'TemplateRegistry', 'ItemHandlerRegistry')                      
    __able_children__: tuple    = ()                                                                        
    __commands__     : tuple    = ()                                                                        
    __constants__    : tuple    = ('mvToggledOpenHandler',)                                                 
    __command__      : Callable = dearpygui.add_item_toggled_open_handler                                   

    def __init__(
        self                                      ,
        label             : str             = None,
        user_data         : Any             = None,
        use_internal_label: bool            = True,
        parent            : Union[int, str] = 0   ,
        callback          : Callable        = None,
        show              : bool            = True,
        **kwargs                                  ,
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            callback=callback,
            show=show,
            **kwargs,
        )


class ClickedHandler(HandlerItem):
    """Adds a clicked handler.
    
    	Args:
    		button (int, optional): Submits callback for all mouse buttons
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		parent (Union[int, str], optional): Parent to add this item to. (runtime adding)
    		callback (Callable, optional): Registers a callback.
    		show (bool, optional): Attempt to render widget.
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """
    button           : int      = ItemAttribute("configuration", "get_item_config", "set_item_config", None)
    show             : bool     = ItemAttribute("configuration", "get_item_config", "set_item_config", None)

    __is_container__ : bool     = False                                                                     
    __is_root_item__ : bool     = False                                                                     
    __is_value_able__: bool     = False                                                                     
    __able_parents__ : tuple    = ('Stage', 'TemplateRegistry', 'ItemHandlerRegistry')                      
    __able_children__: tuple    = ()                                                                        
    __commands__     : tuple    = ()                                                                        
    __constants__    : tuple    = ('mvClickedHandler',)                                                     
    __command__      : Callable = dearpygui.add_item_clicked_handler                                        

    def __init__(
        self                                      ,
        button            : int             = -1  ,
        label             : str             = None,
        user_data         : Any             = None,
        use_internal_label: bool            = True,
        parent            : Union[int, str] = 0   ,
        callback          : Callable        = None,
        show              : bool            = True,
        **kwargs                                  ,
    ) -> None:
        super().__init__(
            button=button,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            callback=callback,
            show=show,
            **kwargs,
        )
