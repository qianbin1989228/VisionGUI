import platform
import paddle

def get_system_info(machine_info={}):
    '''get system information'''
    machine_info['systemName'] = platform.system()
    machine_info['systemVersion'] = platform.version()
    machine_info['systemArch'] = platform.architecture()
    machine_info['pythonVersion'] = platform.python_version()
    
    machine_info['cudnnVersion'] = paddle.device.get_cudnn_version()
    machine_info['cudaVersion'] = paddle.version.cuda()
    
    machine_info['paddleVersion'] = paddle.__version__

    return machine_info


# def _get_gpu_info(queue):
#     gpu_info = dict()
#     mem_free = list()
#     mem_used = list()
#     mem_total = list()
#     import pycuda.driver as drv
#     from pycuda.tools import clear_context_caches
#     drv.init()
#     driver_version = drv.get_driver_version()
#     gpu_num = drv.Device.count()
#     for gpu_id in range(gpu_num):
#         dev = drv.Device(gpu_id)
#         try:
#             context = dev.make_context()
#             free, total = drv.mem_get_info()
#             context.pop()
#             free = free // 1024 // 1024
#             total = total // 1024 // 1024
#             used = total - free
#         except:
#             free = 0
#             total = 0
#             used = 0
#         mem_free.append(free)
#         mem_used.append(used)
#         mem_total.append(total)
#     gpu_info['mem_free'] = mem_free
#     gpu_info['mem_used'] = mem_used
#     gpu_info['mem_total'] = mem_total
#     gpu_info['driver_version'] = driver_version
#     gpu_info['gpu_num'] = gpu_num
#     queue.put(gpu_info)
    

# def get_gpu_info():
#     try:
#         import pycuda
#     except:
#         gpu_info = dict()
#         message = "未检测到GPU \n 若存在GPU请确保安装pycuda \n 若未安装pycuda请使用'pip install pycuda'来安装"
#         gpu_info['gpu_num'] = 0
#         return gpu_info, message
#     queue = mp.Queue(1)
#     p = mp.Process(target=_get_gpu_info, args=(queue, ))
#     p.start()
#     p.join()
#     gpu_info = queue.get(timeout=2)
#     if gpu_info['gpu_num'] == 0:
#         message = "未检测到GPU"
#     else:
#         message = "检测到GPU"

#     return gpu_info, message