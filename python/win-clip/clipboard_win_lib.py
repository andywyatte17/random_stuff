import ctypes
import ctypes.wintypes as w

def InitClipFns():
    user32 = ctypes.windll.user32
    kernel32 = ctypes.windll.kernel32

    global IsClipboardFormatAvailable, OpenClipboard, EmptyClipboard, \
           CloseClipboard, GlobalSize, SetClipboardData, GlobalAlloc, \
           GetClipboardData, RegisterClipboardFormatA, GlobalLock, \
           GlobalUnlock
    # ...
    IsClipboardFormatAvailable = user32.IsClipboardFormatAvailable
    # ...
    OpenClipboard = user32.OpenClipboard
    OpenClipboard.argtypes = [w.HWND]
    OpenClipboard.restype = w.BOOL
    # ...
    EmptyClipboard = user32.EmptyClipboard
    EmptyClipboard.argtypes = []
    EmptyClipboard.restype = w.BOOL
    # ...
    CloseClipboard = user32.CloseClipboard
    CloseClipboard.argtypes = []
    CloseClipboard.restype = w.BOOL
    # ...
    GlobalSize = kernel32.GlobalSize
    GlobalSize.argtypes = [w.HGLOBAL]
    GlobalSize.restype = w.ctypes.c_size_t
    # ...
    SetClipboardData = user32.SetClipboardData
    SetClipboardData.argtypes = w.UINT, w.HGLOBAL
    SetClipboardData.restype = ctypes.c_void_p
    # ...
    GlobalAlloc = kernel32.GlobalAlloc
    GlobalAlloc.argtypes = w.UINT, w.ctypes.c_size_t,
    GlobalAlloc.restype = w.HGLOBAL
    # ...
    GlobalLock = kernel32.GlobalLock
    GlobalLock.argtypes = [w.HGLOBAL]
    GlobalLock.restype = ctypes.c_void_p
    # ...
    GlobalUnlock = kernel32.GlobalUnlock
    GlobalUnlock.argtypes = [ctypes.c_void_p]
    # ...
    GetClipboardData = user32.GetClipboardData
    GetClipboardData.argtypes = [w.UINT]
    GetClipboardData.restype = ctypes.c_void_p
    # ...
    RegisterClipboardFormatA = user32.RegisterClipboardFormatA
    RegisterClipboardFormatA.argtypes = [w.LPCSTR]
    RegisterClipboardFormatA.restype = ctypes.c_uint32

initClipFnsResult = InitClipFns()

CF_TEXT, CF_DIBV5, CF_UNICODETEXT = 1, 17, 13
PNG = RegisterClipboardFormatA("PNG".encode("ascii"))

def ReadClipData(fmt):
    '''
      Import clipboard bytes as a bytes objects if present.
      fmt indicates the type, for example CF_DIBV5 or PNG.
    '''
    OpenClipboard(0)
    try:
        if IsClipboardFormatAvailable(fmt):
            data = GetClipboardData(fmt)
            size = GlobalSize(data)
            raw_data = ctypes.create_string_buffer(size)
            data_locked = GlobalLock(data)
            ctypes.memmove(raw_data, data_locked, size)
            GlobalUnlock(data_locked)
            return raw_data.raw
    finally:
        CloseClipboard()
    return None

def InstallClipData(clipType, clipBytes):
    '''
    Clear the current Windows clipboard and store data of type
    'clipType' with bytes 'clipBytes'.
    '''
    OpenClipboard(0)
    EmptyClipboard()
    GHND = 0x0042 # GMEM_MOVEABLE | GMEM_ZEROINIT
    handle = GlobalAlloc(GHND, len(clipBytes))
    pcontents = GlobalLock(handle)
    ctypes.memmove(pcontents, clipBytes, len(clipBytes))
    GlobalUnlock(handle)
    SetClipboardData(clipType, handle)
    CloseClipboard()
