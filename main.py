import psutil
from matplotlib import pyplot
import time


def monitor():
    # Get memory info
    cap_memory = psutil.virtual_memory()
    # Get cpu info
    cpu = psutil.cpu_percent(interval=1)

    return cap_memory, cpu


if __name__ == "__main__":
    input("Press the enter.. ")
    print("start Monitoring...")
    i = 1
    # byte convert
    gb = 1024 * 1024 * 1024
    mem_total_arr = []
    mem_used_arr = []
    mem_free_arr = []
    cpu_used_arr = []
    while i <= 10:
        memory, cpu = monitor()
        print(f"{i}回目----")
        # memory capacity
        print(f"memory capacity > {round(memory.total / gb, 2)}GB")
        mem_total = round(memory.total / gb, 2)
        mem_total_arr.append(mem_total)
        # Used memory volume
        print(f"Used memory > {round(memory.used / gb, 2)}GB")
        mem_used = round(memory.used / gb, 2)
        mem_used_arr.append(mem_used)
        # free memory Volume
        print(f"free memory > {round(memory.available / gb, 2)}GB")
        mem_free = round(memory.available / gb, 2)
        mem_free_arr.append(mem_free)
        # Used cpu activity
        print(f"Used cpu > {cpu}%")
        cpu_used_arr.append(cpu)
        time.sleep(2)
        i += 1
    x = list(range(10))
    fig = pyplot.figure()
    fig_mem = fig.add_subplot(211, title="Used Memory", ylabel="GB")
    fig_mem.plot(x, mem_used_arr, color="r")
    pyplot.grid(ls="--")
    fig_cpu = fig.add_subplot(212, title="Used Cpu", ylabel="%")
    fig_cpu.plot(x, cpu_used_arr, color="g")
    pyplot.grid(ls="--")
    pyplot.show()
    input("exit Press the enter..")
