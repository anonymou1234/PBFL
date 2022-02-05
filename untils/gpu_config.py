from tensorflow import config

gpus = physical_devices = config.list_physical_devices('GPU')
if len(gpus) == 0:
    print('当前没有检测到gpu，设置显存增量模式无效。')
for gpu in gpus:
    try:
        # 显示显存的使用大小，最大12 *1024 M
        config.experimental.set_virtual_device_configuration(
            gpu,[config.experimental.VirtualDeviceConfiguration(memory_limit=1024*12)]
        )
        # config.experimental.set_memory_growth(gpu, True)
    except RuntimeError as e:
        print(e)

pass