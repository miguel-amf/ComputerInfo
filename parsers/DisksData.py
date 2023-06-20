def get_internal_disks():
    return DeviceList()
    internal_disks = []
    disks = DeviceList()
    for disk in disks:
        if not disk.is_external:
            internal_disks.append(disk)
    return internal_disks